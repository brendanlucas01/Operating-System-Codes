import math as m
def FCFS():
	print("\nFirst Come First Serve Disk Scheduling\n\n")
	prev=int(input("Enter the starting disk location: "))
	processes = [int(x) for x in input("Enter the Cylinder Calls Index:\n").split()]
	pros_len = len(processes)
	dist_travel = []
	expand_exp=[]
	for i in range(pros_len):
		curr = processes.pop(0)
		dist_travel.append(abs(curr-prev))
		print(f"{i+1}) {prev}=>{curr} ")
		expand_exp.append(f"({curr}-{prev})")
		prev=curr
	total_dist=sum(dist_travel)
	s = [str(i) for i in dist_travel]
	ex="+".join(expand_exp)
	exp_dist="+".join(s)
	print("Total distance travelled is=\n{}\n=> {}={}".format(ex,exp_dist,total_dist))
	print("Average seek time is {}\n".format(total_dist/pros_len))
	
def SSTF():
	print("\nShortest Seek Time First Disk Scheduling\n\n")
	prev=int(input("Enter the starting disk location: "))
	#processes = {int(x):abs(int(x)-prev) for x in input("Enter the Processes for paging:\n").split()}
	processes = [int(x) for x in input("Enter the Cylinder Call Index:\n").split()]
	dist_travel = []
	expand_exp=[]
	processes.append(prev)
	processes.sort()
	#print(processes)
	pros_len = len(processes)
	#print(pros_len)
	for i in range(pros_len-1):
		prev_loc = processes.index(prev)
		#print(prev,prev_loc,processes)
		if processes[prev_loc-1] and processes[prev_loc+1]:
			if processes[prev_loc-1]<processes[prev_loc+1]:
				curr = processes[prev_loc-1]
			else:
				curr = processes[prev_loc+1]
		elif processes[prev_loc-1]:
			curr=processes[prev_loc-1]
		elif processes[prev_loc+1]:
			curr=processes[prev_loc+1]
		dist_travel.append(abs(curr-prev))
		print(f"{i+1}) {prev}=>{curr} ")
		expand_exp.append(f"({curr}-{prev})")
		processes.pop(prev_loc)
		prev=curr
	total_dist=sum(dist_travel)
	s = [str(i) for i in dist_travel]
	ex="+".join(expand_exp)
	exp_dist="+".join(s)
	print("Total distance travelled is=\n{}\n=> {}={}".format(ex,exp_dist,total_dist))
	print("Average seek time is {}\n".format(total_dist/pros_len))
		
	#min_dist = {k: v for k, v in sorted(processes.items(), key=lambda item: item[1])}
	
def look():
	print("\nLOOK Disk Scheduling\n\n")
	prev=int(input("Enter the starting disk location: "))
	#processes = {int(x):abs(int(x)-prev) for x in input("Enter the Processes for paging:\n").split()}
	processes = [int(x) for x in input("Enter the Cylinder Call Index:\n").split()]
	start,end = input("Enter the start and end index of the cylinder disk: ").split()
	start,end = int(start),int(end)
	dir = int(input("Enter the direction of the head.\n0 for high to low\n1 for low to high\n"))
	dist_travel = []
	expand_exp=[]
	processes.append(prev)
	processes.append(start)
	processes.append(end)
	processes = list(set(processes))
	processes.sort()
	#print(processes)
	prev_loc = processes.index(prev)
	if dir==1:
		fir_sec = processes[prev_loc:]
		sed_sec = processes[:prev_loc]
		sed_sec.reverse()
	else:
		sed_sec = processes[prev_loc+1:]
		fir_sec = processes[:prev_loc+1]
		fir_sec.reverse()
	#print(fir_sec)
	#print(sed_sec)
	new_sche=[]
	new_sche.extend(fir_sec)
	new_sche.extend(sed_sec)
	#print(new_sche)
	prev = new_sche.pop(0)
	pros_len = len(new_sche)
	for i in range(pros_len):
		curr = new_sche.pop(0)
		dist_travel.append(abs(curr-prev))
		print(f"{i+1}) {prev}=>{curr} ")
		expand_exp.append(f"({curr}-{prev})")
		prev=curr
	total_dist=sum(dist_travel)
	s = [str(i) for i in dist_travel]
	ex="+".join(expand_exp)
	exp_dist="+".join(s)
	print("Total distance travelled is=\n{}\n=> {}={}".format(ex,exp_dist,total_dist))
	print("Average seek time is {}\n".format(total_dist/pros_len))
	

