def swap_case(s):
    new = ""
    for i in range(0, len(s)):
        if s[i].isupper():
            new += s[i].lower() #s.replace(s[i],s[i].lower())
        elif s[i].islower():
            new += s[i].upper() #s.replace(s[i], s[i].upper())
        else:
            new += s[i]
    #print(new)
    return new

s = input()
print(swap_case(s))