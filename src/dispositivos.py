
# Información del router R1
nombre_r1 = "R1"
tipo_r1 = "Router"
ip_r1 = "10.1.1.1"
loopback_r1 = "1.1.1.1"
interfaz_r1 = "GigabitEthernet0/0"
estado_r1 = "Activo"

# Información del router R2
nombre_r2 = "R2"
tipo_r2 = "Router"
ip_r2 = "10.1.1.2"
loopback_r2 = "2.2.2.2"
interfaz_r2 = "GigabitEthernet0/0"
estado_r2 = "Activo"

# Mostrar información de R1
print("=== Router R1 ===")
print("Nombre:", nombre_r1)
print("Tipo:", tipo_r1)
print("Dirección IP:", ip_r1)
print("Loopback:", loopback_r1)
print("Interfaz:", interfaz_r1)
print("Estado:", estado_r1)

# Mostrar información de R2
print("\n=== Router R2 ===")
print("Nombre:", nombre_r2)
print("Tipo:", tipo_r2)
print("Dirección IP:", ip_r2)
print("Loopback:", loopback_r2)
print("Interfaz:", interfaz_r2)
print("Estado:", estado_r2)


# Paso 6: Diccionario para representar R1
router1 = {
    "nombre": "R1",
    "tipo": "Router",
    "ip": "10.1.1.1",
    "loopback": "1.1.1.1",
    "interfaz": "GigabitEthernet0/0",
    "estado": "Activo"
}


# Paso 7: Consultar información de R1
print("Dispositivo:", router1["nombre"])
print("Dirección IP:", router1["ip"])
print("Estado:", router1["estado"])

# Mostrar toda la información del dispositivo
print("\n=== Información completa de R1 ===")
print("Nombre:", router1["nombre"])
print("Tipo:", router1["tipo"])
print("Dirección IP:", router1["ip"])
print("Loopback:", router1["loopback"])
print("Interfaz:", router1["interfaz"])
print("Estado:", router1["estado"])



# Lista de dispositivos con información adicional
dispositivos = [
    {
        "nombre": "R1",
        "tipo": "Router",
        "ip": "10.1.1.1",
        "estado": "Activo",
        "fabricante": "Cisco",
        "funcion": "Enrutamiento"
    },
    {
        "nombre": "R2",
        "tipo": "Router",
        "ip": "10.1.1.2",
        "estado": "Activo",
        "fabricante": "Cisco",
        "funcion": "Enrutamiento"
    },
    {
        "nombre": "S1",
        "tipo": "Switch",
        "ip": "10.1.1.3",
        "estado": "Activo",
        "fabricante": "Cisco",
        "funcion": "Conectividad"
    }
]



# Paso 9: Recorrer y mostrar la lista de dispositivos
print("\n=== Lista de dispositivos de la red ===")


# Paso 10: Identificar el estado de los dispositivos
print("\n=== Estado de los dispositivos ===")

for dispositivo in dispositivos:
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])

    if dispositivo["estado"] == "Activo":
        print("El dispositivo está disponible.")
    else:
        print("El dispositivo requiere atención.")

    print("--------------------")


# Paso 12: Mostrar información adicional
def mostrar_dispositivo(dispositivo):
    print("Nombre:", dispositivo["nombre"])
    print("Tipo:", dispositivo["tipo"])
    print("IP:", dispositivo["ip"])
    print("Estado:", dispositivo["estado"])
    print("Fabricante:", dispositivo["fabricante"])
    print("Función:", dispositivo["funcion"])

    if dispositivo["estado"] == "Activo":
        print("El dispositivo está disponible.")
    else:
        print("El dispositivo requiere atención.")
