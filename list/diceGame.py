import random
class diceGame:
    def diceSelect(self,dicelist):

        choice= random.choice(myDice)
        return choice

myDice=[1,2,3,4,5,6]
newObj=diceGame()
output=newObj.diceSelect(myDice)
print(output)