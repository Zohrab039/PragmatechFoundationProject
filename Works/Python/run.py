""" adlar=[]
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

İstifadəçilər=[] """


""" class Users():
    user='Userler'

    def __init__(self, ad, soyad, yas, email):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.email=email
user2=Users('Zohrab', 'Semedzade', '18', 'zohrab@gmail.com')
print(user2.email) """
#class
""" 
class Ucus():
    havayolu='THY'

    def __init__(self, kod, kalkis, varis, sure, kapasite, yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu
    def anons_yap(self):
        return '{} sefer sayili {}-{} ucusumuz {} dakika surecektir'.format(self.kod, self.kalkis, self.varis, self.sure)
    def koltuk_sayisi_guncelle(self):
        return self.kapasite - self.yolcu
    def bilet_satis(self, bilet_adedi=1):
        self.yolcu +=bilet_adedi
        self.koltuk_sayisi_guncelle
        print('{} adet bilet satilmistir, kalan koltuk sayisi {}'.format(bilet_adedi, self.koltuk_sayisi_guncelle()))
            
            
ucus2=Ucus('TK123', 'IST', 'ANK', 60, 300, 50)
ucus3=Ucus('TH223', 'BOD', 'ANT', 40, 250, 250)
print(ucus2.bilet_satis(10)) """

""" NewBooks=[]
class Books():

    def __init__(self, id, ad, yazar, sehife):
        self.id=id
        self.ad=ad
        self.yazar=yazar
        self.sehife=sehife

    def id(self):
        self.id=1
        self.id+=1

    def addToList(self):
        NewBooks.append(self)

    def showBook(self):
        print(f'{self.id}{self.ad},{self.yazar},{self.sehife}')
    
    def addBook(self):
        self.id+=1


id=0


    def CreateBook():
        global id
        ad=input('Kitab adi: ')
        yazar=input('Kitabin yazari: ')
        sehife=input('Kitabin sehifesi: ')
        book1=Books(id,ad,yazar,sehife)

        book1.addToList()

        book1.id=id
        book1.addBook()
        id+=1

while True:
    emr=input('')

    if emr=='1':
        CreateBook()

    if emr=='2':
        for book1 in Books:
            book1.showBook()
            break
"""

"""     def kitab_goster(self):
        return '{} kitabinin muellifi {} {} sehifedir '.format(self._id, self.ad, self.yazar, self.sehife())

book1=Books( '1', 'Deli kur', 'ismayil sixli', '300')
print(book1.kitab_goster()) """

""" books=[]
class book:
    def __init__(self,id,ad,yazar,sehife):
        self.id=id
        self.ad=ad
        self.yazar=yazar
        self.sehife=sehife
    
    def addToList(self):
        books.append(self)
    def showBook(self):
        print(f'{self.id},{self.ad},{self.yazar},{self.sehife}')
    def artsn(self):
        self.id+=1

id=0

def createBook():
    global id
    ad=input('ad: ')
    yazar=input('yazar: ')
    sehife=input('sehife: ')
    book1=book(id,ad,yazar,sehife)

    book1.addToList()

    book.id=id
    book1.artsn()
    id+=1

while True:
    emr=input('kitab yaratmaq ucun 1-e basn')

    if emr=='1'
        createBook()

    if emr=='2'
        for book1 in books:
            book1.showBook() """

""" def cem(c):
    sum = 0
    for cemi in str(c): 
      sum += int(cemi)      
    return sum
   
c = 917
print(cem(c)) """

#task
""" a = [8,2,3,0,7]
total = sum(a)
print(total)
"""

#task

""" def multiply(multiple) :
    multi = 1
    for x in multiple:
         multi = multi * x
    return multi
a = [8,2,3,1,7]

print(multiply) """

#task

""" a=[1,2,3,4,5,6,7,8,9,10]
for num in a:
    if num % 2==0:
        print(num)

for num in a:
    if num%2==1:
        print(num) """

