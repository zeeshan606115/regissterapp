def string_value(str):
	s1 = str.split()
	s = len(s1)
	l = []
	i = 0
	for j in range(1, s):
		if(i == j):
			l = s1.insert(i+1, '*')
	print(l)

string_value('abcaabaa')
