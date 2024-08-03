year_pushkin='1799' #год рождения
data_pushkin='26' # дата рождения

def funcion(str,data):
    year = input(f'Ввведите {str} А.С.Пушкина:')
    while year != data:
        print("Не верно")
        year = input('Ввведите год рождения А.С.Пушкина:')

funcion('год рождения',year_pushkin)
funcion('дату рождения',data_pushkin)


