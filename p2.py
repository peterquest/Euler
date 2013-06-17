first=1
second=2
new=0
eventotal=0
while (new<=4000000):
	if (second%2==0):
		eventotal+=second
	new = first + second
	first = second
	second = new
	print eventotal

