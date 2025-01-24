class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = set("qwertyuiop")
        secondRow = set("asdfghjkl")
        thirdRow = set("zxcvbnm")
        result = []
        
        for word in words:
            word_set = word.lower()
            word_set = set(word_set)
            if len(word_set-firstRow) == 0 or len(word_set-secondRow) == 0 or len(word_set-thirdRow) == 0:
                result.append(word)
        
        return result