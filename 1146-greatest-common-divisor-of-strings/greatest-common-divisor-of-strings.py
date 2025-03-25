class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        #check if the number has a nonzero gcd
        if str1 + str2 != str2 + str1:
            return ""

        #find the gcd of the length
        max_length = self.gcd(len(str1), len(str2))
        return str1[:max_length]

    def gcd(self, a, b):
        if(b == 0):
            return abs(a)
        else:
            return self.gcd(b, a%b)
