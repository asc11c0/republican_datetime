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
- conversion exact to the microsecond
- full time zone support
- Republican- and decimal-time-specific formatting functions
- custom `republican_strftime` method for formatting Republican dates
- full support of the day names of the French Republican Calendar

## Examples

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
>>> import republican_datetime as rdatetime
>>> import datetime
>>>
>>> g = datetime.date(year=2018, month=10, day=25)
>>> d = rdatetime.date.from_gregorian(g)
>>> d.historical_format()
'3 Brumaire an CCXXVII'
```

Converting a Republican date:
```python
>>> import republican_datetime as rdatetime
>>> import datetime
>>>
>>> d = rdatetime.date(year=227, month=4, day=17)
>>> g = d.to_gregorian()
>>> g.isoformat()
'2019-01-07'
```

Sexagesimal (normal) time to decimal time conversion:
```python
>>> import republican_datetime as rdatetime
>>> import datetime
>>>
>>> s = datetime.time(hour=15, minute=3, second=45)
>>> t = rdatetime.time.from_sexagesimal(s)
>>> t.isoformat()
'6.27.60'
```

Decimal time to sexagesimal time:
```python
>>> import republican_datetime as rdatetime
>>> import datetime
>>>
>>> t = rdatetime.time(hour=4, minute=75, second=39)
>>> s = t.to_sexagesimal()
>>> t.isoformat()
'11:24:33.696000'
```
