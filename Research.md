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
++a yazdıqda 1+a-dan başlayır amma a++ yazdıqda 0+a-dan başlayır