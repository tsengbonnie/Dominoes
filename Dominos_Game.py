#Author: Bonnie Tseng
#Date: June 5, 2013
#Purpose: to simulate a game of dominos

from Tkinter import*
dices = Tk()

#IMPORTS
import random
import time

#CLASSES
#DOMINO Class
#Fields:
#   intValue: represents the value of a domino 0...66
#   intSize: represents the size of the domino
#   intRadius: represents the size of the dots on the domino
#   intGap: represents the space between the dots on the domino
#Methods:
#   __init__: initializes a value for the value of the domino, size of the domino and radius and gap
#   setValue: sets a specific value for the domino
#   value: returns the value of the domino
#   displayValue: displays the dominos on the canvas
#   horizontalOutline: displays the outline for a horizontal outline on the canvas
#   verticalOutline: displays the outline for a vertical outline on the canvas

class Domino:
#Author: Bonnie Tseng
#Date: June 10, 2013
#Purpose: initializes a value for the value of the domino and the size, radius and gap of the domino 
#Input: self is the domino class, value is the value of the domino
#Output: none
    def __init__(self, value = -1):
        if value >=0:
            self.intValue = value
        else:
            self.intValue = 10* random.randint(0,6) + random.randint(0,6)
        self.intSize = 30
        self.intRadius = (self.intSize)/5
        self.intGap = (self.intRadius)/ 2

#Author: Bonnie Tseng
#Date: June 10, 2013
#Purpose: sets a value for the domino
#Input: self is the domino class, value is the value of the domino
#Output: the value of the domino
    def setValue(self,value= 66):
        if value % 10 < 0 or value % 10 > 6 or (value - value % 10)/ 10 < 0 or (value - value % 10)/10 > 6:
            self.intValue = 66
        else:
            self.intValue = value
        return self.intValue

#Author: Bonnie Tseng
#Date: June 10, 2013
#Purpose: returns the value of the domino
#Input: self is the domino class
#Output: the value of the domino
    def value(self):
        return self.intValue

#Author: Bonnie Tseng
#Date: June 10, 2013
#Purpose: displays either a horizontal or vertical domino according to given parameters
#Input: self is the domino class, canvas is the convas on which the domino is to be drawn on, x is the x-coordinate of the top left corner of the domino. y is the y-coordinate of the top left corner of the domino,
#       orientation determines the orientation of the domino, faceup determines whether to display the dots or not
#Output: none
    def displayValue(self, canvas, x= 10, y = 10, orientation = "horizontal", faceup= True):
        def drawOneDot():
            canvas.create_oval (x+ 2*self.intRadius, y + 2*self.intRadius, x+ 3*self.intRadius, y + 3*self.intRadius, outline = "black", fill = "black")
        def drawTwoDots():
            canvas.create_oval (x + self.intGap, y + self.intGap, x + self.intGap + self.intRadius, y + self.intGap + self.intRadius, outline = "black", fill = "black")
            canvas.create_oval (x + self.intSize - self.intGap - self.intRadius, y + self.intSize - self.intGap - self.intRadius, x + self.intSize - self.intGap, y + self.intSize - self.intGap,outline = "black", fill = "black")
        def drawFourDots():
            drawTwoDots() 
            canvas.create_oval (x + self.intSize - self.intGap - self.intRadius, y + self.intGap, x + self.intSize - self.intGap, y + self.intGap + self.intRadius, outline = "black", fill = "black")
            canvas.create_oval (x + self.intGap, y + self.intSize - self.intGap - self.intRadius, x + self.intGap + self.intRadius, y + self.intSize - self.intGap,outline = "black", fill = "black")
        def drawSixDots():
            drawFourDots()
            canvas.create_oval (x + self.intGap, y + 2*self.intRadius, x + self.intGap + self.intRadius, y + 3*self.intRadius,outline = "black", fill = "black")
            canvas.create_oval (x + self.intSize - self.intGap - self.intRadius,y + 2*self.intRadius, x + self.intSize - self.intGap, y + 3*self.intRadius,outline = "black", fill = "black")
        firstDomino = (self.intValue - self.intValue % 10)/ 10
        secondDomino = self.intValue % 10
        if orientation == "vertical":
            self.verticalOutline(x,y)
        elif orientation == "horizontal":
            self.horizontalOutline(x,y)
        if firstDomino == 1:
            drawOneDot()
        elif firstDomino == 2:
            drawTwoDots()
        elif firstDomino == 3:
            drawOneDot()
            drawTwoDots()
        elif firstDomino == 4:
            drawFourDots()
        elif firstDomino == 5:
            drawFourDots()
            drawOneDot()
        elif firstDomino == 6:
            drawSixDots()
        if orientation == "vertical":
            y = y + self.intSize
        elif orientation == "horizontal":
            x = x + self.intSize
        if secondDomino == 1:
            drawOneDot()
        elif secondDomino == 2:
            drawTwoDots()
        elif secondDomino == 3:
            drawOneDot()
            drawTwoDots()
        elif secondDomino == 4:
            drawFourDots()
        elif secondDomino == 5:
            drawFourDots()
            drawOneDot()
        elif secondDomino == 6:
            drawSixDots()

