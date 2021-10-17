def isEmpty(s):
    if len(s)==0:
        return True
    else:
        return False

def push(s,item):
    s.append(item)
    top=len(s)-1
    
def pop(s):
    if isEmpty(s):
        return 'Underflow occurs'
    else:
        val=s.pop()
        if len(s)==0:
            top=None
        else:
            top=len(s)-1
        return val

def peek(s):
    if isEmpty(s):
        return 'Underflow occurs'
    else:
        top=len(s)-1
        return s[top]
    
def show(s):
    if isEmpty(s):
        print('no item found')
    else:
        t=len(s)-1
        print('(TOP)',end='')
        while(t>=0):
            print(s[t],'<==',end='')
            t=t-1
        print()

s=[]
top=None
while True:
    print('****** STACK IMPLEMENTATION USING LIST ******')
    print('1: PUSH')
    print('2: POP')
    print('3: PEEK')
    print('4: Show')
    print('0: Exit')
    ch=int(input('Enter choice:'))
    if ch==1:
        val=int(input('Enter no to push:'))
        push(s,val)
    elif ch==2:
        val=pop(s)
        if val=='Underflow':
            print('Stack is empty')
        else:
            print('\nDeleted item is:',val)
    elif ch==3:
        val=peek(s)
        if val=='Underflow':
            print('Stack is empty')
        else:
            print('\nTop item is:',val)
    elif ch==4:
        show(s)
    elif ch==0:
        print('Bye')
        break