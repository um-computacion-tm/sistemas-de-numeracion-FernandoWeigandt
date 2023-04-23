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
        s.append(int(i)(base*cont))
        cont+=1
    return sum(s)

def baseChanger_bin_dec(num):
    return baseChanger_all_dec(num,2)

def baseChanger_hex_dec(num):
    return baseChanger_all_dec(num,16)

def baseChanger_oct_dec(num):
    return baseChanger_all_dec(num,8)


#Pasaje de Binario a Octal y Hexadecimal

def baseChanger_bin_to_oct_and_hex(num,base):
    cadena_final= ''
    if base==8:
        dic_bin = {"000": '0', "001": '1', "010": '2', "011": '3', "100": '4', "101": '5', "110": '6', "111": '7'}
        salto=3
    elif base==16:
        dic_bin = {
            "0000": '0', "0001" : '1', "0010" : '2', "0011" : '3', "0100" : '4', "0101" : '5', "0110" : '6', "0111" : '7', "1000" : '8', "1001" : '9',
              '1010' : 'A', '1011' : 'B', '1100' : 'C', '1101' : 'D', '1110' : 'E', '1111' : 'F'}
        salto=4
    for i in range (0,len(str(num)),salto):
        num_3=str(num)[i:i+salto]
        if num_3 in dic_bin.keys():
            cadena_final+=str(dic_bin.get(num_3))

    return cadena_final

def baseChanger_bin_oct(num):
    return baseChanger_bin_to_oct_and_hex(num,8)

def baseChanger_bin_hex(num):
    return baseChanger_bin_to_oct_and_hex(num,16)


#Pasaje de Octal a Binario y Hexadecimal

def baseChanger_oct_to_bin_and_hex(num,base):
    cadena_final=''
    if base==2:
        dic={'0' : "000", '1' : "001", '2' : "010", '3' : "011", '4' : "100", '5' : "101" , '6' : "110", '7' : "111"}
        for i in str(num):
            if i in dic.keys():
                cadena_final+=str(dic.get(i))
    elif base==16:
        cadena_final=hex(num)
    return cadena_final

def baseChanger_oct_bin(num):
    return baseChanger_oct_to_bin_and_hex(num,2)

def baseChanger_oct_hex(num):
    return baseChanger_oct_to_bin_and_hex(num,16)

#ver oct to hex

#Pasaje de Hexadecimal a Binario y Octal

def baseChanger_hex_to_bin_and_oct(num,base):
    cadena_final=''
        
def baseChanger_hex_bin(num):
    return baseChanger_hex_to_bin_and_oct(num,2)

def baseChanger_hex_oct(num):
    return baseChanger_hex_to_bin_and_oct(num,8)