def sumoflist(n):
	a=[]
	for x in range(1,n):
		a.append(x)
		b=sum(a)
	return b


def functionname(lists,i,s):
	m=[]
	n=[]
	for x in lists:
		if x%i==0 and x%s==0:
			m.append(x)
			n.append(x)
		elif x%s==0:
			n.append(x)
		elif x%i==0:
			m.append(x)
	print(m)
	print(n)


def createdict(i):
	g=dict()
	for x in i:
		g[x] = x**3
	print(g)

h = range(0,10)
f= dict()
for x in h:
	f[x]= x**3
print(f)
		

