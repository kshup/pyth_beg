
print("""
ATM MAKINESI V2.0

1- BAKIYE SORGULAMA

2- PARA YATIRMA ISLEMLERI

3- PARA CEKME

4- Elinde ki Parayi ogrenme

Cikmak icin 'q' ya basiniz


BANKAMIZA YENI GELENLERE OZEL 1000 TL BAKIYE!!!

""")

system_kullanici_adi = 'alimuraat'
system_kullanici_parola = 'almuta'
sys_2 = 'ayse'
sysp_3 = '1234'
kalan_hak = 3

while True:
    kullanici_adi = input('Kullanici adi giriniz: ')
    if kullanici_adi == 'q':
        print('Yine bekleriz')
        break
    parola = input('Parola giriniz: ')
    if parola == 'q':
        print('Yine bekleriz')

    if system_kullanici_adi != kullanici_adi and sys_2 != kullanici_adi or system_kullanici_parola != parola and sysp_3 != parola:
        print('Hatali giris')
        kalan_hak -= 1
        print('Kalan Hakkiniz: ', kalan_hak)
    elif system_kullanici_adi != kullanici_adi and sys_2 != kullanici_adi or system_kullanici_parola == parola and sysp_3 == parola:
        print('Yanlis Kullanici adi')
        kalan_hak -= 1
        print('Kalan Hakkiniz: ', kalan_hak)

    elif system_kullanici_adi == kullanici_adi and sys_2 == kullanici_adi or system_kullanici_parola != parola and sysp_3 != parola:
        print('Parola hatali...')
        kalan_hak -=1
        print('Kalan Hakkiniz: ',kalan_hak)
    else:
        print('Giris Basarili !!')
        if kullanici_adi == 'alimuraat':
            Bakiye = 20000
            print('Bakiyeniz:',Bakiye)

        else:
            Bakiye = 1000
            print('Bakiyeniz:',Bakiye)
        eldeki_para = int(input('Elinizdeki parayi giriniz: '))


        while True:

                guncel_bakiye = eldeki_para + Bakiye
                secim_menusu = input('Yapmak istediginiz islem?')
                if secim_menusu == 'q':
                    secim = input('Hesaptan cikmak istediginize emin misiniz? Y/N')
                    if secim == 'Y' or secim == 'y':
                        print('Giris kismina yonlendiriliyor...')

                        break

                    elif secim == 'N' or secim == 'n':
                        continue


                elif secim_menusu == '1':
                    print('BAKIYENIZ: ', Bakiye)
                elif secim_menusu == '2':
                    paray = int(input('Yatirmak istediginiz Miktari giriniz'))
                    sonpara = eldeki_para
                    if eldeki_para < paray or eldeki_para < sonpara:
                        print('Bu kadar paraniz yok!')
                        continue
                    eldeki_para = eldeki_para - paray

                    Bakiye = paray + Bakiye
                    sonpara=eldeki_para

                    print('Bakiyeniz', Bakiye)

                elif secim_menusu == '3':
                    paray = int(input('Cekmek istediginiz parayi giriniz'))
                    if paray > Bakiye:
                        print('Yetersiz bakiye')
                        continue
                    Bakiye = Bakiye - paray
                    print(Bakiye)
                elif secim_menusu == '4':
                    eldeki_para =   paray - eldeki_para
                    print('Elinizdeki Kalan Paraniz:', sonpara)

                else:
                    print('Islemini Bulunamadi')

    if kalan_hak == 0:
        print('Giris Hakkiniz kalmadi, lutfen daha sonra tekrar deneyiniz...')
        break


