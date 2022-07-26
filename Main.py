class postfix:
    def __init__(self):
        self.stack=[]
        self.maxsize=20
        self.top=-1

    def push(self, data):
        if(self.top==self.maxsize-1):

            print("Stack is full")
        else:
            self.top+=1
            self.stack.append(data)

    def pop(self):
        if(self.top==-1):
            print("Stack is empty")
        else:
            x=self.stack.pop()
            self.top-=1
            return x

ob=postfix()
data =[]

while True:
    c=input("Enter a char: ")
    if(c==""):

        break
    data.append(c)

for i in range(len(data)):
    if(data[i].isdigit()==True):
        ob.push(int(data[i]))
    elif(data[i]=="+"):
       a=ob.pop()
       b=ob.pop()
       result=b+a
       ob.push(result)
    elif(data[i]=="-"):
       a=ob.pop()
       b=ob.pop()
       result=b-a
       ob.push(result)
    elif(data[i]=="*"):
       a=ob.pop()
       b=ob.pop()
       result=b*a
       ob.push(result)
    elif(data[i]=="/"):
       a=ob.pop()
       b=ob.pop()
       result=b/a
       ob.push(result)
print("The result is: ",ob.stack[0])
