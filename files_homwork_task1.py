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
        
file_len = []
countt = 0

def file_print(file, f):
    a = file.name.replace('.txt', '')
    print(file.name)
    print((len(f)))
    count = 1
    for i in f:
        print(f'Строка номер {count} файл номер {a}')
        count += 1
    count = 1

with open('1.txt', 'rt') as file:
    f = file.readlines()
    file_len.append(len(f))
with open('2.txt') as file2:
    f2 = file2.readlines()
    file_len.append(len(f2))
with open('3.txt') as file3:
    f3 = file3.readlines()
    file_len.append(len(f3))


while countt <= 2:
    if len(f) == min(file_len):
        file_print(file, f)
    if len(f2) == min(file_len):
        file_print(file2, f2)
    if len(f3) == min(file_len):
        file_print(file3, f3)
    file_len.remove(min(file_len))
    countt += 1