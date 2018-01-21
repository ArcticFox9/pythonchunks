# fibonacci secquence
print "Welcome"
#int1 is input
int1 = input("How far do you want to go?")

i=1
j=1
print(i)
print(j)
#loop
for u in range(1, int1):
  f=i+j
  print(f)
  i=j
  j=f
