import bcrypt

import bcrypt

# Hashear una contraseña
password = b"mi_super_secreta_contrasena"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

print(f"Contraseña hasheada: {hashed}")

# Verificar una contraseña
if bcrypt.checkpw(password, hashed):
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")
