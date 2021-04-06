print(type(17))
print(type('17'))
pi = 3.1415926535897931
print(type(pi))

'''
Python reserves 35 keywords:
and
as
assert
break
class
continue
def
del
elif
else
except
False
finally
for
from
global
if
import
in
is
lambda
None
nonlocal
not
or
pass
raise
return
True
try
while
with
yield
async
await
'''

'''
name = input('What is your name?\n')
print(name)

if -3 < 0 :
    pass

inp = input('Enter Fahrenheit Temperature:')
try:
    fahr = float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a number')
'''


x = 1
y = 0
print(y != 0 and (x/y) > 2)

'''
len - функция, которая сообщает, сколько элементов находится в ее аргументе

len('Hello world')

int может преобразовывать значения с плавающей запятой в целые числа, но не округляет; отрубает дробную часть:
>>> int(3.99999)
3
>>> int(-2.3)
-2

Этот оператор создает объект модуля с именем math.
>>> import math
Объект модуля содержит функции и переменные, определенные в модуле. Чтобы получить доступ к одной из функций, вы должны указать имя модуля и имя функции, разделенные точкой


Модуль random
Функция random возвращает случайное число с плавающей запятой от 0,0 до 1,0 (не включая)
import random

for i in range(10):
    x = random.random()
    print(x)
Функция randint принимает параметры lowи highи возвращает целое число от lowдо high(включая оба).
random.randint(5, 10)

Чтобы выбрать элемент из последовательности случайным образом, вы можете использовать choice:
>>> t = [1, 2, 3]
>>> random.choice(t)
2
'''



def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')
repeat_lyrics()


'''
continue завершает текущую итерацию цикла

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print('Done!')

sum(arr)-кол-во элементов

>>> 'a' in 'banana'
True
>>> 'seed' in 'banana'
False


В Python есть функция, dirкоторая перечисляет методы, доступные для объекта.
>>> stuff = 'Hello world'
>>> type(stuff)
<class 'str'>
>>> dir(stuff)

>>> help(str.capitalize)
Help on method_descriptor:

capitalize(...)
    S.capitalize() -> str

    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.
>>>

Оператор формата
>>> camels = 42
>>> 'I have spotted %d camels.' % camels
'I have spotted 42 camels.'

>>> 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')
'In 3 years I have spotted 0.1 camels.'

Методы строк stripи replace особенно полезны.
'''
print(dir('None'))

fhand = open('lists')
print(fhand)
#Чтение файлов
fhand = open('data')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

'''
Если вы знаете, что файл относительно мал по сравнению с размером вашей основной памяти, вы можете прочитать весь файл в одну строку, используя метод read 
fhand = open('lists')
inp = fhand.read()
'''

# команда exit() завершает программу

'''
Запись файлов
fout = open('output.txt', 'w')
fout.write('line for write')
fout.close()

class PartyAnimal:
   x = 0

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
PartyAnimal.party(an)


class PartyAnimal:
   x = 0

   def __init__(self):
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)




class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, nam):
     self.name = nam
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
j = PartyAnimal('Jim')

s.party()
j.party()
s.party()



from party import PartyAnimal

class CricketFan(PartyAnimal):
   points = 0
   def six(self):
      self.points = self.points + 6
      self.party()
      print(self.name,"points",self.points)

s = PartyAnimal("Sally")
s.party()
j = CricketFan("Jim")
j.party()
j.six()
print(dir(j))
'''
def f():
  mm=0
  def f1():
    global mm
    mm=mm+1
    print('count=',mm)
  return f1

a=f()
a()