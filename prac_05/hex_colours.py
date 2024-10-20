"""
CP1404 Practical
State names in a dictionary
File needs reformatting
"""

COLOR_TO_CODE = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                 "alizarin crimson":"#e32636",
                 "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc", "antiquewhite": "#faebd7",
                 "aqua": "#00ffff", "aureolin": "#fdee00"}
for key in COLOR_TO_CODE:
    print(f"{key.title(): <3} is {COLOR_TO_CODE[key]}")

color = input("Enter color: ").lower()
while color != "":
    try:
        print(color, "is", COLOR_TO_CODE[color])
    except KeyError:
        print("Invalid color name")
    color = input("Enter color: ").lower()