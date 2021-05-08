s='syeda nusrat khaledur'
t= list(s)
print (t)
p=s.split()
print(p)
a='spam-spam-spam'
delimiter='-'
print(a.split(delimiter))
b=['join','is','the','inverse','of','split']
delimiter=' '
print (delimiter.join(b))
l= 'navan'
w=l[::-1]
print (w)
if l==w:
    print('palindrom')

else :
    print('not palindrom')

str1=input()
str2=reversed(str1)
if list(str1)==list(str2):
     print('palindrom')
else :
    print('not palindrom')

r='mist cse-15 mirpur dhaka'
print(r[::-1])
a = "i love bangladesh"
print( " ".join(a.split()[::-1]))
s='The dog ran'
print(' '.join(w[::-1] for w in s.split()))





