import tkinter as tk
from tkinter import ttk

class UserManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestión de Usuarios")
        self.geometry("400x300")

        # Crear el icono de usuario
        self.user_icon = tk.PhotoImage(file="")  # Reemplaza con tu archivo de icono
        self.user_icon_label = tk.Label(self, image=self.user_icon)
        self.user_icon_label.pack(pady=10)

        # Crear los botones
        self.register_button = ttk.Button(self, text="Registrar un nuevo usuario", command=self.register_user)
        self.register_button.pack(pady=5)

        self.modify_button = ttk.Button(self, text="Modificar datos de un usuario", command=self.modify_user)
        self.modify_button.pack(pady=5)

        self.delete_button = ttk.Button(self, text="Borrar un usuario", command=self.delete_user)
        self.delete_button.pack(pady=5)

        self.exit_button = ttk.Button(self, text="Salir", command=self.quit)
        self.exit_button.pack(pady=10)

        # Crear la etiqueta de información del administrador
        self.admin_info_label = ttk.Label(self, text="Información Administrador")
        self.admin_info_label.pack(pady=10)

    def register_user(self):
        # Implementar la función para registrar un nuevo usuario
        print("Registrando un nuevo usuario...")

    def modify_user(self):
        # Implementar la función para modificar datos de un usuario
       print("Modificando datos de un usuario...")

    def delete_user(self):
        # Implementar la función para borrar un usuario
        print("Borrando un usuario...")

if __name__ == "__main__":
    app = UserManagementApp()
    app.mainloop()