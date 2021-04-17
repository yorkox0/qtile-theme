from funciones import dark_grey, dracula, material_ocean, material_darker, nord, nord_wave, onedark, rosepine
import os

themes = ["dark-grey", "dracula", "material-darker", "material-ocean", "nord", "nord-wave", "onedark", "rosepine"]

def main():
    print("Choose a Theme:\n")
    for choose in themes:
        print(choose)
    theme = input("\n-->> ")
    
    if theme == "dark-grey":
       dark_grey()

    if theme == "dracula":
        dracula()

    if theme == "material-darker":
        material_darker()

    if theme == "material-ocean":
        material_ocean()

    if theme == "nord":
        nord()

    if theme == "nord-wave":
        nord_wave()

    if theme == "onedark":
        onedark()

    if theme == "rosepine":
        rosepine()

main()
