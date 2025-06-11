import os
from termcolor import colored, cprint

os.system("cls")

def pertamina_logo():
    logo = [
        "                            ",
        "               zzzzzzzz     ",
        "                zzzzzzzz    ",
        "                 zzzzzzzz   ",
        "                            ",
        "     wwwwwwww    mmmmmmmm   ",
        "    wwwwwwww    mmmmmmmm    ",
        "   wwwwwwww    mmmmmmmm     ",
        "  wwwwwwww                  ",
        " wwwwwwww                   ",
        "wwwwwwww                    " 
    ]

    
    # LOGO PERTAMINA
    for line in logo:
        posisi_logo = line.center(70)
        for pertamina in posisi_logo:
            if pertamina == "w":
                cprint(" ", "white", "on_blue", end="")
            elif pertamina =="m":
                cprint(" ", "white", "on_green", end="")
            elif pertamina =="z":
                cprint(" ", "white", "on_red", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "_main_":
    pertamina_logo() 

pertamina_logo()
print()
print(" "*18, "P  E  R  T  A  M  I  N  A")
print()