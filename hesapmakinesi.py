islem = int(input("1: Toplama\n2: Cikarma\n3: Carpma\n4: Bolme:\nYapmak istediginiz islem: "))

sayi1 = int(input("Birinci sayiyi giriniz: "))
sayi2 = int(input("Ikinci sayiyi giriniz: "))

if islem == 1:
    print(sayi1+sayi2)
elif islem == 2:
    print(sayi1-sayi2)
elif islem == 3:
    print(sayi1*sayi2)
elif islem == 4:
    print(sayi1/sayi2)