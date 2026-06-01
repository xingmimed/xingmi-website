from PIL import Image
import os

# 从嵌入图裁切左右两半
img = Image.open('C:/Users/Administrator/WorkBuddy/Claw/xingmi-website/ew_embedded_0.png')
w, h = img.size
print(f'Full image: {w}x{h}')

# 裁切左半（X550EW或X500EW之一）
left = img.crop((0, 0, w//2, h))
right = img.crop((w//2, 0, w, h))

# 缩小到合适OCR的尺寸
def resize_for_ocr(im, max_w=1500):
    rw, rh = im.size
    if rw > max_w:
        ratio = max_w / rw
        im = im.resize((max_w, int(rh*ratio)), Image.LANCZOS)
    return im

left_r = resize_for_ocr(left)
right_r = resize_for_ocr(right)

left_r.save('C:/Users/Administrator/WorkBuddy/Claw/xingmi-website/ocr_left.png')
right_r.save('C:/Users/Administrator/WorkBuddy/Claw/xingmi-website/ocr_right.png')
print(f'Left: {left_r.size}, Right: {right_r.size}')
print('Left size:', os.path.getsize('C:/Users/Administrator/WorkBuddy/Claw/xingmi-website/ocr_left.png'))
print('Right size:', os.path.getsize('C:/Users/Administrator/WorkBuddy/Claw/xingmi-website/ocr_right.png'))
