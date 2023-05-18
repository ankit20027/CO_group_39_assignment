def add(reg, str1, str2, str3, flag):
    res = reg[str2] + reg[str3]
    if(res>65535):        # 16 bit
        abc = reg[flag] 
        abc = abc[13:]
        reg[flag] = "000000000000"+"1"+abc
        reg[str1] = int(res % 65535)
        return
    reg[str1] = res

def sub(reg, str1, str2, str3, flag):
    subt =  reg[str2] - reg[str3]
    if(subt<0):
        abc = reg[flag] 
        abc = abc[13:]
        reg[flag] = "000000000000"+"1"+abc
        reg[str1] = 0
        return
    reg[str1] = subt

def mul(reg, str1, str2, str3, flag):
    r1 = reg[str2]
    r2 =  reg[str3]
    res = r1*r2
    if(res>65535):
        abc = reg[flag] 
        abc = abc[13:]
        reg[flag] = "000000000000"+"1"+abc
        reg[str1] = int(res % 65536)
        return
    reg[str1] = res


def xor(reg,str1, str2, str3):
    r1 = reg[str2]
    r2 =  reg[str3]
    res = r1^r2
    reg[str1] = res


def Or(reg, str1, str2, str3):
    r1 = reg[str2]
    r2 =  reg[str3]
    res = r1 | r2
    reg[str1] = res


def And(reg, str1, str2, str3):
    r1 = reg[str2]
    r2 =  reg[str3]
    res = r1 & r2
    reg[str1] = res


def Invert(reg, str1, str2):
    r1 = bin(reg[str2]).replace("0b","")
    res = ""
    for i in r1:
        if(i=="1"):
            res = res + "0"
        if(i=="0"):
            res = res + "1"
    res = binaryToDecimal(int(res))
    reg[str1] = res

    
def binaryToDecimal(num):
    decimal = 0
    i = 0
    while(num != 0):
        dec = num % 10
        decimal = decimal + dec * pow(2, i)
        num = num//10
        i += 1
    return decimal 


def divide(reg,str3, str4):
    r1 = reg[str3]
    r2 = reg[str4]
    quotient = int(r1/r2)
    remainder = r1%r2
    reg["000"] = quotient 
    reg["001"] = remainder


def mov(reg, str1, str2):
    if(str2=="111"):
        s = reg["111"]
        reg[str1] = binaryToDecimal(int(s))
        return
    reg[str1] = reg[str2]



def movImm(reg, str1, n):
    res = binaryToDecimal(int(n))
    reg[str1] = res


def leftShift(reg, str1, ImmediateString):
    numberToBeShifted = reg[str1]
    sr1 = str(bin(numberToBeShifted)).replace("0b","")
    shiftBy = binaryToDecimal(int(ImmediateString))
    n1 = len(sr1)
    res = ""
    for i in range(0,16):
        if(i<shiftBy):
            res = res + "0"
        elif(i<n1+shiftBy):
            res = sr1[i-shiftBy] + res
        else:
            res = "0" + res
    val = binaryToDecimal(int(res))
    reg[str1] = val


def rightShift(reg, str1, ImmediateString):
    numberToBeShifted = reg[str1]
    sr1 = str(bin(numberToBeShifted)).replace("0b","")
    shiftBy = binaryToDecimal(int(ImmediateString))
    n = len(sr1) - shiftBy
    res = ""
    if(n>0):
        res = sr1[0:n]
    else:
        res="0"
    
    n = binaryToDecimal(int(res))
    reg[str1] = n



def cmp(reg, str1, str2):
    r1 = reg[str1]
    r2 = reg[str2]
    flag = reg["111"]
    if(r1<r2):
        abc = flag[0:13]
        xyz = flag[14:]
        reg["111"] = abc + "1" + xyz
        return

    elif(r1>r2):
        abc =  flag[0:14]
        xyz = flag[15]
        reg["111"] = abc + "1" + xyz
        return

    elif(r1==r2):
        abc = flag[0:15]
        reg["111"] = abc +"1"
        return

###################################################
#BINARY TO INTEGER CONVERSION
def binaryToInteger(n):
    return int(n,2)

#LOAD TYPE-D
def Load(Reg , RegD , var , varD):

    RegD[Reg]=varD[var]

    return (RegD , varD)

# STORE TYPE-D
def Store(Reg , RegD , var , varD):

    varD[var]=RegD[Reg]

    return (RegD , varD)

#Unconditional Jump TYPE-E
def Uncodition_Jump(mem_add):
    
    mem_add=binaryToInteger(mem_add)
    
    return mem_add

#Jump If Less Than TYPE-E
def Jump_if_less(regD, mem_add, pc):
    
    if (regD["111"][-3] == "1"):
        mem_add=binaryToInteger(mem_add)
        return mem_add

    elif (regD["111"][-3] == "0"):
        return pc+1
    
    else:
        pass

#Jump If Greater Than TYPE-E
def Jump_if_greater(regD, mem_add , pc):

    if (regD["111"][-2] == "1"):
        mem_add=binaryToInteger(mem_add)
        return mem_add
        
    elif (regD["111"][-2] == "0"):
        return pc+1
    
    else:
        pass


#Jump If Equal TYPE-E
def Jump_if_Equal(regD,mem_add , pc):
   
    if (regD["111"][-1] == "1"):
        mem_add=binaryToInteger(mem_add)
        return mem_add
        
    elif (regD["111"][-1] == "0"):
        return pc+1
    
    else:
        pass
