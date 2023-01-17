# p5.4
letter ='''      Dear {saturation} {name},\n
      Thank you for your letter. We are sorry that our {product} {verbed} in your
{room}.Please note that it should never be used in a {room}, especially near any
{animals}.

      Send us your receipt and {amount} for shipping and handling. We will send you
another {product} that, in our tests, is {percent}% less likely to have {verbed}.
      Thank you for your support.
      Sincerely,
      {spokesman}
      {job_title}'''
print(letter)
# p5.5
letter ='''      Dear {0[saturation]} {0[name]},\n
      Thank you for your letter. We are sorry that our {0[product]} {0[verbed]} in your
{0[room]}.Please note that it should never be used in a {0[room]}, especially near any
{0[animals]}.

      Send us your receipt and {0[amount]} for shipping and handling. We will send you
another {0[product]} that, in our tests, is {0[percent]}% less likely to have {0[verbed]}.
      Thank you for your support.
      Sincerely,
      {0[spokesman]}
      {0[job_title]}'''
list = {'saturation' : 'Sir',
'name' : 'Alex',
'product' : 'ball',
 'verbed' : 'served',
 'room' : 'room 201',
 'animals' : 'dog',
 'amount' : 'box',
 'percent' : '20',
 'spokesman' : 'James',
'job_title' : 'courier'
        }
print(letter.format(list))

# p5.6
boat = 'duck'
English_submarine="%sy mc%sface" % (boat,boat)
print(English_submarine.title())
horse = 'gourd'
Australian_racehorse = "%sy mc%sface" % (horse, horse)
print(Australian_racehorse.title())
train = 'spitz'
Swedish_train = "%sy mc%sface" %(train, train)
print(Swedish_train.title())

# p5.6 다른방법
list = ["duck", "gourd", "spitz"]
for i in range(0,3):
    print("%sy Mc%sface" %(list[i].capitalize(),list[i].capitalize()))

# p5.7
list = ["duck", "gourd", "spitz"]
for i in range(0,3):
    print("{}y Mc{}face".format(list[i].capitalize(),list[i].capitalize()))
# p5.8
list = ["duck", "gourd", "spitz"]
for i in range(0,3):
    print(f'{list[i].capitalize()}y Mc{list[i].capitalize()}face')

# p6.2
guess_me = 7
number = 1
while number< guess_me:
  print("too low")
  number += 1
  while number == guess_me:
   print("found it!")
   break
  while number > guess_me:
   print('oops')
   break

# #6.3
guess_me = 5
for number in range(10):
    if(number < guess_me):
        print('too low')
    elif(number == guess_me):
        print('found it!')
        break
    else:
        print('oops')
        break






