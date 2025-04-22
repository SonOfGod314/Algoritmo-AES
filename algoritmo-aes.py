from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

# Gerando uma chave aleatória de 16 bytes (128 bits)
key = os.urandom(16)

# Inicialização do modo CBC (Cipher Block Chaining)
iv = os.urandom(16)  
cipher = AES.new(key, AES.MODE_CBC, iv)

# Mensagem a ser criptografada
mensagem = "Mensagem secreta"
mensagem_bytes = mensagem.encode()

# Criptografando
mensagem_criptografada = cipher.encrypt(pad(mensagem_bytes, AES.block_size))
print(" Mensagem Criptografada:", mensagem_criptografada.hex())

# Descriptografando
decipher = AES.new(key, AES.MODE_CBC, iv)
mensagem_descriptografada = unpad(decipher.decrypt(mensagem_criptografada), AES.block_size)
print(" Mensagem Descriptografada:", mensagem_descriptografada.decode())
