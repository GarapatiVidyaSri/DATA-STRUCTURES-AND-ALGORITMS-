def isBalanced(s):
    output=[]
    #print("hi")
    for ch in s:
        #print("hiii")
        if ch=='{' or ch=='(' or ch=='[':
                #print("hiiiii")
                output.append(ch)
                print(output)
        elif ch=='}':
                if output[-1]=='{':
                 output.pop()
                else:
                 output.append(ch)
        elif ch==')':
                if output[-1]=='(':
                    output.pop()
                else:
                   output.append(ch)
        elif ch==']':
                if output[-1]=='[':
                  output.pop()
                else:
                 output.append(ch)
        print(output)
    if output==[]:
        print("YES")
    else:
        print("NO")
             
        
isBalanced("{[()]}")
isBalanced("{[(])}")
isBalanced("{{[[(())]]}}")
isBalanced("[]][{]{(({{)[})(}[[))}{}){[{]}{})()[{}]{{]]]){{}){({(}](({[{[{)]{)}}}({[)}}([{{]]({{")
""""

 h1=0
    h2=0
    while h1+h2<maxSum:
        a1=a[0]
        b1=b[0]
        i=0
        if a1<b1:
            h1=a1.pop()
            i+=1
        else:
            h2=b1.pop()
            i+=1
    return i"""
