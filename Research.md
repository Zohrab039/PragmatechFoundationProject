## Justify-content Align-items
1. Justify-content və align-items arasındakı fərqlər:
Justify-content content elementlərini hizalayır yəni 1 ox boyunca align-items isə containerlardakı maddələri standart uyğunlaşdırır.
2. Justify-content:space-around xüsusiyyəti maddələrin əvvəlində ortasında və sonrasında boşluqlar yaradır.
3. Align-items containerlardakı maddələri standart uyğunlaşdırır align-content isə flew-wrapdan asılıdır amma align-itemsdan fərqli olaraq flexin sətrlərini hizalayır.
4. Container içərisindəki itemları vəziyyətdən asılı olaraq nə qədər kiçildəcəyini müəyyən edir.
5. Flex-shrinkin əksini edir.
## Translator haqqında.
1. Translator səhifəni müxtəlif dillərə translate yəni tərcümə etmək üçündür.
2. Translator (Tərcüməçi)-u web səhifədə göstərmək üçün hər hansısa bir "<div>" class açırıq və "id" veririk
3. Sadə translator (tərcüməçi) yazılış şəkili: <div id="google_translate_element"></div>
4. JavaScript funksiyası əlavə etmək üçün: <script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
}</script>
5. Və sonda istədiyimiz content(məzmun)-u rahat bir şəkildə translate(tərcümə) edirik.
6. Translate(Tərcümə) button(düymə)-ı dizayn və görünüş baxımından sadə görünə bilər və ya siz istəmədiyiniz yöndə ola bilər. Buna translate button-ı 3 fərqli vəziyətdə ola bilir.
 1. Vetically(şaquli)
 2. Horizontally(üfüqi)
 3. Dropdown menu(açılan menyu)


## JavaScript statements
1. Break: "Break" ifadəsi yazıldığı sətrdən alt sətrə sıçrayır.
2. Continue: "Continue" ifadəsi döngədə müəyyən bir vəziyyət baş verərsə döngədə həmin döngəni pozur və döngədəki növbəti təkrar ilə davam edir.
3. Arguments: "Function"-un qarşısındakı parametrin dəyərini 
4. Await: Məlumat tapdım başa düşmədim.
5. Case: Məlumat tapmadım.
6. Catch: Try ... catch ifadəsi cəhd etmək üçün bir bəyanat blokunu işarələyir və bir istisna atılacağı təqdirdə cavabı bildirir. Try ifadəsi bir və ya daha çox ifadəyə aid olan bir cəhd blokundan ibarətdir. {} həmişə tək ifadələr üçün istifadə edilməlidir. Ən azı bir tutma bloku və ya nəhayət blok olmalıdır. Try ifadəsinin 3 forması var:
try...catch
try...finally
try...catch...finally
7. Class: Class deklarasiyası prototipə əsaslanan mirasdan istifadə edərək müəyyən adla yeni bir class yaradır.
8. Const: "Let" kimi "const"da da dəyişənlər olur və constda dəyişənlər yenidən təyin edilə bilməz.

## JS research
1.  a=5 və var a=5 yazmağın fərqi nədir.
a=5 console bölməsinə yazdıqda 5 rəqəmi olduğu kimi görünür amma var a=5 yazdıqda undefined yazılır.
2.  a=5; b=6 yenidən təyin etmeden ele edin ki c.log(a) yazanda 6 digersinde 5 cixsin.
Bunun etmək üçün a=5 b=6 yazırıq sonra isə a=b console.log(a) yazanda console-da 5 dəyişir 6 olaraq görünür.
3. "Salam"<"salam" in nəticəsi nedir ve niye?
"Salam"<"salam"-ın nəticəsi true-dir.
4. İmplicit və explicit type conversion nədir? Fərqlərini izah edin.
İmplicit conversion vəziyyətində məcburiyyət gizlin edilir və JS səhv bir məlumat tipini işləyərkən onu doğru məlumat tipinə çevirməyə çalışır.
Explicit conversion vəziyyətində developer tərəfindən kodlar açıq şəkildə göstərilir.
5. ++a və a++ fərqləri nedir?
++a yazdıqda 1+a-dan başlayır amma a++ yazdıqda 0+a-dan başlayır.

