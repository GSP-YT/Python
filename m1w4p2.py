userInput = list((input("Enter num list :").split()))
numList = []
for num in range(userInput): numList.append(int(num))
def isEvent(x) : return x % 2 == 0
print(filter(isEvent,numList))