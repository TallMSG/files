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
        # dishname = str(ingridients[0])
        # ing_numb = int(ingridients[1])
        ingridients.remove(ingridients[0])
        ingridients.remove(ingridients[0])

        ing_list = []
        for item in ingridients:
            aaa = item.split(' | ')
            ing_list.append(aaa)


        ing_descript = {}
        for item in ing_list:
            ing_descript[item[0]] = {}
            ing_descript[item[0]]['ingridient_name'] = item[0]
            ing_descript[item[0]]['quantity'] = item[1]
            ing_descript[item[0]]['measure'] = item[2]

    return ing_descript



def open_all ():
    a = open_dish('dish1.txt')
    b = open_dish('dish2.txt')
    c = open_dish('dish3.txt')
    cook_book = {}
    cook_book['Омлет'] = a
    cook_book['Утка по-пекински'] = b
    cook_book['Запеченный картофель'] = c
    return cook_book


# open_all()



def cook_omelet(person):
    uuu = open_all()
    omelet_ing = {}
    for k, v in uuu.items():
        if k == 'Омлет':
            omelet_ing = v

    ing = []
    quant = []
    meas = []
    for k, v in omelet_ing.items():
        name = v['ingridient_name']
        quantity = v['quantity']
        measure = v['measure']
        ing.append(name)
        quant.append(int(quantity)*person)
        meas.append(measure)
    print(ing[0], quant[0], meas[0])
    print(ing[1], quant[1], meas[1])
    print(ing[2], quant[2], meas[2])


def cook_duck(person):
    uuu = open_all()
    duck_ing = {}
    for k, v in uuu.items():
        if k == 'Утка по-пекински':
            duck_ing = v

    ing = []
    quant = []
    meas = []
    for k, v in duck_ing.items():
        name = v['ingridient_name']
        quantity = v['quantity']
        measure = v['measure']
        ing.append(name)
        quant.append(int(quantity)*person)
        meas.append(measure)
    print(ing[0], quant[0], meas[0])
    print(ing[1], quant[1], meas[1])
    print(ing[2], quant[2], meas[2])
    print(ing[3], quant[3], meas[3])


def cook_potatoes(person):
    uuu = open_all()
    potatoes_ing = {}
    for k, v in uuu.items():
        if k == 'Запеченный картофель':
            potatoes_ing = v

    ing = []
    quant = []
    meas = []
    for k, v in potatoes_ing.items():
        name = v['ingridient_name']
        quantity = v['quantity']
        measure = v['measure']
        ing.append(name)
        quant.append(int(quantity)*person)
        meas.append(measure)
    print(ing[0], quant[0], meas[0])
    print(ing[1], quant[1], meas[1])
    print(ing[2], quant[2], meas[2])


def get_shop_list_by_dishes():

    dishes = input('Введите блюда (Омлет - a, Утка по-пекински - b, Запечённый картофель - c): ')
    person_count = int(input('Введите количество персон: '))
    print('')

    while True:
        print('Потребуется:')
        if 'a' in dishes:
            cook_omelet(person_count)
        if 'b' in dishes:
            cook_duck(person_count)
        if 'c' in dishes:
            cook_potatoes(person_count)
        else:
            return
        break

get_shop_list_by_dishes()




