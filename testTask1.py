def Stirling(N,K):
    if N==K:
      return 1
    elif K==0:
      return 0
    else:
      return Stirling(N-1,K-1) + K * Stirling(N-1,K)
#527 9486
nod,nok=[int(i) for i in input().split()]
n=nok//nod
if nok%nod!=0:
  print(0)
else:
  count=set()
  while n>1:
  #print(n)
    for i in range(2,n+1):
      if n%i==0:
        count.add(i)
        n//=i
        break
  n=len(count)
  print(Stirling(n,2)*2+1)

'''
https://www.programiz.com/python-programming/online-compiler/
2
sandwich 7 3
butter 10 g
toasted_bread 2 cnt
sausage 30 g
omelet 9 4
egg 4 cnt
milk 120 ml
salt 1 g
sausage 50 g
7
egg 61 1 tens
milk 58 1 l
sausage 100 480 g
butter 120 180 g
cream 100 350 g
salt 14 1000 g
toasted_bread 40 20 cnt
8
egg 1 cnt 13 12 1 16.4
milk 1 l 3 4.5 4.7 60
chocolate 90 g 6.8 36.3 47.1 546
salt 1 kg 0 0 0 0
strawberry 100 g 0.4 0.1 7 35
sausage 100 g 10 18 1.5 210
toasted_bread 5 cnt 7.3 1.6 52.3 248
butter 100 g 0.8 72.5 1.3 661





1
omelet 9 4
egg 4 cnt
milk 120 ml
salt 1 g
sausage 50 g
7
egg 61 1 tens
milk 58 1 l
sausage 100 480 g
butter 120 180 g
cream 100 350 g
salt 14 1000 g
toasted_bread 40 20 cnt
8
egg 1 cnt 13 12 1 16.4
milk 1 l 3 4.5 4.7 60
chocolate 90 g 6.8 36.3 47.1 546
salt 1 kg 0 0 0 0
strawberry 100 g 0.4 0.1 7 35
sausage 100 g 10 18 1.5 210
toasted_bread 5 cnt 7.3 1.6 52.3 248
butter 100 g 0.8 72.5 1.3 661
'''

units={'kg':('g',1000),'l':('ml',1000),'tens':('cnt',10)}

def translate(count,nameUnit):
  res=count
  if nameUnit in units:
    res=count*units[nameUnit][1]
    return (res,units[nameUnit][0])
  else:
    return (res,nameUnit)

def findCount(countPL,unitPL,count):
    c,u=translate(countPL,unitPL)
    resCount=count//c
    if count%c!=0:
      resCount+=1
    return resCount
    
def findCountProp(countPL,unitPL,count):
    if unitPL in units:
        return count/(countPL*units[unitPL][1])
    else:
        return count/countPL


dish={}
ingredients={}

n=int(input())
dish={}
ingredients={}
for i in range(n):
  name,c,z=input().split()
  dish[name]={'Prop':{'b':0,'g':0,'u':0,'kk':0},'Ingreg':{}}
  for j in range(int(z)):
    ingredient,count,unit=input().split()
    count=int(count)
    count,unit=translate(count,unit)
    dish[name]['Ingreg'][ingredient]=count
    count*=int(c)
    if ingredient in ingredients:
      lastCount=ingredients[ingredient][0]
      ingredients[ingredient]=(lastCount+count,unit)
    else:
      ingredients[ingredient]=(count,unit)
  #print(dish)
#print(ingredients)




k=int(input())
resSum=0
resIngr={}
for i in range(k):
  name,price,count,unit=input().split()
  count=int(count)
  if name in ingredients:
      resCount=findCount(count,unit,ingredients[name][0])
      resIngr[name]=resCount
      resSum+=resCount*int(price)
  else:
      resIngr[name]=0
print(resSum)
for key,val in resIngr.items():
    print(key,val)

m=int(input())
for i in range(m):
  name,count,unit,b,g,u,kk=input().split()
  count=int(count)
  b=float(b)
  g=float(g)
  u=float(u)
  kk=float(kk)
  #print('result:',name,count,unit,b,g,u,kk)
  for k,v in dish.items():
      if name in v['Ingreg']:
          #print(name,'in', k,'value:',v['Ingreg'][name])
          recCount=findCountProp(count,unit,v['Ingreg'][name])
          #print('recCount',recCount)
          v['Prop']['b']+=recCount*b
          v['Prop']['g']+=recCount*g
          v['Prop']['u']+=recCount*u
          v['Prop']['kk']+=recCount*kk
          #print('change ',v['Prop'])
         # print()
for k,v in dish.items():
    print(k,end=' ')
    for i in list(v['Prop'].values()):
        print(i,end=' ')
    print()
          




