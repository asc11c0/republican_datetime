# republican_datetime
This library is a fork of the Python "datetime" library, adapted for the [French
Republican Calendar](https://en.wikipedia.org/wiki/French_Republican_calendar) 
and the [decimal time](https://en.wikipedia.org/wiki/Decimal_time) introduced during the French Revolution.

## Main features:
- Republican `datetime`, `date` and decimal `time` and `timedelta` classes
- standard Python `datetime` functionality adapted for the French Republican Calendar
- conversion to and from standard Gregorian `datetime`, `date`, `time` and
 `timedelta` classes
- correct calculation of the leap years by the time of the autumn equinoxes,
instead of the obsolete Romme rule
- support of negative Republican years (i. e. 17 Messidor -3 for 14 July 1789)
- conversion exact to the microsecond
- Republican- and decimal-time-specific formatting functions
- custom `republican_strftime` method for formatting Republican dates
- full support of the day names of the French Republican Calendar

## Examples

### Republican calendar
Printing today's date:
```python
>>> import republican_datetime as rdatetime
>>>
>>> d = rdatetime.date.today()
>>> d.isoformat()
'0227-08-21'
>>> d.historical_format()
'21 Floréal an CCXXVII'
>>> d.year
227
>>> d.month
8
>>> d.day
21
```

Converting a Gregorian date:
```python
>>> import datetime
>>>
>>> g = datetime.date(year=2018, month=10, day=25)
>>> d = rdatetime.date.from_gregorian(g)
>>> d.historical_format()
'3 Brumaire an CCXXVII'
```

Converting a Republican date:
```python
>>> d = rdatetime.date(year=227, month=4, day=17)
>>> g = d.to_gregorian()
>>> g.isoformat()
'2019-01-07'
```

### Decimal time

Sexagesimal (normal) time to decimal time conversion:
```python
>>> s = datetime.time(hour=15, minute=3, second=45)
>>> t = rdatetime.time.from_sexagesimal(s)
>>> t.isoformat()  # H.MM.SS
'6.27.60'
```

Decimal time to sexagesimal time:
```python
>>> t = rdatetime.time(hour=4, minute=75, second=39)
>>> s = t.to_sexagesimal()
>>> t.isoformat()
'11:24:33.696000'
```

### `datetime` and `timedelta` classes

```python
>>> t1 = rdatetime.datetime.now()
>>> t1.date().historical_format()
'5 Thermidor 227'
>>> t1.time().isoformat()
'7.39.62'
>>>
>>> t2 = rdatetime.datetime.now()
>>> delta = t2-t1
>>> str(delta) # H.MM.SS.UUUUUU
0.00.25.601462
```

### `republican_strftime` formatting

```python
>>> t = rdatetime.datetime.now()
>>> s = t1.republican_strftime("Today is %A, %d %B %Y, %e.%nCurrent time is %H.%M.%S"))
>>> print (s)
Today is Duodi, 22 Floréal 227, Fritillaire.
Current time is 7.25.45
```

## Function outline
As this library is a fork of the standard `datetime` library, their usages are basically
identical. For the official Python's `datetime` library,
see [datetime](https://docs.python.org/3/library/datetime.html).

The following is a detailed function outline of the included classes. Function
arguments an return values are equivalent to their standard `datetime` counterparts.
The custom functions should be pretty self-explanatory.

- `class datetime`:
  - Constructors:
    - `__init__(year, month, day, hour, minute, second, tzinfo=None, fold=0)`
    - `combine(date, time)`
    - `from_gregorian(gregorian_datetime)`
    - `fromtimestamp(unixtime, tz=None)`
    - `now(tz=None)`
  - Methods:
    - `astimezone(tz)`
    - `date()`
    - `dst()`
    - `isoformat()`
    - `replace(year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=None, fold=None)`
    - `republican_strftime(format_string)`
    - `time()`
    - `timestamp()`
    - `timetz()`
    - `to_gregorian()`
    - `tzname()`
    - `utcoffset()`
  - Properties (Republican calendar and decimal time fields):
    - `year`
    - `month`
    - `day`
    - `hour`
    - `minute`
    - `second`
    - `microsecond`
    - `tzinfo`
    - `fold`



- `class date`:
  - Constructors:
    - `__init__(year, month, day)`
    - `from_gregorian(gregorian_date)`
    - `fromordinal(ordinal)`
    - `fromtimestamp(unixtime)`
    - `today()`
  - Methods:
    - `historical_format()`
    - `isoformat()`
    - `replace(year=None, month=None, day=None)`
    - `republican_strftime(format_string)`
    - `to_gregorian()`
    - `toordinal()`
    - `totimestamp()`
  - Properties (Republican calendar fields):
    - `year`
    - `month`
    - `day`



- `class time`:
  - Constructors:
    - `__init__(hour, minute, second, tzinfo=None, fold=0)`
    - `from_sexagesimal(sexagesimal_time)`
  - Methods:
    - `dst()`
    - `isoformat()`
    - `replace(hour=None, minute=None, second=None, microsecond=None, tzinfo=None, fold=None)`
    - `republican_strftime(format_string)`
    - `to_sexagesimal()`
    - `tzname()`
    - `utcoffset()`
  - Properties (decimal time fields):
    - `hour`
    - `minute`
    - `second`
    - `microsecond`
    - `tzinfo`
    - `fold`



- `class timedelta`:
  - Constructors:
    - `__init__(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, decades=0)`
    - `from_sexagesimal(standard_timedelta)`
  - Methods:
    - `to_sexagesimal()`
    - `total_seconds()`
  - Properties (decimal time fields):
    - `days`
    - `seconds`
    - `microseconds`

#### Constants
- `MONTH_NAMES`: list of all month names (like 'Thermidor')
- `MONTHS_ABBRVS`: list off all month names (abbreviated, like 'The')

- `DECADE_DAYS`: list of all decade days (like 'Primidi')
- `DECADE_DAYS`_ABBRVS: list of all decade days (abbreviated, like 'Pri')

- `DAY_NAMES`: list of all day names (like 'Raisin' for 1 Vendémiaire)

#### `republican_strftime` arguments

- `%%`: the character '%'
- `%a`: abbreviated day of decade (like 'Pri') or day name in the Sans-Cullotides (like 'Fête de la Vertu')
- `%A`: day of decade (like 'Primidi')
- `%b`: abbreviated name of month (like 'Vne')
- `%B`: name of month (like 'Vendémiaire)
- `%c`: date and time formatted like Quintidi, 15 Floréal 5.58.73
- `%C`: century
- `%d`: day of month
- `%e`: name of day (like 'Raisin')
- `%F`: date in ISO format (like '0227-08-21')
- `%H`: decimal hour
- `%j`: day of year
- `%m`: month
- `%M`: decimal minute
- `%n`: newline (\n)
- `%N`: decimal nanosecond
- `%q`: quarter of year (1 for autumn months, 2 for winter months, 3 for spring months and 4 for summer months)
- `%R`: time (H.MM)
- `%S`: decimal second
- `%t`: tab (\t)
- `%T`: time (H.MM.SS)
- `%u`: number of day of decade (1-10 for Primidi-Décadi)
- `%U`: decade number of year
- `%X`: year in Roman numerals (uppercase)
- `%x`: year in Roman numerals (lowercase)
- `%y`: last 2 digits of year
- `%Y`: year
- `%Z`: time zone

## Calculation of the autumn equinoxes
The calculation of the exact time of the autumn equinox is crucial for the correct conversion.
Currently, the autumn equinoxes are calculated by taking a reference autumn equinox (currently
23 September 2018 CE, 01:54 UTC) and repeatedly adding or subtracting the average length of the tropical
year (currently 365.2421896698 ephemeris days).

## License
This project is licensed under the GNU GPLv3 License - see
[LICENSE.md](LICENSE.md) for details.




