from commands import motivame, track_tiempo, focus, unfocus  
from colorama import init, Fore, Style 
init(autoreset=True)

comandos = {
    "!motivame": motivame.run,
    "!track tiempo": track_tiempo.run,
    "!focus": focus.run,
    "!unfocus": unfocus.run,
}

def main():
    print(Fore.MAGENTA + Style.BRIGHT + "🧙 Bienvenido a Magic Shell")
    print(Fore.CYAN + "Escribe un comando mágico. Usa !salir para cerrar.\n")

    while True:
        cmd = input(Fore.YELLOW + "🔮 > ").strip()
        if cmd in comandos:
            comandos[cmd]()
        elif cmd == "!salir":
            print(Fore.GREEN + "Hasta luego, hechicero ✨")
            break
        else:
            print(Fore.RED + "Comando no reconocido 🐍")

if __name__ == "__main__":
    main()
