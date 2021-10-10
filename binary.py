# script by Ahmad
# recode? boleh asal demi perkembanganb script

from os import system # import module
from sys import *
from time import sleep

print ("\033[32;1m")
# ========== program ========== #

def animate(teks):
    for i in teks:
        stdout.write(i)
        stdout.flush()
        sleep(0.1)

def biner(teks):
    print (66*'_')  

    biner = ''.join(format(ord(x),'08b') for x in teks)
    octal = ''.join(format(ord(x),'0o') for x in teks)
    hexa = ''.join(format(ord(x), '0x') for x in teks)

    print (f'\n{66*"_"}\n\n{teks} in binary >> {biner}')
    print (f'{teks} in octal >> {octal}')
    print (f'{teks} in hexa >> {hexa}')

    print (f'\nbytes(binary) = {len(teks)}')
    print (f'bits(binary) = {len(biner)}')
    print (66*'_')

    def tri():
        back = input('\ntry again?(y/n) ')
        if back=="y":
            menu()
        elif back=="n":
            print("\nbyee .\n")
            exit()
        else:
            print ("\n[!] error! Enter just y or n")
            sleep(1)
            tri()
    tri()
        

def menu():
        system ("clear")
        system ('figlet -f pagga -tc Daftar menu')
        print ("script by Ahmad")

        print (66*"_")
        print ("""

    1. desimal/ascii > biner/octal/hexa
    2. about
    3. exit

            """)

        
            
        etc = input("Enter your choice > ")
        if etc == "1":
            de = input('Enter > ')
            biner(de)
        
        elif etc == "2":
            name = input ('Enter your name: ')
            system("clear")
            animate (f'Hello {name}')
            
            print ("\n\nThis script was made by Ahmad,he is 16 ")
            print ("years old. the function of this script is")
            print ('to convert both numbers and letters to ')
            print ('binary,octal and hexadecimal.')
            print ("\n[!] anonymouse\n")

        elif etc == "3":
            print ("\nbyee..\n")
            exit()

        else:
            menu()

menu()

# ========= done ========= #
print ('\033[0m')

