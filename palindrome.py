from collections import deque
import copy

def palindrome (input_string):
    q = deque()
    visited = []
    answers = []
    q.append({"number": 0, "string":input_string})
    while q:
        a = q.pop()
        # print("Start", a, "q", q)
        x = a["string"]
        y = x[::-1]
        if x ==y:
            answers.append(x)
            continue
        num = a["number"]
        if num == 0:
            if not x[num] == y[num]:
                x = x + x[0]
                a["string"]=x
                a["number"]=num+1
                if a not in visited:
                    q.append(a)
            else:
                a["number"]=num+1
                q.append(a)
        else:
            if not x[num] == y[num]:
                b = copy.deepcopy(a)
                c = x[0:num]+y[num]+x[num:]
                d = y[0:num]+x[num]+y[num:]
                # print("c",c)
                # print("d",d)
                a["string"]=c
                a["number"]=num+1
                if a not in visited:
                    q.append(a)
                b["string"]=d
                b["number"]=num+1
                if b not in visited:
                    q.append(b)
            else:
                a["number"]=num+1
                q.append(a)
    answers.sort()
    smallest_answers = min(answers, key=len)
    return smallest_answers

    



# print("Answer", "abcdba", palindrome("abcdba"))
# print("Answer","abcbabba", palindrome("abcbabba"))
# print("Answer","acbabba", palindrome("acbabba"))
# print("Answer",palindrome("acbabb"))
# print("Answer",palindrome("acbzbb"))
# print("Answer",palindrome("zcyayy"))
# print("Answer",palindrome("abc"))

strings = ["some", "example", "words", "that", "i","j", "am", "fond", "of"]

print(sorted(strings, key=len)[0])

y = strings.sort()
x = min(y, key=len)
print(x)