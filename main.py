# Importo la librería tkinter para hacer la interfaz gráfica
import tkinter as tk

# Importo las funciones que programé en logica.py
from logica import calcular_direccion_fisica, decimal_a_hex, hex_a_decimal

# Esta función se ejecuta cuando el usuario presiona el botón "Calcular"
def calcular():
    # Obtengo el segmento y el offset ingresados en los campos de texto
    segmento = entry_segmento.get()
    offset = entry_offset.get()
    
    # Llamo a la función que calcula la dirección física
    resultado = calcular_direccion_fisica(segmento, offset)
    
    # Muestro el resultado en la etiqueta correspondiente
    label_resultado.config(text=f"Dirección física: {resultado}H")

# Esta función convierte un número decimal a hexadecimal
def convertir_a_hex():
    # Obtengo el valor decimal ingresado por el usuario
    valor = entry_decimal.get()
    
    # Llamo a la función que hace la conversión
    resultado = decimal_a_hex(valor)
    
    # Muestro el resultado en la etiqueta correspondiente
    label_hex_resultado.config(text=f"{resultado}H")

# Esta función convierte un número hexadecimal a decimal
def convertir_a_decimal():
    # Obtengo el valor hexadecimal ingresado
    valor = entry_hex.get()
    
    # Llamo a la función que hace la conversión
    resultado = hex_a_decimal(valor)
    
    # Muestro el resultado
    label_decimal_resultado.config(text=resultado)

# Esta función limpia todos los campos de entrada y salida
def limpiar_campos():
    # Borro el contenido del campo segmento
    entry_segmento.delete(0, tk.END)
    
    # Borro el contenido del campo offset
    entry_offset.delete(0, tk.END)
    
    # Borro el resultado de dirección física
    label_resultado.config(text="")

    # Borro el valor decimal ingresado
    entry_decimal.delete(0, tk.END)
    
    # Borro el resultado de la conversión a hex
    label_hex_resultado.config(text="")

    # Borro el valor hexadecimal ingresado
    entry_hex.delete(0, tk.END)
    
    # Borro el resultado de la conversión a decimal
    label_decimal_resultado.config(text="")

# Creo la ventana principal de la calculadora
ventana = tk.Tk()
ventana.title("Calculadora 8086")
ventana.geometry("350x500")  # Tamaño de la ventana

# ------------------ Sección: Cálculo de Dirección Física ------------------

# Etiqueta para el campo de segmento
tk.Label(ventana, text="Segmento (hex):").pack(pady=5)

# Campo de entrada para el segmento
entry_segmento = tk.Entry(ventana)
entry_segmento.pack()

# Etiqueta para el campo de offset
tk.Label(ventana, text="Offset (hex):").pack(pady=5)

# Campo de entrada para el offset
entry_offset = tk.Entry(ventana)
entry_offset.pack()

# Botón para calcular la dirección física
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

# Botón para limpiar todos los campos
tk.Button(ventana, text="Limpiar", command=limpiar_campos).pack(pady=5)

# Etiqueta donde se mostrará la dirección física
label_resultado = tk.Label(ventana, text="", font=("Courier", 12))
label_resultado.pack()

# ------------------ Sección: Conversión Decimal a Hex ------------------

# Etiqueta para indicar esta sección
tk.Label(ventana, text="Decimal a Hexadecimal:").pack(pady=15)

# Campo de entrada para el número decimal
entry_decimal = tk.Entry(ventana)
entry_decimal.pack()

# Botón para convertir decimal a hex
tk.Button(ventana, text="Convertir a Hex", command=convertir_a_hex).pack(pady=5)

# Etiqueta para mostrar el resultado en hex
label_hex_resultado = tk.Label(ventana, text="", font=("Courier", 12))
label_hex_resultado.pack()

# ------------------ Sección: Conversión Hex a Decimal ------------------

# Etiqueta para esta sección
tk.Label(ventana, text="Hexadecimal a Decimal:").pack(pady=15)

# Campo de entrada para el valor hexadecimal
entry_hex = tk.Entry(ventana)
entry_hex.pack()

# Botón para convertir hex a decimal
tk.Button(ventana, text="Convertir a Decimal", command=convertir_a_decimal).pack(pady=5)

# Etiqueta para mostrar el resultado en decimal
label_decimal_resultado = tk.Label(ventana, text="", font=("Courier", 12))
label_decimal_resultado.pack()

# Inicio del bucle principal de la aplicación
ventana.mainloop()
