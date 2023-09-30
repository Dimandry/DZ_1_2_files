
ingredients_list = []
cook_book = {}
dish_list = []
with open('recept.txt', encoding='utf8') as f:
    for line in f:
        dish_name = line.strip()
        num = int(f.readline())
        for i in range(num):
            a1, a2, a3 = f.readline().strip().split('|')
            dish_list.append(dict({'ingredient_name': a1, 'quantity': int(a2), 'measure': a3}))
        f.readline()
        cook_book.update({dish_name: dish_list})
        dish_list = []
for key, value in cook_book.items():
    print("{0}: {1}".format(key, value))


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    print(ingr_list)
    return ingr_list

get_shop_list_by_dishes(['Омлет', 'Фахитос'], 4)









