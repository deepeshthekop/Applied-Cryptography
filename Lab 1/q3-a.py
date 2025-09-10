# Write a short Python function that takes a sequence of integer values and -
# determines if their product is odd.

integer1 = input("Integer 1: ")
integer2 = input("Integer 2: ")
integer3 = input("Integer 3: ")
integer4 = input("Integer 4: ")
integer5 = input("Integer 5: ")
product = int(integer1) * int(integer2) * int(integer3) * int(integer4) * int(integer5)
print("The product is:", product)
if product % 2 != 0:
    print("The product is odd.")
else:
    print("The product is not odd.")