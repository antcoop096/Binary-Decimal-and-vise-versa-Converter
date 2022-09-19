
def DecimalToBinary(decimal_number): #make a procedure that converts decimal to binary
  while decimal_number > 0: #while the decimal number is greater than 0
    print(decimal_number % 2) #the remainder of the decimal number divided by 2 is printed
    decimal_number = decimal_number // 2
  
      #the decimal number becomes the quotient of the decimal number divided by 2

      #the process above repeats itself until the decimal number hits zero

def BinaryToDecimal(binary_number): #make a procedure that converts binary to decimal
  done = False
  binary_number = " ".join(binary_number) 
  #use .join to add a space between each digit in the binary number
  print('Your binary number is:', binary_number)
  binary_number_list = binary_number.split() 
  #turn the binary number into a list (each digit in the binary number being an item in the list) by using .split
  binary_number_list.reverse() 
  #reverse the list
  power_list = [] 
  #make a power list
  number = 0 #number = 0
  while number < len(binary_number_list): #while number is less than the length of the binary number list
   for digit in binary_number_list: 
    #for each digit in the binary number (list)
    power = 2 ** number
    #power = 2 to the power of number
    if digit == '1':
    #if digit is 1
     power_list.append(power)
    #add power to the power list
    elif digit == '0': 
      #if digit is 0
     power_list.append(0) 
      #add 0 to the power list
    else: 
     print('SORRY, THAT IS NOT A BINARY NUMBER. PLEASE RESTART AND TRY AGAIN...')
     done = True
    #if the digit is not a binary number, inform the user
    number = number + 1
    #add 1 to number
  if done == False:
    decimal_conversion = sum(power_list) 
    #find the sum of all the items in the power list
    print('The decimal conversion is:')
    print(decimal_conversion)
    #print the sum of all the items in the power list
    return decimal_conversion #return the decimal conversion


def BinaryNumberComparison(first,second): #create a procedure that compares two binary numbers
   result = '' #variable = ''
   if first > second: #if the first binary number is greater than the second, let the user know by how much
    result = 'The first binary number(',first,') is greater than the second binary number(',(second),') by',first - second,'.'
   elif second > first: #if the second binary number is greater than the first, let the user know by how much
    result = 'The second binary number(',second,') is greater than the first binary number(',(first),') by',second - first,'.'
   elif first == second: #if the two binary numbers are both equal to each other, let the user know
     result ='The first binary number(',first,') is equal to the second binary number(',(second),').'
   else: #if their is an input error, let the user know to try again
     result = 'Please try again...'
   return result #return the variable storing the result
   




#provide information for the user
print('BINARY CONVERTER PROGRAM')
print('Please choose an action:')
print('Press 1 to convert decimal to binary:')
print('Press 2 to convert binary to decimal:')
print('Press 3 to compare binary numbers:')
action = input() #have the user choose if they want to convert from decimal to binary, from binary to decimal, or compare binary numbers

if action == '1': #if the user wants to convert decimal to binary
  print('Enter a decimal number:') 
  decimal_number = input() #have the user enter a number through input()
  is_numeric = decimal_number.isnumeric() #check to see if the input is an acceptable number
  if is_numeric == True: #if it is
   decimal_number = int(decimal_number) #turn it into an integer
   DecimalToBinary(decimal_number) #use the decimal to binary procedure and plug in the decimal number as the argument
  else: #if the input has any non-numeric characters in it, inform the user
    print("SORRY PLEASE TRY AGAIN...")

  


elif action == '2': #if the user wants to convert binary to decimal
 
  print('Enter a binary number:')
  binary_number = input() #have the user enter a binary number
  BinaryToDecimal(binary_number) #use the procedure that converts binary to decimal and plug in the binary number as the argument


elif action == '3': #if the user wants to compare 2 binary numbers
 print('Enter the first binary number:')
 first = input() #have the user enter the first binary number
 binary_number_1 = BinaryToDecimal(first)
 
 print('Enter the second binary number:')
 second = input() #have the user enter the second binary number
 binary_number_2 = BinaryToDecimal(second)
 print(BinaryNumberComparison(binary_number_1,binary_number_2))
      #print out the binary number comparison procedure to compare the two binary numbers
else:
 print("That is not an option. Please try again...") #if the user enters something else besides 1, 2, or 3 then tell them their option is not valid and they should try again

  
