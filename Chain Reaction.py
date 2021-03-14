from tkinter import *
from random import randint
from random import uniform
from time import sleep
import threading
from threading import Thread
import math
WIDTH = 800
HEIGHT = 800
CANVAS_MID_X = WIDTH/2
CANVAS_MID_Y = HEIGHT/2
SIDE = WIDTH/64
lastKnownCursor = [0,0]
root = Tk()
canvas = Canvas(root, bg="black", height=HEIGHT, width=WIDTH)
canvas.pack()
expanding = False
moveSpeed = 2
EXPANSION_SIZE = SIDE * 1.6
EXISTANCE_TIME = 300 # 0.007 * time

COLOURS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace','linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff','navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender','lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray','light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue','slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue','dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue','light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise','cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green','dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green','lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green','forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow','light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown','indian red', 'saddle brown', 'sandy brown','dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange','coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink','pale violet red', 'maroon', 'medium violet red', 'violet red','medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple','thistle', 'snow2', 'snow3','snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2','AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2','PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4','LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3','cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4','LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3','MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3','SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4','DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2','SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4','SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2','LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3','SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3','LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4','LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2','PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3','CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3','cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4','aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3','DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2','PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4','green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4','OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2','DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4','LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4','LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4','gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4','DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4','RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2','IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1','burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1','tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2','firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2','salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2','orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4','coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2','OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4','HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4','LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1','PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2','maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4','magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1','plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3','MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4','purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2','MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3']

defualtSpeed = 5
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle_arc = _create_circle_arc

def graduallyExpand(center,count):
    global expanding
    while count < WIDTH/16:
        canvas.create_circle(center[0], center[1], count, fill="blue")
        root.update()
        count=count+1 
    expanding = False

def createBallData(numberOfBallz):
    arrayOfBallz = []
    for i in range (0,numberOfBallz):
        arrayOfBallz.append([ [randint(1,WIDTH),randint(1,HEIGHT)] , COLOURS[randint(0,len(COLOURS)-1)], randint(0,360)]) #[ [randomx, randomy],randomColourName,direction (0,360)
    return(arrayOfBallz)

def drawBallz(arrayOfBallz):
    for ballData in arrayOfBallz:
        canvas.create_circle(ballData[0][0], ballData[0][1], SIDE, fill=str(ballData[1]))
    root.update()

def updateBallPositions(ballsData):
    newBallData = []
    for ballData in ballsData:
        angle = ballData[2]
        currentXY = ballData[0]

        newXY = [currentXY[1] + (moveSpeed*math.degrees(math.sin(angle))),currentXY[0] + (moveSpeed*math.degrees(math.cos(angle)))]

        newBallData.append([newXY,ballData[1],ballData[2]])
    return(newBallData)

