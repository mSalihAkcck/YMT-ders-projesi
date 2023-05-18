class Magaza:
    sonuclar = ""
    def __init__(self, magaza_adi, satici_adi, satici_cinsi, fiyat):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi              # private değişkenlerimizi tanımlıyoruz
        self.__satici_cinsi = satici_cinsi
        self.__fiyat = fiyat

    def get_magaza_adi(self):
        return self.__magaza_adi
    def get_satici_adi(self):                       # private değişkenlere erişebilmek için
        return self.__satici_adi                    # accesor metodunu kullanıyoruz
    def get_satici_cinsi(self):
        return self.__satici_cinsi
    def get_fiyat(self):
        return self.__fiyat

    def magaza_satis_tutar(self, satici):
        if satici in tutarlar:                  # aynı mağazaların satış tutarlarını hesaplıyoruz
            tutarlar[satici] += self.get_fiyat()
        else:
            tutarlar[satici] = self.get_fiyat()

        for k, v in tutarlar.items():   # mağazaların toplam tutarlarını yazdırmak için string oluşturuyoruz
            self.sonuclar += f"{k} mağazasının yaptığı toplam satış: {v}\n"
        return self.sonuclar

    def __str__(self):
        self.sonuc = ""                 # mağazaların ve satıcıların tutarlarını ayrı ayrı ekrana yazdırıyoruz
        for k, v in islemler.items():
            self.sonuc += f"{k}'in yaptığı toplam satış: {v}\n"
        return f"{self.sonuclar}\n{self.sonuc}"

islemler = {}   # her kişinin değerleri tutmak için boş dictionary oluşturuyoruz
tutarlar = {}   # her mağazanın toplam satış tutarlarını dictionary de tutuyoruz
