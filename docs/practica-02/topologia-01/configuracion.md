# Configuración de la Topología 1

## Dispositivos

- PC1
- Switch
- PC2

## Direccionamiento IP

| Dispositivo | Dirección IP | Máscara |
|---|---|---|
| PC1 | 10.1.1.1 | 255.255.255.0 |
| PC2 | 10.1.1.2 | 255.255.255.0 |

## Configuración

Se configuró la dirección IP de PC1 como 10.1.1.1/24 y la de PC2 como 10.1.1.2/24.

Los dispositivos fueron conectados mediante el switch para permitir la comunicación entre ambas PCs.

## Pruebas de conectividad

Se realizaron pruebas mediante ping desde PC1 hacia PC2 y desde PC2 hacia PC1.

- PC1 → PC2: conectividad comprobada.
- PC2 → PC1: conectividad comprobada.