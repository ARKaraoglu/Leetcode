# @leet start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        squareNum = image[sr][sc]
        newImage = image

        row = len(image)
        column = len(image[0])
        
        if image == None:
            return -1

        coordStack = []
        visitedCords = []
        coordStack.append([sc, sr])
        
        image[sr][sc] = color

        while coordStack:
            x = coordStack[0][0]
            y = coordStack[0][1]
            
            if x - 1 != -1:
                localX  = x - 1
                if newImage[y][localX] == squareNum and [localX, y] not in coordStack and [localX, y] not in visitedCords:
                    newImage[y][localX] = color
                    coordStack.append([localX, y])
            
            if x + 1 < column:
                localX  = x + 1
                if newImage[y][localX] == squareNum and [localX, y] not in coordStack and [localX, y] not in visitedCords:
                    newImage[y][localX] = color
                    coordStack.append([localX, y])

            if y - 1 != -1:
                localY = y - 1
                if newImage[localY][x] == squareNum and [x, localY] not in coordStack and [x, localY] not in visitedCords:
                    newImage[localY][x] = color
                    coordStack.append([x, localY])

            if y + 1 < row:
                localY = y + 1

                if newImage[localY][x] == squareNum and [x, localY] not in coordStack and [x, localY] not in visitedCords:
                    newImage[localY][x] = color
                    coordStack.append([x, localY])

            coordStack.pop(0)
            visitedCords.append([x, y])
        
        return newImage


        
# @leet end
