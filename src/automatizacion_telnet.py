import telnetlib
import time

HOST = "192.168.127.132"
PORT = 23
USER = "erik"
PASSWORD = "cisco"


def enviar(tn, comando):
    tn.write(comando.encode("ascii") + b"\n")
    time.sleep(1)
    respuesta = tn.read_very_eager().decode(
        "ascii", errors="ignore"
    )
    print(respuesta)


try:
    tn = telnetlib.Telnet(HOST, PORT, timeout=10)

    tn.read_until(b"Username:", timeout=5)
    tn.write(USER.encode("ascii") + b"\n")

    tn.read_until(b"Password:", timeout=5)
    tn.write(PASSWORD.encode("ascii") + b"\n")
    time.sleep(2)
    tn.read_very_eager()

    enviar(tn, "enable")
    enviar(tn, "terminal length 0")
    enviar(tn, "configure terminal")

    enviar(tn, "interface Loopback0")
    enviar(tn, "ip address 1.1.1.1 255.255.255.255")
    enviar(tn, "no shutdown")
    enviar(tn, "exit")

    enviar(tn, "interface Loopback1")
    enviar(tn, "ip address 2.2.2.2 255.255.255.255")
    enviar(tn, "no shutdown")
    enviar(tn, "exit")

    enviar(tn, "router ospf 1")
    enviar(tn, "network 1.1.1.1 0.0.0.0 area 0")
    enviar(tn, "network 2.2.2.2 0.0.0.0 area 0")
    enviar(tn, "end")
    enviar(tn, "write memory")

    tn.close()
    print("[+] Automatizacion finalizada")

except Exception as e:
    print(f"[-] Error: {e}")