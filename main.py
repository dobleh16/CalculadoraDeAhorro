import tkinter as tk
from tkinter import messagebox


def calcular_ahorro_diario():
    try:
        meta = float(entry_meta.get())
        dias = int(entry_dias.get())

        if dias <= 0:
            raise ValueError("El número de días debe ser mayor que 0.")

        ahorro_diario = meta / dias
        label_resultado.config(text=f"Necesitas Ganar o Ahorrar {ahorro_diario:.2f} por día.")
    except ValueError as e:
        messagebox.showerror("Entrada inválida", f"Por favor, ingresa valores válidos. {str(e)}")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Ahorro Diario")

# Crear y colocar los widgets
label_meta = tk.Label(ventana, text="Meta de Ahorro:")
label_meta.pack(pady=5)

entry_meta = tk.Entry(ventana)
entry_meta.pack(pady=5)

label_dias = tk.Label(ventana, text="Días para alcanzar la meta:")
label_dias.pack(pady=5)

entry_dias = tk.Entry(ventana)
entry_dias.pack(pady=5)

boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_ahorro_diario)
boton_calcular.pack(pady=10)

label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
