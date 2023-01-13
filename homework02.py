food_list = ['완두콩', '체리', '수박', '호박']
small = False
green = False
if small:
    if green:
        print(f'{food_list[0]}은 작고 녹색이다')
    else:
        print(f'{food_list[1]}는 작고 녹색이 아니다')
else:
    if green:
        print(f'{food_list[2]}은 크고 녹색이다')
    else:
        print(f'{food_list[3]}은 크고 녹색이 아니다')


