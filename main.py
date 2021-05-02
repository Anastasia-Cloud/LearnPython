'''
Значение параметров по умолчанию высчитывается, когда функция определяется, а не выполняется.
'''

'''
a=[1,2,3]

def f(x,y=a):
  y.append(x)
  return y

a.append(999)
print(f(5))
print(f(6))
'''


'''
def f(x,y=[]):
  y.append(x)
  return y

print(f(5))
print(f(6))
'''

'''
def print_args(*args):
  print(args)

a=(1,2,3)
print_args(a)
print_args(*a)
'''

'''
def print_args(**args):
  print(args)
d={'a':123, 'b':456}
print_args(**d)

'''

def f(*,a=1,b=2):
  print(a,b)
#f(a=4)

d1={'a':1, 'b':2}
d2={'a':3, 'd':4}
#print({**d1,**d2})

def func():
  '''
  do anything...
  '''
  return 0

help(func)