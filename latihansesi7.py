while True :
    print (10*"=", "LUAS SEGITIGA", "="*10)
    alas = float(input("masukan alas = "))
    tinggi = float(input("masukan tinggi = "))
    rumus1 = 1/2 * alas * tinggi
    print ("Luas segitiga = ", float(rumus1))
    print ("apakah lanjut luas persegi panjang? y or n")
    jawab = input()
    if jawab == "y" :
        print(10*"=", "LUAS PERSEGI PANJANG", "="*10)
        while True :
            panjang = float(input("masukan panjang = "))
            lebar = float(input("masukan lebar = "))
            rumus2 = panjang * lebar
            print ("luas persegi panjang = ",rumus2)
            print ("apakah lanjut mengetahui ganjil/genap? y or n")
            jawab = input()
            if jawab == "y" :
                print (10*"=", "HASIL GANJIL/GENAP", "="*10)
                if rumus1 %2 == 0 :
                    print (f"hasil luas segitiga {rumus1} adalah bilangan genap") 
                else :
                    print (f"hasil luas segitiga {rumus1} adalah bilangan ganjil") 

                if rumus2 %2 == 0 :
                    print (f"hasil luas segitiga {rumus2} adalah bilangan genap") 
                else :
                    print (f"hasil luas segitiga {rumus2} adalah bilangan ganjil") 
                    break              
            else :
                continue
    else :
        continue