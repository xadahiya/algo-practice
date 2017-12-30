## Solving tower of hanoi using recursion

## There are 3 poles A,B,C and we need to move n disks from A to C
def solve_tower(height, from_pole, with_pole, to_pole):
    if height >= 1:
        solve_tower(height -1, from_pole, to_pole, with_pole)
        move_disk(from_pole, to_pole)
        solve_tower(height -1, with_pole, from_pole, to_pole)


def move_disk(from_pole, to_pole):
    print("Moving disk from %s to %s"%(from_pole, to_pole))


solve_tower(10, "A", "B", "C")