## Week05-Day05 HomeWork
1. Hal hazırda istifadə olunan proqramlaşdırma paradigmaları hansılardır?
Hal hazırda istifadə olunan proqramlaşdırma paradigmaları: imperative, procedural, object-oriented, declarative, functional, logic, mathematical, reactive-dir.
- Hər paradigma haqqında bir neçə paraqraflıq dəyərləndirmə yazın
Imperative- proqramçının maşına vəziyyətini necə dəyişdirməyi göstərir.
Procedural- təlimatları prosedurlara qruplaşdırır.
Object-oriented- təlimatları işlədikləri dövlətin bir hissəsi ilə qruplaşdırır.
Declarative- proqramçının yalnız istədiyi nəticənin xüsusiyyətlərini elan etdiyini açıqlayır amma onun necə hesablanacağını yox.
Functional- istənilən nəticənin bir sıra funksiya tətbiqlərinin dəyəri olaraq elan edir.
Logic- istədiyiniz nəticənin faktlar və qaydalar sistemi haqqında bir suala cavab olaraq elan edir.
Mathematical- istədiyiniz nəticənin optimallaşdırma probleminin həlli olaraq elan edir.
Reactive- məlumat axınları və dəyişikliyin yayılması ilə istənilən nəticənin elan edir.
2. Obyekt yönümlü proqramlaşdırma paradigması haqqında ümümi izahat yazın.
Kompüter proqramları və tətbiqləri yaratmaq üçün proqramlaşdırma paradiqmasıdır.
- Niyə belə bir paradigmaya ehtiyac duyulub?
Bir proqram proqramını, obyektlərin fərdi nümunələrini yaratmaq üçün istifadə olunan sadə, təkrar istifadə edilə bilən kod planlarına (ümumiyyətlə siniflər adlanır) qurmaq üçün istifadə olunur.
- Ilk kimlər tərəfindən ortaya atılıb?
- OOP prinsipləri nələrdir? Araşdıraraq izah etməyə cəhd edin.
enkapsulyasiya (encapsulation),
varislik (inheritance),
polimorfizm (polymorphism),
abstraksiyası (abstraction),
obyektlər arasında informasiya axınının təşkili (sending messages / message sending),
təkrar istifadə oluna bilərlik (reusability).

//Javascript və Python dillərinin data tipləri arasındakı oxşar və fərqli cəhətlər nədir?

JS-in 8 ədəd basic data types-ı vardır:

  -String: Mətn məlumatlarını təmsil edir.
  -Number: Tam ədədləri təmsil edir.
  -BigInt: Ixtiyari dəqiqliyi olan tam ədədləri təmsil edir.
  -Boolean: 2 dəyəri vardır: doğru(true) və səhv(false).
  -undefined: Dəyişəninin işə salınmadığı bir məlumat növüdür.
  -null: Boşluq və ya sıfır dəyərini göstərir.
  -Symbol: Nümunələri unikal və dəyişməz olan məlumat növüdür.
  -Object: Məlumatların toplanmasının əsas dəyər cütləridir.


Pythonun 7 ədəd data types-ı vardır:
  -Text Type:	Example: x = "Hello World"
  -Numeric Types:	
    int: Example: x = 20
    float: Example: x = 20.5	
    complex: Example: x = 1j	
  -Sequence Types:
    list: Example: x = ["apple", "banana", "cherry"]
    tuple: Example: x = ("apple", "banana", "cherry")
    range: Example: x = range(6)
  -Mapping Type:
    dict: Example: x = {"name" : "John", "age" : 36}
  -Set Types:
    set: Example: x = {"apple", "banana", "cherry"}
    frozenset: Example: x = frozenset({"apple", "banana", "cherry"})
  -Boolean Type:
    bool: Example: x = True(False)
  -Binary Types:
    bytes: Example: x = b"Hello"
    bytearray: Example: x = bytearray(5)
    memoryview: Example: x = memoryview(bytes(5))	

Python və JavaScript -də Məlumat Növləri və Dəyərləri:
(Fərqli cəhətlər)
  Numeric Data Types
    Python, elmi məqsədlər üçün dəqiq hesablamalar aparmağımıza kömək edəcək üç ədəd növə malikdir. Bu numeric tipinə daxildir:
    int (tam ədədlər), float (üzən nöqtə ədədləri) və complex. Hər birinin öz xüsusiyyətləri, xarakteristikaları və tətbiqləri var.
    Bunun əksinə olaraq, JavaScript -in yalnız iki ədəd numeric tipi var: Number və BigInt. İntegers və floating-point numbers Number tip sayılır.

  "None" və "Null"
    Python'da, dəyişənin proqramın müəyyən bir nöqtəsində bir dəyəri olmadığını göstərmək üçün istifadə etdiyimiz None adlı xüsusi bir dəyər var.
    JS'də isə buna bərabər dəyər olaraq Null vardır "hər hansı bir obyekt dəyərinin qəsdən yoxluğunu ifadə edir"

  Undefinied
    JavaScript -də, bir ilkin dəyər təyin etmədən bir dəyişəni elan edərkən avtomatik olaraq təyin olunan xüsusi bir dəyərimiz var. Example:
      var x;
      undefined
    =============
      x;
      undefined
    Burada x dəyişəninin dəyəri qeyri-müəyyəndir.

    Python -da, dəyişənə ilkin dəyər təyin etməlisiniz. İlkin dəyər olmadan elan edə bilmərik.
    Tip: Bir dəyərin olmadığını göstərmək üçün Python -da bir dəyişənin başlanğıc dəyəri olaraq None təyin edə bilərsiniz.

(Oxşar cəhətlər)