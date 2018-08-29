def CompleteSequence(list):
	min_required_steps=1
	for index in range(len(list),0,-1):
		if index==len(list):
			continue
		if list[index-1]>=min_required_steps:
			min_required_steps=1
		else:
			min_required_steps+=1
	return min_required_steps==1
	

def printevenodd():
	for i in range(10,0,-1):
		if i%2==1:
			print 'odd'
		else:
			print 'even'
"""printevenodd()
"""
print CompleteSequence([11,1,0,0,1,1,0,0,0,0])