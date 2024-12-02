import argparse

def main(file):
    total_distance = 0
    similarity_score = 0

    left_list, right_list = parseInputFile(file)

    left_list.sort()
    right_list.sort()

    for i in range(0, len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
        similarity_score +=  left_list[i] * right_list.count(left_list[i])

    print("Total Distance: ", total_distance)
    print("Similarity score: ", similarity_score)

def parseInputFile(file):
    left_list = []
    right_list = []

    file = open(file, "r")

    for line in file:
        line_parts = line.split("   ")
        left_list.append(int(line_parts[0]))
        right_list.append(int(line_parts[1].replace("\n", "")))

    file.close()

    return left_list, right_list

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    main(args.file)