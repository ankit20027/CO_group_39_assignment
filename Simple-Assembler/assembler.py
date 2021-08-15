# Ankit Chaurasia -> 2020027
# Ronit Mehta -> 2020539
# Mithun -> 2020522

from fun import *

def is_alpha(st):
    s = st.split('_')
    boo = True
    for i in s:
        if i != '':
            boo = boo & i.isalnum()
    return boo

def get_inp():
    cmds = {}
    i = 0
    var = {}
    j = 0
    labels = {}
    k = 1
    varRead = False
    while True:
        try :
            line = input()
            if line == '':
                pass
            elif line[:2] == '//':
                varRead = True
                pass
            elif line.split()[0] == "var":
                if len(line.split()) == 2 and is_alpha(line.split()[1]) and not varRead:
                    var[j] = line.split()[1]
                    j += 1
                else:
                    print(f"Invalid Syntax in line no. {k} X_X") ## error in defining the variable
                    exit()
            elif line.split()[0][-1] == ':':
                varRead = True
                if len(line.split()[0]) > 1:
                    if len(line.split()) > 1 and is_alpha(line.split()[0][:-1]):
                        cmds[i] = [line.split()[1:],k]          ## [ins array, line no(actual)]
                        labels[line.split()[0][:-1]] = i
                        i += 1
                    else:
                        print(f"Invalid Syntax in line no. {k} X_X")
                        exit()
                else:
                    print(f"Invalid Syntax in line no. {k} X_X")
                    exit()
            else:
                varRead = True
                cmds[i] = [line.split(),k]          ## [ins array, line no(actual)]
                i += 1
            k += 1
        except EOFError:
            break;
    return (cmds,var,labels)



def correctReg(reg):
    return reg in ["R0","R1","R2","R3","R4","R5","R6"]

def correctFlagReg(reg):
    return reg in ["R0","R1","R2","R3","R4","R5","R6","FLAGS"]

def correctImmd(num):
    try:
        if (num[0] == '$'):
            n = int(num[1:])
            return (n >= 0) and (n <= 255) and (n % 1 == 0)
        else:
            return False
    except:
        return False;

def correctVar(var, varDict):           ## dont return error for invalid syntax eg. var X Y Z -> None
    return var in list(varDict.values())    ## count var length also while defining the erro,

def correctLabel(label,labelDict):
    return label in list(labelDict.keys())

