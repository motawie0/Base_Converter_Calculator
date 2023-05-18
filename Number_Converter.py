num = input("Enter a number or a letter from A to F or 0 and 1 to convert: ")
current_type = input("Enter the given number type, B for binary, O for octal, D for decimal or H for hexadecimal: ")
converted_type = input("Enter the type of number to convert to, B for binary, O for octal, D for decimal or H for hexadecimal: ")


#binary to hex / hex to binary check
#hex to decimal/ decimal to hex check
#binary to decimal/decimal to binary check
#binary to octal/ octal to binary check
#octal to decimal/decimal to octal check
# octal to hex/hex to octal check

def binary_decimal(current, converted, numb):
    #binary to decimal
    if (current == "B" or current == "b") and (converted == "D" or converted == "d") and "." not in numb:
        binary_to_decimal = int(numb, 2)
        return binary_to_decimal
    #fractional binary to decimal
    elif (current == "B" or current == "b") and (converted == "D" or converted == "d") and "." in numb:
        before_decimal = int(numb[:numb.find(".")], 2)
        after_point_binary = numb[numb.find(".")+1:]
        n = -1
        after_decimal = 0
        for i in after_point_binary:
            if i == "1":
                after_decimal += 2**(n)
                n -= 1
            else:
                n -= 1
        return before_decimal + after_decimal
    #integer decimal to binary
    elif (current == "D" or current == "d") and (converted == "B" or converted == "b"):
        if "." not in numb:
            decimal_to_binary = bin(int(numb))
            return decimal_to_binary[2:]
        #float decimal to binary
        else:
            numb = float(numb)
            int_numb = int(numb)
            float_decimal_to_binary = bin(int_numb)
            before_decimal_point = float_decimal_to_binary[2:]
            new_Fnum = "."
            float_numb = float(numb) - int(numb)
            while float_numb % 2 != 0:
                if int(float_numb * 2) != 0:
                    new_Fnum += "1"
                    float_numb = (float_numb * 2) - int(float_numb * 2)
                else:
                    new_Fnum += "0"
                    float_numb = (float_numb * 2)
        return before_decimal_point + new_Fnum

def binary_octal(current, converted, numb):
    # binary to octal
    if (current == "B" or current == "b") and (converted == "O" or converted == "o") and "." not in numb:
        binary_to_decimal = int(numb, 2)
        binary_to_octal = oct(binary_to_decimal)
        return binary_to_octal
    #fractional binary to octal
    elif (current == "B" or current == "b") and (converted == "O" or converted == "o") and "." in numb:
        binary_before_decimal = int(numb[:numb.find(".")], 2)
        octal_before_decimal = oct(binary_before_decimal)
        binary_AfterDecimalPoint = (numb[numb.find(".") + 1:])
        letter_count = len(binary_AfterDecimalPoint)
        if (letter_count % 3 != 0):
            while letter_count % 3 != 0:
                binary_AfterDecimalPoint += "0"
                letter_count = len(binary_AfterDecimalPoint)
            split_3 = [binary_AfterDecimalPoint[i:i + 3] for i in range(0, len(binary_AfterDecimalPoint), 3)]
            after_decimal = 0
            after_point_octal = ""
            for i in split_3:
                n = 3
                after_decimal = 0
                for x in i:
                    n -= 1
                    if x == "1":
                        after_decimal += 2 ** n
                after_point_octal += str(after_decimal)
            return octal_before_decimal[2:] + "." + after_point_octal
        else:
            binary_after_decimal = int(binary_AfterDecimalPoint, 2)
            octal_after_decimal = oct(binary_after_decimal)
        return (octal_before_decimal[2:] + "." + octal_after_decimal[2:]).upper()
    # octal to binary
    elif (current == "O" or current == "o") and (converted == "B" or converted == "b") and "." not in numb:
        octal_to_decimal = int(numb, 8)
        octal_to_binary = bin(octal_to_decimal)
        return octal_to_binary[2:]
    # fractional octal to binary
    elif (current == "O" or current == "o") and (converted == "B" or converted == "b") and "." in numb:
        octal_before_decimal = int(numb[:numb.find(".")], 8)
        binary_before_decimal = bin(octal_before_decimal)
        octal_after_decimal = numb[numb.find(".") + 1:]
        binary_after_decimal = ""
        for i in octal_after_decimal:
            x = bin(int(i, 8))[2:]
            while len(x) != 3:
                x = "0" + x[:]
            else:
                binary_after_decimal += x
        return binary_before_decimal[2:] + "." + binary_after_decimal

