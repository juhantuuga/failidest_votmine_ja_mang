import csv

import unicodedata


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


# print(strip_accents('Šaša;Želežnjov'))
# Muutujad
src = 'Persons.csv'  # Originaalfail
dst = 'Persons_new.csv'  # Uus fail
line_counter = 0  # Faili ridade lugeja
my_header = ['Kasutajanimi', 'E-post']  # Kaks uut päist
domains = ['@woman.ee', '@man.ee']

# Loome uue päise
f = open(src, 'r', encoding='utf-8')
data = csv.reader(f, delimiter=';')  # Peame ütlema, sest meil on eraldajaks ;, mitte ,
header = next(data)
f.close()

# Uus päis
header_fin = ';'.join(header + my_header)  # Lisame algse päise uue päisega
# print(header_fin)

with open(src, 'r', encoding='utf-8') as f:
    with open(dst, 'w', encoding='utf-8') as fn:
        data = csv.reader(f, delimiter=';')  # Kogu failisisu listi
        for row in data:
            if line_counter == 0:  # Olen esimesel real
                line_counter += 1
                fn.write(header_fin + '\n')
            # print(row, row[0])  # Testiks, et saaks aru, mis sisu antakse
            else:
                first_name = row[0]
                last_name = row[1]
                # Asenda eesnimes olev tühik sidekriipsuga
                first_name = first_name.replace(' ', '-')
                username = '.'.join([first_name, last_name])
                username = strip_accents(username.lower())  # Kas paned lower() kohe pärast username või pärast sulge

                if row[3] == 'N':
                    email = username + domains[0]
                else:
                    email = username + domains[1]
                new_line = ';'.join(row + [username, email])
                fn.write(new_line + '\n')
                print(new_line)
print('Valmis')

