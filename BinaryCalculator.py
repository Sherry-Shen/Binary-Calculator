#!usr/bin/python3
'''
Created on Sep 8, 2016
This program is a simple calculater for binary numbers
The numbers are in 8-bit format. The valid operators are +, -, *, and /. 
Numbers are intergers
@Author: Sherry Shen
'''

answer = "Y"
while answer == 'Y' or answer == 'y':
	#Get the input string 
    equation = input("Enter the binary expression: ")     
	
	#chunk the string
    num1 = equation[:8]
    num2 = equation[9:]
    op = equation[8]
	#initialize the numbers
    number1 = 0
    number2 = 0

    #Convert the num1 and num2 to decimal number
    for i in range(1,8):
        number1 += (int(num1[i]))*(2**(7-i))
        
    if num1[0] == '1':
        number1 = 0-number1
            
    else :
        number1 = number1

    for i in range(1,8):
        number2 += (int(num2[i]))*(2**(7-i))
        
    if num2[0] == '1':
        number2 = 0-number2
            
    else:
        number2 = number2
     
    #Check the operator and decimalo the calculation.
    if op == '+':
        result = number1 + number2

    elif op == '-':
        result = number1 - number2
    
    elif op == '*':
        result = number1 * number2
    
    elif op == '/':
        if number2 == 0:
            print("Error: can't divide by zero.")
            break
        else:
            #Only show the integer part of the division operation
            result = number1 // number2
    else:
        print("Error: wrong operator.")
        break
    
    #Check if the result is overflow
    if result > 127 or result <-128:
        print("Error: the result is overflow")
        
    #Convert result to binary    
    else:
        bi_result = []
		# Negtive result
        if result < 0:
            result = 0-result
            
        # Result is divided by two
            for i in range(0,7):
				#If result is bigger than 1, add the mod to the list
                if result/2 >= 1:
                    bi_result.append(str(int(result%2)))
                    result = result//2
                #If only 1 is left, add 1 to the list    
                elif result == 1:
                    bi_result.append('1')
                    result = 0
                else :
                    bi_result.append('0')
			#Add the negative sign number '1'		
            bi_result.append('1')
        
		#Positive number
        else:
            for i in range(0,7):
                if result/2 >= 1:
                    bi_result.append(str(int(result%2)))
                    result = result//2
                elif result == 1:
                    bi_result.append('1')
                    result = 0
                else :
                    bi_result.append('0')
			#Add the positive sign number '0'
            biresult.append('0')

        #Reverse the list        
        bi_result.reverse()
        
        #Conver result to string
        b = ""
        b = b.join(bi_result)
        
        print(equation, "=", b)
        
    answer = input ("Do you want to continue the binary calculation? Y/N: ")


