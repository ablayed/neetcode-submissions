class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word            # length, then the word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0                                    # where the next length starts
        while i < len(s):
            j = i
            while s[j] != "#":                   # move j to the "#"
                j += 1
            length = int(s[i:j])                   # the digits between i and j
            word = s[j + 1 : j+1+length]               # exactly `length` characters after the "#"
            res.append(word)
            i = j+1+length                             # jump to the start of the next length
        return res