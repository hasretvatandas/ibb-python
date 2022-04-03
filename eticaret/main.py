USERNAME = "hasret"
PASSWORD = "hasret"

# Daha onceden verilmis siparisler
ONAYLANMIS_SIPARISLER = [
    {
        "urunler": [
            {"urun_id": 1, "urun_adi": "Laptop", "fiyati": 1000, "kategori": "Elektronik"},
            {"urun_id": 5, "urun_adi": "Bilgisayar", "fiyati": 200, "kategori": "Elektronik"},
        ],
        "toplam_fiyat": 1200,
    }
]

# Database olmadigi icin urunleri tuttugumuz bir liste
URUNLER = [
    {"urun_id": 1, "urun_adi": "Laptop", "fiyati": 1000, "kategori": "Elektronik"},
    {"urun_id": 2, "urun_adi": "Telefon", "fiyati": 500, "kategori": "Elektronik"},
    {"urun_id": 3, "urun_adi": "Tablet", "fiyati": 700, "kategori": "Elektronik"},
    {"urun_id": 4, "urun_adi": "Kulaklik", "fiyati": 300, "kategori": "Elektronik"},
    {"urun_id": 5, "urun_adi": "Bilgisayar", "fiyati": 200, "kategori": "Elektronik"},
    {"urun_id": 6, "urun_adi": "Suc ve Ceza", "fiyati": 200, "kategori": "Kitap"},
    {"urun_id": 7, "urun_adi": "Savas ve Baris", "fiyati": 200, "kategori": "Kitap"},
    {"urun_id": 8, "urun_adi": "Momo", "fiyati": 200, "kategori": "Kitap"},
    {"urun_id": 9, "urun_adi": "Ataturk", "fiyati": 200, "kategori": "Kitap"},
    {"urun_id": 10, "urun_adi": "Python 101", "fiyati": 200, "kategori": "Kitap"},
    {"urun_id": 11, "urun_adi": "Kola", "fiyati": 100, "kategori": "Icecek"},
    {"urun_id": 12, "urun_adi": "Fanta", "fiyati": 100, "kategori": "Icecek"},
    {"urun_id": 13, "urun_adi": "Ayran", "fiyati": 100, "kategori": "Icecek"},
    {"urun_id": 14, "urun_adi": "Cay", "fiyati": 100, "kategori": "Icecek"},
    {"urun_id": 15, "urun_adi": "Kahve", "fiyati": 100, "kategori": "Icecek"},
    {"urun_id": 16, "urun_adi": "Eldiven", "fiyati": 300, "kategori": "Spor"},
    {"urun_id": 17, "urun_adi": "Koltuk", "fiyati": 300, "kategori": "Spor"},
    {"urun_id": 18, "urun_adi": "Sapka", "fiyati": 300, "kategori": "Spor"},
    {"urun_id": 19, "urun_adi": "Sort", "fiyati": 300, "kategori": "Spor"},
    {"urun_id": 20, "urun_adi": "Tayt", "fiyati": 300, "kategori": "Spor"},
    {"urun_id": 21, "urun_adi": "Oje", "fiyati": 300, "kategori": "Kozmetik"},
    {"urun_id": 22, "urun_adi": "Krem", "fiyati": 300, "kategori": "Kozmetik"},
    {"urun_id": 23, "urun_adi": "Parfum", "fiyati": 300, "kategori": "Kozmetik"},
    {"urun_id": 24, "urun_adi": "Ruj", "fiyati": 300, "kategori": "Kozmetik"},
    {"urun_id": 25, "urun_adi": "Dedorant", "fiyati": 300, "kategori": "Kozmetik"},
]

# Siparis sepeti
SIPARIS_SEPETI = {"urunler": [], "toplam_fiyat": 0}

# kategoriler
KATEGORILER = ["Elektronik", "Icecek", "Kozmetik", "Spor", "Kitap"]

# login islemi icin kontrol
def auth_user(username, password):
    if username == USERNAME and password == PASSWORD:
        return True
    else:
        return False


def display_ekran2():
    print(
        """
    Ekran 2
    1. Siparislerim
    2. Sepetim
    3. Alisveris
    4. Cikis
    """
    )


