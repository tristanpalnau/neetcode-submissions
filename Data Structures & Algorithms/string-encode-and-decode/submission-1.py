class Solution:

    def encode(self, strs: List[str]) -> str:
        conc = ""
        for s in strs:
            conc += f"{len(s)}#{s}"
        return conc
                    

    def decode(self, s: str) -> List[str]:
        msgs = []
        i = 0
        while i < len(s):
            pos = s.find('#', i)
            length = int(s[i:pos])
            msgs.append(s[pos+1:pos+1+length])
            i = pos + length + 1
        return msgs