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
col = 0

with open(filename, 'r', encoding='utf-8') as f:  # Avab faili ja sulgeb. Windowsi variandis 3 argumenti (sulgudes)  #
    all_lines = f.readlines()  # Kogu faili sisu listi ridade kaupa
#   print(all_lines)  # Testiks
    for line in all_lines:  # Võtab ühe rea ja kasutades print käsklust, siis paneb ühe tühja rea vahele
        line = line.strip()  # (strip) võtab ära tühjad kohad (tühikud, reavahetused) ära.
        parts = line.split(';')  # Tükelda rida semikoolonist
        if is_number(parts[col]):  # Kas on täisarv
            total += int(parts[col])  # += on sama kui total = total + int(parts[col])

print(total)
