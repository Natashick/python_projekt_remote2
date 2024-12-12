import time
import os

fire = ["o    ", " o   ", "  o  ", "   o ", "    o", "   o ", "  o  ", " o   "]

try:
    while True:
        for frame in fire:
            os.system("cls" if os.name == "nt" else "clear")  # Очистка экрана
            print(frame)
            time.sleep(0.2)
except KeyboardInterrupt:
    print("\nОгонь остановлен!") 
    