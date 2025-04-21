
import platform
import os

def run():
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if platform.system() == "Windows" else "/etc/hosts"
    redirect = "127.0.0.1"
    sitios = ["www.youtube.com", "www.instagram.com", "www.tiktok.com", "twitter.com"]

    print("\n🧘 Activando modo enfoque...")

    try:
        with open(hosts_path, "r+") as file:
            contenido = file.read()
            for sitio in sitios:
                if sitio not in contenido:
                    file.write(f"{redirect} {sitio}\n")
        print("✅ Sitios bloqueados. ¡Ahora a concentrarse!\n")
    except PermissionError:
        print("❌ No tienes permisos suficientes. Ejecuta el script como administrador.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error: {e}")