class Ball:
    def __init__(self,xyPair):
        self.x = xyPair[0]
        self.y = xyPair[1]
        self.angle = uniform(0,2*math.pi) # Returns random float between 0 and 2* pi, which is 360 Degrees
        
        #self.angle = (math.radians(360))
        self.colour = COLOURS[randint(0,len(COLOURS)-1)]
        
        self.expanded = False
        self.expanding = False
        self.expansionCounter = 0

        self.existanceCounter = 0
        
        self.shrinking = False
        self.shrunk = False
        self.shrinkingCounter = EXPANSION_SIZE
        
        self.circleObject = canvas.create_circle(self.x, self.y, SIDE, fill=self.colour)

        self.currentRadius = SIDE
        self.normal = True

    def expand(self):
        self.expanding = True

    def updatePosition(self):
        if (self.expanded == False) and (self.expanding == False) and (self.shrinking == False) and (self.shrunk == False):
            newXY = [self.x + (moveSpeed*math.cos(self.angle)),self.y + (moveSpeed*math.sin(self.angle))]
            self.x = newXY[0]
            self.y = newXY[1]
            canvas.coords(self.circleObject,self.x-SIDE, self.y-SIDE,self.x+SIDE, self.y+SIDE)
            newXY = [self.x + (moveSpeed*math.cos(self.angle)),self.y + (moveSpeed*math.sin(self.angle))]
            nextX = self.x
            nextY = self.y

            if nextX < 0:
                if (self.angle > math.radians(90) ) and (self.angle < math.radians(180)):
                    self.angle = abs( (self.angle - math.radians(90)   + math.radians(90) ) - math.radians(180)  )
                    
                elif (self.angle < math.radians(270) ) and (self.angle > math.radians(180)):
                    angleT = self.angle - math.radians(180)
                    trigCornerAngle = math.radians(90) - angleT
                    angleX = abs((trigCornerAngle + math.radians(90)) - math.radians(180))
                    self.angle = math.radians(270) + ( math.radians(90) - angleX )
                else:
                    #print("The ball should have hit at exactly 90 Degrees, the X wall Left")
                    #print(self.angle)
                    if randint(0,1) == 1:
                        self.angle = math.radians(randint(290,340))
                    else:
                        self.angle = math.radians(randint(10,70))

            elif nextX > WIDTH:
                if (self.angle > math.radians(270) ) and (self.angle < math.radians(360)):
                    angleT = self.angle - math.radians(270)
                    angleX = abs(math.radians(180) - (angleT + math.radians(90)))
                    self.angle = angleX + math.radians(180)
                elif (self.angle < math.radians(90) ) and (self.angle > math.radians(0)):
                    angleX = abs(math.radians(180) - (self.angle + math.radians(90)))
                    self.angle = math.radians(180) - angleX
                else:
                    #print("The ball should have hit at exactly 0 Degrees, the X wall Right")
                    #print(self.angle)
                    self.angle = math.radians(randint(100,250))

            elif nextY < 0:
                if (self.angle > math.radians(180) ) and (self.angle < math.radians(270)):
                    angleT = self.angle - math.radians(180)
                    angleX = abs(math.radians(180) - (angleT + math.radians(90)) )
                    self.angle = angleX + math.radians(90)

                elif (self.angle < math.radians(360) ) and (self.angle > math.radians(270)):
                    angleT = abs(math.radians(90) - (self.angle - math.radians(270)))
                    angleX = abs(math.radians(180) - (angleT + math.radians(90)) )
                    self.angle = angleX
                else:
                    #print("The ball should have hit at exactly 0 Degrees, the Y wall Top")
                    #print(self.angle)
                    self.angle = math.radians(randint(10,160))
                    
            elif nextY > HEIGHT:
                if (self.angle > math.radians(0) ) and (self.angle < math.radians(90)):
                    self.angle = (math.radians(270) + ( math.radians(90) - self.angle ))

                elif (self.angle < math.radians(180) ) and (self.angle > math.radians(90)):
                    angleT = self.angle - math.radians(90)
                    angleX = abs(math.radians(180) - (angleT + math.radians(90)) )
                    self.angle = math.radians(180) + angleX
                else:
                    #print("The ball should have hit at exactly 0 Degrees, the Y wall Bottom")
                    #print(self.angle)
                    self.angle = math.radians(randint(190,340))

    def changeSizeIfNesacery(self):
        if (self.expanded == False) and (self.expanding == True):
            canvas.delete(self.circleObject)
            self.circleObject = canvas.create_circle(self.x, self.y, SIDE + self.expansionCounter, fill=self.colour)
            self.expansionCounter = self.expansionCounter + 1
            self.currentRadius = self.expansionCounter

        if self.expansionCounter > EXPANSION_SIZE:
            self.expansionCounter = 0
            self.expanded = True
            self.expanding = False
            
        if (self.expanded == True) and (self.shrinking == False):
            self.existanceCounter = self.existanceCounter + 1
            if self.existanceCounter > EXISTANCE_TIME:
                self.shrinking = True

        if (self.shrinking == True) and (self.shrunk == False):
            self.shrinkingCounter = self.shrinkingCounter - 2
            self.currentRadius = self.currentRadius - 2
            canvas.delete(self.circleObject)
            self.circleObject = canvas.create_circle(self.x, self.y, SIDE + self.shrinkingCounter, fill=self.colour)

        if (int(self.shrinkingCounter) < -SIDE) and (self.shrunk == False):
            self.shrinking = False
            self.shrunk = True
            self.shrinkingCounter = EXPANSION_SIZE
            canvas.delete(self.circleObject)
            self.normal = False

    def checkForCollision(self, ballArray, currentBallInArray):
    
        for i in range(0,len(ballArray)):
            if i != currentBallInArray:
                if (self.expanded == True) or (self.expanding == True):
                    # if touching other ball
                    x0 = self.x
                    y0 = self.y
                    R0 = SIDE + self.currentRadius

                    x1 = ballArray[i].x
                    y1 = ballArray[i].y
                    R1 =(ballArray[i].currentRadius)

                    xLen = abs(x0-x1)
                    yLen = abs(y0-y1)
                    hLenS = xLen**2 + yLen**2
                    hLen = math.sqrt(hLenS)
                    if hLen <= (R0 + R1):
                        ballArray[i].expand()
                        
        if ((cursorObject.expanded == True) or (cursorObject.expanding == True)) and (cursorObject.shrunk == False):
            x0 = self.x
            y0 = self.y
            R0 = SIDE + self.currentRadius

            x1 = cursorObject.x
            y1 = cursorObject.y
            R1 =(cursorObject.currentRadius)

            xLen = abs(x0-x1)
            yLen = abs(y0-y1)
            hLenS = xLen**2 + yLen**2
            hLen = math.sqrt(hLenS)
            if hLen <= (R0 + R1):
                self.expand()                   

    def AUTOLYSIS(self,ballArray,ballRef): # programmed cell death
        if self.shrunk == True:
            return("DeadBall")            
        else:
            return(ballArray[ballRef])


