import subprocess

# 1. OBTENCIÓN DE DATOS BRUTOS
# Ejecutamos el comando de Windows 'netsh' para listar todos los perfiles WiFi guardados.
# 'shell=True' permite ejecutar el comando como si estuviéramos en el CMD.
# .decode(errors="ignore") convierte los bytes de salida en texto legible, ignorando caracteres extraños.
profiles_data = subprocess.check_output("netsh wlan show profiles", shell=True).decode(errors="ignore")

# 2. PROCESAMIENTO Y FILTRADO (Lógica de extracción)
# Creamos una lista vacía para almacenar solo los nombres de las redes.
names = []

# Recorremos cada línea de la respuesta que nos dio el sistema.
for line in profiles_data.split("\n"):
    # La línea que contiene el nombre de la red siempre tiene un ":" (ej. "Perfil de todos los usuarios : MiCasa_2.4G")
    if ":" in line:
        # Dividimos la línea en dos partes usando el ":" como separador y tomamos la segunda parte [1].
        # .strip() elimina espacios en blanco innecesarios al inicio y al final.
        name = line.split(":")[1].strip()
        
        # Si el nombre no está vacío, lo guardamos en nuestra lista.
        if name:
            names.append(name)

# 3. INTERFAZ DE USUARIO (Visualización)
if not names:
    print("No se encontraron redes Wi-Fi guardadas.")
else:
    print("--- REDES DISPONIBLES ---")
    # Mostramos las redes con un índice (1, 2, 3...) para que el usuario elija fácilmente.
    for i, n in enumerate(names, 1):
        print(f"[{i}] {n}")
    
    # 4. SELECCIÓN Y OBTENCIÓN DE LA CLAVE
    try:
        # Solicitamos el número al usuario y restamos 1 porque las listas en Python empiezan en 0.
        ch = int(input("\nSelecciona el número del perfil para ver la clave: "))
        wifi_name = names[ch-1]
        
        # Ejecutamos el comando 'key=clear' para que Windows muestre la contraseña en texto plano.
        # Usamos f-strings con comillas dobles "{wifi_name}" para manejar nombres de red que tengan espacios.
        result = subprocess.check_output(f'netsh wlan show profile "{wifi_name}" key=clear', shell=True).decode(errors="ignore")
        
        # 5. RESULTADO FINAL
        print("-" * 50)
        print(f"Información completa para la red: {wifi_name}")
        print("-" * 50)
        print(result)
        
    except (ValueError, IndexError):
        # Manejo de errores por si el usuario ingresa algo que no es un número o un índice inexistente.
        print("Error: Selección no válida.")

# Pausa final para que la ventana no se cierre de golpe si se ejecuta como .exe
input("\nPresiona Enter para salir...")