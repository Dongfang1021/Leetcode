class Solution:
    def toHex(self, num: int) -> str:
        hex="0123456789abcdef" #created string for reference
        ot="" # created a string variable to store and update output string
        if num==0:
            return "0"
        elif num<0:
            num+=2**32
        while num:
            ot=hex[num%16]+ot # we update the output string with the reminder of num/16 , 16 because we are dealing with hex.
            num//=16 # now we are updating num by dividing it by 16 ***// operator used for floor division , means division will be always integer not float.
        return ot # then we simply return ot