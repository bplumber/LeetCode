class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punc = "!?',;."
        for i in paragraph:
            if i in punc:
                paragraph = paragraph.replace(i, " ")
        paragraph = paragraph.lower()
        paragraph = paragraph.split(" ")
        v_max = 0
        key = paragraph[0]
        dick = dict(Counter(paragraph))
        for k in dick:
            if dick[k]>v_max and k not in banned and len(k)!=0:
                v_max = dick[k]
                key = k
        return key