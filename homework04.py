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

#8.1
e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)
#8.2
print(e2f['walrus'])

#8.3
f2e = {}  #f2e 라는 새로운 프랑스어-영어 dictionary 만들기
for key, value in e2f.items():
    f2e[value]=key
print(f2e)
#8.3 다른방법
f2e={v:k for k,v in e2f.items()}
print(f2e)

#8.4
print(e2f['dog'])

#8.5
print(e2f.keys())

#8.6
life = {'animals' : {'cats' : {'Henri', 'Grumpy','lucy'}, 'octopi' : '', 'emus' : ''}, 'plants' : '', 'other' : '' }

#8.7
print(life.keys())
print(list(life.keys()))  # list 함수를 활용해 정리해서 출력

#8.8
print(life['animals'].keys())

#8.9
cat = life['animals']['cats']
print(cat)

#8.10
squares =  {i : i**2 for i in range(10)}
print(squares)