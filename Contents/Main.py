
from email.errors import ObsoleteHeaderDefect
from operator import length_hint
from sys import getdefaultencoding
from tokenize import Exponent
from unicodedata import decimal
stop = True

def denary_converter(binary_num):
  current = 0
  calc = 0
  total = 0
  length_check = 0
  binary_num = binary_num
  length_check = len(binary_num)
  y = length_check - 1
  for x in range(0,length_check,1):
      if x == 0:
          current = int(binary_num[x])
          calc = -(current * (2**y))
          y = y - 1
      else:
        current = int(binary_num[x])
        calc = current * (2**y)
        total = calc + total
        y = y - 1
  print(total)
  return total

def fixed_point(binary_num):
    current = 0
    calc = 0
    total = 0
    total1 = 0
    length_check = 0
    binary_num = binary_num
    count = 0
    current = str(binary_num[count])
    length = len(binary_num)
    while current != ".": #this finds where the full stop is in the binary num
        count = count + 1
        current = str(binary_num[count])
    multiplier = count - 1
    for x in range(0,count,1): #this finds the denary value before the fixed-point and adds it to the total
        if x == 0:
            current = int(binary_num[x]) #this turns the MSB into a negative
            calc = -(current * (2**multiplier))
            total = total + calc
            multiplier = multiplier - 1
        else:
            current = int(binary_num[x])
            calc = current * (2**multiplier)
            total = total + calc 
            multiplier = multiplier - 1
    y = 1 #y starts from one as 1/2**0 is 1/1 which is a whole number, therrefore it starts at 1/2**1(0.5)
    for x in range(count+1,length,1): #this finds the decimals for the value and adds it to the total
        current = int(binary_num[x])
        calc = current * (1/2**y)
        print("decimal current is",  current)
        total = total + calc
        y = y + 1
    print("Your final denary value is:", total)
    return total


