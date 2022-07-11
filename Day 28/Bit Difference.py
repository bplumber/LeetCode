class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self,a,b):
        ct = 0
        while a or b:
            if a%2!=b%2:
                ct+=1
            a = int(a/2)
            b = int(b/2)
        return ct