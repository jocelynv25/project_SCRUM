import tkinter as tk
from tkinter import ttk

class PreviewApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Información previa")
        self.geometry("500x400")

        # Crear un área para mostrar la información previa
        self.preview_frame = ttk.LabelFrame(self, text="Información previa")
        self.preview_frame.pack(fill="both", padx=10, pady=10, expand=True)

        self.preview_text = tk.Text(self.preview_frame, height=10, width=40)
        self.preview_text.pack(pady=10)

        # Botón para salir
        self.exit_button = ttk.Button(self, text="Salir", command=self.quit)
        self.exit_button.pack(pady=10)

        # Cargar información previa (simulada)
        self.preview_text.insert("1.0", "Esta es la información previa guardada.\n\nEl usuario podrá implementar o modificar esta información manualmente después.")
        self.preview_text.config(state="disabled")

if __name__ == "__main__":
    app = PreviewApp()
    app.mainloop()