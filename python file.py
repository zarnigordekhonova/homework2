'''
m = ['banan','anjir', 'anor', 'banan', 'xurmo', 'banan']
d = m.count('banan')
print(d, 'marta')
'''

list = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
d = max(set(list), key = list.count)
m = list.count(d)
print(d, '--->', m, 'marta')
