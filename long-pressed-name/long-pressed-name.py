class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) > len(typed):
            return False
        if name == typed:
            return True
        
        i = 0
        j = 0
        while(i<len(name) and j < len(typed)):
            if name[i]!=typed[j]:
                return False
            # Scan For repeating elements
            c1 = 0
            while(j+1 < len(typed) and typed[j]==typed[j+1]):
                j+=1
                c1+=1
            c2 = 0   
            while(i+1 < len(name) and name[i]==name[i+1]):
                i+=1
                c2+=1
      
            if c2 > c1:
                return False
            
            i+=1
            j+=1
        
        
   
        if i != len(name) or j != len(typed):
            return False
        return True