import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

#ingresar datos para generar el codigo qr
data = input("Ingrese el texto para generar el codigo QR: ")
filename = input("Ingrese el nombre del archivo: ")

generate_qr_code(data, filename+".png")
print("El codigo QR se genero correctamente")
