# Kenneth Tran

def left_to_right(n, disks):
    counter = 0  # Counter for amount of swaps done

    while True:
        swapped = False  

        for i in range(2*n - 1):
            if disks[i] == "D" and disks[i+1] == "L":
                # Swap disks if current is dark and next is light
                disks[i], disks[i+1] = disks[i+1], disks[i]
                counter += 1  # Increment the counter
                swapped = True
        
        # If no swaps were made, list is sorted, break out of while loop
        if not swapped:
            break

    return disks, counter

def lawnmower(n, disks):
    counter = 0  # Swap counter
    
    while True:
        swapped = False  

        for i in range(2*n - 1):
            if disks[i] == "D" and disks[i+1] == "L":
                # Swap dark and light disks
                disks[i], disks[i+1] = disks[i+1], disks[i]
                counter += 1  # Increment the counter
                swapped = True
        

        for i in range(2*n - 2, -1, -1):    # This time start from the right
            if disks[i] == "D" and disks[i+1] == "L":
                # Swap disks
                disks[i], disks[i+1] = disks[i+1], disks[i]
                counter += 1  # Increment
                swapped = True
        
        # If no swaps were made, sorted
        if not swapped:
            break

    return disks, counter #return disks and amount of times swapped


if __name__ == '__main__':
    #change these for left to right algorithm
    diskList = ['L', 'D', 'L', 'D', 'L', 'D', 'L', 'D']
    n = 4
    print(left_to_right(n, diskList))

    #change these for lawnmower algorithm
    diskList = ['L', 'D', 'L', 'D', 'L', 'D', 'L', 'D']
    n = 4
    print(lawnmower(n, diskList))