def binary_hexdecimal(current, converted, numb):
    #binary to hexadecimal
    if (current == "B" or current == "b") and (converted == "H" or converted == "h") and "." not in numb:
        binary_to_decimal = int(numb, 2)
        decimal_to_hex = hex(binary_to_decimal)
        return decimal_to_hex[2:].upper()
    #fractional binary to hexadecimal
    elif (current == "B" or current == "b") and (converted == "H" or converted == "h") and "." in numb:
        binary_before_decimal = int(numb[:numb.find(".")], 2)
        hexa_before_decimal = hex(binary_before_decimal)
        binary_AfterDecimalPoint = (numb[numb.find(".") + 1:])
        letter_count = len(binary_AfterDecimalPoint)
        if (letter_count % 4 != 0):
            while letter_count % 4 != 0:
                binary_AfterDecimalPoint += "0"
                letter_count = len(binary_AfterDecimalPoint)
            split_4 = [binary_AfterDecimalPoint[i:i + 4] for i in range(0, len(binary_AfterDecimalPoint), 4)]
            after_decimal = 0
            after_point_hexa = ""
            for i in split_4:
                n = 4
                after_decimal = 0
                for x in i:
                    n -= 1
                    if x == "1":
                        after_decimal += 2 ** n
                after_point_hexa += hex(after_decimal)[2:]
            return hexa_before_decimal[2:] + "." + after_point_hexa.upper()
        else:
            binary_after_decimal = int(binary_AfterDecimalPoint, 2)
            hex_after_decimal = hex(binary_after_decimal)
        return (hexa_before_decimal[2:] + "." + hex_after_decimal[2:]).upper()
    #hexadecimal to binary
    elif (current == "H" or current == "h") and (converted == "B" or converted == "b") and "." not in numb:
        hexadecimal_to_decimal = int(numb, 16)
        hexadecimal_to_binary = bin(hexadecimal_to_decimal)
        return hexadecimal_to_binary[2:]
    #fractional hexadecimal to binary
    elif (current == "H" or current == "h") and (converted == "B" or converted == "b") and "." in numb:
        hex_before_decimal = int(numb[:numb.find(".")], 16)
        binary_before_decimal = bin(hex_before_decimal)
        hex_after_decimal = numb[numb.find(".")+1:]
        binary_after_decimal = ""
        for i in hex_after_decimal:
            x = bin(int(i, 16))[2:]
            while len(x) != 4:
                x = "0" + x[:]
            else:
                binary_after_decimal += x
        return binary_before_decimal[2:] + "." + binary_after_decimal

def hexa_decimal(current, converted, numb):
    # decimal to hexadecimal
    if (current == "D" or current == "d") and (converted == "H" or converted == "h"):
        y = binary_decimal("D", "B", numb)
        return binary_hexdecimal("B", "H", y).upper()
    # hexadecimal to decimal
    elif (current == "H" or current == "h") and (converted == "D" or converted == "d"):
        y = binary_hexdecimal("H", "B", numb)
        return binary_decimal("B", "D", y)

def octal_decimal(current, converted, numb):
    # decimal to octal
    if (current == "D" or current == "d") and (converted == "O" or converted == "o"):
        y = binary_decimal("D", "B", numb)
        return binary_octal("B", "O", y)
    # octal to decimal
    elif (current == "O" or current == "o") and (converted == "D" or converted == "d"):
        y = binary_octal("O", "B", numb)
        return binary_decimal("B", "D", y)

