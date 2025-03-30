##############Creating a tuple##############

t1 = ()  # creates an empty tuple with no data
t2 = (11, 22, 33)
t3 = tuple([1, 2, 3, 4, 4])  # tuple from array
t4 = tuple("abc")  # tuple from string

print(t1) # ()
print(t2) # (11, 22, 33)
print(t3) # (1, 2, 3, 4, 4)
print(t4) # ('a', 'b', 'c')

#########Tuples functions#################
t1 = (1, 12, 55, 12, 81)
t2 = ( )
print(min(t1)) #1
print(max(t1)) # 81
print(sum(t1)) #161
print(len(t1)) #5
print(t1.count(12))
print(t1.index(81))
print(sorted(t1)) # Purpose: Returns a sorted list of the elements in the tuple.
print(any(t2)); print(any(t1))
# Purpose: Returns True if any element of the tuple is true. If the tuple is empty, returns False.
my_list = [1, 2, 3]
my_tuple = tuple(my_list)  # Output: (1, 2, 3)
print(my_tuple) # Purpose: Converts an iterable (like a list, string, etc.) into a tuple.

###Iterating through tuples###############
my_tuple1 = (11,22,33,44,55)

for i in my_tuple1:
    print(i, end=" ") #11 22 33 44 55 
# ----------------------------------------------------------
my_tuple2 = (10, 20, 30, 40, 50)
"""If you need both the index and the value, 
you can use the enumerate() function, 
which provides both:"""
for index, item in enumerate(my_tuple2):
    print(f"Index {index} has value {item}")
    # output => Index 0 has value 10
                 # Index 1 has value 20
                 # Index 2 has value 30
                 # Index 3 has value 40
                 # Index 4 has value 50
# ----------------------------------------------------------
"""If you have a tuple of tuples (or other nested structures),
 you can use nested loops to iterate through the elements:"""
nested_tuple = ((1, 2), (3, 4), (5, 6))

for inner_tuple in nested_tuple:
    for item in inner_tuple:
        print(item, end=' ') # output => 1 2 3 4 5 6
print("\n......................")
# ----------------------------------------------------------
"""You can also iterate through a tuple using a while loop with an index:"""
my_tuple3 = (10, 20, 30, 40, 50)
index = 0
while index < len(my_tuple3):
    print(my_tuple3[index])
    index += 1
# ....................********************...................................

#........ Iterating through tuples part2 .................
"""List Comprehensions with Tuples
Although list comprehensions are typically used to generate lists, 
they can also be used to iterate through tuples:"""
my_tuple4 = (10, 20, 30, 40, 50)

# Example: Create a list of the squares of each item in the tuple
squared = [item**2 for item in my_tuple4]
print(squared) # [100, 400, 900, 1600, 2500]
# ----------------------------------------------------------
"""Unpacking Tuples While Iterating
If each element in your tuple is itself a tuple 
(or another iterable with a fixed number of elements), 
you can unpack the elements directly in the loop:"""
coordinates = ((10, 20), (30, 40), (50, 60))
for x, y in coordinates:
    print(f"x: {x}, y: {y}")
# output =>
# x: 10, y: 20
# x: 30, y: 40
# x: 50, y: 60
# ----------------------------------------------------------

##########Slicing ###############
"""Basic Slicing:
Extract a portion of the tuple from index start to end-1."""
my_tuple = (10, 20, 30, 40, 50)
sliced_tuple = my_tuple[1:4]  # Output: (20, 30, 40)
print(sliced_tuple)
# ----------------------------------------------------------
sliced_tuple = my_tuple[:3]  # Output: (10, 20, 30)
print(sliced_tuple)
# ----------------------------------------------------------
""" Reversing the tuple:  """
reversed_tuple = my_tuple[::-1]  # Output: (50, 40, 30, 20, 10)


##########in  and not in  operator###########
t = (11,22,33,44,55)
print(22 in t) #True
print(22 not in t) #False















