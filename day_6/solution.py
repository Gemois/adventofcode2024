import argparse

def main(file):
    map = []

    file = open(file, "r")
    for line in file:
        map.append(line)
    file.close()

    direction = 0  # 0: up, 1: right, 2: down, 3: left
    
    print("Distinct Positions: ", predict_guard_path(findGuard(map), direction, map))

def predict_guard_path(guard_position, direction, map):
    distinct_positions = []
    while True:
        if (not(guard_position in distinct_positions)):
            distinct_positions.append(guard_position)

        next_position = calcMovePosition(direction, guard_position)

        if not withinbounds(map, next_position):
            return len(distinct_positions)

        if map[next_position[0]][next_position[1]] != '#':
            guard_position = next_position
        else:
            direction = (direction + 1) % 4
            continue

def changeAxis(current):
    return -current

def calcMovePosition(direction, indices):
    i, j = indices
    if direction == 0:
        return (i - 1, j)
    elif direction == 1:
        return (i, j + 1)
    elif direction == 2:
        return (i + 1, j)
    elif direction == 3:
        return (i, j - 1)

def withinbounds(map, indices):
    i, j = indices
    return 0 <= i < len(map) and 0 <= j < len(map[i])

def findGuard(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                return (i, j)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    main(args.file)
