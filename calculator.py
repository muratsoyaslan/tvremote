a= int(input("Birinci Sayı:"))
b= int(input("İkinci Sayı:"))

islem= (input("işlemi giriniz:"))

if islem == "1inci" :
   print("{} ile  {} in toplamı {} dır".format(a,b,a+b))
elif islem == "2nci":  
   print("{} ile  {} in farkı {} dır".format(a,b,a-b))
elif islem == "3üncü":   
   print("{} ile  {} in çarpımı {} dır".format(a,b,a*b)) 
elif islem == "4üncü":   
   print("{} ile  {} in bölümü {} dır".format(a,b,a/b)) 
else:
   print("sonuç bulunamadı")    
