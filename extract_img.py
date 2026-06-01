import fitz
import os

doc = fitz.open('D:/\u753b\u518c\u6700\u7ec8\u7248/\u5236\u6c27\u673a\u5355\u9875/X550EW\u3001X500EW.pdf')
page = doc[0]
imgs = page.get_images(full=True)
print('Found', len(imgs), 'images')

for idx, img in enumerate(imgs):
    xref = img[0]
    pix = fitz.Pixmap(doc, xref)
    print(f'Image {idx}: {pix.width}x{pix.height}, colorspace={pix.colorspace}')
    if pix.n > 4:
        pix = fitz.Pixmap(fitz.csRGB, pix)
    out_path = f'C:/Users/Administrator/WorkBuddy/Claw/xingmi-website/ew_embedded_{idx}.png'
    pix.save(out_path)
    print(f'Saved: {out_path}, size: {os.path.getsize(out_path)} bytes')

# 也用高DPI渲染整页
mat = fitz.Matrix(4, 4)
clip = page.rect
pix2 = page.get_pixmap(matrix=mat, clip=clip)
out2 = 'C:/Users/Administrator/WorkBuddy/Claw/xingmi-website/ew_render_4x.png'
pix2.save(out2)
print(f'4x render: {pix2.width}x{pix2.height}, saved to {out2}')
