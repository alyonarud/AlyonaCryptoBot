keys = {
        'рубль': 'RUB',
        'евро': 'EUR',
        'доллар': 'USD',
        'австралийский доллар': 'AUD',
        'британский фунт':'GBP',
        'биткоин': 'BTC',
}


TOKEN = "удален"

#print(keys.keys())
#print(keys.values())


keys_more = {
        'BTC': 'Биткоин',
        'USD': 'Доллар_США',
        'EUR': 'Евро',
        'GBP': 'Фунт_стерлингов_Великобритании',
        'JPY': 'Японская_йена',
        'CHF': 'Швейцарский_франк',
        'CNY': 'Китайский_юань',
        'RUB': 'Российский_рубль',
        'UAH': 'Украинская_гривна',
        'BYN': 'Белорусский_рубль',
        'BRL': 'Бразильский_реал',
        'CAD': 'Канадский_доллар',
        'GEL': 'Грузинский_лари',
        'AED': 'Дирхам_ОАЭ',
        'AFN': 'Афганский_афгани',
        'ALL': 'Албанский_лек',
        'AMD': 'Армянский_драм',
        'AOA': 'Ангольская_кванза',
        'ARS': 'Аргентинский_песо',
        'AUD': 'Австралийский_доллар',
        'AZN': 'Азербайджанский_манат'

}


#print(key_get(keys_more,'Евро'))

#(base_key = i) for i, j in keys_more.items() if j == base
# Коды валют по ISO 4217

# UAH	980	Украинская гривна
# Основные валюты
# USD	840	Доллар США	$
# EUR	978	Евро	€
# GBP	826	Фунт стерлингов Великобритании	£
# JPY	392	Японская йена	¥
# CHF	756	Швейцарский франк
# CNY	156	Китайский юань женьминьби
# RUB	643	Российский рубль
# Прочие валюты
# AED	784	Дирхам ОАЭ
# AFN	971	Афганский афгани
# ALL	008	Албанский лек
# AMD	051	Армянский драм
# AOA	973	Ангольская кванза
# ARS	032	Аргентинский песо
# AUD	036	Австралийский доллар
# AZN	944	Азербайджанский манат
# BDT	050	Бангладешская така
# BGN	975	Болгарский лев
# BHD	048	Бахрейнский динар
# BIF	108	Бурундийский франк
# BND	096	Брунейский доллар
# BOB	068	Боливийский боливиано
# BRL	986	Бразильский реал
# BWP	072	Ботсванская пула
# BYN	933	Белорусский рубль
# CAD	124	Канадский доллар
# CDF	976	Конголезский франк
# CLP	152	Чилийский песо
# COP	170	Колумбийский песо
# CRC	188	Костариканский колон
# CUP	192	Кубинский песо
# CZK	203	Чешская крона
# DJF	262	Джибутийский франк
# DKK	208	Датская крона
# DZD	012	Алжирский динар
# EGP	818	Египетский фунт
# ETB	230	Эфиопский быр
# GEL	981	Грузинский лари
# GHS	936	Ганский седи
# GMD	270	Гамбийский даласи
# GNF	324	Гвинейский франк
# HKD	344	Гонконгский доллар
# HRK	191	Хорватская куна
# HUF	348	Венгерский форинт
# IDR	360	Индонезийская рупия
# ILS	376	Израильский шекель
# INR	356	Индийская рупия
# IQD	368	Иракский динар
# IRR	364	Иранский риал
# ISK	352	Исландская крона
# JOD	400	Иорданский динар
# KES	404	Кенийский шиллинг
# KGS	417	Киргизский сом
# KHR	116	Камбоджийский риель
# KPW	408	Северо-корейская вона (КНДР)
# KRW	410	Южно-корейская вона (Корея)
# KWD	414	Кувейтский динар
# KZT	398	Казахский тенге
# LAK	418	Лаосский кип
# LBP	422	Ливанский фунт
# LKR	144	Шри-ланкийская рупия
# LYD	434	Ливийский динар
# MAD	504	Марокканский дирхам
# MDL	498	Молдовский лей
# MGA	969	Малагасийский ариари
# MKD	807	Македонский денар
# MNT	496	Монгольский тугрик
# MRO	478	Мавританская угия
# MUR	480	Маврикийская рупия
# MVR	462	Мальдивская руфия
# MWK	454	Малавийская квача
# MXN	484	Мексиканский песо
# MYR	458	Малайзийский ринггит
# MZN	943	Мозамбикский метикал
# NAD	516	Намибийский доллар
# NGN	566	Нигерийская наира
# NIO	558	Никарагуанская кордоба
# NOK	578	Норвежская крона
# NPR	524	Непальская рупия
# NZD	554	Ново­зеландский доллар
# OMR	512	Оманский риал
# PEN	604	Перуанский соль
# PHP	608	Филиппинский песо
# PKR	586	Пакистанская рупия
# PLN	985	Польский злотый
# PYG	600	Парагвайский гуарани
# QAR	634	Катарский риал
# RON	946	Новый румынский лей
# RSD	941	Сербский динар
# SAR	682	Саудовский риял
# SCR	690	Сейшельская рупия
# SDG	938	Суданский фунт
# SEK	752	Шведская крона
# SGD	702	Сингапурский доллар
# SLL	694	Сьерра-леонский леоне
# SOS	706	Сомалийский шиллинг
# SRD	968	Суринамский доллар
# SYP	760	Сирийский фунт
# SZL	748	Свазилендский лилангени
# THB	764	Таиландский бат
# TJS	972	Таджикский сомони
# TMT	795	Туркменский манат
# TND	788	Тунисский динар
# TRY	949	Новая турецкая лира
# TWD	901	Тайваньский доллар
# TZS	834	Танзанийский шиллинг
# UGX	800	Угандийский шиллинг
# UYU	858	Уругвайский песо
# UZS	860	Узбекский сум
# VEF	937	Венесуэльский боливар
# VND	704	Вьетнамский донг
# XAF	950	Франк КФА (Центральная Африка)
# XDR	960	СПЗ
# XOF	952	Франк КФА (Западная Африка)
# YER	886	Йеменский риал
# ZAR	710	Южно-африканский рэнд
# ZMK	894	Замбийская квача
