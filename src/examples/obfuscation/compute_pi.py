import string

def pi(x):
    _ = [0] * 10000

    a = ['@!&ABCDE?FG','_[999','_[998','(_)','while ','\n','\t',
         'return string.join','.append(str','99','.insert','for i in[']
    b = "*A@8]&:_[?77]&BCA_[?70]&:_[?71]&BC!7]F(1,'.')BCD(!7],'')
        $-!6]<!1]$*G?72,?74,?78,?75,?76,?73]:_[i]&$"\
        "*!9],!5]=0,!2]$*!6]+=1$*A@8]&:!0]&$*if !4]==10:_[?79]&$*if !6]:
        !7]E(@1]))$*_[@5]&],!5]=@4]&$*@1]=!4"\
        "]BC!4]=!3]+(!9]/10)BC!3]=!9]%10$*@1],!4]=@1]+1,0$*@0]=@9]&BC!9]=@3]&
        BC_[@5]&]=@2]&BC!5]=@5]&$x$(!1]"\
        "*10)/3$0$0$!2]$0$[]$2$0$0$0$-@0]%@7](_,!5])$-@0]/@7](_,@6]&)$-(!8],@5]
        &)$-!5]-1$-!5]$-x*!8]-1$-!5]>"\
        "0$-_[!5]-1]*10+(!9]*@6]&)"

    c={}
    for i in range(256):c[chr(i)]=chr(i)
    for i in range(1,len(a)):c[a[0][i-1]]=a[i]
    b = string.join(map(lambda x,_=c:_[x],list(b)),'').split('$')
    r = len(_)-len(b)
    for i in range(r,len(_)):
        _[1],_[2],_[3],=b[i-r],"def f%d(_,x=%d):\n\t"%(i,x),"f%d"%i
        if _[1][0]=='-':exec(_[2]+"return %s\n"%(_[1][1:]))
        elif _[1][0] == '*':exec(_[2]+"%s\n"%(_[1][1:]))
        else: _[3]=b[i-r]
        _[i]=eval(_[3])

    return _[9969](_)

# prints PI to the selected number of digits - for example: 20
print "PI=",pi(20)
