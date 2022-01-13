import pprint
q1=[[i*10+j for j in range(10,0,-1)]for i in range(9,-1,-1)]
pprint.pprint(q1)


q2=[[1 if i==j or i+j ==4 else 0 for j in range(5)]for i in range(5)]
pprint.pprint(q2)


q3=[[i*10 -j*10 for j in range(10)] for i in range(10)]
pprint.pprint(q3)


q4=[[1 if i== j else 2 if j<i else 0 for j in range(5)] for i in range(5)]
pprint.pprint(q4)


q5=[[i+1 if i==j else 0 for j in range(4)]for i in range(4)]
pprint.pprint(q5)


q6=[[i+j for j in range(9)]for i in range(60,100,10)]
pprint.pprint(q6)


q7=[[i*j for j in range(1,10)] for i in range(1,10)]
pprint.pprint(q7)


q8=[[3 if i==1 and j==1 else 7 for j in range(3)]for i in range(3)]
pprint.pprint(q8)


q9=[[i*j for j in range(1,10)]for i in range(3,10,2)]
pprint.pprint(q9)


q10=[[i+j*2 for j in range(5)]for i in range(2,0,-1)]
pprint.pprint(q10)


q11=[['*' if i%2==0 and j%2!=0 else '_'for j in range(10)]for i in range(10)]
pprint.pprint(q11)


q12=[[i**2+j for j in range(10)]for i in range(10)]
pprint.pprint(q12)


q13=[[i - j for j in range(i)]for i in range(10,0,-1)]
pprint.pprint(q13)
        
