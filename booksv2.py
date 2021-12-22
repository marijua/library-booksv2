kitapListesi = ["kitap1","kitap2"]

kitapListesi.append("kitap3")
kitapListesi.remove("kitap1")

# Kütüphane Uygulaması 22.12.2021 : 


kitapListesi1 = list() # Listemizin Adı

anasayfa = """
Basit Eğlenceli Kitap Ekleme Uygulaması 

[1] Kitap Ekleme Bölümü
[2] Kitap Silme Bölümü (Bakımda)
[3] Eklenen Kitapları Görme Bölümü
[0] Çıkış

	"""

def kitapEkle(kitap,liste):
	liste.append([kitap])
	print("Kitap Başarıyla Eklenmiştir")
	input("Ana Sayfaya Dönmek İçin Tıklayın : ")

def kitapSil(kitap,liste):
	liste.remove([kitap])
	print("Kitap Başarıyla Silinmiştir")
	input("Ana Sayfaya Dönmek İçin Tıklayın : ")

def kitapListele(liste):
	for i in liste:
		print("Kitapların İsmi : {}".format(i))


def cik():
	quit()


while True:
	print(anasayfa)

	secme = input("Seçimi Yapınız : ")

	if secme == "1":
		kitapİsmi = input("Ekleyeceğiniz Kitabın Adı : ")
		kitapEkle(kitapİsmi,kitapListesi1)

	elif secme == "2":
		kitapİsmi = input("Sileceğiniz Kitabın Adı : ")
		kitapSil(kitapİsmi,kitapListesi1)

	elif secme == "3":
		kitapListele(kitapListesi1)

	elif secme == "4":
		cik()

	else:
		print("Hatalı Bir Komut Girdiniz")
		input("Ana Sayfaya Dönmek İçin Tıklayınız : ")