def floating_point(binary_num):
    current = 0
    calc = 0
    calc2 = 0
    calc3 = 0
    total_mantissa = 0
    total_exponent = 0
    decimal_final = 0
    mantissa = 0
    binary_num = binary_num
    length_for_end = len(binary_num)
    binary_num2 = ""
    length_check = len(binary_num)
    exponent = int(input("Please input the size of your exponent"))
    mantissa = (length_check  - exponent)
    mantissatrue = mantissa + 1 
    mantissa_multiplier = mantissa  
    next_mantissa = 0 
    exponent_multiplier = exponent
    finalnum = 0
    mantissa_final = 0
    other = ""
    for x in range(mantissa,length_check,1):  #finds the exponent
        current = int(binary_num[x])
        if x == mantissa and current == 1: #this creates a negative MSB
            calc = current * (2**(exponent_multiplier-1))
            calc2 = calc * 2
            calc3 = calc - calc2
            total_exponent = calc3 + total_exponent
            exponent_multiplier = exponent_multiplier - 1
            other = other + str(current)
            print(other)
        else:
            calc = current * (2**(exponent_multiplier-1))
            total_exponent = calc + total_exponent
            exponent_multiplier = exponent_multiplier - 1
            other = other + str(current)
            print(other)
    next_mantissa = (total_exponent)
    if total_exponent > 0 and total_exponent < mantissa: #this checks to see whether the exponent is a negative, or greater than the mantissa - as this changes the needed operations
        for x in range(0,total_exponent+1, 1): #this allows the program to go to the found floating point dictated by the total_exponent
            current = int(binary_num[x])
            if x == 0 and current == 1: #this creates a negative MSB
                calc = current * (2**(next_mantissa)) 
                calc2 = calc * 2
                calc3 = calc - calc2
                mantissa_final = calc3 + mantissa_final
                next_mantissa = next_mantissa - 1
            else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                current = int(binary_num[x])
                calc = current * (2**(next_mantissa))
                next_mantissa = next_mantissa - 1
                mantissa_final = mantissa_final + calc
        decimal_change = 1
        decimal_final = 0
        for x in range(total_exponent+1,mantissa, 1): #this finds the denary value up to where the exponent starts
           current = int(binary_num[x])
           calc = current * (1/(2**(decimal_change)))
           decimal_change = decimal_change + 1
           decimal_final = decimal_final + calc
    elif total_exponent > mantissa: #if the total_exponent is greater than the mantissa, then the programme moves the numbers before the exponent by the valid steps to the left
        zerostr = ""
        binary_num2 = ""
        next_mantissa = 0
        for x in range(0,total_exponent,1): #this creates a new number which allows for new iterations with the change in values
            zerostr = "0" + zerostr
        placeholder = binary_num[0:mantissa]
        binary_num2 = placeholder + zerostr
        length = len(binary_num2)
        next_mantissa = length
        other = ""
        for x in range(0,length, 1):
            current = int(binary_num2[x])
            if x == 0: #this creates a negative MSB
                calc = current * (2**(next_mantissa)) 
                calc2 = calc * 2
                calc3 = calc - calc2 # this is a long winded way to find the negative, I forgot to change it
                mantissa_final = calc3 + mantissa_final
                next_mantissa = next_mantissa - 1
                other = other + str(current)
                print(other)
                length2 = len(other)
                print(length2)
            else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
                current = int(binary_num2[x])
                calc = current * (2**(next_mantissa))
                next_mantissa = next_mantissa - 1
                mantissa_final = mantissa_final + calc
                other = other + str(current)
                print(other)
                length2 = len(other)
                print(length2)
    else:
        neg_mantissa_check = int(binary_num[0]) 
        print(binary_num)
        print(neg_mantissa_check)
        placeholder = ""
        other2 = ""
        if neg_mantissa_check == 0: #if the mantissa is positive and the exponent is negative, 0's are added and the program finds the newly smaller decimal number
            zerostr = ""
            for x in range(0,(total_exponent),-1): #this adds more 0's to the original number
                zerostr = "0" + zerostr
                print(zerostr) 
            placeholder = binary_num   
            for x in range(0,mantissa+abs(total_exponent), 1):
                current = int(binary_num2[x])
                calc = current * (1/(2**(x)))
                decimal_final = decimal_final + calc
                other2 = other2 + str(current)
                print(other2)
        else:
            zerostr = ""
            for x in range(0,total_exponent,-1): #if the mantissa is negative and the exponent is negative, 1's are added and the program finds the newly negative smaller decimal number
                zerostr = "1" + zerostr 
            placeholder = binary_num
            binary_num2 = zerostr + placeholder 
            print(binary_num2)
            for x in range(1,(mantissa+abs(total_exponent)), 1): #it starts at one due to the rule that the number will always have -1 at the start, therefore there's no need to find that number and write the relevant code
                current = int(binary_num2[x])
                calc = current * (1/(2**(x)))
                decimal_final = decimal_final + calc
                print(calc)
            decimal_final = -1 + decimal_final #this is where I add the negative one


    finalnum = mantissa_final + decimal_final
    print("Your binary number was:", binary_num)
    print("The length of this binary was:", length_for_end)
    print("Your mantissa position was:", (mantissatrue-1))
    print("Your exponent position was:", exponent)
    print("Your final number is:", finalnum )


def mainmenu(): #I'd say this is rather self explanatory 
    stop2 = True
    print("1 - Binary to Denary Conversion")
    print("2 - 8 Bit Fixed point Binary to Denary Conversion")
    print("3 - Floating point Binary to Denary Conversion")
    print("4 - Quit Program")
    user_question = str(input("Would you like to find the denary for a binary number, find the fixed-point value of an 8 bit binary number, or the floating point of a binary number? "))
    if user_question == "1":
        binary_num = str(input("Please input your binary number, type 'stop' to return to the main menu: "))
        while binary_num != "stop":
            floating_point(binary_num)
            binary_num = str(input("Please input your binary number, type 'stop' to return to the main menu: "))
    if user_question == "2":
        binary_num = str(input("Please input your binary number with your fixed point as a full-stop (.), type 'stop' to return to the main menu: "))
        while binary_num != "stop":
            fixed_point(binary_num)
            binary_num = str(input("Please input your binary number, type 'stop' to return to the main menu: "))
    if user_question == "3":
        binary_num = str(input("Please input your binary number, type 'stop' to return to the main menu: "))
        while binary_num != "stop":
            floating_point(binary_num)
            binary_num = str(input("Please input your binary number, type 'stop' to return to the main menu: "))
    if user_question == "4":
        print("Goodbye!")
        quit()

while stop:
    mainmenu()