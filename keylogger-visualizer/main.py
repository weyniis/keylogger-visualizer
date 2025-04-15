import tkinter as tk
from monitor import start_keylogger
from visualizer import update_stats

def refresh_stats():
    update_stats(canvas)
    root.after(3000, refresh_stats)

root = tk.Tk()
root.title("Keylogger Visualizer")
root.geometry("600x400")

canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack(pady=20)

start_keylogger()
refresh_stats()

root.mainloop()
