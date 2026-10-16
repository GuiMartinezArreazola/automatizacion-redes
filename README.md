# automatizacion-redes
# Mi estación de automatización de redes

## 1. Datos del equipo
## Integrantes:
Erik Meléndez Escobedo
Lázaro Ezequiel Escamilla Mendoza
Guillermo Martínez Arreazola
## Grupo:
3IRI2V
## Asignatura:
Automatización de Infraestructura Digital I
## Fecha: 
7 de Septiembre de 2026

---

## 2. Propósito de la práctica
Instalar y configurar diversas herramientas esenciales para preparar un entorno de desarrollo de software colaborativo y un laboratorio de redes virtuales para la automatización de redes, así como documentar todo el proceso de instalación y verificación

---

## 3. Herramientas instaladas
Durante la práctica se instalaron y verificaron las siguientes herramientas.
1. Python 3: Lenguaje de programación base para el desarrollo de scripts de automatización.
2. Visual Studio Code: Editor de código fuente integrado.
3. Git: Sistema de control de versiones distribuido.
4. Postman: Plataforma y cliente para desarrollo y pruebas de APIs.
5. OpenConnect: Cliente VPN para conexiones remotas.
6. Docker:*Plataforma de virtualización a nivel de sistema operativo para desplegar contenedores.
7. VMware Workstation Pro: Hipervisor de tipo 2 para ejecutar máquinas virtuales.
8. GNS3 GUI y GNS3 VM: Simulador gráfico de redes y su entorno virtual basado en Ubuntu.

---

## 4. Configuración realizada
Identidad de Git: Configuración global del nombre de usuario y correo electrónico asociado a GitHub.
Entorno Virtual en Python: Creación y activación de un entorno aislado dentro de la carpeta del proyecto 
Integración VS Code y Python: Instalación de la extensión oficial de Python y selección del intérprete/entorno virtual activo dentro del editor.
Integración GNS3 GUI y GNS3 VM: Importación de la plantilla en VMware Workstation y posterior habilitación y vinculación desde la interfaz gráfica de GNS3 

---

## 5. Verificación del entorno
Comprobación de versión de Python desde la terminal/Git Bash.
Ejecución correcta del primer script de prueba desde el entorno virtual en VS Code.
Verificación del servicio de Docker mediante la consulta de versión y ejecución de contenedores de prueba.
Verificación del encendido y comunicación adecuada entre GNS3 GUI y la VM en VMware Workstation.

---

## 6. Estructura del proyecto
La estructura de archivos y carpetas del repositorio local y remoto queda organizada de la siguiente manera:
```
automatizacion-redes/
│
├── README.md
│
├── requirements.txt
│
├── src/
│   └── hola_mundo.py
│
├── tests/
│
├── data/
│
└── docs/
    │
    └── practica-01/
        │
        ├── evidencias/
        │   ├── 01-python.png
        │   ├── 02-vscode.png
        │   ├── 03-python-vscode.png
        │   ├── 04-entorno-virtual.png
        │   ├── 05-hola-mundo.png
        │   ├── 06-git.png
        │   ├── 07-git-identidad.png
        │   ├── 08-github.png
        │   ├── 09-postman.png
        │   ├── 10-openconnect.png
        │   ├── 11-docker.png
        │   ├── 12-gns3.png
        │   ├── 13-gns3-vm.png
        │   ├── 14-vmware.png
        │   ├── 15-importacion-gns3-vm.png
        │   └── 16-integracion-gns3.png
        │
        ├── instalacion.md
        ├── configuracion.md
        └── verificacion.md
```

## 7. Problemas encontrados y soluciones
Por el momento no se presentaron problemas.

---

## 8. Conclusiones
La preparación previa de la estación de trabajo es un paso fundamental antes de abordar proyectos de automatización de redes. Herramientas como Python y VS Code nos brindan el entorno de codificación y depuración necesario; Git y GitHub aseguran un control de versiones colaborativo y trazabilidad; Docker y Postman facilitan las pruebas de servicios y APIs de red; mientras que GNS3 y VMware nos otorgan un laboratorio virtual robusto e integrador. Contar con un entorno estandarizado, virtualizado y aislado garantiza un desarrollo ágil, libre de conflictos de dependencias y fácil de replicar.


---

## 9. Práctica 2: Construcción de la red simulada en GNS3

### 9.1 Propósito de la práctica

Construir y configurar una infraestructura de red virtual utilizando GNS3, con el propósito de contar con un entorno de pruebas que posteriormente pueda ser utilizado para desarrollar y comprobar scripts de automatización de redes.

### 9.2 Actividades a realizar

Durante la práctica se trabajará con diferentes dispositivos y topologías de red dentro de GNS3.

1. Construcción de una topología básica utilizando dos PCs y un switch.
2. Configuración de direcciones IP en los dispositivos.
3. Realización de pruebas de conectividad mediante comandos de ping.
4. Construcción de una segunda topología utilizando dos routers y un switch.
5. Configuración de interfaces y direcciones IP en los routers.
6. Configuración de una interfaz Loopback en cada router.
7. Configuración de la dirección IP del switch.
8. Configuración del protocolo OSPF para permitir el intercambio de rutas entre los routers.
9. Verificación de los vecinos OSPF y de las tablas de enrutamiento.
10. Registro de las configuraciones, pruebas y resultados obtenidos durante la práctica.

### 9.3 Infraestructura a utilizar

La práctica utilizará GNS3 como entorno principal para crear una red virtual. Se trabajará con PCs, switches y routers virtuales, realizando las configuraciones necesarias para establecer comunicación entre los diferentes dispositivos.

### 9.4 Integración con el proyecto de automatización

La infraestructura creada servirá como laboratorio para las siguientes prácticas del proyecto. A partir de esta red será posible desarrollar y probar scripts de Python que permitan consultar información de los dispositivos y automatizar diferentes tareas de configuración.

### 9.5 Resultado esperado

Al finalizar la práctica se espera contar con una red virtual funcional, con conectividad entre los dispositivos y con OSPF configurado y verificado. Esta infraestructura quedará disponible como base para continuar con el desarrollo de las prácticas de automatización de redes.
