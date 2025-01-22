import tkinter as tk
from PIL import Image, ImageTk
import requests

bg_color = "#c12026"

class PokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PokeApp")
        self.root.geometry("800x500")
        
        self.bg_img = Image.open("Assets/pokemonmainbg.jpg")
        self.bg_img = self.bg_img.resize((800, 500))
        self.poke_bg = ImageTk.PhotoImage(self.bg_img)
        tk.Label(self.root, image=self.poke_bg).place(relheight=1,relwidth=1)
        
        self.create_menu()
        
    def create_menu(self):
        self.menu_frame = tk.Frame(self.root, bg=bg_color)
        tk.Label(self.menu_frame, text="PokeApp", font=("Roboto", 50), bg=bg_color, fg="white").place(x=140,y=80)
        tk.Entry(self.menu_frame, text="", width=30).place(x=180,y=200)
        tk.Button(self.menu_frame, text="Search", font=("Roboto", 12), width=15).place(x=200,y=250)
        tk.Button(self.menu_frame, text="Random" , command=self.create_app, font=("Roboto", 12), width=15).place(x=200,y=300)
        tk.Button(self.menu_frame, text="Instruction", font=("Roboto", 12), width=15).place(x=200,y=350)
        self.menu_frame.place(x=0,y=0, width=500,height=500)
        
    def create_app(self):
        self.menu_frame.pack_forget()
        
        self.back_frame = tk.Frame(self.root)
        tk.Button(self.back_frame, text="<").grid(row=0,column=0)
        tk.Label(self.back_frame, text="Pokedex").grid(row=0,column=4)
        self.back_frame.grid(row=0,column=0)
        
        self.img_frame = tk.Frame(self.root)
        self.poke_img = tk.Canvas(self.img_frame, width=50, height=20)
        self.poke_img.pack()
        self.img_frame.pack()
        
        self.poke_frame = tk.Frame(self.root)
        self.poke_number = tk.Label(self.poke_frame, text="No. ")
        self.poke_number.pack()
        self.poke_name = tk.Label(self.poke_frame, text=" ")
        self.poke_name.pack()
        self.poke_type = tk.Label(self.poke_frame, text="Type: ")
        self.poke_type.pack()
        self.poke_frame.pack()
        
        self.detail_frame = tk.Frame(self.root)
        tk.Button(self.detail_frame, text="Info").pack()
        tk.Button(self.detail_frame, text="Stats").pack()
        tk.Button(self.detail_frame, text="Abilities").pack()
        self.poke_text = tk.Text(self.detail_frame, wrap = "word", width=50, height=10)
        self.poke_text.pack()
        self.poke_text.config(state="disabled")
        self.detail_frame.pack()
        
        self.bio_frame = tk.Frame(self.root)
        self.poke_bio = tk.Label(self.bio_frame, text="Bio:")
        self.poke_bio.pack()
        self.bio_frame.pack()

root = tk.Tk()
app = PokeApp(root)
root.mainloop()