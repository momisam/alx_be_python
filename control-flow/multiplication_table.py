#Multiplication table using Loop (for loop)
#Ask user to enter number they want the multiplication table

number = int(input("Enter a number to see its multiplication table:"))


#print multiplication table

for n in range(1,11):
    print(f'{number} * {n} = {number * n}')
