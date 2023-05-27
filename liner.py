"""
matris toplamı cıkarma carpma                                           tamam
skaler sayı carpma                                                      tamam
A verilip simetrik metris cıkarma  aynı sek. ters simetrik metris cıkarma
özel carpma kısımları 
sıfır ve birim matris                                                   tamam
matrisin tersi alma
cıkıs taplo seklinde olacak                                             tamam

"""
import numpy as np

A=[#4X3
    [1,1,1],
    [1,1,1],
    [1,1,1],
    [1,1,1]
  
]
B=[#2X3
    [9,8,7],
    [6,5,4],
    [6,5,4],
    [6,5,4],


]
def show(C):
    if isinstance(C, list):
        for i in range(len(C)):
            for j in range(len(C[0])):
                print(C[i][j],end=" ")
            print("\n")
    else:
        print(C)

def topla(A,B):
    ara=[]
    C=[]
    top=0
    satırA=len(A)#3
    sutunA=len(A[0])#3
    satırB=len(B)
    sutunB=len(B[0])
    if satırA==satırB and sutunA==sutunB:
        for i in range(0,satırA):#3
            for j in range(0,sutunA):#3
                top=A[i][j]+B[i][j]
                ara.append(top)
                top=0
            C.append(ara)
            ara=[]
        #print(C)
        return C  
    else:
        return "satır yada sutunlar aynı degil"      
    
def Cikar(A,B):
    ara=[]
    C=[]
    top=0
    satırA=len(A)#3
    sutunA=len(A[0])#3
    satırB=len(B)
    sutunB=len(B[0])
    if satırA==satırB and sutunA==sutunB:
        for i in range(0,satırA):#3
            for j in range(0,sutunA):#3
                top=A[i][j]-B[i][j]
                ara.append(top)
                top=0
            C.append(ara)
            ara=[]
        #print(C)
        return C  
    else:
        return "satır yada sutunlar aynı degil"      

def skaler_carpma(x,A):
    satırA=len(A)
    sutunA=len(A[0])
    ara=[]
    top=0
    C=[]
    for i in range(satırA):
        for j in range(sutunA):
            top=x*A[i][j]
            ara.append(top)
            top=0
        C.append(ara)
        ara=[]
    return C

def Carpma(A,B):
    ara=[]
    C=[]
    top=0
    satırA=len(A)#3
    sutunA=len(A[0])#3
    satırB=len(B)
    sutunB=len(B[0])
    if sutunA==satırB:
        for i in range(satırA):#3     i 2  j 2
            for j in range(sutunB):#3
                top=A[i][0]*B[0][j]
                top=top+A[i][1]*B[1][j]
               # print("satır: ",str(i) +" sutun: ",str(j) )
                ara.append(top)
                top=0
            C.append(ara)
            ara=[]
        return C
    else:
        return "satır sutun aynı degil "

def sifir(X,Y):
    C=np.zeros((X,Y),dtype=int)
    return  C

def birim(X):
    C=np.identity(X,dtype=int)
    return C

def hademad_carp(A,B):
    ara=[]
    C=[]
    top=0
    satırA=len(A)#3
    sutunA=len(A[0])#3
    satırB=len(B)
    sutunB=len(B[0])
    if satırA==satırB and sutunA==sutunB:
        for i in range(0,satırA):#3
            for j in range(0,sutunA):#3
                top=A[i][j]*B[i][j]
                ara.append(top)
                top=0
            C.append(ara)
            ara=[]
        #print(C)
        return C  
    else:
        return "satır yada sutunlar aynı degil"  

def kroneker_carp(A,B):# gosterimi pek anlaşılır degil dogru calısıyor 
    satırA=len(A)#3
    sutunA=len(A[0])#3
    satırB=len(B)
    sutunB=len(B[0])
    ara=[]
    C=[]
    for i in range(0,satırA):#3
        for j in range(0,sutunA):#3
            top=skaler_carpma(A[i][j],B)
            ara.append(top)
            show(ara)
            exit()
            top=0
        C.append(ara)
        ara=[]
    return C

def tranpoz(A):
    satırA=len(A)#X 4
    sutunA=len(A[0])#Y 3
    C=sifir(sutunA,satırA) # 3X4
    for i in range(satırA):
        for j in range(sutunA):
            C[j][i]=A[i][j]
    return C





#result=topla(A,B)
#result=Cikar(A,B)
#result=skaler_carpma(-2,B)
#result= Carpma(A,B)
#C=sifir(4,3)
#C=birim(3)
#result=hademad_carp(A,B)
#result=kroneker_carp(A,B)
result=tranpoz(B)
show(result)



