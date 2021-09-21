adlar=[]
soyadlar=[]
yaslar=[]
emailler=[]
hamisi=[adlar, soyadlar, yaslar, emailler]
while True:
    
    emr=input('Yeni istifadəçi əlavə etmək üçün "1" düyməsinə basın:')

    if emr=='1':
        ad=input('İstifadəçi adını daxil edin: ')
        adlar.append(ad)
        break

while True:

    emr=input('Yeni soyad əlavə etmək üçün "1" düyməsinə basın:')

    if emr=="1":
        soyad=input('Soyad daxil edin:')
        soyadlar.append(soyad)
        break

while True:

    emr=input('Yeni yaş əlavə etmək üçün "1" düyməsinə basın:')

    if emr=="1":
        yas=input('Yaş daxil edin:')
        yaslar.append(yas)
        break

while True:

    emr=input('Yeni e-mail əlavə etmək üçün "1" düyməsinə basın:')

    if emr=="1":
        email=input('E-mail daxil edin:')
        emailler.append(email)
        break

while True:
    emr=input('Bütün istifadəçiləri görmək üçün "2" düyməsinə basın:')
    if emr=='2':
        print(hamisi)
        break