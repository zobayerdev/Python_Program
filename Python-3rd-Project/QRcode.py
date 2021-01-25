import pyqrcode

from pyzbar.pyzbar import decode

from PIL import Image

qr = pyqrcode.create("coding with Nayem, I stays in Bangladesh")
qr = pyqrcode.create("Email:zobayer.hp3@gmail.com")


qr.png("mycode.png", scale = 10)

d= decode(Image.open("mycode.png"))
print(d[0].data.decode("ascii"))