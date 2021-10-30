def isEmpty(Arr):
    if len(Arr)==0:
        return True
    else:
        return False

def push(Arr,item):
    Arr.append(item)
    top=len(Arr)-1
    
def pop(Arr):
    if isEmpty(Arr):
        return 'Underflow occurs'
    else:
        val=Arr.pop()
        if len(Arr)==0:
            top=None
        else:
            top=len(Arr)-1
        return val
 
def show(Arr):
    if isEmpty(Arr):
        print('no item found')
    else:
        t=len(Arr)-1
        print('(TOP)',end='')
        while(t>=0):
            print(Arr[t],'<==',end='')
            t=t-1
        print()

Arr=[]
top=None
while True:
    print('****** STACK IMPLEMENTATION USING LIST ******')
    print('1: PUSH')
    print('2: POP')
    print('3: Show')
    print('0: Exit')
    ch=int(input('Enter choice:'))
    if ch==1:
        val=int(input('Enter no to push:'))
        push(Arr,val)
    elif ch==2:
        val=pop(Arr)
        if val=='Underflow':
            print('Stack is empty')
        else:
            print('\nDeleted item is:',val)
    
    elif ch==3:
        show(Arr)
    elif ch==0:
        print('Bye')
        break