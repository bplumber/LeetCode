class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e','i','o','u', 'I', 'A', 'E', 'O', 'U']
        a = "a"
        lt = sentence.split(" ")
        for i in range(len(lt)):
            if lt[i][0] in vowels:
                lt[i] = str(lt[i])+("ma")
            else:
                lt[i] = str(lt[i][1:]) + str(lt[i][0]) + ("ma")
            lt[i] = str(lt[i])+a
            a+="a"
        return " ".join(lt)