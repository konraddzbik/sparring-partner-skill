"""Plugin icon and README banner for sparring-partner."""
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

BG = (13, 17, 23); ORANGE = (217, 119, 87); BLUE = (88, 166, 255); FG = (201, 209, 217); DIM = (125, 133, 144)
MENLO = "/System/Library/Fonts/Menlo.ttc"


def chevrons(d, cx, cy, s, w):
    # two opposing chevrons meeting in the middle: › ‹  (two sides, one exchange)
    g = s * 0.16
    d.line([(cx - g - s * 0.55, cy - s * 0.5), (cx - g, cy), (cx - g - s * 0.55, cy + s * 0.5)], fill=ORANGE, width=w, joint="curve")
    d.line([(cx + g + s * 0.55, cy - s * 0.5), (cx + g, cy), (cx + g + s * 0.55, cy + s * 0.5)], fill=BLUE, width=w, joint="curve")


def icon(path, n=1024):
    im = Image.new("RGB", (n, n), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([40, 40, n - 40, n - 40], radius=200, outline=(48, 54, 61), width=12)
    chevrons(d, n / 2, n / 2, n * 0.46, int(n * 0.075))
    im.save(path)


def banner(path, w=1600, h=480):
    im = Image.new("RGB", (w, h), BG)
    glow = Image.new("RGB", (w, h), BG)
    gd = ImageDraw.Draw(glow)
    gd.ellipse([w * 0.08, h * 0.1, w * 0.38, h * 0.9], fill=(70, 38, 30))
    gd.ellipse([w * 0.62, h * 0.1, w * 0.92, h * 0.9], fill=(24, 46, 72))
    im = Image.blend(im, glow.filter(ImageFilter.GaussianBlur(120)), 1.0)
    d = ImageDraw.Draw(im)
    chevrons(d, w / 2, h * 0.36, 150, 18)
    title = ImageFont.truetype(MENLO, 64, index=1)
    sub = ImageFont.truetype(MENLO, 26, index=0)
    t = "sparring-partner"
    d.text(((w - d.textlength(t, font=title)) / 2, h * 0.58), t, font=title, fill=(240, 246, 252))
    s = "AI that challenges your decisions instead of rubber-stamping them"
    d.text(((w - d.textlength(s, font=sub)) / 2, h * 0.58 + 90), s, font=sub, fill=FG)
    s2 = "asks before guessing  ·  holds its ground  ·  leaves the call with you"
    d.text(((w - d.textlength(s2, font=sub)) / 2, h * 0.58 + 132), s2, font=sub, fill=DIM)
    im.save(path, optimize=True)


icon(sys.argv[1]); banner(sys.argv[2])
