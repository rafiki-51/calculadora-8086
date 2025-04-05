# logica.py

# Esta función calcula la dirección física según la arquitectura del 8086.
# Para eso, recibe el segmento y el offset (ambos en hexadecimal).
def calcular_direccion_fisica(segmento_hex, offset_hex):
    try:
        # Convierto el segmento de texto hexadecimal a entero.
        segmento = int(segmento_hex, 16)
        
        # Convierto el offset también a entero.
        offset = int(offset_hex, 16)
        
        # Para calcular la dirección física, multiplico el segmento por 16 (o lo desplazo 4 bits a la izquierda)
        direccion_fisica = (segmento << 4) + offset
        
        # Devuelvo el resultado en hexadecimal en mayúsculas, sin el prefijo "0X"
        return hex(direccion_fisica).upper().replace("0X", "")
    
    except ValueError:
        # Si el usuario pone algo que no es hexadecimal, devuelvo un mensaje de error
        return "Error: entrada inválida"

# Esta función convierte un número en decimal (string) a hexadecimal
def decimal_a_hex(decimal_str):
    try:
        # Convierto el número decimal de texto a entero
        decimal = int(decimal_str)
        
        # Lo convierto a hexadecimal, lo paso a mayúscula y le quito el prefijo "0X"
        return hex(decimal).upper().replace("0X", "")
    
    except ValueError:
        # Si el usuario pone algo que no es un número, devuelvo un mensaje de error
        return "Error: número decimal inválido"

# Esta función convierte un número en hexadecimal a decimal
def hex_a_decimal(hex_str):
    try:
        # Quito espacios, paso todo a mayúscula y elimino la "H" si el usuario la escribió
        valor = hex_str.strip().upper().replace("H", "")
        
        # Convierto el valor hexadecimal a decimal y lo devuelvo como texto
        return str(int(valor, 16))
    
    except ValueError:
        # Si el usuario puso algo que no es hexadecimal, devuelvo un mensaje de error
        return "Error: número hexadecimal inválido"
