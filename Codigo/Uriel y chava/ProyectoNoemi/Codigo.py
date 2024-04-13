import cv2
import numpy as np
from firebase_admin import db, credentials, initialize_app
import firebase_admin
from firebase_admin import storage
import urllib.request
import urllib.error
import tkinter as tk
from PIL import Image, ImageTk

# Inicializar Firebase
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "proyectorf-52d41",
    "private_key_id": "3aa6c7b8371eec97bc09d5aa34c161fa46c3ca08",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCxVOMEFbAbhn6q\nrMTkw38YrMZUUUAdd2DOMKcGuAEuDTw9D25TmVgxFFJCTwF1pOCw3EFLZM/bhb+u\nDBgpinGOklXzrDenS+M4qwvI12oT4fHwA2Q0p3E67WxWL3jyW3ixy3zPNmcJ1JPj\n/ch+13LkqzkEthQN2qJ1DoRLdpzgKQrJ6FlepnAJN0e40PJptoxHmCB7L/NqCAEM\nuMgoAqm4aKtnlM9EfG90lY1CXLCB/64lAHBbXokyp9CCY3d4wzkRxxXf/kK0apMQ\nbkZwjO6fEHw3uV1vnjFp97w0kbf+ZsWm36psv1535A3FpDNR0FOTAgi440AJWW8A\nJE8XpUjNAgMBAAECggEAKZZQRRF3AwWIKCurY0DryhQe0QBbCm4IMGLdkOhPMocd\nFO7M/2MLeTscTXusynO31BJbZ7yFOKTFvqIMepWCqx5rdOFzDdNwvsXyVhAayv3m\nmNSax/RqzBiJGy837JKCHCQuKYRHJtmJM2M9hW2ufq0fCplO267mAZC9etse0Dy7\nOE1g1NscvaBDbhaE4RfcscHupIXDlcyjIWR0ojBpRAWxqHXacAyPznIYIhHwf5CW\nSjdFeGGaJnNqsKoxCRyVEinF4yyHnkrtp/c8cABo4XhB6keCiafw3S57ZcC6dAtl\nPhica0OilyMyuvezKw/i5idMKX9mnTLmDjELkghhgQKBgQDu9uqXdymCeRlgJdxA\n6m97UjVLTAcQiCqg+fH3tpFLPwqzsyNRtDZSQ+YnwUfhPbb0LrZXYjmTkXl3gj5z\ncZuRS6KZrZ1Z4qHNWyUUZFxf8rJrkvMjT/AKESoqEjlwfwIWgLo9AR1LON83B8Xj\nPjrqJw8ZZLvpSpkeps6+Q7+RDQKBgQC9+SygUBMCMBnjtDPpwrCyNPHUTVv4M41b\n+bLzejYwkfxf/N+S9/fU3jzf1Ytku4iuUpKw86FB0KAmYWlR9UFz+hiohS/iiN7I\n11/9yMiujjvYr5xMNbVsgqm7vOOKKyO8eWfNg1nSgbTIP3TCV9cr+cZOpe90czkE\nr5iLgTUmwQKBgQDcnOiHXWPdKJ/cvBdTdxvk5kh9c3syMAPrCdXxs4L/zPu8Wy3I\nSG++EyFwomgR8j/tvxJoKi6tpihVxNCTE9djlEhRSI90ZF6sj/DzmpQNoKpH1irR\n9wLMyHv8y0ZsLVVoIP/PQjAhOigZTfvLh7AsbFLsRquU/WHPgoBr92/sIQKBgGNM\na1cgg88Q9XdgKgJ2EYYUxpMCHKCP0cPRsQgzST/6DsDdnL9lfdV2lLsrE8GDhN4Z\nqzNzJUcRlaR6JmMAn0XP5DOx6mWuxUSVz0cIPF2BWybYJApxyHL/mVjYUtdV1Uge\n7XMuxTSTN7uz74PmBkKmPFG/ynpD//nDDylcUDwBAoGBAJ0mVAv3X1aQIJzNM8AN\n6I3+Ac6zqG7pZaphw1cR26WHw7/+3r5k48+7yPa7SRHXg/elwkA9/omy5QZc1ss1\nIXaDEm1cR7ekhp8854GEOitZkdIE/bosTrwo4jMaGaYCGFby/SJqZy01cBQrbPeG\nth+id/oiPfNXlQAwApw/htqr\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-vonb4@proyectorf-52d41.iam.gserviceaccount.com",
    "client_id": "112944908226093822334",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-vonb4%40proyectorf-52d41.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
})

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://proyectorf-52d41-default-rtdb.firebaseio.com/',
    'storageBucket': 'proyectorf-52d41.appspot.com'  # Solo proporciona el nombre del bucket
})

