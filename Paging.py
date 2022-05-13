import collections
def fifo():
	print("First In First Out Paging Algorithm\n\n")
	processes = [int(x) for x in input("Enter the Processes for paging:\n").split()]
	table_len = int(input("Enter the size of page table: "))
	table = collections.deque([],table_len)
	hits = 0
	miss = 0
	process_len = len(processes)
	
	prev_table = table.copy()
	frames = {}
	no_frame = 0
	
	print("\nThe Processes are as follows\n")
	for i in range(process_len):
		curr_pros= processes.pop(0)
		try:
			table.index(curr_pros)
			hits +=1
			val_sts = "hit"
		except ValueError:
			miss +=1
			table.append(curr_pros)
			val_sts = "miss"
			try:
				rem_val = list(set(prev_table)-set(table))[0]
				frame_key = list(frames.keys())[list(frames.values()).index(rem_val)]
				frames[frame_key] = curr_pros
			except:
				frames[no_frame] = curr_pros
				no_frame+=1
			prev_table = table.copy()
		print("{}) For process {} table status is {}. ie. {} \n".format(i+1,curr_pros,frames,val_sts))
		
	print("\nNo of Hits are",hits)
	print("\nNo of Misses are",miss)
	print("\nHit Ratio is",hits/process_len)
	print("\nMiss Ratio is",miss/process_len)
	
def lru():
	print("Least Recently Used Paging Algorithm\n\n")
	processes = [int(x) for x in input("Enter the Processes for paging:\n").split()]
	table_len = int(input("Enter the size of page table: "))
	table = collections.deque([],table_len)
	hits = 0
	miss = 0
	val_sts = ""
	process_len = len(processes)
	prev_table = table.copy()
	frames = {}
	no_frame = 0
	print("\nThe Processes are as follows\n")
	for i in range(process_len):
		curr_pros= processes.pop(0)
		try:
			table.index(curr_pros)
			table.remove(curr_pros)
			table.append(curr_pros)
			hits +=1
			val_sts = "hit"
		except ValueError:
			miss +=1
			table.append(curr_pros)
			val_sts = "miss"
			try:
				rem_val = list(set(prev_table)-set(table))[0]
				frame_key = list(frames.keys())[list(frames.values()).index(rem_val)]
				frames[frame_key] = curr_pros
			except:
				frames[no_frame] = curr_pros
				no_frame+=1
			prev_table = table.copy()
		#print("{}) For process {} table status is {}. ie. {} \n".format(i+1,curr_pros,table,val_sts))
		print("{}) For process {} table status is {}. ie. {} \n".format(i+1,curr_pros,frames,val_sts))
		
	print("\nNo of Hits are",hits)
	print("\nNo of Misses are",miss)
	print("\nHit Ratio is",hits/process_len)
	print("\nMiss Ratio is",miss/process_len)
	
	
def optimal():
	print("Optiml Future Paging Algorithm\n\n")
	processes = [int(x) for x in input("Enter the Processes for paging:\n").split()]
	table_len = int(input("Enter the size of page table: "))
	table = collections.deque([],table_len)
	hits = 0
	miss = 0
	val_sts = ""
	block_key = False
	next_use=[]
	process_len = len(processes)
	prev_table = table.copy()
	frames = {}
	no_frame = 0
	print("\nThe Processes are as follows\n")
	for i in range(process_len):
		#curr_pros= processes[0]
		curr_pros=processes.pop(0)
		try:
			table.index(curr_pros)
			#table.remove(curr_pros)
			#table.append(curr_pros)
			hits +=1
			val_sts = "hit"
		except ValueError:
			miss +=1
			next_use.clear()
			for num in table:
				try:
					next_occ = processes.index(num)
					next_use.append(next_occ)
					block_key = True
				except:
					block_key = False
					if len(table)==table_len:
						table.remove(num)
					break
			if block_key:
				last = max(next_use)
				last_index = next_use.index(last)
				#print(table,last_index,last,next_use)
				last_ele = table[last_index]
				if len(table)==table_len:
					table.remove(last_ele)
				#next_use.clear()
				block_key = False
				
			table.append(curr_pros)
			val_sts = "miss"
			try:
				rem_val = list(set(prev_table)-set(table))[0]
				frame_key = list(frames.keys())[list(frames.values()).index(rem_val)]
				frames[frame_key] = curr_pros
			except:
				frames[no_frame] = curr_pros
				no_frame+=1
			prev_table = table.copy()
		#processes.pop(0)
		#print("{}) For process {} table status is {}. ie. {} \n".format(i+1,curr_pros,table,val_sts))
		print("{}) For process {} table status is {}. ie. {} \n".format(i+1,curr_pros,frames,val_sts))
		
	print("\nNo of Hits are",hits)
	print("\nNo of Misses are",miss)
	print("\nHit Ratio is",hits/process_len)
	print("\nMiss Ratio is",miss/process_len)
	
if __name__=="__main__":
	print("Enter the Proccesses required(in order)\n")
	print("1 for FIFO Algorithm")
	print("2 for LRU Algorithm")
	print("3 for Optimal Algorithm")
	opts = [int(x) for x in input().split()]
	for i in opts:
		if i==1:
			fifo()
		if i==2:
			lru()
		if i==3:
			optimal()