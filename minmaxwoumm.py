#for maximum value without using min max
#for max
t=(1,7,8,11,9,3,65)
ma=t[0]
for i in t:
    if (ma<i):
        ma=i
print ("max= ",ma)

#for min
t=(1,7,8,11,9,3,65)
ma=t[0]
for i in t:
    if (ma>i):
        ma=i
print ("min= ",ma)



#another method
#for max
t=(1,7,8,11,9,3,65)
ma=t[0]
for i in range (1, len (t)):
    if (ma<t[i]):
        ma=t[i]
print("max: ",ma)

#for min
t=(1,7,8,11,9,3,65)
ma=t[0]
for i in range (1, len (t)):
    if (ma>t[i]):
        ma=t[i]
print("min: ",ma)
