import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.height = 0
        
        # Configuración de la ventana
        self.root.title("Confirmar Altura")
        self.root.geometry("400x300")

        # Crear una regla deslizante
        self.slider = tk.Scale(root, from_=0, to=200, orient=tk.HORIZONTAL)
        self.slider.set(0)
        self.slider.pack(pady=20)

        # Botón para confirmar altura
        self.confirm_button = tk.Button(root, text="Confirmar", command=self.confirm_height)
        self.confirm_button.pack()

    def confirm_height(self):
        self.height = self.slider.get()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

    # La altura confirmada se puede usar en otra parte del programa
    altura_confirmada = app.height
    print("La altura confirmada es:", altura_confirmada)
