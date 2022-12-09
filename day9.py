#!/usr/bin/env python3
import numpy as np

encoding = {
    'L': np.array([-1,0]),
    'R': np.array([1,0]),
    'U': np.array([0,1]),
    'D': np.array([0,-1]),
}

def main():

    f = open("inputs/day9.txt", "r")
    instructions = [(instruction[0], int(instruction[2:])) for instruction in f.read().split("\n")]

    H = np.array([0, 0])
    T = np.array([0, 0])

    visited = set()

    for (direction, steps) in instructions:


        for _ in range(steps):
            H += encoding[direction]

            if H[0] - 1 <= T[0] <= H[0] + 1 and H[1] - 1 <= T[1] <= H[1] + 1:
                pass
            else: 
                difference = H - T
                step_direction = np.array([x if abs(x) < 2 else np.sign(x) for x in difference])
                print(difference, step_direction)
                T += step_direction

            #print(H, T)
            visited.add((T[0], T[1]))

    print(visited) 
    print(len(visited)) 



if __name__ == "__main__":
    main()
