# 7.8
# surprise = ['Groucho', 'Chico', 'Harpo']
# print(surprise)

#7.9
# name = surprise[-1].lower()
# print(name)
# name_list = list(name)
# print(name_list)
# name_list.reverse()
# print(name_list)   # list는 역순으로 저장됨.
# name2 = ''.join(name_list)
# print(name2)
# name3 =name2.capitalize()
# print(name3)
# surprise[-1] = name3
# print(surprise)

#7.9 다른방법
# surprise[2] = surprise[2].lower()
# surprise[2]= surprise[2][::-1]
# surprise[2]=surprise[2].capitalize()
# print(surprise)

#7.10
# number_list=[number for number in range(10) if number %2 ==0]
# print(number_list)

#7.11
# start1= ["fee", "fie", "foe"]
# rhymes = [
#     ("flop", "get a mop"),
#     ("fope", "turn the rope"),
#     ("fa", "get your ma"),
#     ("fudge", "call the judge"),
#     ("fat", "pet the cat"),
#     ("fog","walk the dog"),
#     ("fun", "say we're done"),
# ]
# start2 = "Someone better"
# for i in range(0,len(start1)):
#     start1_mod=f'{start1[i].capitalize()}! '
#     start1[i]=start1_mod
#     inx1, inx2, inx3 = start1
# for k in range(0,len(rhymes)):
#     a,b = list(rhymes[k])
#     print(f'{inx1} {inx2} {inx3} {a.capitalize()}!\nSomeone better {b}.')

