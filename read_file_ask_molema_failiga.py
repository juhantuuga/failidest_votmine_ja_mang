def is_number(string):
    try:
        int(string)  # int kaotab murdarvul komakoha ära ja annab täisarvu ehk 45.5 on 45 ntks #
        return True
    except ValueError:
        return False


# print(is_number('5'))
# print(is_number('Lammas'))
# print(is_number('4w6'))

filename = 'Create-MyCSV-s.csv'
total = 0

f = open(filename, 'r')  # See fail ei vaja encodingut, sest pole täpitähti
cols = len(f.readline().strip().split(';'))  # Mitu veergu failis on. Esimene variant
'''line = f.readline().strip()  # 1. Loe failist üks rida ilma reavahetuseta. Teine variant kolme reaga
parts = line.split(';')  # 2. Tükelda rida semikoolonist
cols = len(parts)  # 3. Mitu elementi on listis'''
f.close()  # Sulge fail, muidu ei saa pärast seda sama faili töödelda

col = input('Mitmes veerg kokku liita [1-'+str(cols)+ ']? ')  # Sisesta number esimene variant
#  col = input(f'Mitmes veerg kokku liita [1-{cols}]? ')  # Sisesta number teine variant
if is_number(col):  # Kas kasutaja sisestus ehk veeru nr on number
    col = int(col)  # Tee kasutaja sisestus numbriks
    if 0 < col <= cols:  # Kas kasutaja sisestatud number on vahemikus
        col -= 1  # ehk col = col - 1, sest kasutajalt küsitakse 10ndani, aga arvuti lõpetab 9ndaga ära.

        with open(filename, 'r', encoding='utf-8') as f:  # Avab faili ja sulgeb. Windowsi variandis 3 argumenti
            all_lines = f.readlines()  # Kogu faili sisu listi ridade kaupa
        #   print(all_lines)  # Testiks
            for line in all_lines:  # Võtab ühe rea ja kasutades print käsklust, siis paneb ühe tühja rea vahele
                line = line.strip()  # (strip) võtab ära tühjad kohad (tühikud, reavahetused) ära.
                parts = line.split(';')  # Tükelda rida semikoolonist
                if is_number(parts[col]):  # Kas on täisarv
                    total += int(parts[col])  # += on sama kui total = total + int(parts[col])

        print(total)
    else:
        print('Vahemikust väljas number, lammas. Proovi uuesti')
else:
    print('See pole ju number, oinas :)')
