adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer =adwentures_of_tom_sawer.replace("\n", " ")
print(adwentures_of_tom_sawer)

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer =adwentures_of_tom_sawer.replace("....", " ")
print(adwentures_of_tom_sawer)

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer =" ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print(count_h)

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
adwentures = adwentures_of_tom_sawer.split()
words = [a for a in adwentures if a[0].isupper()]
print(words)


import string  # додав ще варіант щоб "Big Missouri" попав (гуглив як вирішити)
words = [word.strip(string.punctuation)
    for word in adwentures
    if word.strip(string.punctuation) and word.strip(string.punctuation)[0].isupper()]
print(words)

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
#Зробив двома щляхами не зрозуміло яку позицію, слова у списку слів чи позицію у символах.
word = adwentures_of_tom_sawer.split()
first_pos = word.index("Tom")
second_pos = word.index("Tom", first_pos + 1)
print(second_pos)

first_pos_1 = adwentures_of_tom_sawer.find("Tom")
second_pos_2 = adwentures_of_tom_sawer.find("Tom", first_pos_1 + 1)
print(second_pos_2)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
import re
adwentures_of_tom_sawer_sentences= re.split(r'(?<=[.!?])\s+', adwentures_of_tom_sawer)
print(adwentures_of_tom_sawer_sentences)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3]
fourth_sentence_lower = fourth_sentence.lower()
print(fourth_sentence_lower)
# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
if any(sentence.startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences):
    print("Є речення, яке починається з 'By the time'")
else:
    print("Такого речення немає")

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
last_sentence = adwentures_of_tom_sawer_sentences[-1]
word_count = len(last_sentence.split())
print(word_count)