#Author: Bonnie Tseng
#Date: June 10, 2013
#Purpose: draws a vertical outline on the canvas 
#Input: self is the domino class, x is the x-coordinate of the left corner of the domino, y is the y-coordinate of the left corner of the domino
#Output: none            
    def verticalOutline(self,x,y):
        canvas.create_rectangle (x, y, x + self.intSize, y + 2*self.intSize, outline = "black", fill = "white")
    
    def horizontalOutline(self, x,y):
        canvas.create_rectangle (x, y, x + 2*self.intSize, y + self.intSize, outline = "black", fill = "white")

#HAND class
#Fields:
#   hand: the list in which the dominoes in the hand are placed
#   intSize: the size of the hands list
#Methods:
#   __init__: initializes the hand list, size of the hand and sorts the hand
#   sizeOfHand: returns the size of the hand list
#   addDomino: adds a domino to the hands list
#   findValue: returns the value of the domino given the position of the domino in the hand list
#   dropDomino: removes a specific domino given from a parameter from the hands list
#   sortHand: sorts the hands list in ascending order
#   displayHand: displays the hand of dominos on the canvas

class Hand: 
#Author: Bonnie Tseng
#Date: April 30, 2013
#Purpose: initializes the hands list, the size of the list and sorts the hands list
#Input: self is the Dice Class, size is the size of the hand list (defaulted to 7)
#Output: none         
    def __init__ (self, size = 7):
        self.hand = []
        self.intSize = len(self.hand)
        self.sortHand()

#Author: Bonnie Tseng
#Date: June 12, 2013
#Purpose: returns the size of the hand list
#Input: self is the domino class
#Output: the size of the hand list
    def sizeOfHand(self):
        return self.intSize

#Author: Bonnie Tseng
#Date: May 10, 2013
#Purpose: inserts a given value into the list at a given position
#Input: self is the hand Class, position is the position in which the value is being inserted, value is the value of the element being inserted
#Output: none
    def addDomino(self, domino):
        self.intSize = self.intSize + 1
        self.hand.append(domino)

#Author: Bonnie Tseng
#Date: May 31, 2013
#Purpose: finds the location of a given parameter value using the "linear search" method
#Input: self is the hand class, key is the value being searched for
#Output: the location of the key
    def findValue (self, key):
        count =1
        while count <= self.intSize and key != self.hand[count-1]:
            count = count + 1
        if count > self.intSize:
            location = -1
        else:
            location = count
        return location

#Author: Bonnie Tseng
#Date: May 10, 2013
#Purpose: remove the element at a given parameter position in the list
#Input: self is the hand Class, position is the position of the element to be removed
#Output: none
    def dropDomino (self,value):
        position = self.findValue(value)
        self.intSize = self.intSize - 1
        del self.hand[position - 1]
        
