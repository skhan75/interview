# Given a sequence of words, and a limit on the number of characters that can be put in one line (line width).
# Put line breaks in the given sequence such that the lines are printed neatly.

import sys
def textify(words, width):

    cost = createCostMatrix(words, width)
    minCost, result = findMinCost(cost, words, width)
    print('Minimum cost is: ', minCost[0], '\n')

    lines = printJustifiedText(words, result)
    for i in lines:
        if(i == '\n'):
            print (i, end="")
        else:
            print(i, end=" ")

def createCostMatrix(words, width):
    cost = [[0 for j in range(len(words))] for i in range(len(words))]

    for i in range(0, len(words)):
        cost[i][i] = (width - len(words[i])) ** 2
        length = 0

        for j in range(i + 1, len(words)):
            length = length + len(words[j]) + len(words[i])
            cost[i][j] = width - (length + 1)

            if (cost[i][j] < 0):
                cost[i][j] = sys.maxsize
            else:
                cost[i][j] = cost[i][j] ** 2
    return cost


def findMinCost(cost, words, width):
    minCost = [0 for i in range(0, len(words))]  # Stores the minimum cost
    result = [0 for i in range(0, len(words))]  # Stores the result

    for i in range(len(words) - 1, -1, -1):
        minCost[i] = cost[i][len(words) - 1]
        result[i] = len(words)

        for j in range(len(words) - 1, i, -1):
            if (cost[i][j - 1] == sys.maxsize):
                continue
            if (minCost[i] > minCost[j] + cost[i][j - 1]):
                minCost[i] = minCost[j] + cost[i][j - 1]
                result[i] = j
    return minCost,result

def printJustifiedText(words, result):
    i = 0
    j = 0
    line = []
    while (j < len(words)):
        j = result[i]
        for k in range(i,j):
            line.append(words[k]+"")
        line.append('\n')
        i = j
    return line



def main():
    width = 10
    words = ["Tushar", "Roy", "likes", "to", "code"]
    textify(words, width)

if __name__ == "__main__":
    main()