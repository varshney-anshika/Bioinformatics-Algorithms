
#Towers of Hanoi Problem:
#Solve the Towers of Hanoi puzzle.
#Input: An integer n.
#Output: A sequence of moves that will solve the Towers of Hanoi puzzle with n disks. 

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("Move disk 1 from source", source, "to target", target)
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print("Move disk", n, "from source", source, "to target", target)
    tower_of_hanoi(n - 1, auxiliary, source, target)

n = int(input("Enter number of disks: "))
tower_of_hanoi(n, "A", "B", "C")

# The function tower_of_hanoi takes four parameters: n, source, auxiliary, and target. It uses the recursive approach to solve the puzzle by dividing the problem into smaller subproblems. The base case is when there is only one disk, in which case it simply prints the steps to move the disk from the source to the target. For larger problems, the function first calls itself to move the top n - 1 disks from the source to the auxiliary tower, then prints the step to move the nth disk from the source to the target, and finally calls itself again to move the n - 1 disks from the auxiliary to the target.
