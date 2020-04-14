from math import ceil
from math import floor

def routh_hurwitz(coeff, ord = 0):

    ord = len(coeff) - 1
    chareqn = ""
    j = 0;
    for i in range(ord, -1, -1):                                      # Forming the Characteristic Equation String
        if coeff[j] == 0:
            j += 1;
            if (i == 0):                                                # Cosmetic - removing the '+' from the string if the last coefficient is zero
                chareqn = chareqn[:-3]
            continue
        
                
        if i > 0 and coeff[j] > 0:                                                           # positive term
            chareqn += str(coeff[j]) + 's^' + str(i) + ' + '
        elif i > 0 and coeff[j] < 0: 
            chareqn = chareqn[:-2] + '- ' + str(abs(coeff[j])) + 's^' + str(i) + ' + '       # negative term
        elif coeff[j] > 0:                                                                   
            chareqn += str(coeff[j])                                                         # positive constant
        else:
            chareqn = chareqn[:-2] + '- ' + str(abs(coeff[j]))                               # negative constant
        j += 1;
    

    print('\n')
    print(chareqn, " is your characteristic equation.")

    while (True):                                                       #Repeating until the user gives a valid answer
        x = input("Do you want to continue? y/n\n")
        if x == 'y' or x == 'Y' or x == 'yes' or x == 'Yes' or x == 'Yeah':
            print("\nOkay then, let's hustle!");
            break
        elif x == 'n' or x == 'N' or x == 'No' or x == 'Nope' or x == 'Nah':
            print("\nOkay then, bye")
            return
        print("I don't understand.")



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
            

        if routhmatrix[i] == [0 for k in range(0, col)]:                # Special Case 1 - when the entire zero is zero
            degree = (ord - i) + 1
            for j in range(0, col):
                routhmatrix[i][j] = routhmatrix[i-1][j] * degree        # Instead of the simple differentiation, (d/dx) x^n = (nx) ^ (n - 1)
                degree -= 2
            

        elif routhmatrix[i][0] == 0:                                    # Special Case 2 - when the first term is zero
            routhmatrix[i][0] = 0.01


    printrouth(routhmatrix, ord)    
    checkrouth(routhmatrix, ord)

    
def printrouth(rmat, orde):

    print("\nLet me print out the Routh-Hurwitz Table for you,\n")
    
    for i in rmat:
        print('s^', orde, sep = '', end = '\t')
        for j in i:
            print(j, '\t', end = '')
        print('\n')
        orde -= 1



def checkrouth(rmat, orde):

    sign = 0
    
    for i in range(0, orde):
        if (rmat[i][0] < 0 and rmat[i+1][0] > 0) or (rmat[i][0] > 0 and rmat[i+1][0] < 0):
            sign += 1

    if sign > 0:
        print("\nThe given system is unstable and it has", sign, "poles on the right-hand side of the s plane.")

    else:
        print("\nThe given system is stable.")




if __name__=="__main__":

    while(True):
        order = int(input("Enter the order of the characteristic equation: "))
        if order > 0:
            break
        else:
            print("Order cannot be zero or negative!\n")

    print(
'''
Now, enter the coefficients of the characteristic equation starting with the coefficient of the highest degree term.
Take for an instance a fifth-order system, As^5 + Bs^4 + Cs^3 + Ds^2 + Es^1 + F where A, B, C, D, E and F are the coefficients.

Type each coefficient and press Enter. Remember, for any non - existing term (say if s^3 is missing) enter 0 as its coefficient.

''')
    coefficients = []
    for i in range(0, order + 1):
        coefficients.append(int(input()))
        
    routh_hurwitz(coefficients, order)

    while(True):
        if input("Do you wanna quit?\n") == 'quit' or 'exit' or 'bye':
            break
        print("I will ask you again.")

    


      
    
    
    
    