def octal_hexadecimal(current, converted, numb):
    # hexadecimal to octal
    if (current == "H" or current == "h") and (converted == "O" or converted == "o"):
        y = binary_hexdecimal("H", "B", numb)
        return binary_octal("B", "O", y)
    # octal to decimal
    elif (current == "O" or current == "o") and (converted == "H" or converted == "h"):
        y = binary_octal("O", "B", numb)
        return binary_hexdecimal("B", "H", y).upper().replace("0", "")

# format check
if (current_type == "B") or (current_type == "b"):
    binary = {"0", "1"}
    checkBinary = set(num.replace(".", ""))
    if binary == checkBinary or checkBinary == {'0'} or checkBinary == {'1'}:
        print("Original Binary:", num)
    else:
        while(checkBinary.issubset(binary) is False):
            num = input("Please enter a correct binary number made of 0 or 1 only: ")
            checkBinary = set(num.replace(".", ""))
        else:
            print("Original Binary:", num)
    if (converted_type == "D") or (converted_type == "d"):
        print("Decimal:", binary_decimal(current_type, converted_type, num))
    elif (converted_type == "O") or (converted_type == "o"):
        print("Octal:", binary_octal(current_type, converted_type, num))
    elif (converted_type == "H") or (converted_type == "h"):
        print("Hexadecimal:", binary_hexdecimal(current_type, converted_type, num))

elif (current_type == "H") or (current_type == "h"):
    hexa = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}
    checkHexa = set(num.replace(".", "").upper())
    if checkHexa.issubset(hexa):
        print("Original Hexadecimal:", num)
    else:
        while (checkHexa.issubset(hexa) is False):
            num = input("Please enter a correct hexadecimal number made of 0 to 9 or A to F only: ")
            checkHexa = set(num.replace(".", "").upper())
        else:
            print("Original Hexadecimal:", num)
    if (converted_type == "D") or (converted_type == "d"):
        print("Decimal:", hexa_decimal(current_type, converted_type, num))
    elif (converted_type == "O") or (converted_type == "o"):
        print("Octal:", octal_hexadecimal(current_type, converted_type, num))
    elif (converted_type == "B") or (converted_type == "b"):
        print("Binary:", binary_hexdecimal(current_type, converted_type, num))

elif (current_type == "D") or (current_type == "d"):
    if num.replace(".", "").isdigit() is True:
        print("Original decimal:", num)
    else:
        while(num.replace(".", "").isdigit() is False):
            num = input("Please enter a correct decimal number: ")
        else:
            print("Original Decimal:", num)
    if (converted_type == "H") or (converted_type == "h"):
        print("Hexadecimal:", hexa_decimal(current_type, converted_type, num))
    elif (converted_type == "O") or (converted_type == "o"):
        print("Octal:", octal_decimal(current_type, converted_type, num))
    elif (converted_type == "B") or (converted_type == "b"):
        print("Binary:", binary_decimal(current_type, converted_type, num))

elif (current_type == "O") or (current_type == "o"):
    octal = {"0", "1", "2", "3", "4", "5", "6", "7"}
    checkOctal = set(num.replace(".", "").upper())
    if (checkOctal.issubset(octal)):
        print("Original Octal:", num)
    else:
        while (checkOctal.issubset(octal) is False):
            num = input("Please enter a correct octal number made of 0 to 7 only: ")
            checkOctal = set(num.replace(".", "").upper())
        else:
            print("Original Octal:", num)
    if (converted_type == "D") or (converted_type == "d"):
        print("Decimal:", octal_decimal(current_type, converted_type, num))
    elif (converted_type == "H") or (converted_type == "H"):
        print("Hexadecimal:", octal_hexadecimal(current_type, converted_type, num))
    elif (converted_type == "B") or (converted_type == "b"):
        print("Binary:", binary_octal(current_type, converted_type, num))
