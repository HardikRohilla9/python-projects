def get_ans(a,b):
    if a==0:
        return 0
    if b==0:
        return 1
    if b==1:
        return a
    if b%2==0:
        return get_ans(a,b/2)**2
    else:
        return (get_ans(a,b//2)**2)*a
    
if __name__=='__main__':
    print('Please enter the values of a and b to get a^b')
    while 1:
        try:
            a=int(input('Enter a: '))
        except:
            continue
        else:
            break
    while 1:
        try:
            b=int(input('Enter b: '))
        except:
            continue
        else:
            break
    print(f'Answer in log(b) time complexity : {get_ans(a,b)}')
    
