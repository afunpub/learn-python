from PIL import ImageGrab, ImageOps
import pyautogui
# print(pyautogui.displayMousePosition())
currentGrid = [
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0]


class Cords:
    cord11 = (170, 360)
    cord12 = (290, 360)
    cord13 = (410, 360)
    cord14 = (530, 360)
    cord21 = (170, 488)
    cord22 = (290, 488)
    cord23 = (410, 488)
    cord24 = (530, 488)
    cord31 = (170, 610)
    cord32 = (290, 610)
    cord33 = (410, 610)
    cord34 = (530, 610)
    cord41 = (170, 729)
    cord42 = (290, 729)
    cord43 = (410, 729)
    cord44 = (530, 729)

    cordArray = [
        cord11, cord12, cord13, cord14,
        cord21, cord22, cord23, cord24,
        cord31, cord32, cord33, cord34,
        cord41, cord42, cord43, cord44
    ]


class Values:
    empty = 193
    two = 228
    four = 224
    eight = 189
    sixteen = 171
    thirtyTwo = 156
    sixtyFour = 134
    oneTwentyEight = 204
    twoFiftySix = 245
    fiveOneTwo = 234
    oneZeroTwoFour = 192
    twoZeroFourEight = 188
    valueArray = [
        empty, two, four, eight, sixteen, thirtyTwo, sixtyFour, oneTwentyEight, twoFiftySix, fiveOneTwo, oneZeroTwoFour, twoZeroFourEight
    ]


def getGrid():
    image = ImageGrab.grab()
    grayImage = ImageOps.grayscale(image)
    for index, cord in enumerate(Cords.cordArray):
        pixel = grayImage.getpixel(cord)
        print(pixel,end=" ")
        pos = Values.valueArray.index(pixel)
        if pos == 0:
            currentGrid[index] = 0
        else:
            currentGrid[index] = pow(2, pos)

def printGrid(grid):
    for i in range(16):
        if i%4==0:
            print(str(grid[i])+" "+str(grid[i+1])+" "+str(grid[i+2])+" "+str(grid[i+3]))
getGrid()
printGrid(currentGrid)
