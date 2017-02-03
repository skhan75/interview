import sys

# BOTTOM UP APPROACH
# Time Complexity = O(mn)
def minimumCoinChangingBottomUp(total, coins):

    T = []
    R = []

    for i in range(0, total):
        if (i == 0):
            T.append(0)
            R.append(-1)
        T.append(sys.maxsize)
        R.append(-1)

    for j in range(0, len(coins)):
        for i in range(1, total+1):
            if(i >= coins[j]):
                if((T[i-coins[j]] + 1) < T[i]):
                    T[i] = 1 + T[i - coins[j]]
                    R[i] = j

    printCombinations(R,coins)
    return T[total]

def printCombinations(R,coins):
    if(R[len(R)-1] == -1):
        print ('No solutions possible')
        return
    start = len(R)-1
    print ('Coins combinations are:')
    while (start != 0):
        j = R[start]
        print(coins[j],end = " ")

        start = start - coins[j]
    print()

def main():
    total = 13
    coins = [7,3,2,6]
    print('Minimum No of coins required are: ',minimumCoinChangingBottomUp(total, coins))

if __name__ == "__main__":
    main()