# Write a short Python function that counts the number of vowels in a given -
# character string.

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)