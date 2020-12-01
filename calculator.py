a= int(input("Birinci Sayı:"))
b= int(input("İkinci Sayı:"))

işlem= (input("işlemi giriniz:"))

if işlem == "1" :
   print("{} ile  {} in toplamı {} dır".format(a,b,a+b))
elif işlem == "2":  
   print("{} ile  {} in farkı {} dır".format(a,b,a-b))
elif işlem == "3":   
   print("{} ile  {} in çarpımı {} dır".format(a,b,a*b)) 
elif işlem == "4":   
   print("{} ile  {} in bölümü {} dır".format(a,b,a/b)) 
else:
   print("İşlem bulunamamaktadır")    
