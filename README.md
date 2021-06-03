Шаблон проекта автотестов
=========================

Что это?
--------

Это пример того, как может выглядет проект для автоматизирвоанного тестирвоания API на Python.

Зачем этот проект?
-----------------

Предполагается, что этот проект можно использовать как основу для автоматизации тестирования API на различных проектах.

Что тут есть полезного?
-----------------------

Постарался собрать основное из того, что для меня важно в проекте автотестов для API:
1. Сфромированная структура проекта, в которой выделены следующие модули:
    - сами тесты, в которых описывается только высокоуровневая логика;
    - хелперы, которые более подробно описывают, как выполнить действия из тестов;
    - сервисы, реализующие непосредственно отправку запросов в API, обращение к БД и т.д.;
    - тестовые данные и их обработчики.
    
2. Пример реализация подготовительных шагов для выполнения тестов.
3. Инфраструктура для работы с конфигами под различные стенды.
4. Пример реализации методологии DDT (Data-driven Testing)
5. Пример проверки ответа по схеме.