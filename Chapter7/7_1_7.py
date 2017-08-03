FilePath = './test.txt'

try:
	f = open(FilePath, 'r')
	try:
		data = f.read(128)
		print(data)
	finally:
		f.close()
except:
	print("fail to open {0} file".format(FilePath))