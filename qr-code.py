import qrcode

def main():
    song = "https://youtu.be/s87moCuLxzw?si=-WoeQFm2-eZ9bRHX"
    qr = qrcode.QRCode(version=1, box_size=5, border=5,)
    qr.add_data(song)
    qr.make(fit=True)

    img = qr.make_image(fill_color="dimgray", back_color="white")
    img.save("My-qrcode.png")

if __name__=="__main__":
    main()
