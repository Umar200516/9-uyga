def eng_uzun_kelgan_takrorlanmasdan(sozlar_):
    if len(sozlar_) == 0:
        return ""
    ozgaruchi_sozlar_ = sozlar_[0]
    uzun_sozlar_ = sozlar_[0]
    for stiring_ in sozlar_[1:]:
        if stiring_ >= ozgaruchi_sozlar_[-1]:
            ozgaruchi_sozlar_ += stiring_
            if len(ozgaruchi_sozlar_) > len(uzun_sozlar_):
                uzun_sozlar_ = ozgaruchi_sozlar_
        else:
            ozgaruchi_sozlar_ = stiring_
    return uzun_sozlar_
soz_ = input("Kiriting :")
print(eng_uzun_kelgan_takrorlanmasdan(soz_))
# s = "ffgabnnkmm"