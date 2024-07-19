print("------postfixevaluation------")
output=[]
operator=[]
exp=input("enter an expression")
for i in exp:
    if (i!='+' and i!='-' and i!='*' and i!='/'):
        operator.append(i)
    else:
        if len(operator)>1:
            ele1=int(operator.pop())
            ele2=int(operator.pop())
            if i=='+':
                ele3=ele2+ele1
            if i=='-':
                ele3=ele2-ele1
            if i=='*':
                ele3=ele2*ele1
            if i=='/':
                ele3=ele2/ele1
            operator.append(ele3)
print(operator)
                
                
            
            
