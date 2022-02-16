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
print(cook_book)