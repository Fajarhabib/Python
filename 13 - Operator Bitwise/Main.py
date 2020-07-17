#bitwise = operasi masing masing bit

a= 9
b = 5

#bitwise or {|}

c = a | b
print("===============OR============")
print('nilai : ',a,' binary : ', format(a,'08b'))
print('nilai : ',b,' binary : ', format(b,'08b'))
print('------------------------------(|)')
print('nilai : ',c,' binary : ', format(c,'08b'))
print('\n')
#bitwise and {&}

c = a & b
print("==============AND============")
print('nilai : ',a,' binary : ', format(a,'08b'))
print('nilai : ',b,' binary : ', format(b,'08b'))
print('------------------------------(&)')
print('nilai : ',c,' binary : ', format(c,'08b'))
print('\n')
#bitwise XOR {^}

c = a ^ b
print("==============XOR============")
print('nilai : ',a,' binary : ', format(a,'08b'))
print('nilai : ',b,' binary : ', format(b,'08b'))
print('------------------------------(^)')
print('nilai : ',c,' binary : ', format(c,'08b'))