import numpy as np
from PIL import Image, ImageFilter
from colorsys import rgb_to_hsv

SRC = '/root/.claude/uploads/c615eec7-a712-5e9a-96bc-1e48fa2d1752/ba212651-image.png'
im = Image.open(SRC).convert('RGB')
a = np.asarray(im).astype(np.float32) / 255.0
R, G, B = a[..., 0], a[..., 1], a[..., 2]

mx = a.max(axis=-1); mn = a.min(axis=-1)
sat = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0.0)
lum = 0.2126 * R + 0.7152 * G + 0.0722 * B

# the red field is the only saturated area; everything else is neutral
red_mask = np.clip((sat - 0.16) / 0.18, 0, 1)

def ramp(t, stops):
    """t in 0..1 -> rgb via piecewise linear stops [(pos,(r,g,b)), ...] in 0..255"""
    pos = np.array([s[0] for s in stops], dtype=np.float32)
    cols = np.array([s[1] for s in stops], dtype=np.float32) / 255.0
    out = np.zeros(t.shape + (3,), dtype=np.float32)
    for c in range(3):
        out[..., c] = np.interp(t, pos, cols[:, c])
    return out

# neutrals -> deep graphite ramp (portfolio background family)
neutral_t = np.clip(lum, 0, 1)
neutral = ramp(neutral_t, [
    (0.00, (7, 8, 11)),
    (0.35, (18, 20, 25)),
    (0.65, (46, 50, 58)),
    (1.00, (92, 99, 110)),
])

# red field -> accent ramp, kept deep so overlaid text stays legible
rl = lum.copy()
lo, hi = np.percentile(rl[red_mask > 0.5], [5, 95]) if (red_mask > 0.5).any() else (0.0, 1.0)
red_t = np.clip((rl - lo) / max(hi - lo, 1e-6), 0, 1)
red = ramp(red_t, [
    (0.00, (58, 14, 16)),
    (0.45, (140, 32, 35)),
    (0.78, (214, 58, 61)),
    (1.00, (255, 77, 79)),
])

m = red_mask[..., None]
out = neutral * (1 - m) + red * m

img = Image.fromarray((np.clip(out, 0, 1) * 255).astype(np.uint8), 'RGB')
img = img.filter(ImageFilter.SMOOTH)
img.save('assets/bg-recolored.png')
print('wrote assets/bg-recolored.png', img.size)
