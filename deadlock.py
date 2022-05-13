def main():
    processes = int(input("Enter the number of processes : "))
    resources = int(input("Enter the number of resources : "))
    available = [int(i) for i in input("Available System resources : ").split()]

    print("\nEach process Allocation : ")
    currently_allocated = [[int(i) for i in input(f"process {j} : ").split()] for j in range(processes)]

    print("\nEach process Request : ")
    req_mat = [[int(i) for i in input(f"process {j} : ").split()] for j in range(processes)]
    print(f"total available resources : {available}\n")
    safe_seq=[]
    running = [True] * processes
    finish_vec = [False]*processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if req_mat[i][j] > available[j]:
                        executing = False
                        break
                if executing:
#                     print(f"process {i} is executing")
                    running[i] = False
                    finish_vec[i] = True
                    safe_seq.append(f"P{i}")
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("Deadlock Detected")
            break

        print(f"No Deadlock Detected.\nFinish Vector : {finish_vec}")
        print("The Safe Sequence is ",safe_seq,"\n")


if __name__ == '__main__':
    main()