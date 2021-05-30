from PIL import Pillow
img= Image.open("1604679777594.png")
blackAndwhite = img.convert("l")
blackAndwhite.save('bw_nayem.png')
blackAndwhite.show()
print("Complete")