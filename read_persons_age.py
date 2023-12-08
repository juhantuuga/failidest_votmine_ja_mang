from datetime import date


def calculate_age(birth_date):
    today = date.today()
    age_func = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age_func


src = 'Persons.csv'
dst = 'Persons_age.csv'
line_counter = 0
f = open(src, 'r', encoding='utf-8')
header = f.readline().strip()  # Eesnimi;Perenimi;Sünniaeg;Sugu;Isikukood
header = header + ';Vanus'  # Eesnimi;Perenimi;Sünniaeg;Sugu;Isikukood;Vanus
f.close()

with open(src, 'r', encoding='utf-8') as f:
    with open(dst, 'w', encoding='utf-8') as fn:
        all_lines = f.readlines()[1:]  # Loe read pärast päist
        fn.write(header + '\n')  # Kirjuta päis ja tee uus rida
        for line in all_lines:
            line = line.strip()  # Poolita read
            # Võta kolmas väärtus semikooloniga eraldatud väljadest
            year = int(line.split(';')[2].split('.')[2])  # Sellest omakorda kolmas väli ehk aasta
            month = int(line.split(';')[2].split('.')[1])  # Sellest omakorda teine väli ehk kuu
            day = int(line.split(';')[2].split('.')[0])  # Sellest omakorda esimene väli ehk päev
            age = calculate_age(date(year, month, day))  # Kasuta funktsiooni calculateAge
            new_line = line + ';' + str(age)  # Anna rida ja lisa lõppu vanus
            fn.write(new_line + '\n')  # Kirjuta antud rida faili ja tee uus rida järgmisele
        print('Valmis')

# Driver code
print(calculate_age(date(1990, 5, 18)), "years")