################################################################################################### change cmds[i] -> cmds[i][0]
def get_asm(i,cmds,var,labels,end,hlt_cnt):                  
# for i in cmds.keys():
    if hlt_cnt < 1:
        ## Type A
        if cmds[i][0][0] == "add" and len(cmds[i][0]) == 4:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]) and correctReg(cmds[i][0][3]):
                return(add(0,0,cmds[i][0][1],cmds[i][0][2],cmds[i][0][3])[1],hlt_cnt)
        
        if cmds[i][0][0] == "sub" and len(cmds[i][0]) == 4:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]) and correctReg(cmds[i][0][3]):
                return(sub(0,0,cmds[i][0][1],cmds[i][0][2],cmds[i][0][3],False)[1],hlt_cnt)
        
        if cmds[i][0][0] == "mul" and len(cmds[i][0]) == 4:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]) and correctReg(cmds[i][0][3]):
                return(mul(0,0,cmds[i][0][1],cmds[i][0][2],cmds[i][0][3],False)[1],hlt_cnt)
        
        if cmds[i][0][0] == "xor" and len(cmds[i][0]) == 4:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]) and correctReg(cmds[i][0][3]):
                return(xor(0,0,cmds[i][0][1],cmds[i][0][2],cmds[i][0][3])[1],hlt_cnt)
        
        if cmds[i][0][0] == "or" and len(cmds[i][0]) == 4:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]) and correctReg(cmds[i][0][3]):
                return(Or(0,0,cmds[i][0][1],cmds[i][0][2],cmds[i][0][3])[1],hlt_cnt)
        
        if cmds[i][0][0] == "and" and len(cmds[i][0]) == 4:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]) and correctReg(cmds[i][0][3]):
                return(And(0,0,cmds[i][0][1],cmds[i][0][2],cmds[i][0][3])[1],hlt_cnt)

        ## Type B
        if cmds[i][0][0] == "mov" and len(cmds[i][0]) == 3:
            if correctReg(cmds[i][0][1]) and correctImmd(cmds[i][0][2]):
                return(movImm(cmds[i][0][1],int(cmds[i][0][2][1:])),hlt_cnt)
            ## Type C
            elif correctReg(cmds[i][0][1]) and correctFlagReg(cmds[i][0][2]):
                return(mov(cmds[i][0][1],cmds[i][0][2]),hlt_cnt)
        
        if cmds[i][0][0] == "rs" and len(cmds[i][0]) == 3:
            if correctReg(cmds[i][0][1]) and correctImmd(cmds[i][0][2]):
                return(rightShift(cmds[i][0][1],1,int(cmds[i][0][2][1:])),hlt_cnt)
        
        if cmds[i][0][0] == "ls" and len(cmds[i][0]) == 3:
            if correctReg(cmds[i][0][1]) and correctImmd(cmds[i][0][2]):
                return(leftShift(cmds[i][0][1],1,int(cmds[i][0][2][1:])),hlt_cnt)
        
        ## Type C
        if cmds[i][0][0] == "div" and len(cmds[i][0]) == 3:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]):
                return(divide(cmds[i][0][1],cmds[i][0][2]),hlt_cnt)
        
        if cmds[i][0][0] == "not" and len(cmds[i][0]) == 3:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]):
                return(Invert(cmds[i][0][1],cmds[i][0][2]),hlt_cnt)
        
        if cmds[i][0][0] == "cmp" and len(cmds[i][0]) == 3:
            if correctReg(cmds[i][0][1]) and correctReg(cmds[i][0][2]):
                return(Compare(cmds[i][0][1],cmds[i][0][2]),hlt_cnt)
        
        ## Type D
        if cmds[i][0][0] == "ld" and len(cmds[i][0]) == 3:
            if correctReg(cmds[i][0][1]) and correctVar(cmds[i][0][2],var):
                for j in range(0,len(var)):
                    if var[j] == cmds[i][0][2]:
                        return(Load(cmds[i][0][1],end+j),hlt_cnt)
        
        if cmds[i][0][0] == "st" and len(cmds[i][0]) == 3:
            if correctReg(cmds[i][0][1]) and correctVar(cmds[i][0][2],var):
                for j in range(0,len(var)):
                    if var[j] == cmds[i][0][2]:
                        return(Store(cmds[i][0][1],end+j),hlt_cnt)
        
        ## Type E
        if cmds[i][0][0] == "jmp" and len(cmds[i][0]) == 2:
            if correctLabel(cmds[i][0][1],labels):
                return(Uncodition_Jump(labels[cmds[i][0][1]]),hlt_cnt)

        if cmds[i][0][0] == "jlt" and len(cmds[i][0]) == 2:
            if correctLabel(cmds[i][0][1],labels):
                return(Jump_if_less(labels[cmds[i][0][1]]),hlt_cnt)

        if cmds[i][0][0] == "jgt" and len(cmds[i][0]) == 2:
            if correctLabel(cmds[i][0][1],labels):
                return(Jump_if_greater(labels[cmds[i][0][1]]),hlt_cnt)

        if cmds[i][0][0] == "je" and len(cmds[i][0]) == 2:
            if correctLabel(cmds[i][0][1],labels):
                return(Jump_if_Equal(labels[cmds[i][0][1]]),hlt_cnt)
        
        ## Type F
        if cmds[i][0][0] == "hlt" and len(cmds[i][0]) == 1:
            hlt_cnt += 1
            return(Halt(),hlt_cnt)
        
        ## return None binary which results in error
        else:
            return(None,hlt_cnt)
    else:
        return(None,hlt_cnt)


def chk_code(labels,var,cmds,end):
    hlt_cnt = 0         # counts the number of times halt is called
    for i in cmds.keys():
        binary,hlt_cnt = get_asm(i,cmds,var,labels,end,hlt_cnt)
        if binary == None:
            print(f"Invalid Syntax in line no. {cmds[i][1]} X_X")
            return False
    return True

if __name__ == "__main__":
    cmds,var,labels = get_inp() # dict(cmds) containing all commands in order 0 to end  # dict(var) containing all vars in order 0 to end   # dict(labels) containing all labels in order 0 to end with their line no as values   
    end = len(cmds)

    if chk_code(labels,var,cmds,end):
        for i in cmds.keys():
            binary = get_asm(i,cmds,var,labels,end,0)[0]
            print(binary)
