class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
            index = 0
            hashMap = {}                                   # checking row's 1-9 rule
            for i in range(0,9):
                hashMap = {}
                for j in range(0,9):
                    if board[i][j] == ".":
                        continue
                    elif board[i][j] not in hashMap:
                        hashMap[board[i][j]] = 1
                    else:
                        return False
                
            hashMap = {}                                    # checking col's 1-9 rule
            for i in range(0,9):
                hashMap = {}  
                for j in range(0,9):
                    if board[j][i] == ".":
                        continue
                    elif board[j][i] not in hashMap:
                        hashMap[board[j][i]] = 1
                    else:
                        return False
                
            hashMap = {}

            # what i need to do is keep x and y in the square: so x can be 0,1,2 and y can be 0,1,2 and influence them accordingly
            a = 0                               
            b = 0
            index = 0
            hashMap = {}                                                        # checking square's 1-9 rule
            for mau in range(3):
                for square in range(3):
                    hashMap = {}
                    for i in range(0,3):
                        for j in range(0,3):
                            if board[i + a][j + b] == ".":
                                continue
                            elif board[i + a][j + b] not in hashMap:
                                hashMap[board[i + a][j + b]] = 1
                            else:
                                return False
                           
                    b += 3     
                a += 3 
                b = 0   
            return True
                  
       
               

                

        
