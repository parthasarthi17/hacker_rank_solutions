def pangram(s):
   s=s.lower()
   a=set(s)
   print(a) 
   if len(a)==27:
        return "pangram"
   else :
        return "not pangram"
    
    
    
s=input()#Enter string
print(pangram(s))
