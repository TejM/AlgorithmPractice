class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if(image[sr][sc]==newColor):
            return image

        startingColor = image[sr][sc]
        moves = [(-1,0), (0,-1), (1,0), (0, 1)]
        
        stack = []
        
        stack.append((sr, sc))
        
        while len(stack) != 0:
            current_row, current_column = stack.pop()
            if image[current_row][current_column] == startingColor:
                image[current_row][current_column] = newColor
                for move in moves:
                    future_row = current_row + move[0]
                    future_column = current_column + move[1]
                    if len(image) > future_row >=0 and len(image[0]) > future_column >=0 and image[future_row][future_column] == startingColor:
                        stack.append((future_row, future_column))
        return image 
                
            
