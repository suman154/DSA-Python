colors = ['green', 'blue', 'red', 'purple', 'orange', 'yellow', 'black', 'white'] # n = 8
other_colors = ['pink', 'brown', 'gray', 'magenta', 'cyan', 'beige', 'turquoise', 'violet'] # n = 8

def complex_algorithm(colors):
    color_count = 0 # O(1)


    for color in colors:
        print(color) # O(n)
        color_count += 1



    for other_color in other_colors:
        print(other_color)
        color_count += 1



    print(color_count) # O(1)

complex_algorithm(colors) # O(n) + O(n) + O(1) = O(n)




'''
Simplify Big O Notation
1. Remove Constants
O(4+2n+2m)->O(n+m)

2. Different terms for inputs
O(n+m)

3. Remove smaller terms
O(n+n^2)->O(n^2)

'''