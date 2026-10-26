"""Render terminal-style animated GIFs from scene scripts (replays of real Claude Code output).

Each scene in scenes/ holds the verbatim result text of a `claude -p` run with the plugin loaded.
Usage (macOS, needs Pillow and the system Menlo font):
    python render.py scenes/confirm.json ../confirm.gif
"""
import json, re, sys, textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1000, 700
PAD, TOP = 28, 52
FS, LH = 16, 23
FONT = "/System/Library/Fonts/Menlo.ttc"
REG = ImageFont.truetype(FONT, FS, index=0)
BOLD = ImageFont.truetype(FONT, FS, index=1)
TITLE = ImageFont.truetype(FONT, 13, index=0)
CW = REG.getlength("M")
COLS = int((W - 2 * PAD) // CW) - 1
ROWS = (H - TOP - 18) // LH

BG = (13, 17, 23)
CHROME = (22, 27, 34)
FG = (201, 209, 217)
DIM = (125, 133, 144)
WHITE = (240, 246, 252)
ORANGE = (217, 119, 87)   # Claude-ish accent
GREEN = (63, 185, 80)
BLUE = (88, 166, 255)
VERDICT = {"stop": (248, 81, 73), "rethink": (219, 109, 40), "do przemyślenia": (219, 109, 40),
           "conditional": (210, 153, 34), "warunkowo": (210, 153, 34),
           "go": (63, 185, 80), "działaj": (63, 185, 80), "strong": (88, 166, 255), "mocne": (88, 166, 255)}


def spans(line, base=FG):
    """Split a markdown-ish line into (text, font, color) spans: **bold**, *italic*, `code`."""
    out = []
    for part in re.split(r"(\*\*[^*]+\*\*|`[^`]+`|\*[^*]+\*)", line):
        if not part:
            continue
        if part.startswith("**"):
            t = part[2:-2]
            m = re.match(r"(Verdict|Werdykt): (.+?)\.?$", t)
            col = VERDICT.get(m.group(2).lower(), WHITE) if m else WHITE
            out.append((t, BOLD, col))
        elif part.startswith("`"):
            out.append((part[1:-1], REG, BLUE))
        elif part.startswith("*"):
            out.append((part[1:-1], REG, DIM))
        else:
            out.append((part, REG, base))
    return out


def wrap_md(text, indent=2):
    """Wrap markdown text to terminal columns, keeping ** pairs intact per line."""
    lines = []
    for para in text.split("\n"):
        if not para.strip():
            lines.append("")
            continue
        lead = re.match(r"^(\s*(?:\d+\.|-|•)\s+)", para)
        hang = " " * (len(lead.group(1)) if lead else 0)
        wrapped = textwrap.wrap(para, COLS - indent, subsequent_indent=hang) or [""]
        # carry open bold markers across wrapped lines
        open_b = False
        for w in wrapped:
            if open_b:
                w = "**" + w
            if w.count("**") % 2:
                w += "**"
                open_b = True
            else:
                open_b = False
            lines.append(" " * indent + w)
    return lines


class Term:
    def __init__(self, title):
        self.title = title
        self.rows = []      # list of list-of-spans
        self.frames = []    # (image, duration)

    def snap(self, ms, cursor=None):
        img = Image.new("RGB", (W, H), BG)
        d = ImageDraw.Draw(img)
        d.rectangle([0, 0, W, 34], fill=CHROME)
        for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
            d.ellipse([16 + i * 22, 11, 28 + i * 22, 23], fill=c)
        tw = TITLE.getlength(self.title)
        d.text(((W - tw) / 2, 10), self.title, font=TITLE, fill=DIM)
        view = self.rows[-ROWS:]
        for r, row in enumerate(view):
            x, y = PAD, TOP + r * LH
            for t, f, c in row:
                d.text((x, y), t, font=f, fill=c)
                x += f.getlength(t)
            if cursor and r == len(view) - 1:
                d.rectangle([x + 2, y + 2, x + CW, y + LH - 4], fill=ORANGE)
        self.frames.append((img, ms))

    def line(self, row_spans):
        self.rows.append(row_spans)

    def type_cmd(self, prefix, text, prefix_col=ORANGE, speed=4):
        """Type a command/prompt character by character, wrapping long prompts."""
        avail = COLS - len(prefix)
        chunks = textwrap.wrap(text, avail) or [""]
        first = True
        for ch in chunks:
            p = prefix if first else " " * len(prefix)
            self.rows.append([(p, BOLD, prefix_col), ("", REG, WHITE)])
            for i in range(0, len(ch), speed):
                self.rows[-1] = [(p, BOLD, prefix_col), (ch[: i + speed], REG, WHITE)]
                self.snap(45, cursor=True)
            first = False
        self.snap(450, cursor=True)

    def out(self, text, per_frame=2, ms=110, indent=2, base=FG):
        for l in wrap_md(text, indent):
            self.rows.append(spans(l, base))
            if len(self.rows) % per_frame == 0:
                self.snap(ms)
        self.snap(ms)

    def save(self, path):
        imgs = [f for f, _ in self.frames]
        durs = [d for _, d in self.frames]
        sample = [imgs[i] for i in sorted({0, len(imgs) // 3, 2 * len(imgs) // 3, len(imgs) - 1, len(imgs) - 2})]
        sheet = Image.new("RGB", (W, H * len(sample)))
        for i, im in enumerate(sample):
            sheet.paste(im, (0, H * i))
        # swatch strip guarantees accent colours survive quantization
        for i, c in enumerate([ORANGE, GREEN, BLUE, WHITE, DIM, (255, 95, 86), (255, 189, 46), (39, 201, 63)] + list(VERDICT.values())):
            sheet.paste(c, (i * 40, 0, i * 40 + 40, 30))
        pal = sheet.quantize(colors=160, method=Image.Quantize.MEDIANCUT)
        q = [im.quantize(palette=pal, dither=Image.Dither.NONE) for im in imgs]
        q[0].save(path, save_all=True, append_images=q[1:], duration=durs, loop=0, optimize=True, disposal=1)


def run(scene_path, out_path):
    global H, ROWS
    sc = json.load(open(scene_path))
    H = sc.get("h", H)
    ROWS = (H - TOP - 18) // LH
    t = Term(sc["title"])
    t.snap(600)
    for ev in sc["events"]:
        k = ev["k"]
        if k == "shell":
            t.type_cmd("$ ", ev["t"], GREEN)
        elif k == "prompt":
            t.type_cmd("> ", ev["t"])
        elif k == "tool":
            t.line([("● ", BOLD, GREEN), (ev["t"], BOLD, WHITE), ("  " + ev.get("d", ""), REG, DIM)])
            t.snap(ev.get("ms", 900))
        elif k == "say":
            for i, l in enumerate(wrap_md(ev["t"], 2)):
                lead = ("● ", BOLD, ORANGE) if i == 0 else ("  ", REG, FG)
                t.rows.append([lead] + spans(l[2:]))
                if i % ev.get("pf", 2) == 0:
                    t.snap(ev.get("ms", 110))
            t.snap(110)
        elif k == "text":
            t.out(ev["t"], ev.get("pf", 3), ev.get("ms", 90), indent=ev.get("i", 0), base=tuple(ev.get("c", FG)))
        elif k == "blank":
            t.line([])
        elif k == "pause":
            t.snap(ev["ms"])
    t.snap(sc.get("hold", 5000))
    t.save(out_path)
    print(out_path, len(t.frames), "frames")


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
