#!/usr/bin/python3

# IP address validation tool using loops, if/else statements

print("Welcome to the IP validation tool")
ipAddr = input("Please enter an address for validation: ")

position = 1
octet = 1
number = ''
failstate = ''

for digit in ipAddr:
    if ipAddr == '0.0.0.0':
        failstate = "Error: 0.0.0.0 is not a valid IP address"
        break
    elif digit != '.':
        if digit in '0123456789':
            number += digit
        else:
            failstate = "Error in position {} in octet {}; Invalid character: {}".format(position, octet, digit)
            break
    else:
        if len(number) == 0 or len(number) > 3:
            failstate = "Error: Octet {} is {} digits long.  Valid octets are between 1-3 digits".format(octet,
                                                                                                         len(number))
            break
        elif int(number) < 0 or int(number) > 255:
            failstate = "Invalid value in octet {}; Acceptable values range from 0 - 255.  " \
                        "Entered value is {}".format(octet, number)
            break
        number = ''
        octet += 1
        if octet > 4:
            failstate = "Too many octets; IPv4 addresses are exactly 4 octets.  Provided address has {}".format(octet)
            break
    position += 1
else:
    if (len(number) == 0) or (len(number) > 3):
        failstate = "Error: Octet {} is {} digits long.  Valid octets are between 1-3 digits".format(octet, len(number))
    elif int(number) < 0 or int(number) > 255:
        failstate = "Invalid value in octet {}; Acceptable values range from 0 - 255.  " \
                    "Entered value is {}".format(octet, number)

    elif position > 16:
        failstate = "Error: IP Address cannot have more than 15 characters.  {} characters found".format(position)
    elif octet != 4:
        failstate = "Error near position {}, IP address contains {} octets, 4 required".format(position, octet)
    else:
        print("pinging {}...".format(ipAddr))
if failstate:
    print(failstate)
else:
    print("{} appears to be a valid IP address".format(ipAddr))
