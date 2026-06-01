import fitz

doc = fitz.open('D:/\u753b\u518c\u6700\u7ec8\u7248/\u5236\u6c27\u673a\u5355\u9875/X550EW\u3001X500EW.pdf')
print('Pages:', doc.page_count)
for i, page in enumerate(doc):
    print(f'=== Page {i} ===')
    t1 = page.get_text('text')
    t2 = page.get_text('words')
    print('text len:', len(t1))
    print('words count:', len(t2))
    if t1.strip():
        print('TEXT:', repr(t1[:1000]))
    if t2:
        print('WORDS:', t2[:30])
    imgs = page.get_images()
    print('Images:', len(imgs))
    print('Size:', page.rect)
