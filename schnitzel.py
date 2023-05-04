koordinaten = [
    (53.55137, 9.94706),    # Kreisel
    (53.5532, 9.952),    # Holstenpark
    (53.55857, 9.94533),    # Kaffee/Kuchen bei Torben
    (53.5585071, 9.9527782),    # Wohlerspark
    (53.55548, 9.96320),    # Schulhof Handelsschule
    (53.55225, 9.96363),    # Schnalke
    (53.55166, 9.95291)    # Grillen bei Hannes
]

names = [
    'Kreisel',
    'Holstenpark',
    'Torben',
    'Wohlerspark',
    'Schach',
    'Schnalke',
    'Hannes'
]


def generate_google_maps_link(coordinate):
    link = f"https://www.google.com/maps/place/{coordinate[0]},{coordinate[1]}"
    return link

links = [generate_google_maps_link(k) for k in koordinaten]


data = zip(links, names)
import os


def generate_qr_pdf(link, name):
    # Step 1: Calculate optimal QR code size
    a4_width = 2480  # A4 page width in pixels at 300 DPI
    qr_size = int(a4_width / 25)  # Divide by number of modules in QR code
    
    # Step 2: Generate QR code as PNG file
    os.system(f"qrencode -s {qr_size} -o {name}.png '{link}'")
    
    # Step 3: Convert PNG file to A4 wide PDF file
    os.system(f"convert -page A4 -compress jpeg -quality 90 {name}.png {name}.pdf")
    
    
    
    
    # Step 5: Return the path to the generated PDF file
    return f"{name}.pdf"


result = [generate_qr_pdf(link, name) for link, name in data]
print(result)

for link, name in zip(links, names):
    print(f"{name}: {link}")