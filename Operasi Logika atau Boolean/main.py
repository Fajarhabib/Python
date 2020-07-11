# NOT
print('==== NOT====')
a = True
c = not a
print('data a = ',a)
print('--------NOT')
print('data c = ',c)
print('\n')

#OR (jika salah satu true, maka dia akan true)
print('==== OR====')
a = True
b = True
c = a or b
print(a,' OR ',b,' = ',c)
a = True
b = False
c = a or b
print(a,' OR ',b,' = ',c)
a = False
b = True
c = a or b
print(a,' OR ',b,' = ',c)
a = False
b = False
c = a or b
print(a,' OR ',b,' = ',c)
print('\n')

#AND (jika salah satu false, maka dia akan false)
print('==== AND====')
a = True
b = True
c = a and b
print(a,' AND ',b,' = ',c)
a = True
b = False
c = a and b
print(a,' AND ',b,' = ',c)
a = False
b = True
c = a and b
print(a,' AND ',b,' = ',c)
a = False
b = False
c = a and b
print(a,' AND ',b,' = ',c)

print('\n')

#XOR (akan true jika salah satu true, sisanya false)
print('==== XOR====')
a = True
b = True
c = a ^ b
print(a,' XOR ',b,' = ',c)
a = True
b = False
c = a ^ b
print(a,' XOR ',b,' = ',c)
a = False
b = True
c = a ^ b
print(a,' XOR ',b,' = ',c)
a = False
b = False
c = a ^ b
print(a,' XOR ',b,' = ',c)