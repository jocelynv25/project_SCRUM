import tkinter as tk
import cv2
from PIL import Image, ImageTk
class CameraApp(tk.Tk):
    def __init__(self):
        super().__init__()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        # Cambiar el icono de la ventana
        self.iconbitmap("Iconos/reconocimiento-facial.ico")

        #Cambiar Titulo de la Ventana
        self.title("Reconocimiento Facial")
        # Crear un lienzo para mostrar la imagen de la cámara
        self.canvas = tk.Canvas(width=screen_width, height=screen_height)
        self.canvas.pack(pady=1)

        # Inicializar la cámara
        self.cap = cv2.VideoCapture(0)  # 0 es la cámara predeterminada
        self.camera_open = True
        self.show_camera()

    def open_camera(self):
        if not self.camera_open:
            self.cap = cv2.VideoCapture(0)  # 0 es la cámara predeterminada
            self.camera_open = True
            self.show_camera()

    def show_camera(self):
        if self.camera_open:
            _, frame = self.cap.read()
            frame = cv2.flip(frame, 1)  # Voltear horizontalmente
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convertir a RGB

            # Escalar la imagen para que coincida con el tamaño del lienzo
            frame = cv2.resize(frame, (self.winfo_screenwidth(), self.winfo_screenheight()))

            # Mostrar la imagen en el lienzo
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
            self.canvas.image = img  # Mantener una referencia para evitar la recolección de basura

            # Llamar al método después de un corto retraso para actualizar continuamente
            self.after(10, self.show_camera)

        else:
            # Abrir un cuadro de texto para ingresar una contraseña
            self.password_entry = tk.Entry(self, show="*")
            self.password_entry.pack(pady=10)
            self.password_button = tk.Button(self, text="Ingresar", command=self.check_password)
            self.password_button.pack()

    def check_password(self):
        password = self.password_entry.get()
        # Aquí puedes implementar la lógica para verificar la contraseña
        if password == "contraseña_correcta":
            print("Contraseña correcta")
        else:
            print("Contraseña incorrecta")

if __name__ == "__main__":
    app = CameraApp()
    app.mainloop()