
from email.errors import ObsoleteHeaderDefect
from operator import length_hint
from sys import getdefaultencoding
from tokenize import Exponent
from unicodedata import decimal
stop = True

def denary_converter():
  current = 0
  calc = 0
  total = 0
  length_check = 0
  binary_num = str(input("Please input your binarry number"))
  length_check = len(binary_num)
  y = length_check - 1
  for x in range(0,length_check,1):
    current = int(binary_num[x])
    calc = current * (2**y)
    total = calc + total
    y = y - 1
  print(total)
  return total

def fixed_point():
    current = 0
    calc = 0
    total = 0
    total1 = 0
    length_check = 0
    binary_num = ""
    while length_check != 8:
        binary_num = str(input("Please input your 8 bit binary number:  "))
        length_check = len(binary_num)
        if length_check != 8:
            print("Error: program is for 8 digit binary numbers!")

    for x in range(0,4, 1):
        current = int(binary_num[x])
        calc = current * (2**(x))
        total = calc + total
    print(total)
    for x in range(5,9, 1):
        current = int(binary_num[x-1])
        calc = current * (1/(2**(x-4)))
        total1 = calc + total1
    totalfin = total1 + total
    print(totalfin)
    return totalfin


def floating_point():
    current = 0
    calc = 0
    calc2 = 0
    calc3 = 0
    total_mantissa = 0
    total_exponent = 0
    decimal_final = 0
    mantissa = 0
    binary_num = ""
    binary_num = input("Please input your binary number")
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
    if total_exponent > 0 and total_exponent < mantissa:
        for x in range(0,total_exponent+1, 1):
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
        for x in range(total_exponent+1,mantissa, 1):
           current = int(binary_num[x])
           calc = current * (1/(2**(decimal_change)))
           decimal_change = decimal_change + 1
           decimal_final = decimal_final + calc
    elif total_exponent > mantissa:
        zerostr = ""
        binary_num2 = ""
        next_mantissa = 0
        for x in range(0,total_exponent,1):
            zerostr = "0" + zerostr
        placeholder = binary_num[0:mantissa]
        print(len(placeholder))
        binary_num2 = placeholder + zerostr
        length = len(binary_num2)
        next_mantissa = length
        other = ""
        for x in range(0,length, 1):
            current = int(binary_num2[x])
            if x == 0 and current == 1: #this creates a negative MSB
                calc = current * (2**(next_mantissa)) 
                calc2 = calc * 2
                calc3 = calc - calc2
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
        if neg_mantissa_check == 0:
            zerostr = ""
            for x in range(0,(total_exponent),-1):
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
            for x in range(0,total_exponent,-1):
                zerostr = "1" + zerostr 
            placeholder = binary_num
            binary_num2 = zerostr + placeholder 
            print(binary_num2)
            for x in range(1,(mantissa+abs(total_exponent)), 1):
                current = int(binary_num2[x])
                calc = current * (1/(2**(x)))
                decimal_final = decimal_final + calc
                print(calc)
            decimal_final = -1 + decimal_final


    finalnum = mantissa_final + decimal_final
    print("Your binary number was:", binary_num)
    print("The length of this binary was:", length_for_end)
    print("Your mantissa position was:", (mantissatrue-1))
    print("Your exponent position was:", exponent)
    print("Your final number is:", finalnum )


while stop:
    print("1 - Binary to Denary Conversion")
    print("2 - 8 Bit Fixed point Binary to Denary Conversion")
    print("3 - Floating point Binary to Denary Conversion")
    print("4 - Quit Program")
    user_question = str(input("Would you like to find the denary for a binary number, find the fixed-point value of an 8 bit binary number, or the floating point of a binary number? "))
    if user_question == "1":
        denary_converter()
    if user_question == "2":
        fixed_point()
    if user_question == "3":
        floating_point()
    if user_question == "4":
        print("Goodbye!")
        quit()

