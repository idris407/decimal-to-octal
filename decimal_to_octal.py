decimal = int(input("Enter a decimal number: "))

octal = ""

while decimal > 0:
    remainder = decimal % 8
    octal = str(remainder) + octal
    decimal = decimal // 8

print("Octal number is:", octal)