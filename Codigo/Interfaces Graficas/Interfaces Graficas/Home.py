import tkinter as tk
from tkinter import ttk

class HomeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Bienvenido a Casa")
        self.geometry("400x400")

        # Crear la lista de opciones
        self.option_list = tk.Listbox(self, height=10, selectmode=tk.SINGLE)
        self.option_list.pack(pady=20)
        self.option_list.insert(tk.END, "Editar informacion")
        self.option_list.insert(tk.END, "Consultar informacion")
        self.option_list.bind('<<ListboxSelect>>', self.open_option_window)

        # Crear el botón de salir
        self.exit_button = tk.Button(self, text="Salir", command=self.quit)
        self.exit_button.pack(pady=10)

        # Inicializar la ventana de opción
        self.option_window = None

    def open_option_window(self, event):
        selected_option = self.option_list.get(self.option_list.curselection())
        if self.option_window is None or not self.option_window.winfo_exists():
            self.option_window = OptionWindow(self, selected_option)
        else:
            self.option_window.update_option(selected_option)

    def execute_actions(self):
        print("Ejecutando acciones...")
        # Aquí puedes agregar la lógica para ejecutar las acciones

class OptionWindow(tk.Toplevel):
    def __init__(self, parent, option):
        super().__init__(parent)
        self.title(option)
        self.geometry("300x200")
        label = tk.Label(self, text=f"Ventana de {option}")
        label.pack(pady=20)

    def update_option(self, option):
        self.title(option)
        self.grab_set()

if __name__ == "__main__":
    app = HomeApp()
    app.mainloop()