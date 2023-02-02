# 10.1
class Thing:
    print('')
    # pass  써도 위와 같음


example = Thing()

print(Thing)  # 출력값 : <class '__main__.Thing'>
print(example)  # 출력값 : <__main__.Thing object at 0x00000201B565C290>


# 10.2
class Thing2:
    pass


some = Thing2()           # some 객체 만듬
some.letters = 'abc'      # some 객체에 letters 속성 할당
print(some.letters)

# 10.2 다른 방법
# class Thing2:
#     letters = 'abc'  # letters 속성 만듬
#
#
# print(Thing2.letters)  # 출력값: abc
# # print(Thing2)     # 출력값: <class '__main__.Thing2'>
# # print(Thing2())   # 출력값: <__main__.Thing2 object at 0x0000017C6A6BC310>


# 10.3
class Thing3:
    pass


inst = Thing3()
inst.letters = 'xyz'
print(inst.letters)


# 10.3 다른방법
class Thing3:
    def __init__(self):
        self.letters = 'xyz'
# print(Thing3.letters)     # 에러나옴 : AttributeError: type object 'Thing3' has no attribute 'letters'


inst = Thing3()
print(inst.letters)


# 10.4
class Element:
    def __init__(self):
        self.name = 'Hydrogen'
        self.symbol = 'H'
        self.number = 1

inst = Element()
print(inst.name,inst.symbol, inst.number)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

inst = Element('Hydrogen', 'H', 1)
print(inst.name, inst.symbol, inst.number)


# 10.5
class Element:
    def __init__(self, el_dict):
        self.el_dict = el_dict

hydrogen = Element({'name': 'Hydrogen',
           'symbol': 'H',
           'number': 1
           })                           # hydrogen 객체 생성
print(hydrogen.el_dict)
