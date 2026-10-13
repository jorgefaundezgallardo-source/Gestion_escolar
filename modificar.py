import urllib.request
import json
import base64

# 1. La URL de tu API para el docente 1
url = "http://127.0.0.1:8000/api/docentes/1/"

# 2. Los datos que queremos modificar (usaremos PATCH para cambiar solo el nombre)
datos = {"nombre": "Alan Modificado por API"}
data_json = json.dumps(datos).encode("utf-8")

# 3. Preparamos la petición
req = urllib.request.Request(url, data=data_json, method="PATCH")
req.add_header("Content-Type", "application/json")

# 4. Tus credenciales de administrador (Cámbialas si usaste otra contraseña)
credenciales = "jorge:123456a." 
auth = base64.b64encode(credenciales.encode("utf-8")).decode("utf-8")
req.add_header("Authorization", f"Basic {auth}")

# 5. Enviamos la petición y leemos la respuesta
try:
    respuesta = urllib.request.urlopen(req)
    print("¡MODIFICACIÓN EXITOSA! Código de estado:", respuesta.getcode())
    print("Respuesta de la Base de Datos:", respuesta.read().decode("utf-8"))
except Exception as e:
    print("Error de conexión:", e)