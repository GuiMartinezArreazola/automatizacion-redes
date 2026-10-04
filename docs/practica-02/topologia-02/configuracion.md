# Configuración de la Topología 2

## Dispositivos

- R1
- R2
- S1

## Direccionamiento IP

| Dispositivo | Interfaz | Dirección IP | Máscara |
|---|---|---|---|
| R1 | Gi0/0 | 10.1.1.1 | 255.255.255.0 |
| R1 | Loopback0 | 1.1.1.1 | 255.255.255.255 |
| R2 | Gi0/0 | 10.1.1.2 | 255.255.255.0 |
| R2 | Loopback0 | 2.2.2.2 | 255.255.255.255 |
| S1 | VLAN 1 | 10.1.1.3 | 255.255.255.0 |

## Configuración de los routers

Se configuraron las interfaces Gi0/0 de R1 y R2 con sus respectivas direcciones IP.

También se configuró una interfaz Loopback en cada router para representar una red adicional dentro de la topología.

## Configuración de OSPF

Se configuró el proceso OSPF 1 en los routers y se asignaron las redes correspondientes al área 0.

## Verificación

Se utilizó el comando:

`show ip ospf neighbor`

para comprobar la relación de vecindad entre R1 y R2.

También se utilizó:

`show ip route`

para revisar las redes conectadas y las rutas aprendidas mediante OSPF.

## Pruebas de conectividad

Se realizaron pruebas de ping entre R1 y R2 para comprobar la comunicación entre los dispositivos.