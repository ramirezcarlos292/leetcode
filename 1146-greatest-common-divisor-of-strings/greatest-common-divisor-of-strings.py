class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)

        greater = len1 if len1 > len2 else len2
    
        while True:
            if (greater % len1 == 0) and (greater % len2 == 0):
                lcm = greater
                break
            greater += 1
    
        gcd = int((len1 * len2) / lcm)

        str_gcd1 = str1[:gcd]*(int(len2/gcd))    
        str_gcd2 = str2[:gcd]*(int(len1/gcd))
        print(str_gcd1, str_gcd2)
        if ((str_gcd1 == str2) & (str_gcd2 == str1)):
            return str1[:gcd]
        else:
            return ""