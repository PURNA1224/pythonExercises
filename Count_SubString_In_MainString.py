'''count of no of times sub string repeated in a main string
    ex: ababab,ab - substring ab repeated 3 times in main string ababab'''
def count_substring(string, sub_string):
    s1_len = len(string)
    s2_len = len(sub_string)
    h = s1_len-s2_len
    count = 0
    i = 0
    j = s2_len
    while i<=h :
        if string[i:j] == sub_string:
            count += 1
        i += 1
        j += 1


    return count

s1 = input()
s2 = input()
print(count_substring(s1,s2))










