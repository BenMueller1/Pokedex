import tkinter as tk
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import chromedriver_autoinstaller

from functools import partial

# TODO make a version of this that uses the API instead of web scraping


poke_data = {}
poke_data["name"] = None
poke_data["types"] = None
poke_data["hp"] = None
poke_data["attack"] = None
poke_data["defense"] = None
poke_data["special attack"] = None
poke_data["special defense"] = None
poke_data["speed"] = None


def scrape(poke_id):
    poke_data = {} #name, types, hp, attack, defense, special attack, special defense, speed, image
    chromedriver_autoinstaller.install() # install and add to path
    driver = webdriver.Chrome()
    driver.get("https://pokemondb.net/pokedex/all")

    # close out of the ad notification that pops up when site is visited
    driver.find_element(
        By.CLASS_NAME,
        "btn-primary"
    ).click()

    # use css selectors to find the nth child from the top of the html element that holds all of the rows
    # scrolls down from poke-idth row until the id of the pokemon in the row matches poke-id
    row_id = 0
    i = poke_id-1
    while (row_id != poke_id):
        i += 1
        row = driver.find_element( 
            By.CSS_SELECTOR,
            f"tr:nth-child({i})"
        )
        row_id = row.find_element(
            By.CSS_SELECTOR,
            "span:nth-child(2)"
        ).text
        row_id = int(row_id)

    #breakpoint()
    row_data = row.find_elements(By.TAG_NAME, "td") 
    #breakpoint()
    poke_data["name"] = row_data[1].find_element(By.TAG_NAME, "a").text
    poke_data["types"] = [typ.text for typ in list(row_data[2].find_elements(By.TAG_NAME, "a"))]
    poke_data["hp"] = row_data[4].text
    poke_data["attack"] = row_data[5].text
    poke_data["defense"] = row_data[6].text
    poke_data["special attack"] = row_data[7].text
    poke_data["special defense"] = row_data[8].text
    poke_data["speed"] = row_data[9].text

    print(poke_data)
    driver.close()
    driver.quit()
    return poke_data



def get_pokemon(entry_var):
    global poke_data
    poke_id = entry_var.get()
    poke_data = scrape(int(poke_id))
    entry_var.set("") # clear entry firld

def run_gui():
    window = tk.Tk()
    window.geometry("400x400")
    entry_var = tk.StringVar()

    l = tk.Label(text="poke ID: ")
    e = tk.Entry(textvariable=entry_var)
    b = tk.Button(text="get", command=partial(get_pokemon, entry_var))
    l.pack(); e.pack(); b.pack(); 
    while True:
        l1 = tk.Label(text=f"Name: {poke_data['name']}")
        l2 = tk.Label(text=f"Types: {poke_data['types']}")
        l3 = tk.Label(text=f"HP: {poke_data['hp']}")
        l4 = tk.Label(text=f"Attack: {poke_data['attack']}")
        l5 = tk.Label(text=f"Defense: {poke_data['defense']}")
        l6 = tk.Label(text=f"Special Attack: {poke_data['special attack']}")
        l7 = tk.Label(text=f"Special Defense: {poke_data['special defense']}")
        l8 = tk.Label(text=f"Speed: {poke_data['speed']}")
        l1.pack(); l2.pack(); l3.pack(); l4.pack() 
        l5.pack(); l6.pack(); l7.pack(); l8.pack()
        window.mainloop()  # opens the window & runs event loop (blocking; listens for button clicks or keypresses)
    


def main():
    # TODO scrape(1) does not work
    # scrape(1)
    # scrape(5)
    #  return

    run_gui()  # gui is initially empty, prompts user to enter a pokemon ID
    # populate_gui(poke_data)




if __name__ == "__main__":
    main()