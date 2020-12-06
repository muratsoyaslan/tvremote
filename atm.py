bakiye = 1000
while True:
    islem= input("İşlemi seçiniz:")
    if(islem == "q"): 
       print("Yine Bekleriz")
       break
    elif (islem=="1"):
       print("Bakiyeniz {} tl dir".format(bakiye))
    elif (islem=="2"):   
       miktar = int(input("Miktarı giriniz:"))
       bakiye += miktar
    elif (islem=="3"):
       miktar = int(input("Miktarı giriniz:"))
       if (bakiye-miktar<0 ):
        print("Böyle bir miktar çekemezsiniz")
        continue
       bakiye -= miktar
    else:
       print("geçersiz işlem")