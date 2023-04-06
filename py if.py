nilai_mhs = [25,90,40,95,35,70,50,20,80,65]
print("nilai mhs : ",nilai_mhs)

print("=====================================")
print("+input angka 1 untuk nilai tertinggi+")
print("+input angka 2 untuk nilai terendah +")
print("=====================================")

nilai =int(input("input di sini : "))

if nilai <= 2:
    if nilai <= 1:
        print("nilai tertinggi = ",max(nilai_mhs))
   
    elif nilai <=2:
        print("nilai terendah = ",min(nilai_mhs))
    
else:
    print("yang anda inputkan salah")
   

