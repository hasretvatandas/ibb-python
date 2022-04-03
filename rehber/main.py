# Rehber Kayitlarimizin Tutulacagi yer
rehber = {}

# Rehber Secim Listesini Goruntule
def menu():
    print(
        """
    Yapmak istediginiz islem nedir?
    1. Rehbere Kisi Ekle
    2. Rehberden Kisi Silme
    3. Isim & Numara Guncelleme
    4. Rehberi Goruntuleme
    """
    )


def add_to_rehber():
    global rehber
    isim = input("Isim: ")
    numara = input("Numara: ")
    if isim in rehber:
        print("Bu isim zaten var")
        print("Lutfen farkli isim giriniz...")
        return
    rehber[isim] = numara


def delete_from_rehber():
    global rehber
    isim = input("Silmek istediginiz isim: ")
    if isim in rehber:
        del rehber[isim]
        print("{} isimli kisi silindi".format(isim))
    else:
        print("{} isimli kisi bulunamadi".format(isim))


def update_rehber():
    global rehber
    isim = input("Guncellemek istediginiz isim: ")
    if isim in rehber:
        numara = input("Numara: ")
        rehber[isim] = numara
        print("{} isimli kisi guncellendi".format(isim))
    else:
        print("{} isimli kisi bulunamadi".format(isim))


def show_rehber():
    global rehber
    print("Rehber:")
    for isim, numara in rehber.items():
        print("{} - {}".format(isim, numara))


if __name__ == "__main__":
    while True:
        menu()
        secim = input("Seciminizi giriniz: ")
        if secim == "1":
            print("Rehbere Kisi Ekleme")
            add_to_rehber()
        elif secim == "2":
            print("Rehberden Kisi Silme")
            delete_from_rehber()
        elif secim == "3":
            print("Isim & Numara Guncelleme")
            update_rehber()
        elif secim == "4":
            print("Rehberi Goruntuleme")
            show_rehber()
        else:
            print("Yanlis secim yaptiniz")
            break
