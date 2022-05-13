def main():
    processes = int(input("Enter the number of processes : "))
    resources = int(input("Enter the number of resources : "))
    available = [int(i) for i in input("Available System resources : ").split()]

    print("\nEach process Allocation : ")
    currently_allocated = [[int(i) for i in input(f"process {j} : ").split()] for j in range(processes)]

    print("\nEach process Maximum : ")
    max_need = [[int(i) for i in input(f"process {j} : ").split()] for j in range(processes)]
    print(f"total available resources : {available}\n")
    safe_seq=[]
    running = [True] * processes
    count = processes
    while count != 0:
        safe = False
        for i in range(processes):
            if running[i]:
                executing = True
                for j in range(resources):
                    if max_need[i][j] - currently_allocated[i][j] > available[j]:
                        executing = False
                        break
                if executing:
                    print(f"process {i} is executing")
                    running[i] = False
                    safe_seq.append(f"P{i}")
                    count -= 1
                    safe = True
                    for j in range(resources):
                        available[j] += currently_allocated[i][j]
                    break
        if not safe:
            print("the processes are in an unsafe state.")
            break

        print(f"The process is in a safe state.\navailable resources : {available}")
        print("The Safe Sequence is ",safe_seq,"\n")


if __name__ == '__main__':
    main()