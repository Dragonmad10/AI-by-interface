import tkinter as tk
from tkinter import messagebox

class AppConMenus:
    def __init__(self, root):
        self.root = root
        self.root.title("App con Menús y Contadores")

        # Contadores
        self.contadores = {
            "Contador 1": 0,
            "Contador 2": 0,
            "Contador 3": 0
        }

        # Crear barra de menús
        self.crear_menus()

        # Frame para contadores
        self.frame_contadores = tk.Frame(root)
        self.frame_contadores.pack(padx=20, pady=20)

        # Crear contadores en la interfaz
        self.labels = {}
        self.crear_contadores()

        # Etiqueta para mostrar resultados
        self.resultado_label = tk.Label(root, text="", fg="blue", font=("Arial", 12))
        self.resultado_label.pack(pady=10)

    def crear_menus(self):
        menubar = tk.Menu(self.root)

        # Menú Archivo
        menu_archivo = tk.Menu(menubar, tearoff=0)
        menu_archivo.add_command(label="Salir", command=self.root.quit)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)

        # Menú Operaciones
        menu_operaciones = tk.Menu(menubar, tearoff=0)
        menu_operaciones.add_command(label="Sumar todos los contadores", command=self.sumar_contadores)
        menu_operaciones.add_command(label="Multiplicar todos los contadores", command=self.multiplicar_contadores)
        menubar.add_cascade(label="Operaciones", menu=menu_operaciones)

        # Menú Ayuda
        menu_ayuda = tk.Menu(menubar, tearoff=0)
        menu_ayuda.add_command(label="Acerca de", command=self.acerca_de)
        menubar.add_cascade(label="Ayuda", menu=menu_ayuda)

        self.root.config(menu=menubar)

    def crear_contadores(self):
        for i, nombre in enumerate(self.contadores.keys()):
            label = tk.Label(self.frame_contadores, text=f"{nombre}: {self.contadores[nombre]}", width=15)
            label.grid(row=i, column=1)
            self.labels[nombre] = label

            btn_sumar = tk.Button(self.frame_contadores, text="+", command=lambda n=nombre: self.modificar_contador(n, 1))
            btn_sumar.grid(row=i, column=2)

            btn_restar = tk.Button(self.frame_contadores, text="-", command=lambda n=nombre: self.modificar_contador(n, -1))
            btn_restar.grid(row=i, column=0)

    def modificar_contador(self, nombre, delta):
        self.contadores[nombre] += delta
        self.labels[nombre].config(text=f"{nombre}: {self.contadores[nombre]}")

    def sumar_contadores(self):
        resultado = sum(self.contadores.values())
        self.resultado_label.config(text=f"Suma de contadores: {resultado}")

    def multiplicar_contadores(self):
        resultado = 1
        for val in self.contadores.values():
            resultado *= val
        self.resultado_label.config(text=f"Multiplicación de contadores: {resultado}")

    def acerca_de(self):
        messagebox.showinfo("Acerca de", "App con menús y contadores interactivos\nCreada con Tkinter.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppConMenus(root)
    root.mainloop()
