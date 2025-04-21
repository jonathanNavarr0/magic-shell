import platform
import os

def run():
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts" if platform.system() == "Windows" else "/etc/hosts"
    sitios = ["www.youtube.com", "www.instagram.com", "www.tiktok.com", "twitter.com"]

    print("\n🧘 Desactivando modo enfoque...")

    try:
        with open(hosts_path, "r") as file:
            lines = file.readlines()

        with open(hosts_path, "w") as file:
            for line in lines:
                if not any(sitio in line for sitio in sitios):
                    file.write(line)

        print("✅ Sitios desbloqueados. Puedes distraerte... pero con sabiduría 😅\n")
    except PermissionError:
        print("❌ No tienes permisos suficientes. Ejecuta el script como administrador.")
    except Exception as e:
        print(f"⚠️ Ocurrió un error: {e}")
