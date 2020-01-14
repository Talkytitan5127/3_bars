# Moscow Bars

## Description

Get info about Moscow Bars. This console programm output next data:

* which bar is the biggest
* which bar is the smallest
* which bar is the nearest to your coordinates

List of Moscow's bar you can download in the [website](https://data.mos.ru/opendata/7710881420-bary), click 'Скачать'
and choose '.json' file's type.

## Requirements

Python 3.5 or greater

## Install

Clone the repository to computer

```bash
git clone https://github.com/Talkytitan5127/3_bars
```

## Usage

```bash
python3 bars.py [-b] [-s] [--filepath FILEPATH] [--location LATITUDE LONGITUDE]
```

## Example

### Get info about the biggest bar

```bash
$ python3 bars.py -b
The biggest bar is Спорт бар «Красная машина».
You can find it at: Автозаводская улица, дом 23, строение 1,
Telephone: (905) 795-15-84,
'Seats count: 450.

```

### Get info about the nearest bar

```bash
$ python3 bars.py --location 55.890833 37.424167
The nearest bar is Таверна.
You can find it at: проспект Защитников Москвы, дом 8,
Telephone: (977) 511-73-23,
'Seats count: 16.

```
