obj={'матем':'Петрова','русский':'Побединский','английский':'Баранова','история':'Сидорова', 'биология':'Соколова','география':'Мирный', 'информатика ':'Голубев '}
key=input('введите учебный предмет: ')
if key in obj :
    teach=obj[key]
    print(f'преподаватель по {key}: {teach}')
else:
    if key not in obj:
        print ('такого предмета нет в списке ')
    for dis, teach in obj.items():
        print(f'{dis}:{teach}')