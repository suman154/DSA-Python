colors = ['green', 'blue', 'red', 'purple', 'orange', 'yellow', 'black', 'white'] # n = 8

def quaditic(colors):
    for first in colors: # O(n)
        for second in colors: # O(n)
            print(first, second)


quaditic(colors)