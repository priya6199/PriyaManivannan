O,P=map(int,input().split())
for l in range(O,P+1):
	if(l==1):
		l+=1
	elif(l%2!=0):
		print(l,end=" ")
