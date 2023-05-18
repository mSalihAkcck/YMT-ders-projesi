import magaza

print("Kodda olan değişikliği commit ettikten sonra göstermek için bu şekilde değişiklik yapıyorum.")
def main():
    while True:                                  # her döngü için
        magaza_ismi = input("Magaza adı: ")      # istenen bilgileri
        satici_ismi = input("Satıcı adı: ")      # klavyeden giriyoruz
        satici_cinsi = input("Satılan eşya(tv, bilgisayar, beyaz eşya, diğer): ")
        tutar = int(input("Satış tutarı: "))

        obj = magaza.Magaza(magaza_ismi, satici_ismi, satici_cinsi, tutar)  # class instance ımızı oluşturuyoruz
        satici = magaza_ismi + " dan " + satici_ismi   # mağaza adı ve personelin ismi satıcı kimliğini oluşturuyor

        if satici in magaza.islemler:          # aynı satıcı satış yaptıysa var olan satış tutarına ekleme yapıyoruz
            magaza.islemler[satici] += tutar   # key değerimizi satıcı yapıyoruz
        else:                           # value değerimizi ise tutar yapıyoruz
            magaza.islemler[satici] = tutar

        satici = satici.split(" ")
        satici = satici[0]    # her mağazanın toplamını hesaplamak için metoda parametreyi mağaza ismiyle yolluyoruz
        obj.magaza_satis_tutar(satici)

        cikis = input("Çıkış yapmak için q'a basınız: ")
        print()
        if cikis == "q":
            break

    print(obj.__str__())

main()