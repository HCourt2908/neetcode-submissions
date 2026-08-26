class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for x in strs:
            length_prefix = '{:4}'.format(len(x))
            string += (length_prefix + x)
        return string

    def decode(self, s: str) -> List[str]:
        strings = list()
        length = 0
        i = 0
        while i < len(s):
            length = int(s[i: i + 4])
            i+=4
            strings.append(s[i: i + length])
            i += length

        return strings
