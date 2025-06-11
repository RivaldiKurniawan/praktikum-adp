import os
from termcolor import colored, cprint

os.system("cls")

def adidas_logo():
    logo = [
        "                      W                 ",
        "                    wWWW                ",
        "                  WWWWWWWW              ",
        "                   WWWWWWWW             ",
        "               W    WWWWWWWW            ",
        "            wwWWW    WWWWWWWW           ",
        "          WWWWWWWW    WWWWWWWW          ",
        "           WWWWWWWW    WWWWWWWW         ",
        "            WWWWWWWW    WWWWWWWW        ",
        "       W     WWWWWWWW    WWWWWWWW       ",
        "     WWWW     WWWWWWWW    WWWWWWWW      ",
        "   WWWWWWWW    WWWWWWWW    WWWWWWWW     ",
        "    WWWWWWWW    WWWWWWWW    WWWWWWWW    ",
        "     WWWWWWWW    WWWWWWWW    WWWWWWWW   "
       
    ]

    
    # LOGO ADIDAS
    for line in logo:
        posisi_logo = line.center(70)
        for adidas in posisi_logo:
            if adidas != " ":
                cprint(" ", "white", "on_white", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "_main_":
    adidas_logo()

adidas_logo()
print()
print(" "*27, "A  D  I  D  A  S")
print()