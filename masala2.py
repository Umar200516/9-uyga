soz_ = input("Kiriting :")
uzunligi_sozni_ = len(soz_)
ortacha_ = uzunligi_sozni_ // 2
yangi_ozgaruvchi_ = soz_[ortacha_:] + soz_[:ortacha_]
print(">", yangi_ozgaruvchi_)