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
6. Example(Məsələn):
<!DOCTYPE html>
<html lang="en-US">
<body>

<h1>My Web Page</h1>

<p>Hello everybody!</p>

<p>Translate this page:</p>

<div id="google_translate_element"></div>

<script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
}
</script>

<script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>

</body>
</html>
7. Translate(Tərcümə) button(düymə)-ı dizayn və görünüş baxımından sadə görünə bilər və ya siz istəmədiyiniz yöndə ola bilər. Buna translate button-ı 3 fərqli vəziyətdə ola bilir.
 1. Vetically(şaquli)
 2. Horizontally(üfüqi)
 3. Dropdown menu(açılan menyu)