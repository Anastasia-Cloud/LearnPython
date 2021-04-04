
for color in 'red','green','white','blue':
  print('this color is ',color)

for color in 'red',12,'white',34,67:
  print('this color is ',color)

for n in 0,1,2,3,4,5:
  print('n=',n,'n*n= ',n**2)
  print('конец итерации' )
print('конец цикла')

for n in range(6):
  print('n=',n,'n*n= ',n**2)
  print('конец итерации' )
print('конец цикла')

for n in range(2,6):
  print('n=',n,'n*n= ',n**2)
  print('конец итерации' )
print('конец цикла')

'''
Например, для того, чтобы просуммировать значения чисел от 1 до n можно воспользоваться следующей программой:
n=8
1+2+3+4+5+6+7+8=?
'''
n=int(input())
sum=0;
for i in range(1,n+1):
  sum=sum+i;
print(sum)

for i in range(100,0,-1):
  print('n=',i)
print('конец цикла')

'''
Например, сделать цикл по всем нечетным числам от 1 до 99
'''
for i in range(1,100,+2):
  print(i)
