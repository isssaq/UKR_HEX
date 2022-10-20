# UKR_HEX
1) Перетворення значення HEX в Little Endian значення
  Функція to_little(s) для перетворення приймає один параметр: рядок формату HEX ("FFFF"), (без "0x") 
  Результат - перетворене значення в Little Endian
2) Перетворення значення HEX в Big Endian значення
  Функція to_big(s) для перетворення приймає один параметр: рядок формату HEX ("FFFF"), (без "0x") 
  Результат - перетворене значення в Big Endian
 
3) Перетворення значення Little Endian на HEX значення:
   Функція from_little_to_hex(x, n) приймає 2 вхідних параметри: число та кількість байтів кінцевого значення
   Обчислює к-ть 0 які потрібно додати, щоб отримати вихідне значення у заданому розмірі
   На виході отримуємо рядок 16 значення числа x ("0xFFFF")
