b = []

def Rec(x):
	if x > 0:
		if x % 2 == 0:
			b.append(x)
		Rec(x - 1)

Rec(10)
print(sum(b))





