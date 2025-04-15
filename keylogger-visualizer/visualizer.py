from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os

os.makedirs("assets", exist_ok=True)

def update_stats(canvas):
    try:
        with open("logs/keylog.txt", "r") as f:
            keys = f.read().split()
        counter = Counter(keys).most_common(5)

        plt.clf()
        keys, counts = zip(*counter)
        plt.bar(keys, counts)
        plt.title("Top 5 Pressed Keys")
        plt.savefig("assets/stats.png")

        img = Image.open("assets/stats.png").resize((500, 300))
        img = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=img)
        canvas.image = img
    except:
        pass
