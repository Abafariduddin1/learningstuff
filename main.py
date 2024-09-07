#tuple
srt = ("red", "green", "blue", "yellow", "purple")
print(srt[0])
for i in srt:
    print(i)

#slicing
print(srt[:4])    

#sets
rtc= {}
print(type(rtc))
tre = set()
print(type(tre))
fct = {"car", "plane", "bike"}
print(fct)
qrt = {4,2,"car",5,1,}
print(qrt)

fct.add("Motorcycle")
fct.remove("car")
print(fct)

lyt = {1,2,3,4,5}
sfd = {4,5,6,7,8}
#union
print(lyt|sfd)
#intersection
print(lyt&sfd)
#difference
print(sfd-lyt)