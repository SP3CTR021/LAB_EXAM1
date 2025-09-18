#Problem 2

def tower_of_hanoi(n, source, target, auxilliary) :

    if (n == 1):
        print (f"move disk 1 from {source} to {target}")
        return
        
tower_of_hanoi(n-1, source, auxilliary,target,)
