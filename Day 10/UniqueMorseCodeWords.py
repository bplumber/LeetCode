class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        st = set()
        for i in words:
            tp = ""
            for j in i:
                tp+=morse[ord(j)-97]
            st.add(tp)
        return len(st)
                