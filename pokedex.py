import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

# TODO make a version of this that uses the API instead of web scraping

# idea, we could just scrape the data once and save locally in a json file to make lookup super easy

# get the pokemon whose id is in the entry field, clear the field, then display the data

def scrape(poke_id):
    poke_data = {}
    chromedriver_autoinstaller.install() # install and add to path
    driver = webdriver.Chrome()
    driver.get("https://pokemondb.net/pokedex/all")
    # use css selectors to find the nth child from the top of the html element that holds all of the rows
    row = driver.find_element(
        By.CSS_SELECTOR,
        f"tr:nth-child({poke_id})"
    )
    breakpoint()

    return poke_data



def get_pokemon():
    # get id from entry field and clear field
    poke_id = entry_var.get()  # TODO figure out how to get this to work
    # scrape website for data about the id
    poke_data = scrape(poke_id)
    

def run_gui():
    global entry_var
    window = tk.Tk()
    window.geometry("400x400")
    entry_var = tk.StringVar()

    l = tk.Label(text="poke ID: ")
    e = tk.Entry()
    b = tk.Button(text="get", command=get_pokemon, textvariable=entry_var)
    l.pack(); e.pack(); b.pack()
    window.mainloop()  # opens the window & runs event loop (blocking; listens for button clicks or keypresses)


def main():
    scrape(3)
    return

    run_gui()  # gui is initially empty, prompts user to enter a pokemon ID
    d = get_pokemon(poke_id)   # poke_id is what user submitted to the gui, this fn returns a dict of data about the pokemon
    # now need to put the data in d in the gui





if __name__ == "__main__":
    main()