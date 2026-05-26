import scapy.all as scapy
import socket
import sys
import os

def obtener_rango_automatico():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Detecta la IP activa
        s.connect(("8.8.8.8", 80))
        mi_ip = s.getsockname()[0]
        rango = ".".join(mi_ip.split(".")[:-1]) + ".0/24"
        return mi_ip, rango
    except Exception:
        return None, None
    finally:
        s.close()

def obtener_nombre(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Oculto/Sin nombre"

def ejecutar_escaneo():
    # Banner de bienvenida
    print("="*60)
    print("         ESCÁNER DE RED LOCAL - VERSIÓN PORTABLE")
    print("="*60)

    mi_ip, rango = obtener_rango_automatico()
    
    if not rango:
        print("[!] ERROR: No se detectó conexión a la red.")
        input("\nPresiona Enter para salir...")
        return

    print(f"[*] Tu IP: {mi_ip}")
    print(f"[*] Escaneando: {rango}")
    print("-" * 60)
    print(f"{'DIRECCION IP':<18} | {'NOMBRE DEL DISPOSITIVO':<25}")
    print("-" * 60)

    try:
        # Ejecución del escaneo
        solicitud = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=rango)
        respuestas = scapy.srp(solicitud, timeout=3, verbose=False)[0]

        # Ordenar por IP (de menor a mayor)
        respuestas = sorted(respuestas, key=lambda x: x[1].psrc)

        for enviado, recibido in respuestas:
            ip_desc = recibido.psrc
            nombre = "ESTA PC (Simon)" if ip_desc == mi_ip else obtener_nombre(ip_desc)
            print(f"{ip_desc:<18} | {nombre:<25}")
            
        print("-" * 60)
        print(f"[*] Escaneo completado. {len(respuestas)} dispositivos activos.")

    except Exception as e:
        if "WinError 10049" in str(e) or "pcap" in str(e).lower():
            print("\n[!] ERROR CRÍTICO: Npcap no está instalado.")
            print("Por favor, instala Npcap desde https://npcap.com/")
        else:
            print(f"\n[!] Error inesperado: {e}")
            print("Asegúrate de ejecutar como ADMINISTRADOR.")

    print("\n" + "="*60)
    input("Presiona Enter para cerrar el programa...")

if __name__ == "__main__":
    ejecutar_escaneo()
