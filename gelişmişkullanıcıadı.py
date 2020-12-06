sys_kullanıcı_adı="Murat"
sys_parola="12345"
giris_hakkı=3

while True:
    kullanıcı_adı=input("Kullanıcı adı:")
    parola=input("Parola:")
    if(kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı adı hatalı")
        giris_hakkı -= 1
    elif(kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola): 
        print("Parola Hatalı...")
        giris_hakkı -= 1
    elif(kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı adı ve Parola Hatalı") 
        giris_hakkı -= 1
    else:
        print("Sisteme başarıyla giriş yapıldı")
        break
    if (giris_hakkı == 0 ):
        print("giriş hakkınız bitti")
        break
      


           