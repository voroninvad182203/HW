print('Введите целое число')
a=int(input())
if a in range(10,22) or a in range(31,40):
    print('Точка в множестве')
else:
    print('Точка вне множества')
    
print('Введите целое число')
a=int(input())
print('Введите целое число')
b=int(input())
if (a in range(-5,1) and b in range(-5,1)) or (a in range(3,8) and b in range(3,8)):
    print('Да')
else:
    print('Нет')
    
print('Введите значение пути')
a=float(input())
print('Введите значение времени')
b=float(input())
c=a/b
if c<30:
    print('Медленно')
elif c>30 and c<=60:
    print('Средне')
elif c>60:
    print('Быстро')

print('Введите трёхзначное число:')
x=int(input())
while x<100 or x>999:
    if x<100 or x>999:
        print('Число должно быть трёхзначным!')
    print('Введите трёхзначное число:')
    x=int(input())
a=x//100
b=x//10%10
c=x%10
d=a+b+c-max(a,b,c)-min(a,b,c)
if d==max(a,b,c)-min(a,b,c):
    print('Число n "интересное"')
else:
    print('Число n не "интересное"')
 
print('Введите ник-нейм')
a=str(input())
if len(a)<3:
    print('Ник-нейм должен состоять минимум из 3 символов!')
elif len(a)>15:
    print('Ник-нейм должен состоять максимум из 15 символов!')
else:
    print('Ник-нейм принят')
    
print('Ввведите значение x:')
x=float(input())
print('Введите значение y')
y=float(input())
while x==0 or y==0:
    if x==0 or y==0:
        print('X и Y не должны равняться 0')
    print('Ввведите значение x:')
    x=float(input())
    print('Введите значение y')
    y=float(input())
if x>0 and y>0:
    print('Точка принадлежит первой четверти')
    print('Введите две строки')
    a=str(input())
    b=str(input())
    if len(a)>len(b):
        print(b)
    else:
        print(a)
elif x<0 and y>0:
    print('Точка принадлежит второй четверти')
    f=(2*abs(x)-y)/y**2
    print(f)
elif x<0 and y<0:
    print('Введите строку')
    a=str(input())
    print('Точка принадлежит третьей четверти')
    print('x=',x*len(a), 'y=',y*len(a))
else:
    print('Точка принадлежит четвёртой четверти')
    if abs(x)>abs(y):
        print('Координата x – наибольшая по модулю')
    elif abs(y)==abs(x):
        print('«Координаты равны по модулю')
    else:
        print('Координата y – наибольшая по модулю')
        
print('Введите любое предложение')
a=str(input())
if 'кот' in a:
    print('Мы погладили кота')       
