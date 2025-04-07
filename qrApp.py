import qrcode
from termcolor import colored

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_code = qr.make_image(fill_color="black", back_color="white")
    # qr_code.show()

    # Convert QR code to terminal-friendly format
    qr_terminal = qr.get_matrix()
    for row in qr_terminal:
        line = ''.join(['██' if cell else '  ' for cell in row])
        print(colored(line, 'black', 'on_white'))

if __name__ == "__main__":
    generate_qr_code("https://www.google.com")