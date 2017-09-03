#captalize
print("PYTHON".capitalize())

#count

print("python is powerful".count("p"))
print("python is powerful".count("p",5))
print("python is powerful".count("p",5,-1))

#encode

print("가나다".encode('cp949'))
print("가나다".encode('utf-8'))
print("가나다abc".encode('latin1','ignore'))
print("가나다abc".encode('latin1','replace'))
print("가나다abc".encode('latin1','xmlcharrefreplace'))

#endswith

print("python is powerful".endswith('ful'))
print("python is powerful".endswith('ful',5))
print("python is powerful".endswith('p',0,-1))
print("python is powerful".endswith(('s','l')))

#expandtabs

print("python\tis\tpowerful")
print("python\tis\tpowerful".expandtabs())
print("python\tis\tpowerful".expandtabs(1))

#slice & find
a = "python is powerful"
print(a[5:-1])
print(a.find('p',5,-1))
print(a.find('pa')) #찾지못하면 -1 반환

# index(keyword, [start,[end]])

print(a.index('p'))
print(a.index('p',5,-1))
print(a.index('pa')) # 찾지못하면 에러발생 
