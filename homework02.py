import random
secret = random.randint(1,10)
guess = random.randint(1,10)
print(secret, guess)

if secret > guess:
    print('too low')
elif secret < guess:
    print('too high')
else:
    print('just right')



