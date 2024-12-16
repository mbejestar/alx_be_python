size = int(input("Enter the size of the pattern: "))  

# Draw the Pattern  
row = 0  # Initialize row counter  
while row < size:  # Iterate through each row  
    for col in range(size):  # Iterate through each column  
        print("*", end="")  # Print asterisk without advancing to a new line  
    print()  # Print new line after completing a row  
    row += 1  # Increment row counter
