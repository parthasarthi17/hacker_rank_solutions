import inflect
h=int(input())
m=int(input())
if m>=0 and m<=30:
    if m==0:       
        print("o' clock")
    elif m==15:
        print("quater past",end=" ")
    elif m==30:
        print("half past",end=" ")
    else:
        k=inflect.engine()
        words=k.number_to_words(m)
        print(words,"minutes past",end=" ")
    if h<=12:
        p=inflect.engine()
        words=p.number_to_words(h)
        print(words)
elif m>30 and m<=59:
    if m==45:
        print("quater to",end=" ")
    else:
        k=inflect.engine()
        words=k.number_to_words(60-m)
        print(words,"minutes to",end=" ")
    if h<=12:
        p=inflect.engine()
        words=p.number_to_words(h+1)
        print(words)