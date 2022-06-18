class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        no_of_lines = 0
        last_line = 0
        temp = 0
        for i in s:
            temp+=widths[ord(i)-97]
            if temp>100:
                no_of_lines+=1
                temp=0
                temp+=widths[ord(i)-97]
        if temp!=0:
            no_of_lines+=1
            last_line = temp
        return [no_of_lines, last_line]
            