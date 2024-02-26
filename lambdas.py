#the structure of an anonymous function
# lambda arguments: expression

#example 1
add = lambda x, y: x + y
print(add(5, 3))
# Output: 8

#example 2
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# Output: [1, 4, 9, 16]

#example 3
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4, 6]

#example 4
points = [(1, 2), (3, 1), (5, 0), (2, 3)]
points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)
# Output: [(5, 0), (3, 1), (1, 2), (2, 3)]


#using a lambda 
#Lambda functions are particularly useful in situations where a simple function is used temporarily 
# or for a short duration, and defining a full function using def would be unnecessarily verbose or complex.
#  They are often used with functions like map(), filter(), and sorted() as well as in frameworks and libraries,
#  especially in functional programming or when working with data.