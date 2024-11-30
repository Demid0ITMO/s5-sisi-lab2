# Лабораторная 2. Разработка системы поддержки принятия решения на основе базы знаний или онтологии
Целью этой лабораторной работы является разработка программы (рекомендательной системы), 
которая будет использовать базу знаний или онтологию для предоставления рекомендаций  
на основе введенных пользователем данных. (Knowledge-based support system)

## Задание
- Создать программу, которая позволяет пользователю ввести запрос через командную строку. Например, информацию о себе, своих интересах и предпочтениях в контексте выбора видеоигры - на основе фактов из БЗ (из первой лабы)/Онтологии(из второй).
- Использовать введенные пользователем данные, чтобы выполнить логические запросы к  БЗ/Онтологии.
- На основе полученных результатов выполнения запросов, система должна предоставить рекомендации или советы, связанные с выбором из БЗ или онтологии.
- Система должна выдавать рекомендации после небольшого диалога с пользователем

## Пример входных данных

- ``Я хочу поиграть в `жанр` игру``
- ``D какие игры я могу поиграть на `платформа` ``

## Данные на основе которых рекомендуются игры
- Возраст (Cпрашивается при входе)
- Жанр (Action / Strategy / Adventure / Role playing (RPG) / Sports)
- Платформа (PC / Xbox / Playstation / Nintendo Switch)
