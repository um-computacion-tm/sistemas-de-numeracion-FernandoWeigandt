#Pasaje de Decimal a Cualquier Base

def baseChanger_dec_all(num,base):
    s = ''
    s_new= ''
    while num>0:
        resto=num%base
        if resto>9:
            resto = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}.get(resto)
        s += str(resto)
        num=num//base
    s_new=s[::-1]
    return s_new    

def baseChanger_dec_bin(num):
    return baseChanger_dec_all(num,2)

def baseChanger_dec_hex(num):
    return baseChanger_dec_all(num,16)

def baseChanger_dec_oct(num):
    return baseChanger_dec_all(num,8)


#Pasaje de Cualquier Base a Decimal

def baseChanger_all_dec(num,base):
    s=[]
    dic_hex={'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
    cont=0
    for i in reversed(str(num)):
        if i in dic_hex.keys():
            i=dic_hex.get(i)
        s.append(int(i)*(base**cont))
        cont+=1
    return sum(s)

def baseChanger_bin_dec(num):
    return baseChanger_all_dec(num,2)

def baseChanger_hex_dec(num):
    return baseChanger_all_dec(num,16)

def baseChanger_oct_dec(num):
    return baseChanger_all_dec(num,8)


#Pasaje de Binario a Octal y Hexadecimal

def baseChanger_bin_oct_and_hex(num,base):
    num=str(num)
    if base==8:

        dic_bin = {"000": 0, "001": 1, "010": 2, "011": 3, "100": 4, "101": 5, "110": 6, "111": 7}
        if len(num)%base==0:
            for i in range(0,len(num),base):
                if i in dic_bin.keys():
                    i=i.get(i)
                    i+=i
        else:
            print('casi')

    elif base==16:

        dic_bin = {"0000": 0, "0001": 1, "0010": 2, "0011": 3, "0100": 4, "0101": 5, "0110": 6, "0111": 7, "1000": 8, "1001": 9}
        if len(num)%base==0:
            for i in range(0,len(num),base):
                if i in dic_bin.keys():
                    i=i.get(i)
                    i+=i
        else:
            print('casi')
    return i

def baseChanger_bin_oct(num):
    return baseChanger_bin_oct_and_hex(num,8)

def baseChanger_bin_hex(num):
    return baseChanger_bin_oct_and_hex(num,16)

print(baseChanger_bin_oct(1010))