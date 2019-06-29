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

with open('dish1.txt') as f:
    ingridients = []
    for line in f:
        line = line.strip()
        ingridients.append(line)
    # print(type(ingridients))
    ing_list = []
    for item in ingridients:
        dishname = str(ingridients[0])
        ing_numb = int(ingridients[1])
        split_list2 = ingridients[2].split(' | ')
        split_list3 = ingridients[3].split(' | ')
        split_list4 = ingridients[4].split(' | ')
    ing_list.append(split_list2)
    ing_list.append(split_list3)
    ing_list.append(split_list4)
    # print(dishname)
    # print(ing_list)
    ing_descript = {}
    for item in ing_list:
        ing_descript['ingridient_name'] = item[0]
        ing_descript['quantity'] = item[1]
        ing_descript['measure'] = item[2]
        print(ing_descript)

# Не могу сохранить словарь после цикла for, сохраняются только последние значения








    # print(f'Читаем файл после цикла: {f.read()}')
# print(f'Все строрки: {all_lines}')



    #   считать первую строку файла:
    #   for line in range(1):
    #     head = next(f).strip()




# преобразовать строки в список
# with open(fname) as f:
#     content = f.readlines()
# # you may also want to remove whitespace characters like '\n' at the end of each line
# content = [x.strip() for x in content]


