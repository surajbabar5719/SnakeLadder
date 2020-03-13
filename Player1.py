class Player:
    def __init__(self):
        self.position=0
        self.ladder=[3,8,17,20,27,50,70,77]
        self.dLadder=[13,30,44,41,83,66,90,96]
        self.snake=[25,51,61,65,73,88,94,97]
        self.dSnake=[10,28,18,58,16,68,74,78]
    def changePosition(self,number):
        self.position+=number
        if self.position>=100:
            self.position-=number
        if self.position in self.snake:
            self.position=self.dSnake[self.snake.index(self.position)]
        if self.position in self.ladder:
            self.position=self.dLadder[self.ladder.index(self.position)]
    def getPosition(self):
        print(self.position)
        return self.position
if __name__=="__main__":
    p=Player()
    k=1
    while k==1:
        k=0
        from Dice import *
        d,a,b=dice()
        p.changePosition(d)
        print(p.getPosition())