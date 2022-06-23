import tkinter as tk
import selenium 



# idea, we could just scrape the data once and save locally in a json file to make lookup super easy

def init_gui():
    window = tk.Tk()
    greeting = tk.Label(text="Hello, Tkinter")
    greeting.pack()
    window.mainloop()


def main():
    init_gui()  # gui is initially empty, prompts user to enter a pokemon ID
    return 
    d = get_pokemon(poke_id)   # poke_id is what user submitted to the gui, this fn returns a dict of data about the pokemon
    # now need to put the data in d in the gui





if __name__ == "__main__":
    main()