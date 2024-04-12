import tkinter as tk
from tkinter import ttk

class UpdateApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Actualizar información")
        self.geometry("500x400")

        # Crear pestañas para contraseña y datos
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", padx=10, pady=10, expand=True)

        # Pestaña para actualizar contraseña
        self.password_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.password_tab, text="Actualizar contraseña")
        self.previous_password_label = ttk.Label(self.password_tab, text="Contraseña anterior:")
        self.previous_password_label.pack(pady=5)
        self.previous_password_value = tk.StringVar()
        self.previous_password_entry = ttk.Entry(self.password_tab, textvariable=self.previous_password_value, state="readonly")
        self.previous_password_entry.pack(pady=5)
        self.new_password_entry = ttk.Entry(self.password_tab, show="*")
        self.new_password_entry.pack(pady=5)
        self.update_password_button = ttk.Button(self.password_tab, text="Actualizar", command=self.update_password)
        self.update_password_button.pack(pady=5)

        # Pestaña para actualizar datos
        self.data_tab = ttk.Frame(self.notebook)
        self.notebook.add(self.data_tab, text="Actualizar datos")
        self.previous_data_label = ttk.Label(self.data_tab, text="Datos anteriores:")
        self.previous_data_label.pack(pady=5)
        self.previous_data_text = tk.Text(self.data_tab, height=5, width=40, state="disabled")
        self.previous_data_text.pack(pady=5)
        self.new_data_text = tk.Text(self.data_tab, height=5, width=40)
        self.new_data_text.pack(pady=5)
        self.update_data_button = ttk.Button(self.data_tab, text="Actualizar", command=self.update_data)
        self.update_data_button.pack(pady=5)

        # Botón para salir
        self.exit_button = ttk.Button(self, text="Salir", command=self.quit)
        self.exit_button.pack(pady=10)

        # Cargar información previa (simulada)
        self.previous_password_value.set("contraseña123")
        self.previous_data_text.insert("1.0", "Estos son los datos anteriores.\nPueden ser modificados.")
        self.previous_data_text.config(state="disabled")

    def update_password(self):
        new_password = self.new_password_entry.get()
        print(f"Nueva contraseña: {new_password}")

    def update_data(self):
        new_data = self.new_data_text.get("1.0", "end-1c")
        print(f"Nuevos datos:\n{new_data}")

if __name__ == "__main__":
    app = UpdateApp()
    app.mainloop()