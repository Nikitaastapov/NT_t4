import os
cook_book={}
path = os.getcwd()
file = 'recipes.txt'
full_name = os.path.join(path, file)
with open (full_name, 'r', encoding='UTF-8') as f:
    num = 1
    for line in f:
        line = line.rstrip('\n')
        if len(line) == 0:
            num = 0
        if num == 1:
            meal = line
            cook_book[meal]=[]
            # print(meal)
        if num >2:
            line = line.split(' | ')
            temp_dic = {}
            temp_dic['ingredient_name'] =line[0]
            temp_dic['quantity']=line[1]
            temp_dic['measure']=line[2]
            cook_book[meal].append(temp_dic)
        num += 1      
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shopping_list = {}
    for asked_meal in dishes:
        if asked_meal not in cook_book.keys():
            print(f'{asked_meal} нет в меню')
        else:
            add_to_buy(asked_meal, person_count, shopping_list)
            # print('Принято')
    return shopping_list

def add_to_buy(asked_meal, person_count, shopping_list):
    for ing in cook_book[asked_meal]:
        if ing['ingredient_name'] not in shopping_list.keys():
            # shopping_list[ing['ingredient_name']] = {}
            shopping_list[ing['ingredient_name']]={'measure': ing['measure']}
            shopping_list[ing['ingredient_name']]['quantity'] = int(ing['quantity'])*person_count
        else:
            shopping_list[ing['ingredient_name']]['quantity'] += int(ing['quantity'])*person_count
  

# print(get_shop_list_by_dishes(['Омлет','Фахитос'] , 2))
# print(get_shop_list_by_dishes(['Омлет','Омлет'] , 1))
# print(get_shop_list_by_dishes(['Рыба','Омлет'] , 1))
# print(get_shop_list_by_dishes(['Омлет'] , 2))