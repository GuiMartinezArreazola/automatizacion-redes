# Práctica 05: Automatización de redes con Python

## 1. Objetivo
Crear un script en Python para conectarse a un router Cisco mediante Telnet y automatizar su configuración.

## 2. Topología
Se utilizó GNS3 con los siguientes dispositivos:
- Network Automation Container (NAC)
- Switch Ethernet
- Switch Cisco IOSvL2 (S1)
- Router Cisco IOSv (R1)
- NAT

## 3. Configuración de red
- IP del NAC: `192.168.127.130/24`
- IP de R1: `192.168.127.132/24`
- Conexión de administración: Telnet, puerto 23

## 4. Script de Python
Archivo: `src/automatizacion_telnet.py`

El script se conecta al router, entra al modo de configuración y crea dos interfaces Loopback. Después configura OSPF, guarda la configuración e informa cuando termina.

## 5. Resultados
Se comprobó la conectividad entre el NAC y R1 mediante ping y se probó el acceso por Telnet. El script configuró correctamente:

- Loopback0: `1.1.1.1/32`
- Loopback1: `2.2.2.2/32`
- OSPF, proceso 1, área 0

## 6. Evidencias
Las capturas de la práctica se guardan en la carpeta `evidencias`.

## 7. Conclusión
Esta práctica me ayudó a entender cómo usar Python para conectarme a un router Cisco y automatizar tareas de configuración de red, ahorrando tiempo al ejecutar varios comandos desde un solo script.
