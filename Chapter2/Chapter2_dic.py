#  사전은 키와 값으로 쌍으로 이루어져 있습니다.

d = dict(a=1,b=2,c=3)
print(d, type(d))

# dict() 생성자 없이도 직접 사전을 생성할 수 있습니다.

colors = {"apple" : "red", "banana":"yellow" }
print(colors)
a = colors["apple"]
print(a)

# 사전에 새로운 값을 추가하는 방법 

colors["cherry"] = "red"
colors["melon"] = "green"
print(colors)

# 사전의 내용을 얻는 방법 - items() , keys(), values()

for c in colors.items():
	print(c)

for k, v in colors.items():
	print(k,v)

for k in colors.keys():
	print(k)

for v in colors.values():
	print(v)

# 사전의 내용의 삭제 - 'del'

del colors['cherry']
print(colors)