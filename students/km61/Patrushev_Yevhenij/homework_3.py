#task1------------------------------------------------------------
"""
	Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
	По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
"""



# program of calculating factorial
n=int(input())# number of factorial
F=1 #factorial
for i in range(1,n+1):
    F*=i
print(F)

#-----------------------------------------------------------------


#task2------------------------------------------------------------
"""
	По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!. 
	В решении этой задачи можно использовать только один цикл. 
	Пользоваться математической библиотекой math в этой задаче запрещено.
"""



# program of calculating the sum of factorial
n=int(input()) #n of last number
F=1 #factorial
sum=0 # sum of factorial
for i in range(1,n+1):
    F*=i
    sum+=F
print(sum)

#-----------------------------------------------------------------


#task3------------------------------------------------------------
"""
	Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
	Подсчитайте количество нулей среди введенных чисел и выведите это количество.
	Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.
"""



# program of calculating the quantity of 0
# N-how many numbers user will be input
# a-numbers which user input
N=int(input())
sum = 0 # sum of 0
for i in range (1,N+1):
    a=int(input())
    if a==0 :
        sum = sum + 1
print(sum)

#-----------------------------------------------------------------


#task4------------------------------------------------------------
"""
	По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без пробелов.
"""



# program which print ladder of natural numbers
# n-the biggest natural numbers in the last stair
# i-how many stairs
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(j+1,end='')
    print()
	
#-----------------------------------------------------------------


