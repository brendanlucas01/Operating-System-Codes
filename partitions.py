def first_fit():
	print("First Fit Algorithm\n\n")
	holes_no = int(input("Enter the Number of holes "))
	holes = {}
	for i in range(holes_no):
		holes[i] = int(input("Enter the size of hole {} ".format(i)))
	pros_no = int(input("\nEnter the Number of processes"))
	process = {}
	dir = {}
	remain=[]
	for i in range(pros_no):
		process[i] = int(input("Enter the size of Process P{} ".format(i)))
	
	for i in range(pros_no):
		for j in range(holes_no):
			if holes[j]-process[i]>=0:
				holes[j] = holes[j]-process[i]
				try:
					dir[j] = dir[j]+", P{}".format(i)
				except:
					dir[j] = "P{}".format(i)
				break
			if j==holes_no-1:
				remain.append("P{}".format(i))
	#print(process)
	print("\n\nResults")
	for j in range(holes_no):
		try:
			print("Hole {} contains process {}. Empty space {}".format(j,dir[j],holes[j]))
		except:
			print("Hole {} contains no process. Empty space {}".format(j,holes[j]))
			
	print("\nRemaining processes:- ",remain)
	#print(dir)
	
	
def best_fit():
	print("Best Fit Algorithm\n\n")
	holes_no = int(input("Enter the Number of holes "))
	holes = {}
	for i in range(holes_no):
		holes[i] = int(input("Enter the size of hole {} ".format(i)))
	pros_no = int(input("\nEnter the Number of processes "))
	process = {}
	dir = {}
	min_size=2000000000000
	min_index=-1
	remain=[]
	for i in range(pros_no):
		process[i] = int(input("Enter the size of Process P{} ".format(i)))
	
	for i in range(pros_no):
		min_size=2000000000000
		min_index=-1
		for j in range(holes_no):
			if holes[j]-process[i]>=0:
				if holes[j]-process[i]<min_size:
					min_size = holes[j]-process[i]
					min_index = j
					
		if min_index!=-1:			
			#holes[min_index] = holes[min_index]-process[i]
			holes[min_index] = min_size
			try:
				dir[min_index] = dir[min_index]+", P{}".format(i)
			except:
				dir[min_index] = "P{}".format(i)
		else:
			remain.append("P{}".format(i))
	#print(process)
	print("\n\nResults")
	for j in range(holes_no):
		try:
			print("Hole {} contains process {}. Empty space {}".format(j,dir[j],holes[j]))
		except:
			print("Hole {} contains no process. Empty space {}".format(j,holes[j]))
			
	print("\nRemaining processes:- ",remain)
	#print(dir)
	
def worst_fit():
	print("Worst Fit Algorithm\n\n")
	holes_no = int(input("Enter the Number of holes "))
	holes = {}
	for i in range(holes_no):
		holes[i] = int(input("Enter the size of hole {} ".format(i)))
	pros_no = int(input("\nEnter the Number of processes "))
	process = {}
	dir = {}
	max_size=-1
	max_index=-1
	remain=[]
	for i in range(pros_no):
		process[i] = int(input("Enter the size of Process P{} ".format(i)))
	
	for i in range(pros_no):
		max_size=-1
		max_index=-1
		for j in range(holes_no):
			if holes[j]-process[i]>=0:
				if holes[j]-process[i]>max_size:
					max_size = holes[j]-process[i]
					max_index = j
					
		if max_index!=-1:			
			#holes[min_index] = holes[min_index]-process[i]
			holes[max_index] = max_size
			try:
				dir[max_index] = dir[max_index]+", P{}".format(i)
			except:
				dir[max_index] = "P{}".format(i)
		else:
			remain.append("P{}".format(i))
	#print(process)
	print("\n\nResults")
	for j in range(holes_no):
		try:
			print("Hole {} contains process {}. Empty space {}".format(j,dir[j],holes[j]))
		except:
			print("Hole {} contains no process. Empty space {}".format(j,holes[j]))
			
	print("\nRemaining processes:- ",remain)
	#print(dir)
	
if __name__=="__main__":
	first_fit()
	best_fit()
	worst_fit()