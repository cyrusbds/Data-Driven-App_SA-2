import tkinter as tk
from PIL import Image, ImageTk
import requests

bg_color = "#c12026"

class PokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PokeApp")
        self.root.geometry("800x500")
        
        self.create_menu()
        
    def create_menu(self):
        
        self.bg_frame = tk.Frame(self.root)
        self.bg_img = Image.open("Assets/pokemonmainbg.jpg")
        self.bg_img = self.bg_img.resize((800, 500))
        self.poke_bg = ImageTk.PhotoImage(self.bg_img)
        self.bg_poke = tk.Label(self.bg_frame, image=self.poke_bg)
        self.bg_poke.pack()
        self.bg_frame.place(x=0, y=0)
        
        self.menu_frame = tk.Frame(self.root, bg=bg_color)
        tk.Label(self.menu_frame, text="PokeApp", font=("Roboto", 50), bg=bg_color, fg="white").place(x=140,y=80)
        tk.Entry(self.menu_frame, text="", width=30).place(x=180,y=200)
        tk.Button(self.menu_frame, text="Search", font=("Roboto", 12), width=15).place(x=200,y=250)
        tk.Button(self.menu_frame, text="Random", command=self.create_app, font=("Roboto", 12), width=15).place(x=200,y=300)
        tk.Button(self.menu_frame, text="Instruction", font=("Roboto", 12), width=15).place(x=200,y=350)
        self.menu_frame.place(x=0,y=0, width=500,height=500)
        
    def create_app(self):
        self.bg_frame.config(bg=bg_color)
        self.bg_poke.destroy()
        self.menu_frame.destroy()
        
        self.back_frame = tk.Frame(self.root, bg=bg_color)
        tk.Button(self.back_frame, text="<- Back", command=self.create_menu, font=("Roboto", 10)).place(x=10, y=15)
        tk.Label(self.back_frame, text="Pokedex", font=("Roboto", 30), bg=bg_color, fg="white").place(x=330, y=10)
        tk.Button(self.back_frame, text="Next ->", font=("Roboto", 10)).place(x=735, y=15)
        self.back_frame.place(x=0, y=0, width=800, height=50)
        
        self.img_frame = tk.Frame(self.root, bg=bg_color)
        self.poke_img = tk.Canvas(self.img_frame, width=250, height=250)
        self.poke_img.pack()
        self.img_frame.place(x=10, y=70, width=250, height=250)
        
        self.poke_frame = tk.Frame(self.root, bg=bg_color)
        self.poke_number = tk.Label(self.poke_frame, text="No. ", font=("Roboto", 15))
        self.poke_number.grid(row=0, column=0, padx=55)
        self.poke_name = tk.Label(self.poke_frame, text="Name: ", font=("Roboto", 15))
        self.poke_name.grid(row=0, column=1, padx=55)
        self.poke_type = tk.Label(self.poke_frame, text="Type: ", font=("Roboto", 15))
        self.poke_type.grid(row=0, column=2, padx=55)
        self.poke_frame.place(x=280, y=70, width=510)
        
        self.desc_bttn_frame = tk.Frame(self.root, bg=bg_color)
        tk.Button(self.desc_bttn_frame, text="Information", font=("Roboto",10), width=20).grid(row=0, column=0)
        tk.Button(self.desc_bttn_frame, text="Abilities", font=("Roboto", 10), width=20).grid(row=0, column=1)
        tk.Button(self.desc_bttn_frame, text="Statistics", font=("Roboto", 10), width=20).grid(row=0, column=2)
        self.desc_bttn_frame.place(x=280, y=110, width=510)
        
        self.desc_frame = tk.Frame(self.root, bg=bg_color)
        self.poke_text = tk.Text(self.desc_frame, wrap = "word", width=63, height=11)
        self.poke_text.pack()
        self.poke_text.config(state="disabled")
        self.desc_frame.place(x=280, y=138)
        
        self.bio_frame = tk.Frame(self.root, bg=bg_color)
        self.poke_bio = tk.Label(self.bio_frame, text=" ", width=780, height=160)
        self.poke_bio.pack()
        self.bio_frame.place(x=10, y=330, width=780, height=160)

root = tk.Tk()
app = PokeApp(root)
root.mainloop()