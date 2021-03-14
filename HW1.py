numbers = list(range(10))

listofEvens = [i for i in numbers if i % 2 == 0 ]
listofOdds =  [i for i in numbers if i % 2 == 1 ]

mergeList = listofEvens + listofOdds
mergeList.sort()

mergeList = [i*2 for i in mergeList]

for i in numbers:
    print(type(mergeList[i]))