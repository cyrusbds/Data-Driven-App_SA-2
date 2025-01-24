import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import requests
import random
import pygame


main_bg_color = "#c12026"
app_bg_color = "#fb0605"

# Pokemon App Class
class PokeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PokeApp")
        self.root.geometry("800x500")
        self.root.config(bg=main_bg_color)
        
        # Play Music
        pygame.mixer.init()
        pygame.mixer.music.load("Assets/Poke_BG_Music.mp3")
        pygame.mixer.music.play(-1)
        
        self.create_menu()
        
    # Function to Create Menu
    def create_menu(self):
        # Menu Frame
        self.menu_frame = tk.Frame(self.root)
        tk.Label(self.menu_frame, text="PokeApp", font=("Helvetica", 50), bg=main_bg_color, fg="white").place(x=140,y=80)
        self.poke_entry = tk.Entry(self.menu_frame, width=15, font=("Helvetica", 20))
        self.poke_entry.place(x=160,y=180)
        tk.Button(self.menu_frame, text="Search", font=("Helvetica", 12), width=15, command=self.get_poke_info).place(x=200,y=250)
        tk.Button(self.menu_frame, text="Random", font=("Helvetica", 12), width=15, command=self.get_random_poke).place(x=200,y=300)
        tk.Button(self.menu_frame, text="Instruction", font=("Helvetica", 12), width=15, command=self.show_instructions).place(x=200,y=350)
        self.menu_frame.place(x=0, y=0, width=800, height=500)
        
        # Background Image for Menu Frame
        self.main_bg = Image.open("Assets/pokemonmainbg.jpg")
        self.main_bg = self.main_bg.resize((800, 500))
        self.main_poke_bg = ImageTk.PhotoImage(self.main_bg)
        self.main_bg_poke = tk.Label(self.menu_frame, image=self.main_poke_bg)
        self.main_bg_poke.pack()
        
    # Function to Create App
    def create_app(self):
        # Hide Menu Frame
        self.menu_frame.pack_forget()
        
        # App Frame
        self.app_frame = tk.Frame(self.root)
        
        # Background Image for App Frame
        self.app_bg = Image.open("Assets/pokemonappbg.jpg")
        self.app_bg = self.app_bg.resize((800, 500))
        self.app_poke_bg = ImageTk.PhotoImage(self.app_bg)
        self.app_bg_poke = tk.Label(self.app_frame, image=self.app_poke_bg)
        self.app_bg_poke.pack()
        
        self.top_frame = tk.Frame(self.root, bg=app_bg_color)
        self.top_frame.place(x=5, y=5, width=790, height=50)
        tk.Button(self.top_frame, text="<", command=self.create_menu, font=("Helvetica", 15), width=3, bg="black", fg="white").place(x=8, y=5)
        tk.Label(self.top_frame, text="Pokedex", font=("Helvetica", 30), bg=app_bg_color, fg="white").place(x=330, y=4)
        tk.Button(self.top_frame, text="Randomize", font=("Helvetica", 10), command=self.get_random_poke, bg="black", fg="white").place(x=705, y=10)
        
        # Display Pokemon Image
        self.poke_img = tk.Canvas(self.app_frame, width=240, height=240, bg=app_bg_color, highlightthickness=0)
        self.poke_img.place(x=25, y=50)
        
        # Details about the Pokemon
        self.poke_info_frame = tk.Frame(self.root, bg="white")
        self.poke_number = tk.Label(self.poke_info_frame, text="", font=("Helvetica", 17), bg="white", fg="black")
        self.poke_number.grid(row=0, column=0, padx=20, pady=5)
        self.poke_name = tk.Label(self.poke_info_frame, text="", font=("Helvetica", 17), bg="white", fg="black")
        self.poke_name.grid(row=0, column=1, padx=40, pady=5)
        self.poke_type = tk.Label(self.poke_info_frame, text="", font=("Helvetica", 17), bg="white", fg="black")
        self.poke_type.grid(row=0, column=2, padx=20, pady=5)
        self.poke_info_frame.place(x=280, y=70, width=510, height=40)
        
        tk.Button(self.app_frame, text="Information", font=("Helvetica",10), width=20, command=self.show_poke_info, bg="black", fg="white").place(x=280, y=120)
        tk.Button(self.app_frame, text="Abilities", font=("Helvetica", 10), width=20, command=self.show_poke_abilities, bg="black", fg="white").place(x=450, y=120)
        tk.Button(self.app_frame, text="Statistics", font=("Helvetica", 10), width=20, command=self.show_poke_stats, bg="black", fg="white").place(x=620, y=120)
        
        # Display the info, ability, and stats
        self.poke_text = tk.Text(self.app_frame, wrap = "word", width=46, height=7, font=("Helvetica", 15), bg="white", fg="black")
        self.poke_text.place(x=280, y=150)
        
        # Pokemon Description
        self.poke_bio = tk.Label(self.app_frame, text="", font=("Helvetica", 15), wraplength=600)
        self.poke_bio.place(x=200, y=330, width=590, height=160)
        self.app_frame.place(x=0, y=0, width=800, height=500)
        
    # Function to get pokemon details and randomize it
    def get_random_poke(self):
        random_url = "https://pokeapi.co/api/v2/pokemon/"
        random_poke = str(random.randint(1, 1025))

        response = requests.get(random_url + random_poke)

        random_data = response.json()
        random_info = {
            'name': random_data['name'].capitalize(),
            'number': random_data['id'],
            'height': random_data['height'],
            'weight': random_data['weight'],
            'types': [pokeType['type']['name'].capitalize() for pokeType in random_data['types']],
            'abilities': [pokeAbility['ability']['name'].capitalize() for pokeAbility in random_data['abilities']],
            'stats': {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in random_data['stats']},
            'image_url': random_data['sprites']['front_default']
        }
        self.current_poke_info = random_info
        self.create_app()
        self.display_poke(random_info)    
        
    # Function to get pokemon details
    def get_poke_data(self, pokemon_name):
        poke_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
        response = requests.get(poke_url)
        if response.status_code == 200:
            pokeData = response.json()
            return {
                'name': pokeData['name'].capitalize(),
                'number': pokeData['id'],
                'height': pokeData['height'],
                'weight': pokeData['weight'],
                'types': [pokeType['type']['name'].capitalize() for pokeType in pokeData['types']],
                'abilities': [pokeAbility['ability']['name'].capitalize() for pokeAbility in pokeData['abilities']],
                'stats': {stat['stat']['name'].capitalize(): stat['base_stat'] for stat in pokeData['stats']},
                'image_url': pokeData['sprites']['front_default']
            }
        else:
            return None

    # Function to get pokemon info from user entry
    def get_poke_info(self):
        pokemon_name = self.poke_entry.get()
        if pokemon_name:
            pokemon_info = self.get_poke_data(pokemon_name)
            if pokemon_info:
                self.current_poke_info = pokemon_info
                self.create_app()
                self.display_poke(pokemon_info)
            # Show error box if user inputs invalid pokemon name or Id number
            else:
                messagebox.showerror("Error: Invalid Pokemon Name or ID Number", f"{pokemon_name} is not a valid Pokemon Name or ID Number")
        else:
            messagebox.showerror("Error: Invalid Pokemon Name or ID Number", "Please Enter a Pokemon Name or ID Number")
        
    # Functions to get the description of pokemon from PokeAPI pokemon-species url
    def get_poke_desc(self, pokemon_id):
        species_url = f'https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}'
        response = requests.get(species_url)
        if response.status_code == 200:
            species_data = response.json()
            # Get the first English flavor text entry
            for entry in species_data['flavor_text_entries']:
                if entry['language']['name'] == 'en':
                    return entry['flavor_text']

    # Function to display pokemon
    def display_poke(self, pokemon_info):
        # Get pokemon image
        image_url = pokemon_info['image_url']
        if image_url:
            image = Image.open(requests.get(image_url, stream = True).raw)
            image = ImageTk.PhotoImage(image.resize((240, 240)))
            self.poke_img.create_image(120, 120, image = image)
            self.poke_img = image
            
        self.poke_name.config(text = f"{pokemon_info['name'].capitalize()}")
        self.poke_type.config(text = f"{' | '.join(pokemon_info['types'])}")
        self.poke_number.config(text = f"No. {pokemon_info['number']}")
        
        desc = self.get_poke_desc(pokemon_info['number'])
        self.poke_bio.config(text=desc)
        
    # Function to show Info
    def show_poke_info(self):
        poke_info = f"Weight: {self.current_poke_info['weight']}\nHeight: {self.current_poke_info['height']}"
        self.poke_text.config(state="normal")
        self.poke_text.delete("1.0", tk.END)
        self.poke_text.insert(tk.END, poke_info)
        self.poke_text.config(state="disabled")

    # Function to show Abilities
    def show_poke_abilities(self):
        poke_abilities = ", \n".join(self.current_poke_info['abilities'])
        self.poke_text.config(state="normal")
        self.poke_text.delete("1.0", tk.END)
        self.poke_text.insert(tk.END, f"Abilities: {poke_abilities}")
        self.poke_text.config(state="disabled")

    # Function to show Statistics
    def show_poke_stats(self):
        stats = "\n".join([f"{key}: {value}" for key, value in self.current_poke_info['stats'].items()])
        self.poke_text.config(state="normal")
        self.poke_text.delete("1.0", tk.END)
        self.poke_text.insert(tk.END, stats)
        self.poke_text.config(state="disabled")
    
    # Function to Show Instructions
    def show_instructions(self):
        messagebox.showinfo("How To Use PokeApp", "To begin using the PokeApp, type in a Pokemon name or ID number.\nFor example, type \"Pikachu\" or any number until 1025 into the searchbar.\nOr use the \"Random\" button to get a random Pokemon.")

root = tk.Tk()
app = PokeApp(root)
root.mainloop()