def clook():
	print("\nC-LOOK Disk Scheduling\n\n")
	prev=int(input("Enter the starting disk location: "))
	#processes = {int(x):abs(int(x)-prev) for x in input("Enter the Processes for paging:\n").split()}
	processes = [int(x) for x in input("Enter the Cylinder Call Index:\n").split()]
	start,end = input("Enter the start and end index of the cylinder disk: ").split()
	start,end = int(start),int(end)
	dir = int(input("Enter the direction of the head.\n0 for high to low\n1 for low to high\n"))
	dist_travel = []
	expand_exp=[]
	processes.append(prev)
	processes.append(start)
	processes.append(end)
	processes = list(set(processes))
	processes.sort()
	#print(processes)
	prev_loc = processes.index(prev)
	if dir==1:
		fir_sec = processes[prev_loc:]
		sed_sec = processes[:prev_loc]
		#sed_sec.reverse()
	else:
		sed_sec = processes[prev_loc+1:]
		fir_sec = processes[:prev_loc+1]
		#fir_sec.reverse()
	#print(fir_sec)
	#print(sed_sec)
	new_sche=[]
	new_sche.extend(fir_sec)
	new_sche.extend(sed_sec)
	#print(new_sche)
	prev = new_sche.pop(0)
	pros_len = len(new_sche)
	for i in range(pros_len):
		curr = new_sche.pop(0)
		dist_travel.append(abs(curr-prev))
		print(f"{i+1}) {prev}=>{curr} ")
		expand_exp.append(f"({curr}-{prev})")
		prev=curr
	total_dist=sum(dist_travel)
	s = [str(i) for i in dist_travel]
	ex="+".join(expand_exp)
	exp_dist="+".join(s)
	print("Total distance travelled is=\n{}\n=> {}={}".format(ex,exp_dist,total_dist))
	print("Average seek time is {}\n".format(total_dist/pros_len))
	
def scan():
	print("\nSCAN Disk Scheduling\n\n")
	prev=int(input("Enter the starting disk location: "))
	#processes = {int(x):abs(int(x)-prev) for x in input("Enter the Processes for paging:\n").split()}
	processes = [int(x) for x in input("Enter the Cylinder Call Index:\n").split()]
	#start,end = input("Enter the start and end index of the cylinder disk: ").split()
	#start,end = int(start),int(end)
	dir = int(input("Enter the direction of the head.\n0 for high to low\n1 for low to high\n"))
	dist_travel = []
	expand_exp=[]
	processes.append(prev)
	#processes.append(start)
	#processes.append(end)
	#processes = list(set(processes))
	processes.sort()
	#print(processes)
	prev_loc = processes.index(prev)
	if dir==1:
		fir_sec = processes[prev_loc:]
		sed_sec = processes[:prev_loc]
		sed_sec.reverse()
	else:
		sed_sec = processes[prev_loc+1:]
		fir_sec = processes[:prev_loc+1]
		fir_sec.reverse()
	#print(fir_sec)
	#print(sed_sec)
	new_sche=[]
	new_sche.extend(fir_sec)
	new_sche.extend(sed_sec)
	#print(new_sche)
	prev = new_sche.pop(0)
	pros_len = len(new_sche)
	for i in range(pros_len):
		curr = new_sche.pop(0)
		dist_travel.append(abs(curr-prev))
		print(f"{i+1}) {prev}=>{curr} ")
		expand_exp.append(f"({curr}-{prev})")
		prev=curr
	total_dist=sum(dist_travel)
	s = [str(i) for i in dist_travel]
	ex="+".join(expand_exp)
	exp_dist="+".join(s)
	print("Total distance travelled is=\n{}\n=> {}={}".format(ex,exp_dist,total_dist))
	print("Average seek time is {}\n".format(total_dist/pros_len))
	
def cscan():
	print("\nC-SCAN Disk Scheduling\n\n")
	prev=int(input("Enter the starting disk location: "))
	#processes = {int(x):abs(int(x)-prev) for x in input("Enter the Processes for paging:\n").split()}
	processes = [int(x) for x in input("Enter the Cylinder Call Index:\n").split()]
	#start,end = input("Enter the start and end index of the cylinder disk: ").split()
	#start,end = int(start),int(end)
	dir = int(input("Enter the direction of the head.\n0 for high to low\n1 for low to high\n"))
	dist_travel = []
	expand_exp=[]
	processes.append(prev)
	#processes.append(start)
	#processes.append(end)
	#processes = list(set(processes))
	processes.sort()
	#print(processes)
	prev_loc = processes.index(prev)
	if dir==1:
		fir_sec = processes[prev_loc:]
		sed_sec = processes[:prev_loc]
		#sed_sec.reverse()
	else:
		sed_sec = processes[prev_loc+1:]
		fir_sec = processes[:prev_loc+1]
		#fir_sec.reverse()
	#print(fir_sec)
	#print(sed_sec)
	new_sche=[]
	new_sche.extend(fir_sec)
	new_sche.extend(sed_sec)
	#print(new_sche)
	prev = new_sche.pop(0)
	pros_len = len(new_sche)
	for i in range(pros_len):
		curr = new_sche.pop(0)
		dist_travel.append(abs(curr-prev))
		print(f"{i+1}) {prev}=>{curr} ")
		expand_exp.append(f"({curr}-{prev})")
		prev=curr
	total_dist=sum(dist_travel)
	s = [str(i) for i in dist_travel]
	ex="+".join(expand_exp)
	exp_dist="+".join(s)
	print("Total distance travelled is=\n{}\n=> {}={}".format(ex,exp_dist,total_dist))
	print("Average seek time is {}\n".format(total_dist/pros_len))

if __name__=="__main__":
	print("Enter the Algorithm required(in order)\n")
	print("1 for FCFS Algorithm")
	print("2 for SSTF Algorithm")
	print("3 for Look Algorithm")
	print("4 for C-Look Algorithm")
	print("5 for Scan Algorithm")
	print("6 for C-Scan Algorithm")
	opts = [int(x) for x in input().split()]
	for i in opts:
		if i==1:
			FCFS()
		if i==2:
			SSTF()
		if i==3:
			look()
		if i==4:
			clook()
		if i==5:
			scan()
		if i==6:
			cscan()