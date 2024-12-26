'''
Practicing with Big O Notation
In this exercise, you will keep practicing your understanding of Big O notation.

In the first step, you will create an algorithm that prints all the elements of the following list:

colors = ['green', 'yellow', 'blue', 'pink']
The algorithm will have an 
 complexity.

In the second and third steps, you will calculate the complexity of two algorithms.
'''

colors = ['green', 'yellow', 'blue', 'pink']

def linear(colors):
  # Iterate the elements of the list
  for color in colors:
    # Print the current element of the list
    print(color)	

linear(colors)