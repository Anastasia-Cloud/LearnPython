'''
Даны три множества целых чисел A, B и C. Все числа в каждом множестве различны. Также дано целое число S. Необходимо найти все такие тройки (a, b, c), что a∈A, b∈B, c∈C, a + b + c = S.

Пример входа
1 2 3
1 2 3
1 2 3
6


'''
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
C=set([int(i) for i in input().split()])
S=int(input())
for a in A:
  for b in B:
    c=S-a-b
    if c in C:
      print('a=',a,'b=',b,'c=',c) 