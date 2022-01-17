x=['ABC']
y=[input()]
print(x[0]==y[0]) #True
print(id(x[0])==id(y[0])) #False
y=x
y[0]='XYZ'
print(x[0])

x=['ABC']
y=['ABC']
print(x[0]==y[0]) #True
print(id(x[0])==id(y[0])) #True 同じ文字列は同じ住所を指すから
y=x
y[0]='XYZ'
print(x[0])


A='XYZ'
B=input()
print(A==B) #True
print(id(A)==id(B)) #False
