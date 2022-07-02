from pdf2image import convert_from_path
import threading
#poppler diye bi uygulamanın yüklü olması lazım
def pdftoimg():
    #images = convert_from_path("123.pdf", 100,poppler_path=r'C:\Users\Kutuphane\Desktop\poppler-22.01.0\Library\bin')
    images = convert_from_path("123.pdf", 90)
    for i, image in enumerate(images):
        fname = 'image'+str(i)+'.png'
        print(i,". Sayfa Yazıldı")
        image.save(fname, "PNG")

#827-1170     100
#2481-3508      300
x = threading.Thread(target=pdftoimg)
x.start()
print("ProccessBaşladı")
