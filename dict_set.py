a = {'mike':77,'mary':66,'jerry':55}
print(a['mike'])
print(a['mike']+a['mary'])
print('mike' in a)
b=a.get('jack',88)
a['jack'] = 99
print(a,a.get('jack'))


s = set([1,2,3])
print(s)
s.add(6)
print(s)
s.remove(1)
print(s)
s.add(1)
print(s)

s1 = set([1,4,5,8])
s2 = set([2,4,5,9])
print(s1 & s2,s1 | s2)