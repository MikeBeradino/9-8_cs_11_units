'''
Mike Beradino
9-8-2020
Units_Example
'''


# Bits and bytes converter
# b is notation for bits --> a bit has a value of 1 or 0
# B is notation for bytes --> a Byte is 8 bits so integer values between 0-255
# This Sci notation is not based on 10x

bit = .125
Nibble = .5
Byte =  1

Kilo = 1024
Mega = 1048576
Giga = 1073741824
Tera = 1099511627776
Peta = 125899906842624

print("Units are as follows:")
#print("bit\nByte\nKilo \nMega \nGiga \nTera \nPeta ")
print("bit\nByte")

get_units_question = input("bits or Bytes?")
how_many = input("how many " +get_units_question+ "(s)")
how_many_float = float(how_many)
'''
These operators change work as normal addition subtraction multiplication and division.
x =1
y = 3 
+ 	Addition: adds two operands                                 x + y  this would output 4
- 	Subtraction: subtracts two operands 	                    x - y  this would output -2
* 	Multiplication: multiplies two operands                     x * y  this would output 3
/ 	Division (float): divides the first operand by the second 	x / y  this would output .3333


These operators compare the values:
== 	If the values of two operands are equal, then the condition becomes true. 	(a == b) is  true.
!= 	If values of two operands are not equal, then condition becomes true. 	(a != b) is true.
> 	If the value of left operand is greater than the value of right operand, then condition becomes true. 	(a > b) is not true.
< 	If the value of left operand is less than the value of right operand, then condition becomes true. 	(a < b) is true.
>= 	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true. 	(a >= b) is not true.
<= 	If the value of left operand is less than or equal to the value of right operand, then condition becomes true. 	(a <= b) is true.

'''


if get_units_question == "bit" or get_units_question == "bits" :
    numb_of_bytes = how_many_float / 8
    print( numb_of_bytes,"Bytes = ", how_many_float,"bits")
    convert_number = how_many_float
if get_units_question == "Byte" or get_units_question == "Bytes" :
    numb_of_bits = how_many_float * 8
    print( how_many_float ,"Bytes = ", numb_of_bits, "bits")
    convert_number = numb_of_bits


if Kilo <= convert_number and convert_number < Mega:
    Kilobits = convert_number / Kilo
    print(Kilobits,"K")

if ------<= ---- and ----- < ----:
    ---- = convert_number / ----
    print(----,"Mb")



def difference_in_bytes():
    first_question = input("Convert from (units):   ")
    second_question = input("How many " + first_question + get_units_question + "(s)")
    third_question = input("Convert to (units):   ")
    # convert from string
    second_question_float = float(second_question)
    # print(second_question_float , "sqf")
    # we need to get the user input for the first value and
    # get the float value for the conversion
    if first_question == "bit" or first_question == "bits":
        fist_question_number = bit
    if first_question == "Nibble":
        fist_question_number = Nibble
    if first_question == "Byte" or first_question == "Bytes":
        fist_question_number = Byte
    if first_question == "Kilo":
        fist_question_number = Kilo
    if first_question == "Mega":
        fist_question_number = Mega
    if first_question == "Giga":
        fist_question_number = Giga
    if first_question == "Tera":
        fist_question_number = Tera
    if first_question == "Peta":
        fist_question_number = Peta

    # think of this as a 2 part problem
    # always convert to bytes then go to second unit


    # we need to get the user input for the third value and
    # get the float value for the conversion
    if third_question == "bit" or third_question == "bits" :
        third_question_number = bit
    if third_question == "Nibble":
        third_question_number = Nibble
    if third_question == "Byte" or third_question == "Bytes":
        third_question_number = Byte
    if third_question == "Kilo":
        third_question_number = Kilo
    if third_question == "Mega":
        third_question_number = Mega
    if third_question == "Giga":
        third_question_number = Giga
    if third_question == "Tera":
        third_question_number = Tera
    if third_question == "Peta":
        third_question_number = Peta

    if third_question_number > fist_question_number:
        conversion = third_question_number / (second_question_float * fist_question_number)
        print("There is", second_question, first_question, get_units_question, "in ", conversion, third_question,
              get_units_question)
    else:
        conversion =   (second_question_float * fist_question_number)/third_question_number
        print("Therdsfsdfdse is", conversion, first_question, get_units_question, "in ",second_question , third_question,
              get_units_question)

def converte_one (one_value):
    # This loop uses functions built into python to demo decimal/hex/binary representations.
    i = int(one_value)
    print(" Decimal-----", i)
    hex_string = hex((i))
    hex_string_sliced = hex_string[2:]
    print(" Hexadecimal-", hex_string_sliced.upper())
    print(" | 128 | 64  | 32  | 16  |  8  |  4  |  2  |  1  |")
    # this stores the var i as a string
    binary_string = bin(i)
    # formating the string to line up with line 21
    binary_string_sliced =binary_string[2:]
    while len(binary_string_sliced) < 8:
        binary_string_sliced = str(0) +  binary_string_sliced
    print(binary_string_sliced.replace("", "  |  ")[1: -1])
    print()

def converter0_256 ():
    # This loop uses functions built into python to demo decimal/hex/binary representations.
    for i in range (256):
        print(" Decimal-----", i)
        hex_string = hex((i))
        hex_string_sliced = hex_string[2:]
        print(" Hexadecimal-", hex_string_sliced.upper())
        print(" | 128 | 64  | 32  | 16  |  8  |  4  |  2  |  1  |")
        # this stores the var i as a string
        binary_string = bin(i)
        # formating the string to line up with line 21
        binary_string_sliced =binary_string[2:]
        while len(binary_string_sliced) < 8:
            binary_string_sliced =  str(0)+ binary_string_sliced
        print(binary_string_sliced.replace("", "  |  ")[1: -1])
        print()

def binary_hex():
    # User inputs and function calls
    print("This program will demonstrate Integer values 0-256, ")
    print ("reperesented as Binary tables and Hexadecimal  ")
    print ("")
    all_or_one = input("Convert Integer to HEX and Binary Y/N ?")
    Run_all = ""
    if all_or_one == "Y" or all_or_one == "y":
        one_value = input("Convert an integer from 0-256 : ")
        converte_one(one_value)
    else:
        Run_all = input("Show all 0-256 Hex and Binary values  Y/N ?")
    if Run_all == "Y"  or Run_all == "y" :
        converter0_256()





