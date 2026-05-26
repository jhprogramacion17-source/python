============================================================
       ESCANER DE RED LOCAL (PORTABLE) - BY SIMON
============================================================

DESCRIPCION:
Este programa escanea la red local (WiFi o Ethernet) para 
identificar dispositivos conectados, mostrando su Direccion IP 
y su Nombre de Host.

------------------------------------------------------------
1. REQUISITOS OBLIGATORIOS (IMPORTANTE)
------------------------------------------------------------
Para que este programa funcione en CUALQUIER computadora, 
debe estar instalado el driver de red NPCAP:

Descarga: https://npcap.com/dist/npcap-1.79.exe

AL INSTALAR NPCAP:
Es vital marcar la casilla que dice:
"Install Npcap in WinPcap API-compatible Mode"

Sin este driver, el programa no podra detectar la tarjeta 
de red y se cerrara con un error.

------------------------------------------------------------
2. MODO DE USO
------------------------------------------------------------
- Si usas el archivo .EXE:
  Simplemente haz doble clic. El programa solicitara 
  permisos de Administrador automaticamente.

- Si usas el archivo .PY (Codigo Fuente):
  1. Instala la libreria Scapy: pip install scapy
  2. Ejecuta la terminal como Administrador.
  3. Corre el script: python wifi_scanner.py

------------------------------------------------------------
3. SOLUCION DE PROBLEMAS
------------------------------------------------------------
- El programa se cierra solo: 
  Verifica que instalaste Npcap con la opcion de 
  compatibilidad activada.
  
- El antivirus detecta el archivo como virus:
  Es un FALSO POSITIVO. Las herramientas de red creadas 
  en Python suelen ser marcadas por Windows Defender. 
  Debes dar permiso o exclusion al archivo.

- No aparecen nombres de dispositivos:
  Algunos celulares (iPhone/Android) ocultan su nombre 
  por privacidad. Es normal.

------------------------------------------------------------
Desarrollado por Simon.
Codigos_VS / Practica Python
============================================================
