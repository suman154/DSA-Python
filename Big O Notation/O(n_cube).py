colors = ['green', 'blue', 'red', 'purple', 'orange', 'yellow', 'black', 'white'] # n = 8

def cubic(colors):
    for color1 in colors:
        for color2 in colors:
            for color3 in colors:
                print(color1, color2, color3)


cubic(colors)