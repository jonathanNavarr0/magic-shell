import time

def run():
    print("\n⏳ Cronómetro iniciado. Presiona Ctrl+C para detener.\n")
    start = time.time()
    try:
        while True:
            elapsed = time.time() - start
            mins, secs = divmod(int(elapsed), 60)
            print(f"\r🕒 Tiempo transcurrido: {mins:02d}:{secs:02d}", end="")
            time.sleep(1)
    except KeyboardInterrupt:
        end = time.time()
        total = round(end - start, 2)
        mins, secs = divmod(int(total), 60)
        print(f"\n\n⏱️  Sesión terminada. Total: {mins} min {secs} seg\n")