class Cursor:
    def __init__(self,x,y):
        self.cursorObject = canvas.create_circle(x, y, SIDE, fill="light blue")
        self.x = x
        self.y = y
        self.expanded = False
        self.expanding = False
        self.expansionCounter = 0

        self.existanceCounter = 0
        
        self.shrinking = False
        self.shrunk = False
        self.shrinkingCounter = EXPANSION_SIZE

        self.currentRadius = SIDE
        self.normal = True

    def resetAll(self,x,y):
        self.cursorObject = canvas.create_circle(x, y, SIDE, fill="light blue")
        self.x = x
        self.y = y
        self.expanded = False
        self.expanding = False
        self.expansionCounter = 0

        self.existanceCounter = 0
        
        self.shrinking = False
        self.shrunk = False
        self.shrinkingCounter = EXPANSION_SIZE

        self.currentRadius = SIDE
        self.normal = True       
    
    def updatePosition(self,center):
        canvas.coords(self.cursorObject,center[0]-SIDE, center[1]-SIDE,center[0]+SIDE, center[1]+SIDE)
        self.x = center[0]
        self.y = center[1]
        
    def expand(self):
        if self.expanded == False:
            self.expanding = True

    def changeSizeIfNesacery(self):
        if (self.expanded == False) and (self.expanding == True):
            canvas.delete(self.cursorObject)
            self.cursorObject = canvas.create_circle(self.x, self.y, SIDE + self.expansionCounter, fill="light blue")
            self.expansionCounter = self.expansionCounter + 1
            self.currentRadius = self.expansionCounter

        if self.expansionCounter > EXPANSION_SIZE:
            self.expansionCounter = 0
            self.expanded = True
            self.expanding = False
            
        if (self.expanded == True) and (self.shrinking == False):
            self.existanceCounter = self.existanceCounter + 1
            if self.existanceCounter > EXISTANCE_TIME:
                self.shrinking = True

        if (self.shrinking == True) and (self.shrunk == False):
            self.shrinkingCounter = self.shrinkingCounter - 2
            self.currentRadius = self.currentRadius - 2
            canvas.delete(self.cursorObject)
            self.cursorObject = canvas.create_circle(self.x, self.y, SIDE + self.shrinkingCounter, fill="light blue")

        if (int(self.shrinkingCounter) < -SIDE) and (self.shrunk == False):
            self.shrinking = False
            self.shrunk = True
            self.shrinkingCounter = EXPANSION_SIZE
            canvas.delete(self.cursorObject)
            self.normal = False

def mouseMove(event):
    if (cursorObject.expanding == False) and (cursorObject.expanded == False):
        x, y = event.x, event.y
        cursorObject.updatePosition([x,y])
        root.update()

cursorObject = Cursor(-WIDTH,-HEIGHT)
def main():
    global ballArray
    
    for level in levelData:
        print("Looping round to do anohter level")
        canvas.delete("all")

        totalBallsAtStart = level[1]
        levelOver = False
        cursorObject.resetAll(-WIDTH,-HEIGHT)
        
        ballArray = []
        for i in range (0,int(level[1])):
            tempBall = Ball([randint(1,WIDTH),randint(1,HEIGHT)])
            ballArray.append(tempBall)
        
        for ball in ballArray:
            ball.updatePosition()

        while levelOver == False:
            if (cursorObject.shrunk == True): # If the cursor has shrunk and disapeared
                # Cursor object gone
                # if all balls are normal then end level
                 infectedBalls = 0
                 for ball in ballArray:
                     #check to see if balls are large, growing, or shrinking
                     if (ball.shrinking == True) or (ball.expanding == True) or (ball.expanded == True):
                         infectedBalls = infectedBalls + 1

                 if infectedBalls == 0:
                    levelOver = True
                    
            sleep(0.007)
            cursorObject.changeSizeIfNesacery()
            
            for ball in ballArray:
                ball.updatePosition()

            for i in range(0,len(ballArray)):
                ballArray[i].checkForCollision(ballArray,i)

            for ball in ballArray:
                ball.changeSizeIfNesacery()

            # Remove dead balls
            newBallArray = []
            for i in range(0,len(ballArray)):       
                possibleBall = ballArray[i].AUTOLYSIS(ballArray,i)
                if possibleBall != "DeadBall":
                    newBallArray.append(possibleBall)
            ballArray = newBallArray[:]
            canvas.update()
        
        
def createLevels(noOfLevels):
    levels = []
    for i in range (3,noOfLevels):
        tempLevel = [str(i),noOfLevels+randint(1,noOfLevels),noOfLevels-(randint(1,round(noOfLevels/2,0)))]
        levels.append(tempLevel[:])
    return(levels)

levelData = createLevels(10) # [Name,totalNumberOfBallz,aimedForNumberOfBallz

levelData = [['3', 60, 5]]

center = (CANVAS_MID_X, CANVAS_MID_Y)
center = (400.0,400.0)

root.bind('<Motion>', mouseMove)
root.bind('<Button-1>', lambda x: cursorObject.expand())

Thread(target = main).start()
mainloop()