#Author: Bonnie Tseng
#Date: June 3, 2013
#Purpose: creates an ascending/descending sorted list (depending on the parameter) using the "insertion sort" method
#Input: self is the hand class, order is the order in which the list is to be sorted
#Output: none
    def sortHand(self, order = "ascending"):
        n = len(self.hand)
        for i in range(1,n):
            hold = self.hand[i]
            j = i - 1
            while j >= 0 and hold < self.hand[j]:
                self.hand[j+1] = self.hand [j]
                j = j - 1
            self.hand [j+1] = hold
            
#Author: Bonnie Tseng
#Date: April 30, 2013
#Purpose: illustrates the hand on the canvas
#Input: self is the hand Class, canvas, hand is the hand of dominos, x is x-coordiate of the top left corner of the first domino in the list
#       y is the y-coordinate of the top left corner of the first dominio in the list, orientation is the orientation of the dominos of the list
#Output: none
    def displayHand (self, canvas, hand,x=30,y=30, orientation = "horizontal"):
        if orientation == "horizontal":
            for i in range(len(hand)):
                domino = Domino(hand[i])
                if i < 4:
                    domino.displayValue(canvas,x + i*70,y,orientation = orientation)
                else:
                    if i == 4:
                        y = y + 40
                    domino.displayValue (canvas, x + (i - 4)*70, y, orientation = orientation)
        elif orientation == "vertical":
            for i in range (len(hand)):
                domino = Domino(hand[i])
                if i < 4:
                    domino.displayValue(canvas, x, y + i*70, orientation = orientation)
                else:
                    if i == 4:
                        x = x + 40
                    domino.displayValue (canvas, x, y + (i - 4)*70, orientation = orientation)

                    
#TABLE class
#Fields:
#   table: the list of dominoes played on the table
#   intSize: the size of the table list
#   left: the first value of the first domino in the table list
#   right: the last value of the last domino in the table list
#Methods:
#   __init__: initializes the table list, determines the size of the table and the left and right domino
#   size: returns the size of the table list
#   findLeft: determines the first value of the first domino in the table list
#   findRight: determines the last value of the last domino in the table list
#   putTable: draws the table list on to the canvas
#   addToTable: adds dominos to the table list

class Table:
#Author: Bonnie Tseng
#Date: June 16, 2013
#Purpose: initializes the table list, size of the table and the left and right values of the table
#Input: self is the table Class
#Output: none
    def __init__(self):
        self.table = []
        self.intSize = len(self.table)
        self.left = 5
        self.right = 6

#Author: Bonnie Tseng
#Date: June 16, 2013
#Purpose: returns the size of the table list
#Input: self is the table Class
#Output: the size of the table list
    def size(self):
        return self.intSize

#Author: Bonnie Tseng
#Date: June 16, 2013
#Purpose: determines the first value of the first domino in the table list
#Input: self is the table Class
#Output: none
    def findLeft(self):
        first = self.table[0]
        self.left = first//10

#Author: Bonnie Tseng
#Date: June 16, 2013
#Purpose: determines the last value of the last domino in the table list
#Input: self is the table Class
#Output: none
    def findRight(self):
        last = self.table[-1]
        self.right = last % 10
        
#Author: Bonnie Tseng
#Date: June 16, 2013
#Purpose: draws the table list on the canvas
#Input: self is the table Class, canvas is the canvas the table list is to be drawn on
#Output: none
    def putTable(self,canvas):
        x = 160
        y = 160
        for i in range(self.intSize):
            value = self.table[i]
            if (i+1) % 6 == 0:
                domino = Domino(value)
                domino.displayValue(canvas, x, y, orientation = "vertical")
                y = y + 60
                if i == 5 or i == 17:
                    x = x - 30
            else:
                if i <= 4 or (i >= 12 and i <=16) or (i >=24 and i <=27):
                    domino = Domino(value)
                    domino.displayValue(canvas, x, y, orientation = "horizontal")
                    x = x + 60
                elif i == 10 or i == 22:
                    storeDigit = value//10
                    value = (value%10) * 10 + storeDigit
                    domino = Domino(value)
                    domino.displayValue(canvas, x, y, orientation = "horizontal")
                    x = x - 30
                else:
                    storeDigit = value//10
                    value = (value%10) * 10 + storeDigit
                    domino = Domino(value)
                    domino.displayValue(canvas, x, y, orientation = "horizontal")
                    x = x - 60

