# -*- coding: cp1254 -*-
alf=[["A","B","C","�","D","E"],["F","G","�","H","I","�"],["J","K","L","M","N","O"],["�","P","R","S","�","T"],["U","�","V","Y","Z"," "],[".",",","?","!",":",";"]]                        
def Sifrele(metin):
    result=""
    for k in metin:
        for i in range(len(alf)):
            for j in range(len(alf[i])):
                if k.upper()==alf[i][j]:
                    result+=str(i+1)+str(j+1)
    return(result)
            
def Coz(metin):
    metin=str(metin)
    result=""
    for i in range(len(metin)):
        if i%2==0:
            result+=alf[int(metin[i])-1][int(metin[i+1])-1]
    return(result)
def main():
    while True:
        try:
            command=input("�ifrele/��z (S/C):").lower()
            if command=="s":
                girdi=input("�ifrelenecek Metin:")
                print(Sifrele(girdi))
            elif command=="c":
                girdi=input("��z�lecek Kombinasyon:")
                print(Coz(girdi))
            else:
                print("�ifrelemek i�in 's' ��zmek i�in 'c' yaz�n�z.")
        except:
            print("�ifrelemek i�in 's' ��zmek i�in 'c' yaz�n�z.")
    return 0
main()
print(Coz(Sifrele("merhaba")))
