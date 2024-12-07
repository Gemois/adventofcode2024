import argparse

def main(file):
    rules, queue = extractRulesAndQueue(file)

    middlePageSum = 0
    fixedMiddlePageSum = 0

    for update in queue:
        if (inRightOrder(update, rules)):
            middlePageSum += int(findMiddlePage(update))
        else:
            fixedMiddlePageSum += int(findMiddlePage(fixUpdate(update, rules)))

    print("Middle page sum of ordered pages: ", middlePageSum)
    print("Middle page sum of fixed pages: ", fixedMiddlePageSum)


def extractRulesAndQueue(file):
    rules = []
    queue = []

    found_separetor = False

    file = open(file, "r")
    for line in file:
        if not found_separetor:
            if line.strip() == "":
                found_separetor = True
            else:
                rules.append(line.strip())
        else:
            queue.append(line.strip().split(","))

    file.close()
    return createRuleMap(rules), queue


def createRuleMap(lines):
    rule_map = {}
    
    for line in lines:
        left, right = map(int, line.split('|'))

        if left in rule_map:
            rule_map[left].append(right)
        else:
            rule_map[left] = [right]
    
    return rule_map


def inRightOrder(update, rule_map):
    for i in range(len(update) - 1, 0, -1):
        current_page = int(update[i])
        for j in range(i - 1, -1, -1):
            if current_page in rule_map:
                if int(update[j]) in rule_map[current_page]:
                    return False
    return True

def findMiddlePage(update):
    length = len(update)
 
    if length % 2 != 0:
        middle_index = length // 2
        return update[middle_index]
 
    middle_index = length // 2 - 1
    return update[middle_index]


def fixUpdate(update, rule_map):
    for i in range(len(update) - 1, 0, -1):
        current_page = int(update[i])
        for j in range(i - 1, -1, -1):
            if current_page in rule_map:
                if int(update[j]) in rule_map[current_page]:
                    update.insert(i + 1, update[j])
                    update.remove(update[j])

    if (not(inRightOrder(update, rule_map))):
        fixUpdate(update, rule_map)

    return update


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    main(args.file)