def display_ekran22():
    print(
        """
    Ekran 2.2
    1. Sepettekileri Listele
    2. Siparisi Onayla
    """
    )


# sepet dolu ise siparis onayinda SIPARIS_SEPETI -> ONAYLAMIS_SIPARISLER e aktarilir
# SIPARIS SEPETI BOSALTILIR
def siparisi_onayla():
    global SIPARIS_SEPETI
    global ONAYLANMIS_SIPARISLER
    if len(SIPARIS_SEPETI["urunler"]) > 0:
        print("Siparis Onaylaniyor...")
        ONAYLANMIS_SIPARISLER.append(SIPARIS_SEPETI)
        SIPARIS_SEPETI = {"urunler": [], "toplam_fiyat": 0}
        print("Siparis Onaylandi!")
    else:
        print("Sepet Bos!")


# Kategori listesi gosterilir
def display_kategori_listesi():
    global KATEGORILER
    print("Kategori Listesi")
    enumerate = 0
    for kategori in KATEGORILER:
        enumerate += 1
        print(f"{enumerate}. {kategori}")


# Kategoriye gore urun listesi gosterilir
def display_kategori_urun_listesi(kategori):
    global URUNLER
    global KATEGORILER
    print("Urun Listesi")
    if kategori in KATEGORILER:
        for urun in URUNLER:
            if urun["kategori"] == kategori:
                print(f"Urun ID: {urun['urun_id']} - Urun Adi: {urun['urun_adi']} - Urun Fiyati: {urun['fiyati']}")
    else:
        print("Kategori Bulunamadi!")


# Sepetteki urunleri listeler
def display_sepet():
    global SIPARIS_SEPETI
    print("Sepet")
    toplam_fiyat = 0
    for urun in SIPARIS_SEPETI["urunler"]:
        toplam_fiyat += urun["fiyati"]
        print(f"Urun ID: {urun['urun_id']} - Urun Adi: {urun['urun_adi']} - Urun Fiyati: {urun['fiyati']}")
    SIPARIS_SEPETI["toplam_fiyat"] = toplam_fiyat
    print(f"Toplam Fiyat: {SIPARIS_SEPETI['toplam_fiyat']}")


# Bir urunu sepete ekler
def add_to_sepet():
    global SIPARIS_SEPETI
    global URUNLER
    print("Sepete Eklemek istediginiz urun ID'sini giriniz: ")
    urun_id = int(input("Urun ID: "))
    for urun in URUNLER:
        if urun["urun_id"] == urun_id:
            SIPARIS_SEPETI["urunler"].append(urun)
            SIPARIS_SEPETI["toplam_fiyat"] += urun["fiyati"]
            print(f"{urun['urun_adi']} sepete eklendi.")
            break
    else:
        print("Urun Bulunamadi!")


# login formu
def display_login_form():
    print("####################################")
    print("######### Eticaret Sistemi #########")
    print("####################################")

    username = input("Kullanici Adi: ")
    password = input("Sifre: ")
    if auth_user(username, password):
        print(f"Uygulamaya Hosgeldin {username}")
        return True
    else:
        print("Kullanici adi yada sifre yanlis!")
        return False


# daha once onaylanmis siparisleri listeler
def display_onaylanmis_siparisler():
    print("Siparisler")
    for siparis in ONAYLANMIS_SIPARISLER:
        for urun in siparis["urunler"]:
            print(f"Urun Adi: {urun['urun_adi']} - Urun Fiyati: {urun['fiyati']}")
        print(f"Toplam Fiyat: {siparis['toplam_fiyat']}")


if __name__ == "__main__":
    if display_login_form():
        while True:
            display_ekran2()
            secim = input("Seciminiz: ")
            if secim == "1":
                display_onaylanmis_siparisler()
            elif secim == "2":
                display_ekran22()
                secim2 = input("Seciminiz: ")
                if secim2 == "1":
                    display_sepet()
                elif secim2 == "2":
                    siparisi_onayla()
            elif secim == "3":
                display_kategori_listesi()
                kategori = input("Kategori Ismi Giriniz: ")
                display_kategori_urun_listesi(kategori)
                add_to_sepet()
            elif secim == "4":
                print("Cikis Yapiliyor...")
                break
            else:
                print("Yanlis secim yaptiniz")
