import argparse

def main(file):
    lines = []

    XMAS = "XMAS"
    MAS = "MAS"
    
    file = open(file, "r")
    for line in file:
        lines.append(line)
    file.close()

    xmasInstances = countHorisontalInstances(XMAS, lines) + countVerticalInstances(XMAS, lines) + countPrimaryDiagonalInstances(XMAS, lines) + countSecontaryDiagonalInstances(XMAS, lines)
    x_masInstances = findMasInstances(MAS, lines)

    print("XMAS instances: ", xmasInstances)
    print("X-MAS instances: ", x_masInstances)

def countHorisontalInstances(wordToMatch, lines):
    counter = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i]) - 3):
            token = lines[i][j] + lines[i][j + 1] + lines[i][j + 2] + lines[i][j + 3]
            if (token == wordToMatch or token == wordToMatch[::-1]):
                counter += 1

    return counter

def countVerticalInstances(wordToMatch, lines):
    counter = 0
    for i in range(0, len(lines) - 3):
        for j in range(0, len(lines[i]) - 1):
            token = lines[i][j] + lines[i + 1][j] + lines[i + 2][j] + lines[i + 3][j]
            if (token == wordToMatch or token == wordToMatch[::-1]):
                counter += 1

    return counter

def countPrimaryDiagonalInstances(wordToMatch, lines):
    counter = 0
    for i in range(0, len(lines) - 3):
        for j in range(0, len(lines[i]) - 3):
                if (i + 3 < len(lines)) and j + 3 < len(lines[i]) - 1:
                    token = lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2] + lines[i + 3][j + 3]
                    if (token == wordToMatch or token == wordToMatch[::-1]):
                        counter += 1

    return counter

def countSecontaryDiagonalInstances(wordToMatch, lines):
    counter = 0
    for i in range(0, len(lines) - 3):
        for j in range(len(lines[i]) - 1, 2, -1):
            if (i + 3 < len(lines)) and j - 3 >= 0:
                token = lines[i][j] + lines[i + 1][j - 1] + lines[i + 2][j - 2] + lines[i + 3][j - 3]
                if (token == wordToMatch or token == wordToMatch[::-1]):
                    print(i,j,token)
                    counter += 1

    return counter

def findMasInstances(wordToMatch, lines):
    counter = 0
    for i in range(0, len(lines) - 2):
        for j in range(0, len(lines[i]) - 2):
                if (i + 2 < len(lines)) and j + 2 < len(lines[i]) - 1:
                    token = lines[i][j] + lines[i + 1][j + 1] + lines[i + 2][j + 2]
                    if (token == wordToMatch or token == wordToMatch[::-1]):
                        xToken = lines[i][j + 2] + lines[i + 1][j + 1] + lines[i + 2][j]
                        if (xToken == wordToMatch or xToken == wordToMatch[::-1]):
                            counter += 1
                            
    return counter


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    main(args.file)