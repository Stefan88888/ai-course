#for i in range(1, 11):
#    print(i ** 2)

#for i in range(10, 0, -1):
#        print(i)
#
#print("Liftoff")

#counter = 10
#while counter >= 1:
#    print(counter)
#    counter = counter - 1

#print("Liftoff!")

#Напиши цикл for по списку чисел [3, 7, 2, 9, 4, 11, 6], который печатает только чётные числа (используй % — оператор остатка от деления, ты его уже применял в своём conditions_practice.py в самом начале).

numbers = [3, 7, 2, 9, 4, 11, 6]
for number in numbers:
    if number %2 == 0:
        print(number)