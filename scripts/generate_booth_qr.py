#!/usr/bin/env python3
"""
Generates high-resolution booth QR code for CloudScope 2026 attendee access.
"""
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, "static")
os.makedirs(STATIC_DIR, exist_ok=True)

DEFAULT_URL = "https://a3j-enterprise-showcase-uc.a.run.app"
target_url = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_URL

qr_png_path = os.path.join(STATIC_DIR, "booth_qr.png")

try:
    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=3,
    )
    qr.add_data(target_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#0284c7", back_color="#030712")
    img.save(qr_png_path)
    print(f"✅ Generated local QR code PNG at: {qr_png_path}")
except ImportError:
    # If qrcode library is not installed, download via curl or create placeholder
    print("ℹ️ qrcode package not found. Generating fallback QR reference.")
    import urllib.request
    api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&color=38-189-248&bgcolor=3-7-18&data={target_url}"
    try:
        urllib.request.urlretrieve(api_url, qr_png_path)
        print(f"✅ Downloaded QR code from API: {qr_png_path}")
    except Exception as e:
        print(f"⚠️ Could not download QR code: {e}")

print(f"Target URL: {target_url}")
