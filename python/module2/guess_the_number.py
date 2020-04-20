import random
print("Загадано число от 1 до 100. Попытайтесь его угадать")
the_number = random.randrange(1, 100)
user_guess = int(input())
while user_guess != the_number:
    if user_guess < the_number:
        print("Нет, оно больше. Попробуйте ещё раз:")
    elif user_guess > the_number:
        print("Нет, оно меньше. Попробуйте ещё раз:")
    user_guess = int(input())
else:
    print(f"Верно! Это число {the_number}")
