from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from base64 import b64encode, b64decode

def get_tt_param(text):
    password = 'webapp1.0+202106'
    text = text + '&is_encryption=1'
    print('''code by t.me/toolav''')
    iv = password.encode()
    password = password.encode()
    msg = pad(text.encode(), AES.block_size)
    cipher = AES.new(password, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(msg)
    out = b64encode(cipher_text).decode('utf-8')
    return out