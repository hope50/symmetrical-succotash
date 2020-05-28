print('enter first & end number for multiplication')

first=int(input( 'first number'))
last=int(input('  end number'))

for x in range(first,last+1):
         for y in range (1,12):
              print(x,'*',y,'=', x*y)