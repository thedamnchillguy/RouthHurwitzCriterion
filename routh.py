from math import ceil
from math import floor

def routh_hurwitz(coeff, ord):
    print("Let's hustle!");
    
    routhmatrix = [[0 for j in range(ceil((ord + 1) / 2))] for i in range(ord + 1)]

    for i in range(0, ord + 1):                                         # Filling the first two rows of the Routh-Hurwitz Table
        if i % 2 == 0:
            routhmatrix[0][i // 2] = coeff[i]
        else:
            routhmatrix[1][floor(i / 2)] = coeff[i]

    

    row = ord + 1
    col = ceil((ord + 1) / 2)

    for i in range(2, row):
        
        for j in range(0, col - 1):

            routhmatrix[i][j] = round((routhmatrix[i-1][0] * routhmatrix[i-2][j+1] - routhmatrix[i-1][j+1] * routhmatrix[i-2][0]) / routhmatrix[i-1][0], 3)

            if routhmatrix[i][j] - int(routhmatrix[i][j]) == 0.0:       # 3.0, 2.0 -> 3, 2 rounding off integers
                routhmatrix[i][j] = int(routhmatrix[i][j])
            

        if routhmatrix[i] == [0 for k in range(0, col)]:                # Special Case 1 - where the entire zero is zero
            degree = (ord - i) + 1
            print(degree)
            for j in range(0, col):
                routhmatrix[i][j] = routhmatrix[i-1][j] * degree
                degree -= 2
            

        elif routhmatrix[i][0] == 0:                                    # Special Case 2 - where the first term is zero
            routhmatrix[i][0] = 0.01

        
    for i in routhmatrix:
        print(i)










order = int(input("Enter the order of the characteristic equation: "))

print(
'''
Now, enter the coefficients of the characteristic equation starting with the coefficient of the highest degree term.
Take for an instance a fifth-order system, As^5 + Bs^4 + Cs^3 + Ds^2 + Es^1 + F where A, B, C, D, E and F are the coefficients.

Type each coefficient and press Enter. Remember, for any non - existing term (say if s^3 is missing) enter 0 as its coefficient.

''')
coefficients = []
for i in range(0, order + 1):
    coefficients.append(int(input()))
    

chareqn = ""
j = 0;
for i in range(order, -1, -1):
    if coefficients[j] == 0:
        j += 1;
        if (i == 0):                                                #Cosmetic - removing the '+' from the string if the last coefficient is zero
            chareqn = chareqn[:-1]
        continue
            
    if i != 0:
        chareqn += str(coefficients[j]) + 's^' + str(i) + '+'
    else:
        chareqn += str(coefficients[j])
    j += 1;
    

print(chareqn, " is your characteristic equation.")

while (True):                                                       #Repeating until the user gives a valid answer
    x = input("Do you want to continue? y/n")
    if x == 'y' or x == 'Y' or x == 'yes' or x == 'Yes' or x == 'Yeah':
        routh_hurwitz(coefficients, order)
        break;
    elif x == 'n' or x == 'N' or x == 'No' or x == 'Nope' or x == 'Nah':
        print("\nOkay then, bye")
        break;
    print("I don't understand.")

    


      
    
    
    
    
