print('введите количество студентов')
N = int(input())
print("введите количество шаурмы")
K = int(input())
print(K // N)
print(K % N)


print("введите число")
d = int(input())
a = str(d % 10)
b = str(d//10 % 10)
c = str(d//100 % 10)
print(a+b+c)
print(a+c+b)
print(b+a+c)
print(b+c+a)
print(c+a+b)
print(c+b+a)

print('введите время готовки')
a = int(input())
print('введите время уборки')
b = int(input())
print('введите время стирки')
c = int(input())
d=600
e=d+a+b+c
i=e%60
t=e//60
if i<10:
    i='0'+str(i)
while t > 24:
    t = t-24
if t < 10:
    t = "0" + str(t)
print(t, ':', i)

print('введите пароль')
a = (input())
print("введите подтверждение пароля")
b = (input())
if a == b:
    print("Пароль принят")
else: print("Пароль не принят")


print('введите число')
A = int(input())
print('введите второе число')
B = int(input())
if A >= B:
    print(str(A),'- наибольшее число')
    print(str(B), " - наименьшее число")
else:
    print(str(B), '- наибольшее число')
    print(str(A), " - наименьшее число")


print('введите возраст')
a = int(input())
if a >= 18:
    print('доступ разрещён')
else:
    print('доступ запрещён')

print('введите число')
d = int(input())
a = str(d % 10)
b = str(d//10 % 10)
c = str(d//100 % 10)
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)

print("введите число")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
count = 0
g = 0
if a % 2 > 0:
    count += 1
    g += a
if b % 2 > 0:
    count += 1
    g += b
if c % 2 > 0:
    count += 1
    g += c
if d % 2 > 0:
    count += 1
    g += d
print(count, 'количество ничетных чисел')
print(g, "сумма ничётных чисел")
