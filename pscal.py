a1 = {0: {0: 0, 1: 0}, 1: {0:0,1:1,2:0}}
def return_dict(a_list):
	c = {}
	b = ''
	for i in range(1, len(a_list)):
		b = ' '.join([str(x) for x in a_list[i].values() if x!=0])
		c[i] = b
		b =''
	return c

def print1(x):
	#x is a dict
	#like {1: '1', 2: '1 1', 3: '1 2 1'}
	l1 = len(x[len(x)])
	bef = '{:^'
	aft = '}'
	for i in x:
		print((bef + str(l1) + aft).format(x[i]))
def func(n):
	#b = {}
	if n ==0:
		return a1[0]
	elif n==1:
		return a1[1]
	else:
		if n not in a1:
			for i in range(len(func(n-1))):
				if i==0:
					a1[n] = {}
					a1[n][0]=0
				else:
					a1[n][i] = func(n-1)[i-1] + func(n-1)[i]
	a1[n][len(a1[n])] = 0
	return a1[n]
if __name__ == '__main__':
    x = input('input: ')
    func(int(x))
    print1(return_dict(a1))
