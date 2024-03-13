def takrorlanmasdan_sozi_aniqla(soz):

    matnlar_s = soz.split()

    unikalniy_s = []

    for word in matnlar_s:
        unikalniy_q = ''
        for qisimlar in word:
            if qisimlar not in unikalniy_q:
                unikalniy_q += qisimlar
        unikalniy_s.append(unikalniy_q)

    for i in range(len(unikalniy_s) // 2):
        print(unikalniy_s[i] + unikalniy_s[-(i + 1)])

with open('file.txt') as file:
    malumot = file.read()

takrorlanmasdan_sozi_aniqla(malumot)
