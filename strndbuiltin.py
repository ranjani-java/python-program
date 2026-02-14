def strlen(s):
    counter = 0
    while s[counter:]:
        counter += 1
    return counter

def strrev(s):
    rstr = ""
    l = strlen(s)
    while l > 0:
        rstr = rstr + s[l - 1]
        l -= 1
    return rstr

def strcat(s1, s2):
    return s1 + s2

def strcmp(s1, s2):
    if s1 == s2:
        print(f'"{s1}" and "{s2}" are same')
    elif s1 > s2:
        print(f'"{s1}" comes after "{s2}" in the Dictionary')
    else:
        print(f'"{s1}" comes before "{s2}" in the Dictionary')


print("String Functions:\n1. String Length\n2. String Reverse\n3. String Concatenation\n4. String Comparison\n5. Exit\n")

while True:
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        s = input("Enter a string: ")
        print("Length of the string is:", strlen(s))
    
    elif choice == 2:
        s = input("Enter a string: ")
        print("Reversed string is:", strrev(s))
    
    elif choice == 3:
        s1 = input("Enter the first string: ")
        s2 = input("Enter the second string: ")
        print("Concatenated string is:", strcat(s1, s2))
    
    elif choice == 4:
        s1 = input("Enter the first string: ")
        s2 = input("Enter the second string: ")
        strcmp(s1, s2)
    
    elif choice == 5:
        print("Exited")
        break
    
    else:
        print("Invalid choice")
