import tkinter as tk
import selenium 



# idea, we could just scrape the data once and save locally in a json file to make lookup super easy

def init_gui():
    window = tk.Tk()
    window.geometry("400x400")

    l = tk.Label(text="poke ID: ")
    l.pack()
    e = tk.Entry()
    e.pack()
    window.mainloop()  # opens the window & runs event loop (blocking; listens for button clicks or keypresses)


def main():
    init_gui()  # gui is initially empty, prompts user to enter a pokemon ID
    return 
    d = get_pokemon(poke_id)   # poke_id is what user submitted to the gui, this fn returns a dict of data about the pokemon
    # now need to put the data in d in the gui





if __name__ == "__main__":
    main()