#Author: Bonnie Tseng
#Date: June 16, 2013
#Purpose: adds a domino to the table list
#Input: self is the table Class, value is the value of the domino to be added to the table list, direction is the side of the list in which the value is to be added
#Output: none
    def addToTable(self, value, direction= "l"):
        if direction == "l":
            self.table.insert(0,value)
        elif direction == "r":
            self.table.append(value)
        self.intSize = self.intSize + 1
                

#DOMINOGAME class
#Fields:
#   available: determines the dominos in a domino set
#   firstHand: the list of dominos dealt to the user
#   secondHand: the list of dominos dealt to the first opponent
#   thirdHand: the list of dominos dealt to the second opponent
#   fourthHand: the list of dominos dealt to the third opponent
#   table: the list of the dominos in the table list
#   names: the list of the names of the players
#   usersDomino: the domino the user has selected to play to the table
#   usersSide: the side of the table list in which the usersDomino is to be played
#Methods:
#   __init__: initializes the available list, the four hands in the game, the table, the names of the players and the user moves options
#   deal: deals the domino set to the fours hands
#   displayHands: displays the hands on the canvas
#   displayNames: displays the names of the players on the canvas
#   getNames: gets the names of the players from the user
#   setUp: displays the initial set up of the game
#   playDominos: initiates the game of dominos
#   getComputerMove: gets the move of the second, third and fourth hand
#   getUserMove: gets the users move
#   usuableDominos: the dominos that can played for the round
#   userDomino: the domino that the user wants to play for the round
#   userSide: the side of the table on which the user's domino is to be played
class DominoGame:

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: initializes the available list, four hands, table, play names and user move information
#Input: self is the table Class
#Output: none
    def __init__(self):
        self.available = []
        for i in range(67):
            if (i // 10) <= (i % 10) and (i // 10) <= 6 and (i%10) <= 6:
                self.available.append(i)
        self.firstHand = Hand()
        self.secondHand = Hand()
        self.thirdHand = Hand()
        self.fourthHand = Hand()
        self.table = Table()
        self.names = ["You", "John", "Bob", "Mary"]
        self.usersDomino = 8
        self.usersSide = "l"

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: deals the dominos to the four player hands
#Input: self is the table Class
#Output: none
    def deal(self):
        self.firstHand.hand = []
        self.secondHand.hand = []
        self.thirdHand.hand = []
        self.fourthHand.hand = []
        for i in self.available:
            hand = random.randint(1,4)
            if hand == 1:
                if len(self.firstHand.hand) >= 7:
                    if len(self.secondHand.hand) >= 7:
                        if len(self.thirdHand.hand) >= 7:
                            self.fourthHand.hand.append(i)
                        else:
                            self.thirdHand.hand.append(i)
                    else:
                        self.secondHand.hand.append(i)
                else:
                    self.firstHand.hand.append(i)
            elif hand == 2:
                if len(self.secondHand.hand) >= 7:
                    if len(self.thirdHand.hand) >= 7:
                        if len(self.fourthHand.hand) >= 7:
                            self.firstHand.hand.append (i)
                        else:
                            self.fourthHand.hand.append(i)
                    else:
                        self.thirdHand.hand.append(i)
                else:
                    self.secondHand.hand.append(i)
            elif hand == 3:
                if len(self.thirdHand.hand) >= 7:
                    if len(self.fourthHand.hand) >= 7:
                        if len(self.firstHand.hand) >= 7:
                            self.secondHand.hand.append (i)
                        else:
                            self.firstHand.hand.append(i)
                    else:
                        self.fourthHand.hand.append(i)
                else:
                    self.thirdHand.hand.append(i)
            elif hand == 4:
                if len(self.fourthHand.hand) >= 7:
                    if len(self.firstHand.hand) >= 7:
                        if len(self.secondHand.hand) >= 7:
                            self.thirdHand.hand.append (i)
                        else:
                            self.secondHand.hand.append(i)
                    else:
                        self.firstHand.hand.append(i)
                else:
                    self.fourthHand.hand.append(i)
        self.firstHand.sortHand()
        self.secondHand.sortHand()
        self.thirdHand.sortHand()
        self.fourthHand.sortHand()

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: displays the four hands
#Input: self is the table Class, canvas is the canvas on which the four hands are to be drawn on
#Output: none
    def displayHands(self, canvas):
        self.firstHand.displayHand(canvas, self.firstHand.hand, x = 210, y = 465, orientation = "horizontal")
        self.secondHand.displayHand (canvas, self.secondHand.hand, x = 65, y = 165, orientation = "vertical")
        self.thirdHand. displayHand(canvas, self.thirdHand.hand, x = 210, y = 65, orientation = "horizontal")
        self.fourthHand.displayHand(canvas, self.fourthHand.hand, x = 565, y = 165, orientation = "vertical")

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: adds a domino to the table list
#Input: self is the table Class, canvas is the canvas on which the players names are to be displayed on
#Output: none        
    def displayNames(self, canvas):
        self.getNames()
        dspFirstName = Label (canvas, text = str(self.names[0]), font = ("Arial", "11", "bold"))
        dspFirstName.place (x = 325, y = 540)
        dspSecondName = Label (canvas,text = str(self.names[1]), font = ("Arial", "11", "bold"))
        dspSecondName.place (x = 65, y = 140)
        dspThirdName = Label (canvas, text = str(self.names[2]), font = ("Arial", "11", "bold"))
        dspThirdName.place (x = 325, y = 35)
        dspFourthName = Label (canvas, text = str(self.names[3]), font = ("Arial", "11", "bold"))
        dspFourthName.place (x = 560, y = 140)

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: gets the player names from the user
#Input: self is the table Class
#Output: none        
    def getNames (self):
        self.names = []
        self.names.append(strFirstName.get())
        self.names.append(strSecondName.get())
        self.names.append(strThirdName.get())
        self.names.append(strFourthName.get())

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: displays the initial set up of the game
#Input: self is the table Class, canvas on which the set up is to be displayed on
#Output: none
    def setUp(self, canvas):
        lblPrompt.destroy()
        lblFirstName.destroy()
        txtFirstName.destroy()
        lblSecondName.destroy()
        txtSecondName.destroy()
        lblThirdName.destroy()
        txtThirdName.destroy()
        lblFourthName.destroy()
        txtFourthName.destroy()
        canvas.create_rectangle (150, 150, 550, 450, outline = "black", fill = "aquamarine2")
        self.deal()
        self.displayHands(canvas)
        self.displayNames(canvas)
        self.playDominos(canvas)
        self.table.putTable(canvas)

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: initializes the first move in the game, player with the 6-6 domino makes a move
#Input: self is the table Class, canvas is the canvas on which the game is to be displayed on
#Output: none
    def playDominos(self,canvas):
        canvas.delete("all")
        canvas.create_rectangle (150, 150, 550, 450, outline = "black", fill = "aquamarine2")
        self.firstHand.intSize = len(self.firstHand.hand)
        self.secondHand.intSize = len(self.secondHand.hand)
        self.thirdHand.intSize = len(self.thirdHand.hand)
        self.fourthHand.intSize = len(self.fourthHand.hand)
        if self.firstHand.findValue(66) > 0:
            self.firstHand.dropDomino(66)
            first = 1
        elif self.secondHand.findValue(66) > 0:
            self.secondHand.dropDomino(66)
            first = 2
        elif self.thirdHand.findValue(66) > 0:
            self.thirdHand.dropDomino(66)
            first = 3
        else:
            self.fourthHand.dropDomino(66)
            first = 4
        self.table.addToTable(66,"l")
        self.table.putTable(canvas)
        self.displayHands(canvas)
        if first + 1 == 2 or first + 1 == 3 or first + 1 == 4:
            self.getComputerMove(canvas,hand = first + 1)
        else:
            self.getUserMove()

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: gets the moves of the second, third and fourth hand
#Input: self is the table Class, canvas is the canvas on which the game is to be displayed on, hand is the player who is making the next move
#Output: none
    def getComputerMove(self,canvas, hand = 0):
        text = canvas.create_text(350,425, text = "It is the computer's turn",font = ("Arial", "12", "bold"))
        while (len(self.firstHand.hand) != 0 or len(self.secondHand.hand) != 0 or len(self.thirdHand.hand) != 0 or len(self.fourthHand.hand) != 0) and hand != 5:
            #delay between each player
            time.sleep(1)
            canvas.update()
            self.table.findLeft()
            self.table.findRight()
            if hand == 2:
                player = self.secondHand
            elif hand == 3:
                player = self.thirdHand
            elif hand == 4:
                player = self.fourthHand
            if len(self.usuableDominos(player.hand)) > 0:
                dominosList = self.usuableDominos(player.hand)
                position = random.randint(0, len(dominosList)-1)
                domino = dominosList[position]
                if domino//10 == self.table.left:
                    storeDigit = domino//10
                    domino = (domino%10) * 10 + storeDigit
                    self.table.addToTable(domino, "l")
                elif domino % 10 == self.table.left:
                    self.table.addToTable(domino, "l")
                elif domino // 10 == self.table.right:
                    if (len(self.table.table) >= 7 and len(self.table.table) <= 11) or (len(self.table.table) >= 19 and len(self.table.table) <= 23):
                        storeDigit = domino//10
                        domino = (domino%10) * 10 + storeDigit
                        self.table.addToTable(domino, "r")
                    else:
                        self.table.addToTable(domino, "r")
                elif domino % 10 == self.table.right:
                    if (len(self.table.table) >= 7 and len(self.table.table) <= 11) or (len(self.table.table) >= 19 and len(self.table.table) <= 23):
                        self.table.addToTable(domino, "r")
                    else:
                        storeDigit = domino//10
                        domino = (domino%10) * 10 + storeDigit
                        self.table.addToTable(domino, "r")
                player.dropDomino(domino)
                canvas.delete("all")
                canvas.create_rectangle (150, 150, 550, 450, outline = "black", fill = "aquamarine2")
                self.displayHands(canvas)
                self.displayNames(canvas)
                self.table.putTable(canvas)
            hand = hand + 1
        self.getUserMove()

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: displays a prompt informing the user that it is his/her turn
#Input: self is the table Class
#Output: none           
    def getUserMove(self):
        text = canvas.create_text(355,420, text = "It is your turn, please key in the domino you wish to place",font = ("Arial", "10", "bold"))

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: determines the dominos that can be used in a given player's move
#Input: self is the table Class, hand represents the player who is currently making a move
#Output: results a list of possible domino to be used     
    def usuableDominos(self,hand):
        storeList = []
        for i in hand:
            if i//10 == self.table.left or i//10 == self.table.right or i % 10 == self.table.left or i % 10 == self.table.right:
                storeList.append(i)
        return storeList

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: gets the domino that the user want to play in his/her move
#Input: self is the table Class, domino is the domino that the user wants to use
#Output: none
    def userDomino(self,domino):
        if int(domino) <= len(self.firstHand.hand):
            canvas.create_text (355, 435, text = "Where would you like to place it? Select 'l'(left) or 'r'(right)", font = ("Arial", "10", "bold"))
            self.usersDomino = int(domino)
        print self.usersDomino

#Author: Bonnie Tseng
#Date: June 17, 2013
#Purpose: gets the side of the table list on which the user wants to play his/her domino
#Input: self is the table Class, side is the side of the table list on which the domino is to be placed
#Output: none
    def userSide(self,side):
        domino = self.firstHand.hand[self.usersDomino - 1]
        if side == "l":
            self.table.findLeft()
            end = self.table.left
            if domino//10 == end:
                storeDigit = domino//10
                domino = (domino%10) * 10 + storeDigit
                self.table.addToTable(domino, "l")
            elif domino % 10 == end:
                self.table.addToTable(domino, "l")
        elif side == "r":
            self.table.findRight()
            end = self.table.right
            if domino//10 == end:
                if (len(self.table.table) >= 7 and len(self.table.table) <= 11) or (len(self.table.table) >= 19 and len(self.table.table) <= 23):
                    storeDigit = domino//10
                    domino = (domino%10) * 10 + storeDigit
                    self.table.addToTable(domino, "r")
                else:
                    self.table.addToTable(domino, "r")
            elif domino % 10 == end:
                    if (len(self.table.table) >= 7 and len(self.table.table) <= 11) or (len(self.table.table) >= 19 and len(self.table.table) <= 23):
                        storeDigit = domino//10
                        domino = (domino%10) * 10 + storeDigit
                        self.table.addToTable(domino, "r")
                    else:
                        self.table.addToTable(domino, "r")
        self.firstHand.dropDomino(domino)
        canvas.delete("all")
        canvas.create_rectangle (150, 150, 550, 450, outline = "black", fill = "aquamarine2")
        self.displayHands(canvas)
        self.displayNames(canvas)
        self.table.putTable(canvas)
        time.sleep(1)
        self.getComputerMove(canvas,hand = 2)        
    
######################################################
#MAIN PART OF THE PROGRAM
dices.title ("Dominos!")
canvas = Canvas(dices, width = 700, height = 600)
canvas.place (x = 1, y = 40)
canvas.pack()
game = DominoGame()

strFirstName = StringVar ()
strFirstName.set(value = "User")
strSecondName = StringVar ()
strSecondName.set(value = "John")
strThirdName = StringVar()
strThirdName.set(value = "Bob")
strFourthName = StringVar()
strFourthName.set(value = "Mary")
lblPrompt = Label (dices, text = "Enter your name and the names of your three opponents, then press tab and 's' to start playing!")
lblPrompt.place ( x = 125, y = 150)

lblFirstName = Label (dices, text = "Your Name :")
lblFirstName.place(x = 220, y = 175)
txtFirstName = Entry (dices, textvariable = strFirstName)
txtFirstName.place(x= 360, y = 175)

lblSecondName = Label (dices, text = "1st Opponent's Name :")
lblSecondName.place(x = 220, y = 200)
txtSecondName = Entry (dices, textvariable = strSecondName)
txtSecondName.place(x= 360, y = 200)

lblThirdName = Label (dices, text = "2nd Opponent's Name :")
lblThirdName.place(x = 220, y = 225)
txtThirdName = Entry (dices, textvariable = strThirdName)
txtThirdName.place(x= 360, y = 225)

lblFourthName = Label (dices, text = "3rd Opponent's Name :")
lblFourthName.place(x = 220, y = 250)
txtFourthName = Entry (dices, textvariable = strFourthName)
txtFourthName.place(x= 360, y = 250)

#game.getNames()
hand = Hand()
#print hand.hand
table = Table()
#table.addToTable(11, "r")
#hand.displayHand(canvas,hand.hand,10,10)
#canvas.create_rectangle (150, 150, 550, 450, outline = "black", fill = "aquamarine2")
#table.addToTable(36,"l")
#print table.table
#drawButton = Button (dices, text= "Get Names!", command = lambda: game.displayHands(canvas),font=("Arial","13"))
#drawButton2 = Button (dices, text= "Display Domino", command = lambda: table.putTable(canvas),font=("Arial","13"))
#drawButton.place (x= 70, y = 450)
#drawButton2.place(x = 70, y = 500)
#domino = Domino()
#print domino.intValue
def keyPressed (event):
    global canvas
    if event.char == "s":
        game.setUp(canvas)
    elif event.char == "1" or event.char == "2" or event.char == "3" or event.char == "4" or event.char == "5" or event.char == "6" or event.char == "7":
        game.userDomino(event.char)
    elif event.char == "l" or event.char == "r":
        game.userSide(event.char)
    elif event.char == "p":
        game.getComputerMove(canvas,hand = 2)

canvas.bind("<Key>", keyPressed)
canvas.focus_set()

#table = Table()
#print table.table
dices.mainloop()
