def lengthOfLastWord(self, s: str) -> int:
    s = s.strip()
    if ' ' not in s:
        return len(s)

    c = 0
    for char in s[::-1]:
        if char == ' ':
            break
        c += 1
    return c