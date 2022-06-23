import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

#chromedriver_autoinstaller.install() # install and add to path
#driver = webdriver.Chrome()

# idea, we could just scrape the data once and save locally in a json file to make lookup super easy

# get the pokemon whose id is in the entry field, clear the field, then display the data
def get_pokemon():
    # get id from entry field and clear field

    # scrape website for data about the id
    pass


def init_gui():
    window = tk.Tk()
    window.geometry("400x400")
    entry_var = tk.StringVar()

    l = tk.Label(text="poke ID: ")
    e = tk.Entry()
    b = tk.Button(text="get", command=get_pokemon)
    l.pack(); e.pack(); b.pack()
    window.mainloop()  # opens the window & runs event loop (blocking; listens for button clicks or keypresses)


def main():
    init_gui()  # gui is initially empty, prompts user to enter a pokemon ID
    return 
    d = get_pokemon(poke_id)   # poke_id is what user submitted to the gui, this fn returns a dict of data about the pokemon
    # now need to put the data in d in the gui





if __name__ == "__main__":
    main()