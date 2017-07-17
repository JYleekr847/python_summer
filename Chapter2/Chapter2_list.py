colors = ['red', 'green', 'gold']
print(colors, type(colors))
colors.append('blue')
print(colors)
colors.insert(1,'black')
print(colors)
colors.extend(['white','gray'])
print(colors)
colors += ['red']
print(colors)
colors += 'red'
print(colors)
print(colors.index('red'))
print(colors.index('red',1))

a = colors.count('red')
b = colors.pop() 
c = colors.pop(1)
print(a)
print(b)
print(c)
print(colors)
colors.remove('r')
colors.remove('e')
print(colors)

def mysort(x):
	return x[-1]
colors.sort(key=mysort)
print(colors)
colors.sort(key=mysort,reverse = True)
print(colors)