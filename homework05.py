#p8.11
odd_number = {i for i in range(10) if i%2==1}
print(odd_number)

#p8.13
keys = 'optimist', 'pessimist', 'troll'
values = 'The glass is half full', 'The glass is half empty', 'How did you get a glass?'
a = dict(zip(keys, values))
print(a)

#p8.14
titles= ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a mon ster', 'A haunted yarn shop']
movies= dict(zip(titles, plots))
print(movies)

#p9.1
def good():
    return ['Harry','Ron','Hermione']
print(good())