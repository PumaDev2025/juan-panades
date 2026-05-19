"""
Generador de QR para Juan Luis Panades Molina
Al escanear el QR, el teléfono abre la página de contacto en GitHub Pages.
"""

import qrcode
from PIL import Image

# ─────────────────────────────────────────
#  DATOS DE CONTACTO  (edita aquí)
# ─────────────────────────────────────────
NOMBRE       = "Juan Luis Panades Molina"
CARGO        = "Gerente de Proyecto"
EMPRESA      = "Puga, Mujica Asociados S.A."
TELEFONO     = "+56933185960"
CORREO       = "jluispanades@gmail.com"
DIRECCION    = "Badajoz 45 Piso 5, Edificio Los Fundadores 2, Las Condes, Santiago, Chile"
WEB          = "https://www.pugamujica.cl/"
ARCHIVO_QR   = r"C:\Users\Public\qr_contacto\juan panades\qr_juan_panades.png"
# ─────────────────────────────────────────

URL_PAGINA   = "https://pumadev2025.github.io/juan-panades/"

print("── Contenido QR ─────────────────────────────")
print(URL_PAGINA)
print("─────────────────────────────────────────────\n")

# Generar el QR
qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=12,
    border=4,
)
qr.add_data(URL_PAGINA)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(ARCHIVO_QR)

print(f"✅ QR generado: {ARCHIVO_QR}")
print(f"   Tamaño imagen: {img.size[0]}x{img.size[1]} px")
print("\nEscanea el QR con la cámara del teléfono para abrir la página de contacto.")
