import pyqrcode as qr
import png

s = "hi test"

url = qr.create(s)
url.svg("qrcode.svg", scale = 8)
url.png("qrcode.png", scale = 8)