s = "the sky is blue"
turnS = s[::-1]
word = ""
words = ""
for j,i in enumerate(turnS):
    print (j,i)
    if i!=" " and word!="" and turnS[j-1]==" ":
        words += (word + " ")
        word = i
    elif i!=" ":
        word = i + word
    else:
        continue
words += word
print (words)
