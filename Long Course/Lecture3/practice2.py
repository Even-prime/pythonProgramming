# Check if a given list is a palindrome or not

list1 = [1, 2, 3, 4, 3, 2, 1]
list2 = list1.copy()
list2.reverse()
if list1 == list2:
    print("This is a palindrome list")
else:
    print("Its not a palindrome list ")
