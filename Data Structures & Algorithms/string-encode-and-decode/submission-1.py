class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            n = len(strs[i])
            new =str(n)+"#"+strs[i]
            encoded_string+=new
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        start = 0
        while start < len(s):
            i = start
            while s[i]!='#':
                i += 1
            
            l=int(s[start:i])
            decoded_strs.append(s[i+1:i+l+1])
            start = i+l+1
               
        return decoded_strs
                
                

