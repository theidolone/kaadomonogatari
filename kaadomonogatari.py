import tkinter as tk
from tkinter import messagebox
import os, sys, random
#-------------------------------------------------------
if getattr(sys, 'frozen', False):
    cwd = os.path.dirname(sys.executable)

else:
    cwd = os.path.dirname(os.path.abspath(__file__))
#--------------------------------------------------------
def resource_path(relative_path):

    if getattr(sys, 'frozen', False):
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(sys.executable))

    else:
        base_path = cwd

    return os.path.abspath(os.path.join(base_path, relative_path))
#----------------------------------------------------------------------------------------------------------------------------------
lolis = {
    "images\\Hachikuji Mayoi.png" : "Hey mister, I need your credit card to buy love at the convenience store for ¥298!",
    "images\\Oshino Shinobu.png"  : "I assure you my master, I absolutely need your credit card to buy the new donut release from Mister Donuts. It's critical!" ,
    "images\\Sengoku Nadeko.png"  : "A-ah Onii-chan.. Can Nadeko p-please have your credit c-card..? I'll be good with it I s-swear..." ,
    "images\\Ononoki Yotsugi.png" : "Devil boy. I want to use your credit card for my own gain, I said with a posed look.",
}
#----------------------------------------------------------------------------------------------------------------------------------
def submit_event():
    global entry
    details = entry.get()
    subroot = tk.Tk()
    subroot.withdraw()
    subroot.attributes("-topmost", True)
    subroot.iconbitmap(resource_path("smirk.ico"))
    confirmation = tk.messagebox.askquestion(title="Confirm", message=f"Are these details correct?: '{details}'.")
    if confirmation == "yes":
        user = os.path.expanduser("~")
        joined = os.path.join(user, "Desktop\\details_file.txt")
        with open(joined, "a") as file:
            file.write(f"{details}\n")

        entry.delete(0, tk.END)
        subroot.destroy()
        root.destroy()

    else:
        entry.delete(0, tk.END)
        subroot.destroy()


def kaadomonogatari():
    display = random.choice(list(lolis.keys()))
    text = lolis[display]
#------------------------------------------------------------
    global root
    root = tk.Tk()
    root.title(os.path.splitext(os.path.basename(display))[0])
    root.iconbitmap(resource_path("smirk.ico"))
    root.attributes("-topmost", True)
#------------------------------------------------------------
    root.update_idletasks()
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    x = (root.winfo_screenwidth() // 2) - (w // 2)
    y = (root.winfo_screenheight() // 2) - (h // 2)

    root.minsize(450,200)
    root.geometry(f"{w}x{h}+{x}+{y}")
#-------------------------------------------------------------
    img = tk.PhotoImage(file=resource_path(display))
    img_label = tk.Label(root, image=img)
    img_label.grid(row=0, column=0, rowspan=3, padx=10, pady=10, sticky="n")

    text_label = tk.Label(root, text=text, wraplength=200, justify="center")
    text_label.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    global entry 
    entry = tk.Entry(root)
    entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

    button = tk.Button(root, text="Submit", command=submit_event)
    button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

    root.grid_columnconfigure(1, weight=1)

    root.img = img
#-------------------------------------------------------------
    root.mainloop()

kaadomonogatari()
