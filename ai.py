import random #angka random
import math #untuk rumus matematika

def fungsi(x1,x2): #rumus yyang ada di soal
    return -1*math.fabs(math.sin(x1)*math.cos(x2)*math.exp
            (math.fabs(1-(math.sqrt((x1*x1)+(x2*x2))/math.pi))))

def akurasi(fa): #rumus akurasi
    return (1-(math.fabs((fa-19.1365)/19.1365)))*100

#init first
x1,x2 = random.uniform(-10,10),random.uniform(-10,10)
solusiSementara = fungsi(x1,x2) #percobaan awal sebelum looping
best = solusiSementara #variabel penampung hasil terbaik
T = 1000 #inisiasi variable T (suhu)
Tmin = 1 #T minimal
a = 0.997 #nilai alpa

while(T>Tmin): #sampai konvergensi yang diinginkan
    x1,x2 = random.uniform(-10,10),random.uniform(-10,10)
    solusi = fungsi(x1,x2) #solusi yg dipecahkan dalam T waktu
    dSolusi = solusi - solusiSementara #penampung fungsi evaluasi (cost function)
    if(dSolusi< 0): #jika cost function <0
        solusiSementara = solusi  #inisiasi
        if(best > solusiSementara): #jika nilai minimum terbaik lebih besar
            best = solusiSementara #inisiasi variabel best dengan solusi semetara
            print(T)
            print("x1: ",x1," x2: ",x2)
            print(best)
            print(akurasi(best),"%")
    else:
        probability = math.exp(1)**(-(dSolusi))/T #2.71828 = e
        if (probability >=random.random()):
            solusiSementara = solusi
    T *=a
print("Best So far: ")
print("x1: ",x1," x2: ",x2)
print(best)
print(akurasi(best),"%")
