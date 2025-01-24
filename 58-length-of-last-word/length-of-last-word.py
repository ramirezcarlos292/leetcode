class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # get a list of words from input string
        list_words = s.split(' ')
        # get its length
        length = len(list_words)
        # go in reverse of list of words
        for i in range(length-1, -1, -1):
            # if last word length is higher than 0, is not an 
            # empty space string, return its value,
            # else continue iterating thru list in reverse order
            if len(list_words[i]) > 0:
                return len(list_words[i])
