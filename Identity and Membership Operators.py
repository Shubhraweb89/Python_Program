my_list = ["apple", "banana", "cherry"]
string_to_check = "banana"

if string_to_check in my_list:
    print("String is in the list")
else:
    print("String is not in the list")


list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1 # list3 points to the same object as list1

print(list1 is list2) # False (different objects with same values)
print(list1 is list3) # True (same object)   