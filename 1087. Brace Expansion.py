#space: O(n)
#time:O(n*n)
class Solution:
    def expand(self, s: str) -> List[str]:

        #first we will create blocks of characters inside {} as one block and each character outside as other blocks
        blocks=[]
        n= len(s)
        i=0
        while i< n:
            if s[i] == '{':
                i+=1
                block=[]
                while s[i] != '}':
                    if s[i]!=',':
                        block.append(s[i])
                    i+=1
            else:
                block=[s[i]]
            block.sort()
            blocks.append(block)
            i+=1
        self.blocks=blocks
        self.result=[]
        #then we will recurse over the blocks as backtracking to find all the subsets 
        self.backtrack(0,'')
        return self.result
    def backtrack(self,index,path):
        if index== len(self.blocks):
            self.result.append(path)
            return
        for c in self.blocks[index]:
            #action
            path+=str(c)
            #recurse
            self.backtrack(index+1,path)
            #backtrack
            path= path[:len(path)-1]
        return
