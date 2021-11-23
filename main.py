"""
Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.
"""
print("Give me four numbers representing the position of the king, the first two is the starting position, the last two is the ending position. ")
firstX = int(input(" Starting X coordinate of King "))
firstY = int(input(" Starting y coordinate of King "))
secondX = int(input(" Ending X coordinate of King "))
secondY = int(input(" Ending y coordinate of King "))
#asks user for data
if firstX > 8 or firstY > 8 or secondX > 8 or secondY > 8:
  print ("Off Limits")
#verifies that the numbers are within limits
XCoord = firstX-secondX
YCoord = firstY-secondY
#converts both x, and y coordinates into one number
if XCoord <= 1 and XCoord >= -1 and YCoord <= 1 and YCoord >= -1:
  print ("Move is possible")
#verifies that the coodinates are within limits
else:
  print("Not Possible in one move")
