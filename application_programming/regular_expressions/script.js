let a = prompt('Задание 18.1 - Определяет, начинается ли строка с http://');
document.write(/^htmp:\/\//.test(a),'<br>');

let b = prompt('Задание 18.2 - Определяет, начинается ли строка с http:// или https://');
document.write(/^http:\/\/|^https:\/\//.test(b),'<br>');

let c = prompt('Задание 18.3 - Определяет, заканчивается ли строка на txt, html и php');
document.write(/\.txt$|\.html$|\.php$/.test(c),'<br>');

let d = prompt('Задание 18.4 - Определяет, заканчивается ли строка на jpg или jpeg');
document.write(/\.jpg$|\.jpeg$/.test(d),'<br>');

let e = prompt('Задание 18.5 - Определяет, заканчивается ли строка на jpg, jpeg или png');
document.write(/\.jpg$|\.jpeg$|\.png$/.test(d),'<br>');

let f = prompt('Задание 18.6 - Определяет, входит ли цифра в диапозоне от 1 до 12');
document.write(/(^[1-9]|^1[0-2])$/.test(f),'<br>');

let g = prompt('Задание 18.7 - Определяет, является ли строка форматом: год-месяц-день');
document.write(/\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[0-1])/.test(g),'<br>');

let h = prompt('Задание 18.8 - Определяет, является ли строка форматом: день:месяц:год');
document.write(/(0[1-9]|[12][0-9]|3[0-1])\.(0[1-9]|1[0-2])\.\d/.test(h),'<br>');

let i = prompt('Задание 18.9 - Определяет, является ли строка форматом: часы:менуты:секунды');
document.write(/([0-1][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]/.test(i),'<br>');

let j = prompt('Задание 18.10 - Определяет, является ли строка Электроной почтой');
document.write(/@((mail|yandex)\.ru|gmail\.com)$/.test(j),'<br>');

let k = prompt('Задание 18.11 - Определяет, верный ли домен');
document.write(/(.su|.ru|.com|.org|.рф)$/.test(k),'<br>');