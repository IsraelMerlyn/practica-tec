import random
import datetime

# Datos del ticket
tienda = "Tienda XYZ"
folio = random.randint(1000, 9999)  # Folio aleatorio de 4 dígitos
fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Fecha y hora actual

# Entrada del cliente
nombre_cliente = input("Ingresa tu nombre: ")
nombre_producto = input("Ingresa el nombre del producto: ")
total_compra = float(input("Ingresa el total de tu compra: "))

# Aplicar descuento si el total supera los 100
if total_compra > 100:
    descuento = total_compra * 0.10  # 10% de descuento
    total_final = total_compra - descuento
    descuento_texto = f"Descuento aplicado: ${descuento:.2f}"
else:
    total_final = total_compra
    descuento_texto = "No se aplica descuento."

# Imprimir el ticket
print("\n==================== TICKET DE COMPRA ====================")
print(f"Tienda: {tienda}")
print(f"Folio: {folio}")
print(f"Fecha y hora: {fecha}")
print("----------------------------------------------------------")
print(f"Cliente: {nombre_cliente}")
print(f"Producto: {nombre_producto}")
print(f"Total de la compra: ${total_compra:.2f}")
print(f"{descuento_texto}")
print(f"Total a pagar: ${total_final:.2f}")
print("\n----------------------------------------------------------")
print("¡Gracias por tu compra! ¡Vuelve pronto!")
print("===========================================================")
