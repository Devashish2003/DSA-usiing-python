def lengthOfLastWord(self, s: str) -> int:
    s = s.strip()
    if ' ' not in s:
        return len(s)

    f = s.rfind(' ')
    sub = s[f + 1:]
    return len(sub)