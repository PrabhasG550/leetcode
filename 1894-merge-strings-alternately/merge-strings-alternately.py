class Solution(object):
    def mergeAlternately(self, word1, word2):
        #i need to append word1 index, then word2 index, repeat
        #edge case: if one of the words ends before the other, append the rest of other word
        #if both words run out of letters, return.
        wone, wtwo, final, = 0, 0, ""
        while wone < len(word1) and wtwo < len(word2):
            final = "".join([final, word1[wone]])
            wone += 1
            final = "".join([final, word2[wtwo]])
            wtwo += 1
            if wone >= len(word1):
                final = "".join([final, word2[wtwo:]])
            if wtwo >= len(word2):
                final = "".join([final, word1[wone:]])
        return final

        