# Crear ventana principal de Tkinter
root = tk.Tk()
root.title("Interfaz de Usuarios")

# Capturar imagen de la cámara
def capturar_imagen():
    # Abrir la cámara
    cap = cv2.VideoCapture(0)

    # Capturar cuadro por cuadro
    ret, frame = cap.read()

    # Guardar el cuadro capturado como imagen
    ruta_imagen = "captured_image.jpg"
    cv2.imwrite(ruta_imagen, frame)

    # Liberar la cámara
    cap.release()

    return ruta_imagen

# Almacenar datos en Firebase
def almacenar_datos(nombre, edad, contacto, ruta_imagen):
    # Push datos a Firebase
    ref = db.reference('usuarios')
    nuevo_usuario_ref = ref.push()
    nuevo_usuario_ref.set({
        'nombre': nombre,
        'edad': edad,
        'contacto': contacto,
        'imagen_url': ''  # La URL se actualizará después de almacenar la imagen
    })

    # Obtener el ID del nuevo usuario
    usuario_id = nuevo_usuario_ref.key

    # Subir imagen a Firebase Storage
    storage_path = f"images/{usuario_id}.jpg"  # Path en Firebase Storage
    bucket = storage.bucket()
    blob = bucket.blob(storage_path)
    blob.upload_from_filename(ruta_imagen)

    # Actualizar la URL de la imagen en la base de datos
    imagen_url = blob.public_url
    nuevo_usuario_ref.update({'imagen_url': imagen_url})

# Recuperar y mostrar datos desde Firebase
def recuperar_datos():
    ref = db.reference('usuarios')
    snapshot = ref.get()

    print("Usuarios:")
    for i, (usuario_id, usuario_data) in enumerate(snapshot.items(), 1):
        print(f"{i}. ID Usuario: {usuario_id}")
        print(f"   Nombre: {usuario_data['nombre']}")
        print(f"   Edad: {usuario_data['edad']}")
        print(f"   Contacto: {usuario_data['contacto']}")
        print(f"   Imagen URL: {usuario_data['imagen_url']}")
        print()

    # Elegir usuario por índice
    seleccion = int(input("Seleccione el usuario por su índice (ingrese 0 para cancelar): "))
    if seleccion == 0:
        return  # Cancelar la operación si el usuario elige 0

    # Obtener el ID del usuario seleccionado
    usuario_id = list(snapshot.keys())[seleccion - 1]

    # Mostrar imagen del usuario seleccionado en una nueva ventana
    mostrar_imagen_usuario(snapshot[usuario_id])

# Mostrar imagen del usuario en una nueva ventana
def mostrar_imagen_usuario(usuario_data):
    # Crear una nueva ventana
    ventana_usuario = tk.Toplevel(root)
    ventana_usuario.title("Detalles del Usuario")

    # Obtener la imagen del usuario desde la URL
    url_imagen = usuario_data['imagen_url']
    img = urllib.request.urlopen(url_imagen)
    img_array = np.array(bytearray(img.read()), dtype=np.uint8)
    imagen = cv2.imdecode(img_array, -1)

    # Convertir la imagen a formato adecuado para Tkinter
    imagen_tk = ImageTk.PhotoImage(Image.fromarray(imagen))

    # Mostrar la imagen en un widget Label
    label_imagen = tk.Label(ventana_usuario, image=imagen_tk)
    label_imagen.pack()

    # Mostrar los datos del usuario debajo de la imagen
    detalles_usuario = f"Nombre: {usuario_data['nombre']}\nEdad: {usuario_data['edad']}\nContacto: {usuario_data['contacto']}"
    label_detalles = tk.Label(ventana_usuario, text=detalles_usuario)
    label_detalles.pack()

    # Establecer la imagen en la ventana destruyendo la variable Tkinter
    ventana_usuario.image = imagen_tk

# Función principal
def principal():
    while True:
        print("Menú:")
        print("1. Agregar nuevo usuario")
        print("2. Recuperar usuario existente")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Capturar imagen
            ruta_imagen = capturar_imagen()

            # Recolectar otros datos
            nombre = input("Ingrese el nombre: ")
            edad = input("Ingrese la edad: ")
            contacto = input("Ingrese el contacto: ")

            # Almacenar datos en Firebase
            almacenar_datos(nombre, edad, contacto, ruta_imagen)
        elif opcion == "2":
            # Recuperar y mostrar datos
            recuperar_datos()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

# Ejecutar la función principal
if __name__ == "__main__":
    principal()

# Iniciar el bucle de eventos de Tkinter
root.mainloop()

