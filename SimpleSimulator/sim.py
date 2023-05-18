import matplotlib.pyplot as plt
from fun import *

reg = {
    "000":0,
    "001":0,
    "010":0,
    "011":0,
    "100":0,
    "101":0,
    "110":0,
    "111":"0000000000000000"}

def intToBin(num):
    return str(bin(num)).replace("0b","")

def prntReg(dump,reg,pc):
    p = str(bin(pc)).replace("0b","")
    for i in range(len(p),8):
        p = "0" + p
    print(p,end=" ")
    for r in list(reg.values())[:7]:
        n = intToBin(r)
        for i in range(len(n),16):
            n = "0" + n
        print(n,end=" ")
    print(list(reg.values())[-1],end="\n")
    dump.append(pc)

def get_inp():
    cmds = {}
    i = 0
    while True:
        try:
            line = input()
            if line == "":
                break
            cmds[i] = line
            i += 1
        except:
            break
    return cmds

def resetFlag(regD):
    regD["111"] = "0000000000000000"

def getPrntVar(varS):
    ls = []
    rVars = {}
    for i in list(varS.keys()):
        ls.append(binaryToDecimal(int(i)))
    for i in sorted(ls):
        temp = intToBin(i)
        for j in range(len(temp),8):
            temp = "0" + temp
        rVars[i] = varS[temp]
    return rVars


cmds = get_inp()
varS = {}
dump = []
isHalted = False
pc = 0
counter  = 0


while(not isHalted):

    ## Type A   -> 2 unused
    if (cmds[pc][:5] == "00000"):
        resetFlag(reg)
        add(reg,cmds[pc][7:10],cmds[pc][10:13],cmds[pc][13:],"111")
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "00001"):
        resetFlag(reg)
        sub(reg,cmds[pc][7:10],cmds[pc][10:13],cmds[pc][13:],"111")
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "00110"):
        resetFlag(reg)
        mul(reg,cmds[pc][7:10],cmds[pc][10:13],cmds[pc][13:],"111")
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "01010"):
        resetFlag(reg)
        xor(reg,cmds[pc][7:10],cmds[pc][10:13],cmds[pc][13:])
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "01011"):
        resetFlag(reg)
        Or(reg,cmds[pc][7:10],cmds[pc][10:13],cmds[pc][13:])
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "01100"):
        resetFlag(reg)
        And(reg,cmds[pc][7:10],cmds[pc][10:13],cmds[pc][13:])
        prntReg(dump,reg,pc)
        pc += 1

    ## Type B
    elif (cmds[pc][:5] == "01001"):
        resetFlag(reg)
        leftShift(reg,cmds[pc][5:8],cmds[pc][8:])
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "01000"):
        resetFlag(reg)
        rightShift(reg,cmds[pc][5:8],cmds[pc][8:])
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "00010"):
        resetFlag(reg)
        movImm(reg,cmds[pc][5:8],cmds[pc][8:])
        prntReg(dump,reg,pc)
        pc += 1

    ##Type C
    elif (cmds[pc][:5] == "00011"):
        mov(reg,cmds[pc][10:13],cmds[pc][13:])
        resetFlag(reg)
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "00111"):
        resetFlag(reg)
        divide(reg,cmds[pc][10:13],cmds[pc][13:])
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "01101"):
        resetFlag(reg)
        Invert(reg,cmds[pc][10:13],cmds[pc][13:])
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "01110"):
        resetFlag(reg)   
        cmp(reg,cmds[pc][10:13],cmds[pc][13:])
        prntReg(dump,reg,pc)
        pc += 1

    ##Type D
    elif (cmds[pc][:5] == "00100"):
        if (cmds[pc][8:] not in varS.keys()):
            varS[cmds[pc][8:]] = 0;
            Load(cmds[pc][5:8],reg,cmds[pc][8:],varS)
        else:
            Load(cmds[pc][5:8],reg,cmds[pc][8:],varS)
        resetFlag(reg)
        prntReg(dump,reg,pc)
        pc += 1
    elif (cmds[pc][:5] == "00101"):
        if (cmds[pc][8:] not in varS.keys()):
            varS[cmds[pc][8:]] = 0;
            Store(cmds[pc][5:8],reg,cmds[pc][8:],varS)
        else:
            Store(cmds[pc][5:8],reg,cmds[pc][8:],varS)
        resetFlag(reg)
        prntReg(dump,reg,pc)
        pc += 1

    ##Type E
    elif (cmds[pc][:5] == "01111"):
        temp = Uncodition_Jump(cmds[pc][8:])
        resetFlag(reg)
        prntReg(dump,reg,pc)
        pc = temp
    elif (cmds[pc][:5] == "10000"):
        temp = Jump_if_less(reg,cmds[pc][8:],pc)
        resetFlag(reg)
        prntReg(dump,reg,pc)
        pc = temp
    elif (cmds[pc][:5] == "10001"):
        temp = Jump_if_greater(reg,cmds[pc][8:],pc)
        resetFlag(reg)
        prntReg(dump,reg,pc)
        pc = temp
    elif (cmds[pc][:5] == "10010"):
        temp = Jump_if_Equal(reg,cmds[pc][8:],pc)
        resetFlag(reg)
        prntReg(dump,reg,pc)
        pc = temp

    #Type F
    elif (cmds[pc][:5] == "10011"):
        isHalted = True
        resetFlag(reg)
        prntReg(dump,reg,pc)
        pc += 1
    counter += 1

intVars = getPrntVar(varS)

for i in range(0,256):
    if i < len(cmds):
        print(cmds[i])
    elif i >= len(cmds) and i in list(intVars.keys()):
        tempBin = intToBin(intVars[i])
        for i in range(len(tempBin),16):
            tempBin = "0" + tempBin
        print(tempBin)
    else:
        print("0000000000000000")


plt.scatter(range(0,counter),dump,c = "blue")
plt.title("mem_addr vs cycle")
plt.xlabel("cycle number")
plt.ylabel("mem_addr")
plt.savefig('plot.png',dpi=300,bbox_inches='tight')

