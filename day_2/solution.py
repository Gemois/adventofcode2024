import argparse

def main(file):

    safe_reports = 0
    tolerated_safe_reports = 0

    file = open(file, "r")
    for line in file:
        report = list(map(int, line.replace("\n", "").split(" ")))
        if (isSafe(report)):
            safe_reports += 1
        else:
            for i in range(0, len(report)):
                copy = report.copy()
                copy.pop(i)
                if (isSafe(copy)):
                    tolerated_safe_reports += 1
                    break


    file.close()

    print("Safe level count: ", safe_reports)
    print("Problem Dampener  safe level count: ", safe_reports + tolerated_safe_reports)


def isSafe(report):
    return isSorted(report) and hasAcceptableDistance(report)


def isSorted(report):
    return report == sorted(report) or report == sorted(report, reverse=True)


def hasAcceptableDistance(report):
    for i in range(0, len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        if (diff < 1 or diff > 3):
            return False
    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    main(args.file)