# 9.3
def test(func):
    def new_function(*arg, **kwangs):
        print('start')
        result = func(*arg, **kwangs)
        print('end')
        return result
    return new_function

@test
def exercise():
    print("실행")
exercise()

