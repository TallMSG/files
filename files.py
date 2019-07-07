with open('recipes.txt') as f:
    record = 1
    output = open('dish{}.txt'.format(record), 'w')
    for line in f:
        if line == "\n":
            record += 1
            output.close()
            output = open('dish{}.txt'.format(record), 'w')
        else:
            output.write(line)

def open_dish(a):

    with open(a) as f:
        ingridients = []
        for line in f:
            line = line.strip()
            ingridients.append(line)
        dishname = str(ingridients[0])
        ing_numb = int(ingridients[1])
        ingridients.remove(ingridients[0])
        ingridients.remove(ingridients[0])

        ing_list = []
        for item in ingridients:
            aaa = item.split(' | ')
            ing_list.append(aaa)
        # print(dishname)
        # print(ing_numb)
        # print(ing_list)

        ing_descript = {}
        for item in ing_list:
            ing_descript[item[0]] = {}
            ing_descript[item[0]]['ingridient_name'] = item[0]
            ing_descript[item[0]]['quantity'] = item[1]
            ing_descript[item[0]]['measure'] = item[2]
        # print(ing_descript)

    return ing_descript



def open_all ():
    a = open_dish('dish1.txt')
    b = open_dish('dish2.txt')
    c = open_dish('dish3.txt')
    cook_book = {}
    cook_book['Омлет'] = a
    cook_book['Утка по-пекински'] = b
    cook_book['Запечёный картофель'] = c
    # print(cook_book)
    return cook_book


# open_all()





# person_count = int(input('Введите количество персон: '))



def cook_omelet():
    uuu = open_all()
    for k, v in uuu.items():
        omelet_ing = {}
        if k == 'Омлет':
            omelet_ing = v


        for k, v in omelet_ing.items():
            new_dict = omelet_ing[k]
            # print(new_dict)


            for k, v in new_dict.items():
                name = new_dict['ingridient_name']
                if k == 'ingridient_name':
                    sss = del new_dict[k]
                    print(sss)




cook_omelet()


# def get_shop_list_by_dishes(dishes, person_count):

# while True:
#     print('Введите блюда:')
#     dishes = input('Омлет - a, Утка по-пекински - b, Запечённый картофель - c: ')
#     if dishes == 'a':
#         cook_omelet()
#     elif dishes == 'b':
#         cook_duck()
#     elif dishes == 'c':
#         cook_potatoes()
#     else:
#         print('Такого блюда не существует')






