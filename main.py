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

def print_args(*args):
  print(args)

a=(1,2,3)
print_args(a)
print_args(*a)
