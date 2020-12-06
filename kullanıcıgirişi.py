sys_kullanıcı_adı="Murat"
sys_parola= "12345"

kullanıcı_adı= input("kullanıcı adı:")
parola= input("parola:")

if (kullanıcı_adı==sys_kullanıcı_adı and parola != sys_parola):
 print("Parola Hatalı fırata sor")
elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
 print("Kullanıcı adı Hatalı")
else: 
 print("Aferin la başarılı giriş")
