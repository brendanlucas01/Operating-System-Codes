def round_robin():
	print("Round Robin Scheduling algorithm\n")
	no_of_processes = int(input("Enter the no of processes "))
	time = 0
	bt = {}
	wt = {}
	tat = {}
	bto = {}
	ttat=0
	twt=0
	gantt=[]
	for a in range(no_of_processes):
		b = input("Enter the burst time of process {} ".format(a))
		b = int(b)
		bto[a] = b
		bt[a]=b
		wt[a]=0
		tat[a]=0
	time_quantam = int(input("Enter the time quantam: "))
	completed = 0
	while completed != no_of_processes:
		for i in range(no_of_processes):
			if bt[i] >time_quantam:
				bt[i] -= time_quantam
				time += time_quantam
				gantt.append("P{}".format(i))
			elif bt[i] > 0:
				time += bt[i]
				bt[i] = 0
				completed+=1
				tat[i] = time
				ttat += time
				wt[i] = time - bto[i]
				twt += wt[i]
				gantt.append("P{}".format(i))
				
	gantt_chart="->".join(gantt)
	print("\nThe Gantt chart is :-\n",gantt_chart)
	for i in range(no_of_processes):
		print("\nFor P{}, TAT:- {} WT:- {}".format(i,tat[i],wt[i]))
	
	print("\n\nAverage Waiting time is {}".format(twt/no_of_processes))
	print("Average Turn Around time is {}".format(ttat/no_of_processes))
	print("Total Waiting time is {}".format(twt))
	print("Total Turn Around time is {}".format(ttat))
	
	
def NPP():
	print("Non-Premptive Priority Scheduling algorithm\n")
	no_of_processes = int(input("Enter the no of processes "))
	time = 0
	bt = {}
	wt = {}
	tat = {}
	priority = {}
	ttat=0
	twt=0
	gantt=[]
	for a in range(no_of_processes):
		b,p = input("Enter the burst time and priority of process {} ".format(a)).split()
		b,p = int(b),int(p)
		priority[a] = p
		bt[a]=b
		wt[a]=0
		tat[a]=0
		
	priority_dict = {k: v for k, v in sorted(priority.items(), key=lambda item: item[1])}
	
	for k,v in priority_dict.items():
		time += bt[k]
		tat[k] = time
		wt[k] = time - bt[k]
		ttat += time
		twt += wt[k]
		gantt.append("P{}".format(k))
	gantt_chart="->".join(gantt)
	print("\nThe Gantt chart is :-\n",gantt_chart)
	for i in range(no_of_processes):
		print("\nFor P{},Priority:-{} TAT:- {} WT:- {}".format(i,priority[i],tat[i],wt[i]))
	
	print("\n\nAverage Waiting time is {}".format(twt/no_of_processes))
	print("Average Turn Around time is {}".format(ttat/no_of_processes))
	print("Total Waiting time is {}".format(twt))
	print("Total Turn Around time is {}".format(ttat))
	#print(priority_dict)
		
		
if __name__ == '__main__':
	round_robin()
	NPP()