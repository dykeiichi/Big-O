from datetime import datetime

def worst(numA, numB):
    i=0
    while(numA != 0 and numB != 0 and not (numA == 1 and numB == 1)):
        print (str(numA) + " : " + str(numB))
        if(numA > numB):
            numA-=2
            numB-=1
        else:
            numA-=1
            numB-=2
        i+=1
    return i

def best(numA, numB):
    i=0
    if numA<numB:
        aux = numA
        numA = numB
        numB = aux

    if(numB*2 <= numA):
        i=numB
    else:
        numD = ((2*numB - numA)/3)
        print (str(numA) + " : " + str(numB))
        i = int(((numA-numD)+ (2*numD))/2)
    return i

def main1():
    numA = 0
    numB = 0
    print("numA: " + str(numA) + " | numB: " + str(numB) + " | best: " + str(best(numA,numB)) + " | worst: " + str(worst(numA,numB)))

    while numA < 1000:
        while numB < 1000:
            if not int(best(numA,numB)) == int(worst(numA,numB)):
                print("numA: " + str(numA) + " | numB: " + str(numB) + " | best: " + str(best(numA,numB)) + " | worst: " + str(worst(numA,numB)))
            numB+=1
        numA+=1
        numB=0
    return 0

def main():
    numA = 100000
    numB = 100000
    print("numA: " + str(numA) + " | numB: " + str(numB))

    worstTimeB = datetime.now()
    numWorst = worst(numA,numB)
    worstTimeA = datetime.now()

    bestTimeB = datetime.now()
    numBest = best(numA,numB)
    bestTimeA = datetime.now()

    print("best: " + str(numBest) + " | worst: " + str(numWorst))
    print("best time: " + str(bestTimeA - bestTimeB))
    print("worst time: " + str(worstTimeA - worstTimeB))

if __name__ == "__main__":
    main()