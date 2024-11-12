# Create an empty list called my_list.

my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
numbers = [10,20,30,40]
my_list.extend(numbers)


# case 2

# for num in numbers:
#     my_list.append(num)


# case 3
# my_list = my_list+numbers

print(my_list)

# Insert the value 15 at the second position in the list.
# my_list.insert(index_to_insert_at, value_to_insert)

my_list.insert(2, 25)
print(my_list)
# Extend my_list with another list: [50, 60, 70].

my_list2 = [50,60,70]

my_list.extend(my_list2)
print(my_list)

# Remove the last element from my_list.
my_list.pop()
# del my_list[-1]
print(my_list)

# Sort my_list in ascending order.

print(sorted(my_list))

# Find and print the index of the value 30 in my_list.
print(my_list.index(30))
