def begin():
    """开始函数"""
    radix=int(input())
    number=input().lower()
    step=0
    for i in range(31):
        decide=ifpalindrome(number)
        if decide==True:
            print("STEP="+str(step))
            break
        elif i<30 and decide==False:
            di_num=trans2num(radix,number)
            inv_di_num=trans2num(radix,getinverse(number))
            newnum=di_num+inv_di_num
            number=trans2str(radix,newnum)
            step+=1
        elif i==30 and decide==False: print('Impossible!')

def trans2str(radix,newnum):
    """得到对应进制数"""
    inv_str=''
    while newnum!=0:
        rad_str_num=newnum%radix
        newnum=int(newnum/radix)
        inv_str+=getradstr(rad_str_num)
    newstr=getinverse(inv_str)
    return newstr

def getradstr(rad_str_num):
    """从位数数字得到字符串"""
    if rad_str_num <10: return str(rad_str_num)
    elif rad_str_num==10:return 'a'
    elif rad_str_num==11:return 'b'
    elif rad_str_num==12:return 'c'
    elif rad_str_num==13:return 'd'
    elif rad_str_num==14:return 'e'
    elif rad_str_num==15:return 'f'
    elif rad_str_num==16:return 'g'
    elif rad_str_num==17:return 'h'
    elif rad_str_num==18:return 'i'
    elif rad_str_num==19:return 'j'

def trans2num(radix,number):
    """回文数转为十进制"""
    strlen=len(number)
    di_num=0
    for i in range(strlen):
        if number[i]>='a' and number[i]<'z':
            rad_num=getradnum(number[i])
        else: rad_num=int(number[i])
        di_num+=rad_num*pow(radix,strlen-1-i)
    return di_num

def getradnum(rad_str):
    """得到位数对应的数字"""
    if rad_str=='a':return 10
    elif rad_str=='b':return 11
    elif rad_str=='c':return 12
    elif rad_str=='d':return 13
    elif rad_str=='e':return 14
    elif rad_str=='f':return 15
    elif rad_str=='g':return 16
    elif rad_str=='h':return 17
    elif rad_str=='i':return 18
    elif rad_str=='j':return 19

def ifpalindrome(newstr):
    """决定是否是回文数"""
    strlen=len(newstr)
    decide= True
    for i in range(strlen):
        if newstr[i]!=newstr[strlen-1-i]:
            decide=False
    if decide== True: return True
    else: return False

def getinverse(number):
    """得到反十进制数"""
    strlen=len(number)
    newstr=''
    for i in range(strlen):
        newstr+=number[strlen-1-i]
    return newstr

begin()