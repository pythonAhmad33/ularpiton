from os import system; system ("clear")

system ('figlet -f smmono12 -t Binary2 | lolcat')

teks = input('masukkan teks: ')

x = ''.join(format(ord(x), '08b') for x in teks)
print (f'{teks} in binary >>> {x}')
print (f'''

        bit = {len(x)}
        byte = {len(teks)}

        ''')
