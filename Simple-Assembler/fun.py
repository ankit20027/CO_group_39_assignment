reg = {
    "R0":"000",
    "R1":"001",
    "R2":"010",
    "R3":"011",
    "R4":"100",
    "R5":"101",
    "R6":"110",
    "FLAGS":"111"
    }

def add(r1, r2, str1, str2, str3):
    res = r1 + r2 
    str = "00000" + "00" + reg[str1] + reg[str2] + reg[str3]
    return (res, str)

def sub(r1, r2, str1, str2, str3, flag):
    subt = r1 - r2
    if(subt<0):
        flag = True
    str = "00001" + "00" + reg[str1] + reg[str2] + reg[str3]
    return (subt, str)

def mul(r1, r2, str1, str2, str3, flag):
    res = r1*r2
    if(res>255):
        flag = True
    str = "00110" + "00" + reg[str1] + reg[str2] + reg[str3]
    return (res, str)


def xor(r1, r2, str1, str2, str3):
    res = r1^r2
    str = "01010" + "00" + reg[str1] + reg[str2] + reg[str3]
    return (res,str)


def Or(r1, r2, str1, str2, str3):
    res = r1 | r2
    str = "01011" + "00" + reg[str1] + reg[str2] + reg[str3]
    return (res,str)


def And(r1, r2, str1, str2, str3):
    res = r1 & r2
    str = "01100" + "00" + reg[str1] + reg[str2] + reg[str3]
    return (res,str)


def Invert(str1, str2):
    strf = "01101" + "00000" + reg[str1] + reg[str2]
    return strf


def divide(str1, str2):
    strf = "00111" + "00000" + reg[str1] + reg[str2]
    return strf


def mov(str1, str2):
    strf = "00011" + "00000" + reg[str1] + reg[str2]
    return strf


def movImm(str1, num):
    res = str(bin(num)).replace("0b","")
    n = len(res) #
    for i in range(n,8):
        res = "0" + res
    
    strf = "00010" + reg[str1] + res
    return strf


def binaryToDecimal(num):
    decimal = 0
    i = 0
    while(num != 0):
        dec = num % 10
        decimal = decimal + dec * pow(2, i)
        num = num//10
        i += 1
    return decimal 


def leftShift(str1, shiftBy, numberToBeShifted):
    sr1 = str(bin(numberToBeShifted)).replace("0b","")
    n1 = len(sr1)
    res = ""
    for i in range(0,8):
        if(i<shiftBy):
            res = res + "0"
        elif(i<n1+shiftBy):
            res = sr1[i-shiftBy] + res
        else:
            res = "0" + res
    val = binaryToDecimal(int(res))
    strf = "01001" + reg[str1] + res
    return (val, strf)


def rightShift(str1, shiftBy, numberToBeShifted):
    sr1 = str(bin(numberToBeShifted)).replace("0b","")
    res = sr1[shiftBy:]
    val = binaryToDecimal(int(res))
    n = len(res)
    for i in range(n, 8):
        res = "0" + res

    strf = "01000" + reg[str1] + res
    return (val, strf)



#############################################################
#BINARY CONVERSION
def decimalToBinary(n):
    bnr = bin(n).replace('0b','')
    x = bnr[::-1]
    while len(x) < 8:
        x += '0'
        bnr = x[::-1]

    return bnr

#LOAD TYPE-D
def Load(Reg , mem_add):
    op="00100"
    B_mem_add=decimalToBinary(mem_add)
    r=reg[Reg]
    ld=op+r+B_mem_add

    return ld

# STORE TYPE-D
def Store(Reg , mem_add):
    op="00101"
    B_mem_add=decimalToBinary(mem_add)
    r=reg[Reg]
    st=op+r+B_mem_add

    return st

#Unconditional Jump TYPE-E
def Uncodition_Jump(mem_add):
    op="01111"
    un_bit="000"
    B_mem_add=decimalToBinary(mem_add)
    uj=op+un_bit+B_mem_add

    return uj

#Jump If Less Than TYPE-E
def Jump_if_less(mem_add):
    op="10000"
    un_bit="000"
    B_mem_add=decimalToBinary(mem_add)
    jl=op+un_bit+B_mem_add

    return jl

#Jump If Greater Than TYPE-E
def Jump_if_greater(mem_add):
    op="10001"
    un_bit="000"
    B_mem_add=decimalToBinary(mem_add)
    jg=op+un_bit+B_mem_add

    return jg

#Jump If Equal TYPE-E
def Jump_if_Equal(mem_add):
    op="10010"
    un_bit="000"
    B_mem_add=decimalToBinary(mem_add)
    je=op+un_bit+B_mem_add

    return je

#halt TYPE-F
def Halt():
    op="10011"
    un_bit="00000000000"
    hlt=op+un_bit

    return hlt

#Compare Type-C
def Compare(Reg1 , Reg2):
    op="01110"
    un_bit="00000"
    r1=reg[Reg1]
    r2=reg[Reg2]
    cmp=op+un_bit+r1+r2
    
    return cmp

# #MAIN FUNCTION
# if _name_ == '_main_':
#     #print(Load("R1",20))
#     #print(Store("R3",90))
#     #print(Uncodition_Jump(20))
#     #print(Jump_if_less(20))
#     #print(Jump_if_greater(299))
#     #print(Jump_if_Equal(299))
#     #print(Halt())
#     #print(Compare("R1","R2"))
#     #print(decimalToBinary(0))