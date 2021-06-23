class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s==t):
            return(1)

        s_p=0
        t_p=0
        t_str=''
        while(s_p<len(s) and t_p<len(t)):
            if(s[s_p]==t[t_p]):
                t_str+=s[s_p]
                s_p+=1
                t_p+=1
            else:
                t_p+=1
        return(s==t_str)
        