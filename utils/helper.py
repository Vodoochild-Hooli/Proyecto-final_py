import os 
from colorama import init, Fore, Style

#inicializacion de colorama
init(autoreset=True)


def Limpiar_pantalla():
    """
    Limpia la pantalla de la consola.
    
    """
    os.system("cls" if os.name == "nt" else "clear")  #esto es un paraguas por si mi OS no es windows

def imprimir_error (texto):
    """
    Muestra un mensaje de error en color rojo,
    El parametro texto es la cadena que se pasa 
    para aplicarle este estilo.
    """
    print(f"{Fore.RED}[X] {texto}{Style.RESET_ALL}")

def imprimir_exito(texto):
    """
    Muestra un mensaje de éxito en color verde,
    indicando que una operación se realizó correctamente.
    El parametro texto es la cadena que se pasa 
    para aplicarle este estilo.
    """
    print(f"{Fore.GREEN}[✔] {texto}{Style.RESET_ALL}")

def imprimir_titulo(texto):
    """
    Imprime un título resaltado en color cyan y estilo brillante.
    El parametro texto es la cadena que se pasa 
    para aplicarle este estilo.
    """
    print(f"\n{Style.BRIGHT}{Fore.CYAN}{texto}{Style.RESET_ALL}")

def validar_input_string(prompt_input):
    """
    Valida el input del usuario 
    """
    while True:
        dato = input(f"{Fore.YELLOW}{prompt_input}: {Style.RESET_ALL}").strip()

        if dato:
            return dato
        else: imprimir_error("No puede estar vacio")

def validar_input_float (prompt_input):
    while True:
        try:
            dato = float(input(f"{Fore.YELLOW}{prompt_input}: {Style.RESET_ALL}"))
            if dato >= 0:
                return dato
            imprimir_error("Solo números positivos")
        except ValueError:
            imprimir_error("No debe estar vacio")

def validar_input_int(prompt_input):
    while True:
        try:
            dato = int(input(f"{Fore.YELLOW}{prompt_input}: {Style.RESET_ALL}"))
            if dato >= 0:
                return dato
            imprimir_error("Solo números positivos")
        except ValueError:
            imprimir_error("Ingrese un valor correcto")

