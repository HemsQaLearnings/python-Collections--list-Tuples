#===============Creating Lists
list1 = list() # Create an empty list
list2 = list([22, 31, 61]) # Create a list with elements 22, 31, 61
list3 = list(["tom", "jerry", "spyke"]) # Create a list with strings
list4 = list("python") # Create a list with characters p, y, t, h, o, n

print(list1)
print(list2)
print(list3)
print(list4)

#===========Accessing elements in list
l = [1,2,3,4,5]
print(l[1]) # access second element in the list 2
print(l[0]) # access first element in the list 1

#==========List Common Operations

list1 = [2, 3, 4, 1, 32]

print(2 in list1) # True
print(33 not in list1) #True
print(len(list1)) # find the number of elements in the list 5
print(max(list1)) # find the largest element in the list 32
print(min(list1)) # find the smallest element in the list 1
print(sum(list1)) # sum of elements in the list 42

#============List slicing
list = [11,33,44,66,788,1]
print(list[0:5])
# this will return list starting from index 0 to index 4 [11,33,44,66,788]
print(list[:3])
#Similar to string start index is optional, if omitted it will be 0.

print(list[2:])
#end index is also optional,
# if omitted it will be set to the last index of the list.
# [44,66,788,1]


#=========+  and *  operators in list

#+  operator joins the two list.
list1 = [11, 33]
list2 = [1, 9]
list3 = list1 + list2
print(list3) #[11, 33, 1, 9]

#*  operator replicates the elements in the list.
list4 = [1, 2, 3, 4]
list5 = list4 * 3
print(list5) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]


#=======in  or not in operator=========

list1 = [11, 22, 44, 16, 77, 98]

print(22 in list1) #True
print(22 not in list1) #False

#==========Traversing list using for loop

list = [1,2,3,4,5]
for i in list:
    print(i, end=" ") #1 2 3 4 5
# ------------------------------------
# using while loop
# Create a list containing the range 1 to 5
my_list = [1, 2, 3, 4, 5]
print("\n------")  # To add a separator
# Initialize the index
index = 0

# Traverse the list using a while loop
while index < len(my_list):
    print(my_list[index],end=" ")
    index += 1
print("\n------")  # To add a separator
#==========Commonly used list methods with return type
list1 = [2, 3, 4, 1, 32, 4]
list1.append(19)
print(list1) #[2, 3, 4, 1, 32, 4, 19]

print(list1.count(4)) # Return the count for number 4 result:2

list2 = [99, 54]
list1.extend(list2)
print(list1) #[2, 3, 4, 1, 32, 4, 19, 99, 54]

print(list1.index(4)) # Return the index of number 4 result:2

list1.insert(1, 25) # Insert 25 at position index 1
print(list1) #result:[2, 25, 3, 4, 1, 32, 4, 19, 99, 54]

list1 = [2, 25, 3, 4, 1, 32, 4, 19, 99, 54]
print(list1.pop(2)) #3
print(list1) #[2, 25, 4, 1, 32, 4, 19, 99, 54]

list1.remove(32) # Remove number 32
print(list1)#[2, 25, 4, 1, 4, 19, 99, 54]

list1.reverse() # Reverse the list
print(list1) #[54, 99, 19, 4, 1, 4, 25, 2]

list1.sort() # Sort the list
print(list1) #[1, 2, 4, 4, 19, 25, 54, 99]

#============List Comprehension
list1 = [ x for x in range(10) ]
print(list1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list2 = [ x + 1 for x in range(10) ]
print(list2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list3 = [ x for x in range(10) if x % 2 == 0 ]
print(list3) #0, 2, 4, 6, 8]

#--------------------------List of Comprehension Example 2
print("\n--------------------------------------------")  # To add a separator
# Basic Example: Creating a list of squares of numbers from 1 to 5.
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Filtering with Condition: Creating a list of even numbers from 1 to 10.
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]

# Transforming Data: Converting a list of strings to uppercase.
words = ["hello", "world", "python"]
uppercased = [word.upper() for word in words]
print(uppercased)  # Output: ['HELLO', 'WORLD', 'PYTHON']

# Nested List Comprehension: Flattening a 2D list (list of lists).
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


















