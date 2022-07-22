class Solution:
    
    #Function to check if two strings are isomorphic.
    def areIsomorphic(self,str1,str2):
        if len(str1)!=len(str2):
            return 0
        dick1 = {}
        dick2 = {}
        for i,j in zip(str1, str2):
            dick1[i]=j
            dick2[j]=i
        for i,j in zip(str1, str2):
            if dick1[i]!=j or dick2[j]!=i:
                return 0
        return 1