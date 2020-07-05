# Operasi komparasi
#setiap hasil dari operasi komparasi adalah boolean
a = 4
b = 2
#lebih besar dari (>)
hasil = a > b
print(a," > ",b, " = ",hasil)

#lebih kecil dari (<)
hasil = a < b
print(a," < ",b, " = ",hasil)

#lebih besar samadengan (>=)
hasil = a >=b
print(a," >= ",b, " = ",hasil)

#lebih kecil samadengan (<=)
hasil = a <=b
print(a," <= ",b, " = ",hasil)

# samadengan (==)
hasil = a == b
print(a," == ",b, " = ",hasil)

#tidak samadengan (!=)
hasil = a !=b
print(a," != ",b, " = ",hasil)

# 'is' sebaai komparasi object
x = 5
y = 5

print('nilai x =',x,'id = ',hex(id(x)))
print('nilai y =',y,'id = ',hex(id(y)))

hasil = x is y
print('x is y =',hasil)