def isEmpty(Arr):
    if len(Arr)==0:
        return True
    else:
        return False

def push(Arr,item):
    if item%5==0:
        Arr.append(item)
        top=len(Arr)-1
    
def show(Arr):
    if isEmpty(Arr):
        print('No item found')
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
    print('2: Show')
    print('0: Exit')
    ch=int(input('Enter choice:'))
    if ch==1:
        val=int(input('Enter no to push:'))
        push(Arr,val)
    elif ch==2:
        show(Arr)
    elif ch==0:
        print('Bye')
        break