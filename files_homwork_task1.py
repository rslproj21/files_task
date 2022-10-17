cook_book = {}

with open('file.txt', encoding='utf8') as dish_list:
    for dishes in dish_list:
        ingridients = []
        ing_names = dishes.replace('\n', '')
        weight_count = dish_list.readline()
        for count in range(int(weight_count)):
            weight = dish_list.readline().replace('\n', '')
            ingridient, size, measure = weight.split(' | ')
            dish_composition = {}
            dish_composition['ingridient'] = ingridient
            dish_composition['quantity'] = size
            dish_composition['measure'] = measure
            ingridients.append(dish_composition)
        cook_book[ing_names] = ingridients
        dish_list.readline()
print(cook_book)

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    if type(dishes) == str:
        cook(dishes, person_count)
    if type(dishes) == list:
        for meals in dishes:
            print()
            cook(meals, person_count)

def cook(dishes, person_count):
    eat = []
    for name, ing in cook_book.items():
        if name == dishes:
            for ingridient in ing:
                ung_name = ''
                ung_name += str((ingridient['ingredient_name']) + ' ' + (str(int(ingridient['quantity']) * person_count)) + ' ' + (ingridient['measure']))
                eat.append(ung_name)
    for meals in eat:
        print(meals)
        
files = []
counting = 0

def data_output(file, some_file):
    replace_view = file.name.replace('.txt', '')
    print(file.name)
    print((len(some_file)))
    count = 1
    for ingor in some_file:
        print(f'Строка номер: {count}, файл номер: {replace_view}')
        count += 1
    count = 1

with open('1.txt', 'rt') as file:
    f = file.readlines()
    files.append(len(f))
with open('2.txt') as file_2:
    f2 = file_2.readlines()
with open('3.txt') as file_3:
    f3 = file_3.readlines()
    files.append(len(f3))

while counting <= 2:
    if len(f) == min(files):
        data_output(file, f)
    if len(f2) == min(files):
        data_output(file, f2)
    if len(f3) == min(files):
        data_output(file, f3)
    files.remove(min(files))
    counting += 1        
        
