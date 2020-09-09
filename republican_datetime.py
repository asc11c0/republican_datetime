# French republican calendar and decimal clock library.
# Copyright (C) 2019 CE / 227 RE  Andreas Hollmeier
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import datetime as _datetime
import time as _time
import math as _math



MINYEAR = _datetime.MINYEAR - 1792
MAXYEAR = _datetime.MAXYEAR - 1793

TROPICAL_YEAR = _datetime.timedelta(days=365.2421896698)
REFERENCE_EQUINOX = _datetime.datetime(year=2018, month=9, day=23, hour=1, minute=54)  # UTC
REFERENCE_YEAR = 227

MONTH_NAMES = ["", "Vendémiaire", "Brumaire", "Frimaire", "Nivose", "Pluviose", "Ventose", "Germinal", "Floréal",
               "Prairial", "Messidor", "Thermidor", "Fructidor", "Sansculotides"]
MONTHS_ABBRVS = ["", "Vne", "Bru", "Fri", "Niv", "Plu", "Vno", "Ger", "Flo", "Pra", "Mes", "The", "Fru", "San"]
DECADE_DAYS = ["Primidi", "Duodi", "Tridi", "Quartidi", "Quintidi", "Sextidi", "Septidi", "Octidi", "Nonidi", "Décadi"]
DECADE_DAYS_ABBRVS = ["Pri", "Duo", "Tri", "Qua", "Qui", "Sex", "Sep", "Oct", "Non", "Dec"]
DAY_NAMES = ['Raisin', 'Safran', 'Châtaigne', 'Colchique', 'Cheval', 'Balsamine', 'Carotte', 'Amaranthe', 'Panais',
             'Cuve', 'Pomme de terre', 'Immortelle', 'Potiron', 'Réséda', 'Âne', 'Belle de nuit', 'Citrouille',
             'Sarrasin', 'Tournesol', 'Pressoir', 'Chanvre', 'Pêche', 'Navet', 'Amaryllis', 'Bœuf', 'Aubergine',
             'Piment', 'Tomate', 'Orge', 'Tonneau', 'Pomme', 'Céleri', 'Poire', 'Betterave', 'Oie', 'Héliotrope',
             'Figue', 'Scorsonère', 'Alisier', 'Charrue', 'Salsifis', 'Mâcre', 'Topinambour', 'Endive', 'Dindon',
             'Chervis', 'Cresson', 'Dentelaire', 'Grenade', 'Herse', 'Bacchante', 'Azerole', 'Garance', 'Orange',
             'Faisan', 'Pistache', 'Macjonc', 'Coing', 'Cormier', 'Rouleau', 'Raiponce', 'Turneps', 'Chicorée',
             'Nèfle', 'Cochon', 'Mâche', 'Chou-fleur', 'Miel', 'Genièvre', 'Pioche', 'Cire', 'Raifort', 'Cèdre',
             'Sapin', 'Chevreuil', 'Ajonc', 'Cyprès', 'Lierre', 'Sabine', 'Hoyau', 'Érable à sucre', 'Bruyère',
             'Roseau', 'Oseille', 'Grillon', 'Pignon', 'Liège', 'Truffe', 'Olive', 'Pelle', 'Tourbe', 'Houille',
             'Bitume', 'Soufre', 'Chien', 'Lave', 'Terre végétale', 'Fumier', 'Salpêtre', 'Fléau', 'Granit', 'Argile',
             'Ardoise', 'Grès', 'Lapin', 'Silex', 'Marne', 'Pierre à chaux', 'Marbre', 'Van', 'Pierre à plâtre', 'Sel',
             'Fer', 'Cuivre', 'Chat', 'Étain', 'Plomb', 'Zinc', 'Mercure', 'Crible', 'Lauréole', 'Mousse', 'Fragon',
             'Perce-neige', 'Taureau', 'Laurier-thym', 'Amadouvier', 'Mézéréon', 'Peuplier', 'Coignée', 'Ellébore',
             'Brocoli', 'Laurier', 'Avelinier', 'Vache', 'Buis', 'Lichen', 'If', 'Pulmonaire', 'Serpette', 'Thlaspi',
             'Thimelé', 'Chiendent', 'Trainasse', 'Lièvre', 'Guède', 'Noisetier', 'Cyclamen', 'Chélidoine', 'Traîneau',
             'Tussilage', 'Cornouiller', 'Violier', 'Troène', 'Bouc', 'Asaret', 'Alaterne', 'Violette', 'Marceau',
             'Bêche', 'Narcisse', 'Orme', 'Fumeterre', 'Vélar', 'Chèvre', 'Épinard', 'Doronic', 'Mouron', 'Cerfeuil',
             'Cordeau', 'Mandragore', 'Persil', 'Cochléaria', 'Pâquerette', 'Thon', 'Pissenlit', 'Sylvie', 'Capillaire',
             'Frêne', 'Plantoir', 'Primevère', 'Platane', 'Asperge', 'Tulipe', 'Poule', 'Bette', 'Bouleau', 'Jonquille',
             'Aulne', 'Couvoir', 'Pervenche', 'Charme', 'Morille', 'Hêtre', 'Abeille', 'Laitue', 'Mélèze', 'Ciguë',
             'Radis', 'Ruche', 'Gainier', 'Romaine', 'Marronnier', 'Roquette', 'Pigeon', 'Lilas', 'Anémone', 'Pensée',
             'Myrtille', 'Greffoir', 'Rose', 'Chêne', 'Fougère', 'Aubépine', 'Rossignol', 'Ancolie', 'Muguet',
             'Champignon', 'Hyacinthe', 'Râteau', 'Rhubarbe', 'Sainfoin', "Bâton d'or", 'Chamerisier', 'Ver à soie',
             'Consoude', 'Pimprenelle', "Corbeille d'or", 'Arroche', 'Sarcloir', 'Statice', 'Fritillaire', 'Bourrache',
             'Valériane', 'Carpe', 'Fusain', 'Civette', 'Buglosse', 'Sénevé', 'Houlette', 'Luzerne', 'Hémérocalle',
             'Trèfle', 'Angélique', 'Canard', 'Mélisse', 'Fromental', 'Martagon', 'Serpolet', 'Faux', 'Fraise',
             'Bétoine', 'Pois', 'Acacia', 'Caille', 'Œillet', 'Sureau', 'Pavot', 'Tilleul', 'Fourche', 'Barbeau',
             'Camomille', 'Chèvrefeuille', 'Caille-lait', 'Tanche', 'Jasmin', 'Verveine', 'Thym', 'Pivoine', 'Chariot',
             'Seigle', 'Avoine', 'Oignon', 'Véronique', 'Mulet', 'Romarin', 'Concombre', 'Échalote', 'Absinthe',
             'Faucille', 'Coriandre', 'Artichaut', 'Girofle', 'Lavande', 'Chamois', 'Tabac', 'Groseille', 'Gesse',
             'Cerise', 'Parc', 'Menthe', 'Cumin', 'Haricot', 'Orcanète', 'Pintade', 'Sauge', 'Ail', 'Vesce', 'Blé',
             'Chalémie', 'Épeautre', 'Bouillon blanc', 'Melon', 'Ivraie', 'Bélier', 'Prêle', 'Armoise', 'Carthame',
             'Mûre', 'Arrosoir', 'Panic', 'Salicorne', 'Abricot', 'Basilic', 'Brebis', 'Guimauve', 'Lin', 'Amande',
             'Gentiane', 'Écluse', 'Carline', 'Câprier', 'Lentille', 'Aunée', 'Loutre', 'Myrte', 'Colza', 'Lupin',
             'Coton', 'Moulin', 'Prune', 'Millet', 'Lycoperdon', 'Escourgeon', 'Saumon', 'Tubéreuse', 'Sucrion',
             'Apocyn', 'Réglisse', 'Échelle', 'Pastèque', 'Fenouil', 'Épine vinette', 'Noix', 'Truite', 'Citron',
             'Cardère', 'Nerprun', 'Tagette', 'Hotte', 'Églantier', 'Noisette', 'Houblon', 'Sorgho', 'Écrevisse',
             'Bigarade', "Verge d'or", 'Maïs', 'Marron', 'Panier', 'Fête de la Vertu', 'Fête du Génie',
             'Fête du Travail', "Fête de l'Opinion", 'Fête des Récompenses', 'Fête de la Révolution']


def _cmp(x, y):
    return 0 if x == y else 1 if x > y else -1


def _divide_and_round(a, b):
    """divide a by b and round result to the nearest integer

    When the ratio is exactly half-way between two integers,
    the even integer is returned.
    """
    # Based on the reference implementation for divmod_near
    # in Objects/longobject.c.
    q, r = divmod(a, b)
    # round up if either r / b > 0.5, or r / b == 0.5 and q is odd.
    # The expression r / b > 0.5 is equivalent to 2 * r > b if b is
    # positive, 2 * r < b if b negative.
    r *= 2
    greater_than_half = r > b if b > 0 else r < b
    if greater_than_half or r == b and q % 2 == 1:
        q += 1

    return q


roman_numerals = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


def _roman_numeral(i):
    if i == 0:
        return "0"
    if i < 0:
        return "-"+_roman_numeral(-i)

    roman = ''
    while i > 0:
        for d, r in roman_numerals:
            while i >= d:
                roman += r
                i -= d
    return roman


def _set_time_to_midnight(d):
    return d.replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=None)


def _find_1_vendemiaire_and_year(d):
    year = REFERENCE_YEAR
    if _set_time_to_midnight(REFERENCE_EQUINOX).replace(tzinfo=None) > d:
        # scroll back until a valid equinox has been found
        equinox = REFERENCE_EQUINOX
        while _set_time_to_midnight(equinox).replace(tzinfo=None) > d:
            equinox -= TROPICAL_YEAR
            year -= 1
        return _set_time_to_midnight(equinox), year

    else:
        # scroll forward until a valid equinox has been found
        equinox = REFERENCE_EQUINOX
        while _set_time_to_midnight(equinox+TROPICAL_YEAR).replace(tzinfo=None) < d:
            equinox += TROPICAL_YEAR
            year += 1
        return _set_time_to_midnight(equinox), year


def _start_of_republican_year(year):
    return _set_time_to_midnight(REFERENCE_EQUINOX+TROPICAL_YEAR*(year-REFERENCE_YEAR))


def _is_sextile_year(republican_year):
    equinox = REFERENCE_EQUINOX + (republican_year - REFERENCE_YEAR) * TROPICAL_YEAR
    next_equinox = equinox + TROPICAL_YEAR
    length_days = next_equinox
    year_length = next_equinox - equinox
    if year_length.days == 365:
        return True
    elif year_length.days == 366:
        return False


def _convert_decimal_to_sexagesimal(dec_hour, dec_minute, dec_second, dec_microsecond):
    total_seconds = round(dec_hour * 8640 + dec_minute * 86.4 + dec_second * 0.864 + dec_microsecond * 0.864e-6, 5)
    hour = int(total_seconds // 3600) % 24
    minute = int(total_seconds//60) % 60
    second = int(total_seconds) % 60
    microsecond = int((total_seconds % 1)*1000000)
    return hour, minute, second, microsecond


def _convert_sexagesimal_to_decimal(hour=0, minute=0, second=0, microsecond=0):
    total_dec_seconds = round((hour*3600 + minute*60 + second + microsecond/1000000)/0.864, 6)
    dec_hour = int(total_dec_seconds//10000) % 10
    dec_minute = int(total_dec_seconds//100) % 100
    dec_seconds = int(total_dec_seconds)     % 100
    dec_microseconds = int((total_dec_seconds % 1)*1000000)
    return dec_hour, dec_minute, dec_seconds, dec_microseconds


def _convert_to_republican(d):
    d = d.replace(tzinfo=None)
    start, year = _find_1_vendemiaire_and_year(d)
    delta = d - start
    hour, minute, second, microsecond = _convert_sexagesimal_to_decimal(second=delta.seconds,
                                                                        microsecond=delta.microseconds)
    return year, int(delta.days) // 30 + 1, int(delta.days) % 30 + 1, hour, minute, second, microsecond


def _check_int_field(value):
    if isinstance(value, int):
        return value
    if not isinstance(value, float):
        try:
            value = value.__int__()
        except AttributeError:
            pass
        else:
            if isinstance(value, int):
                return value
            raise TypeError('__int__ returned non-int (type %s)' %
                            type(value).__name__)
        raise TypeError('an integer is required (got type %s)' %
                        type(value).__name__)
    raise TypeError('integer argument expected, got float')


def _check_date_fields(year, month, day):
    year = _check_int_field(year)
    month = _check_int_field(month)
    day = _check_int_field(day)

    if not MINYEAR <= year <= MAXYEAR:
        raise ValueError("year must be in %d..%d" % (MINYEAR, MAXYEAR))
    if not 1 <= month <= 13:
        raise ValueError("month must be in 1..13")
    if not ((month != 13 and 1 <= day <= 30) or (month == 13 and 1 <= day <= 5+_is_sextile_year(year))):
        raise ValueError("day must be in 1..30 or 1..5/6 in the epagomenal days")
    return year, month, day


def _check_time_fields(hour, minute, second, microsecond, fold):
    hour = _check_int_field(hour)
    minute = _check_int_field(minute)
    second = _check_int_field(second)
    microsecond = _check_int_field(microsecond)
    fold = _check_int_field(fold)

    if not 0 <= hour <= 9:
        raise ValueError("hour must be in 0..9")
    if not 0 <= minute <= 99:
        raise ValueError("minute must be in 0..9")
    if not 0 <= second <= 99:
        raise ValueError("second must be in 0..9")
    if not 0 <= microsecond <= 999999:
        raise ValueError("microsecond must be in 0..999999")
    if not 0 <= fold <= 1:
        raise ValueError("fold must be in 0..1")
    return hour, minute, second, microsecond, fold


def _check_tzinfo_arg(tz):
    if tz is not None and not isinstance(tz, tzinfo):
        raise TypeError("tzinfo argument must be None or of a tzinfo subclass")


def _check_tzname(name):
    if name is not None and not isinstance(name, str):
        raise TypeError("tzinfo.tzname() must return None or string, "
                        "not '%s'" % type(name))


def _republican_strftime(d, fmt):

    if hasattr(d, "day") and hasattr(d, "month"):
        downame = DECADE_DAYS[(d.day-1)%10]
        if d.month == 13:
           downame = DAY_NAMES[359+d.day]

    out = ""
    i = 0
    while i < len(fmt):
        if fmt[i] != "%":
            out += fmt[i]
            i += 1
        else:
            i += 1
            chr = fmt[i]
            if chr == "%": out += "%"
            elif chr == "a": out += DECADE_DAYS_ABBRVS[(d.day-1)%10]
            elif chr == "A": out += downame
            elif chr == "b": out += MONTHS_ABBRVS[d.month]
            elif chr == "B": out += MONTH_NAMES[d.month]
            elif chr == "c": out += "%s, %d %s %d.%02d.%02d" % (downame, d.day, MONTH_NAMES[d.month],
                                                              d.hour, d.minute, d.second)
            elif chr == "C": out += str(d.year//100)
            elif chr == "d": out += str(d.day)
            elif chr == "e": out += DAY_NAMES[(d.month-1)*30+d.day-1]
            elif chr == "F": out += "%04d-%02d-%02d" % (d.year, d.month, d.day)
            elif chr == "H": out += str(d.hour)
            elif chr == "j": out += str((d.month-1)*30+d.day)
            elif chr == "m": out += "%02d" % d.month
            elif chr == "M": out += "%02d" % d.minute
            elif chr == "n": out += "\n"
            elif chr == "N": out += "%09d" % (d.microsecond*1000)
            elif chr == "q": out += str((d.month-1)//3+1)
            elif chr == "R": out += "%02d.%02d" % (d.hour, d.minute)
            elif chr == "S": out += "%02d" % d.second
            elif chr == "t": out += "\t"
            elif chr == "T": out += "%d.%02d.%02d" % (d.hour, d.minute, d.second)
            elif chr == "u": out += str((d.day-1)%10+1)
            elif chr == "U": out += str((d.month-1)*3+(d.day-1)//10+1)
            elif chr == "X": out += _roman_numeral(d.year)
            elif chr == "x": out += _roman_numeral(d.year).lower()
            elif chr == "y": out += "%02d" % (d.year%100)
            elif chr == "Y": out += str(d.year)
            elif chr == "Z": out += d.tzstr()

            else:
                raise ValueError("unrecognized format string '%%%s'" % chr)

            i += 1

    return out

# Republican timedelta class, using decades, decimal hours, minutes, and seconds.
# Mostly copy-pasted from datetime.py, too.
# All date and time fields are republican unless stated otherwise.
class timedelta:
    """Represent the difference between two datetime objects.

    Supported operators:

    - add, subtract timedelta
    - unary plus, minus, abs
    - compare to timedelta
    - multiply, divide by int

    In addition, datetime supports subtraction of two datetime objects
    returning a timedelta, and addition or subtraction of a datetime
    and a timedelta giving a datetime.

    Representation: (days, seconds, microseconds).
    """
    __slots__ = '_days', '_seconds', '_microseconds', '_hashcode'

    def __new__(cls, days=0, seconds=0, microseconds=0,
                milliseconds=0, minutes=0, hours=0, decades=0):
        # Doing this efficiently and accurately in C is going to be difficult
        # and error-prone, due to ubiquitous overflow possibilities, and that
        # C double doesn't have enough bits of precision to represent
        # microseconds over 10K years faithfully.  The code here tries to make
        # explicit where go-fast assumptions can be relied on, in order to
        # guide the C implementation; it's way more convoluted than speed-
        # ignoring auto-overflow-to-long idiomatic Python could be.

        # XXX Check that all inputs are ints or floats.

        # Final values, all integer.
        # s and us fit in 32-bit signed ints; d isn't bounded.
        d = s = us = 0

        # Normalize everything to days, seconds, microseconds.
        days += decades*10
        seconds += minutes*100 + hours*10000
        microseconds += milliseconds*1000

        # Get rid of all fractions, and normalize s and us.
        # Take a deep breath <wink>.
        if isinstance(days, float):
            dayfrac, days = _math.modf(days)
            daysecondsfrac, daysecondswhole = _math.modf(dayfrac * (10.*10000.))
            assert daysecondswhole == int(daysecondswhole)  # can't overflow
            s = int(daysecondswhole)
            assert days == int(days)
            d = int(days)
        else:
            daysecondsfrac = 0.0
            d = days
        assert isinstance(daysecondsfrac, float)
        assert abs(daysecondsfrac) <= 1.0
        assert isinstance(d, int)
        assert abs(s) <= 10*10000
        # days isn't referenced again before redefinition

        if isinstance(seconds, float):
            secondsfrac, seconds = _math.modf(seconds)
            assert seconds == int(seconds)
            seconds = int(seconds)
            secondsfrac += daysecondsfrac
            assert abs(secondsfrac) <= 2.0
        else:
            secondsfrac = daysecondsfrac
        # daysecondsfrac isn't referenced again
        assert isinstance(secondsfrac, float)
        assert abs(secondsfrac) <= 2.0

        assert isinstance(seconds, int)
        days, seconds = divmod(seconds, 10*10000)
        d += days
        s += int(seconds)    # can't overflow
        assert isinstance(s, int)
        assert abs(s) <= 2 * 10 * 10000
        # seconds isn't referenced again before redefinition

        usdouble = secondsfrac * 1e6
        assert abs(usdouble) < 2.1e6    # exact value not critical
        # secondsfrac isn't referenced again

        if isinstance(microseconds, float):
            microseconds = round(microseconds + usdouble)
            seconds, microseconds = divmod(microseconds, 1000000)
            days, seconds = divmod(seconds, 10*10000)
            d += days
            s += seconds
        else:
            microseconds = int(microseconds)
            seconds, microseconds = divmod(microseconds, 1000000)
            days, seconds = divmod(seconds, 10*10000)
            d += days
            s += seconds
            microseconds = round(microseconds + usdouble)
        assert isinstance(s, int)
        assert isinstance(microseconds, int)
        assert abs(s) <= 3 * 10 * 10000
        assert abs(microseconds) < 3.1e6

        # Just a little bit of carrying possible for microseconds and seconds.
        seconds, us = divmod(microseconds, 1000000)
        s += seconds
        days, s = divmod(s, 10*10000)
        d += days

        assert isinstance(d, int)
        assert isinstance(s, int) and 0 <= s < 10*10000
        assert isinstance(us, int) and 0 <= us < 1000000

        if abs(d) > 999999999:
            raise OverflowError("timedelta # of days is too large: %d" % d)

        self = object.__new__(cls)
        self._days = d
        self._seconds = s
        self._microseconds = us
        self._hashcode = -1
        return self

    @classmethod
    def from_sexagesimal(cls, d):
        if d == None:
            return None
        return cls(days=d.days, seconds=d.seconds/0.864, microseconds=d.microseconds/0.864)

    def to_sexagesimal(self):
        return _datetime.timedelta(days=self._days, seconds=self._seconds*0.864, microseconds=self._microseconds*0.864)

    def __repr__(self):
        if self._microseconds:
            return "%s.%s(%d, %d, %d)" % (self.__class__.__module__,
                                          self.__class__.__qualname__,
                                          self._days,
                                          self._seconds,
                                          self._microseconds)
        if self._seconds:
            return "%s.%s(%d, %d)" % (self.__class__.__module__,
                                      self.__class__.__qualname__,
                                      self._days,
                                      self._seconds)
        return "%s.%s(%d)" % (self.__class__.__module__,
                              self.__class__.__qualname__,
                              self._days)

    def __str__(self):
        mm, ss = divmod(self._seconds, 100)
        hh, mm = divmod(mm, 100)
        s = "%d.02d.%02d" % (hh, mm, ss)
        if self._days:
            def plural(n):
                return n, abs(n) != 1 and "s" or ""
            s = ("%d day%s, " % plural(self._days)) + s
        if self._microseconds:
            s = s + ".%06d" % self._microseconds
        return s

    def total_seconds(self):
        """Total seconds in the duration."""
        return ((self.days * 100000 + self.seconds) * 10**6 +
                self.microseconds) / 10**6

    # Read-only field accessors
    @property
    def days(self):
        """days"""
        return self._days

    @property
    def seconds(self):
        """seconds"""
        return self._seconds

    @property
    def microseconds(self):
        """microseconds"""
        return self._microseconds

    def __add__(self, other):
        if isinstance(other, timedelta):
            # for CPython compatibility, we cannot use
            # our __class__ here, but need a real timedelta
            return timedelta(self._days + other._days,
                             self._seconds + other._seconds,
                             self._microseconds + other._microseconds)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, timedelta):
            # for CPython compatibility, we cannot use
            # our __class__ here, but need a real timedelta
            return timedelta(self._days - other._days,
                             self._seconds - other._seconds,
                             self._microseconds - other._microseconds)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, timedelta):
            return -self + other
        return NotImplemented

    def __neg__(self):
        # for CPython compatibility, we cannot use
        # our __class__ here, but need a real timedelta
        return timedelta(-self._days,
                         -self._seconds,
                         -self._microseconds)

    def __pos__(self):
        return self

    def __abs__(self):
        if self._days < 0:
            return -self
        else:
            return self

    def __mul__(self, other):
        if isinstance(other, int):
            return timedelta(self._days * other,
                             self._seconds * other,
                             self._microseconds * other)
        if isinstance(other, float):
            usec = self._to_microseconds()
            a, b = other.as_integer_ratio()
            return timedelta(0, 0, _divide_and_round(usec * a, b))
        return NotImplemented

    __rmul__ = __mul__

    def _to_microseconds(self):
        return ((self._days * (10*10000) + self._seconds) * 1000000 +
                self._microseconds)

    def __floordiv__(self, other):
        if not isinstance(other, (int, timedelta)):
            return NotImplemented
        usec = self._to_microseconds()
        if isinstance(other, timedelta):
            return usec // other._to_microseconds()
        if isinstance(other, int):
            return timedelta(0, 0, usec // other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float, timedelta)):
            return NotImplemented
        usec = self._to_microseconds()
        if isinstance(other, timedelta):
            return usec / other._to_microseconds()
        if isinstance(other, int):
            return timedelta(0, 0, _divide_and_round(usec, other))
        if isinstance(other, float):
            a, b = other.as_integer_ratio()
            return timedelta(0, 0, _divide_and_round(b * usec, a))

    def __mod__(self, other):
        if isinstance(other, timedelta):
            r = self._to_microseconds() % other._to_microseconds()
            return timedelta(0, 0, r)
        return NotImplemented

    def __divmod__(self, other):
        if isinstance(other, timedelta):
            q, r = divmod(self._to_microseconds(),
                          other._to_microseconds())
            return q, timedelta(0, 0, r)
        return NotImplemented

    # Comparisons of timedelta objects with other.

    def __eq__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) == 0
        else:
            return False

    def __le__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) <= 0
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) < 0
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) >= 0
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, timedelta):
            return self._cmp(other) > 0
        else:
            return NotImplemented

    def _cmp(self, other):
        assert isinstance(other, timedelta)
        return _cmp(self._getstate(), other._getstate())

    def __hash__(self):
        if self._hashcode == -1:
            self._hashcode = hash(self._getstate())
        return self._hashcode

    def __bool__(self):
        return (self._days != 0 or
                self._seconds != 0 or
                self._microseconds != 0)

    # Pickle support.

    def _getstate(self):
        return (self._days, self._seconds, self._microseconds)

    def __reduce__(self):
        return (self.__class__, self._getstate())


timedelta.min = timedelta(-999999999)
timedelta.max = timedelta(days=999999999, hours=9, minutes=9, seconds=9,
                          microseconds=999999)
timedelta.resolution = timedelta(microseconds=1)


# This class has mostly been copy-pasted from datetime.py, with some edits for the republican calendar.
# Gregorian-format-specific functions have been removed. Functions for converting to and from the republican calendar
# have been added.
# All date fields are republican unless stated otherwise.
class date:
    """Concrete republican date type.

    Constructors:

    __new__()
    fromtimestamp()
    today()
    fromordinal()

    Operators:

    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__, __format__
    __add__, __radd__, __sub__ (add/radd only with timedelta arg)

    Methods:

    isoformat(), strftime(), to_gregorian(), totimestamp(), toordinal()

    Properties (readonly):
    year, month, day
    """
    __slots__ = '_year', '_month', '_day', '_hashcode'

    def __new__(cls, year, month=None, day=None):
        """Constructor.

        Arguments:

        year, month, day (required, base 1)
        """
        if month is None and isinstance(year, bytes) and len(year) == 4 and \
                1 <= year[2] <= 13:
            # Pickle support
            self = object.__new__(cls)
            self.__setstate(year)
            self._hashcode = -1
            return self
        year, month, day = _check_date_fields(year, month, day)
        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        self._hashcode = -1
        return self

    # Additional constructors

    @classmethod
    def fromtimestamp(cls, t):
        "Construct a date from a POSIX timestamp (like time.time())."
        return cls.from_gregorian(_datetime.datetime.fromtimestamp(t))

    @classmethod
    def from_gregorian(cls, d):
        "Construct a date from a standard Gregorian date class."
        if not isinstance(d, _datetime.date):
            raise TypeError("d has to be a datetime.date object")
        year, month, day, hour, minute, second, microsecond = _convert_to_republican(
            _datetime.datetime.combine(d, _datetime.time(hour=0, minute=0, second=0)))
        return cls(year, month, day)

    @classmethod
    def fromordinal(cls, o):
        """Construct a Republican date from a proleptic Gregorian ordinal."""
        year = 1
        month = 1
        day = 1
        rem_o = o-654415  # 654415 = 1 Vendemiaire an 1
        if rem_o >= 0:
            while rem_o >= 365+_is_sextile_year(year):
                rem_o -= 365 + _is_sextile_year(year)
                year += 1
        else:
            while rem_o <= -(365+_is_sextile_year(year-1)):
                rem_o += (365+_is_sextile_year(year-1))
                year -= 1
            if rem_o < 0:
                year -= 1
                rem_o += 365+_is_sextile_year(year)
        month += rem_o // 30
        day += rem_o % 30
        return cls(year=year, month=month, day=day)

    @classmethod
    def today(cls):
        "Construct a date from time.time()."
        t = _time.time()
        return cls.fromtimestamp(t)

    def __repr__(self):
        return "%s.%s(%d, %d, %d)" % (self.__class__.__module__,
                                      self.__class__.__qualname__,
                                      self._year,
                                      self._month,
                                      self._day)

    def republican_strftime(self, fmt):
        return _republican_strftime(self, fmt)

    def __format__(self, fmt):
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.republican_strftime(fmt)
        return str(self)

    def isoformat(self):
        return "%04d-%02d-%02d" % (self._year, self._month, self._day)

    def historical_format(self):
        """Equivalent to republican_strftime("%d %B an %X")"""
        return self.republican_strftime("%d %B an %X")

    __str__ = isoformat

    # Read-only field accessors
    @property
    def year(self):
        return self._year

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    def replace(self, year=None, month=None, day=None):
        """Return a new date with new values for the specified fields."""
        if year is None:
            year = self._year
        if month is None:
            month = self._month
        if day is None:
            day = self._day
        return type(self)(year, month, day)

    def to_gregorian(self):
        start = _start_of_republican_year(self.year)
        return start.date() + _datetime.timedelta(days=(self.month - 1) * 30 + self.day - 1)

    def totimestamp(self):
        return _time.mktime(self.to_gregorian().timetuple())

    def toordinal(self):
        """Return proleptic Gregorian ordinal."""
        o = 0
        if self._year >= 1:
            for y in range(1, self._year):
                o += 365+_is_sextile_year(y)
        else:
            for y in range(1, self._year, -1):
                o -= 365+_is_sextile_year(y-1)
        o += (self._month-1)*30
        o += self._day-1
        return o+654415  # 654415 = 1 Vendemiaire an 1

    def __eq__(self, other):
        if isinstance(other, date):
            return self._cmp(other) == 0
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, date):
            return self._cmp(other) <= 0
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, date):
            return self._cmp(other) < 0
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, date):
            return self._cmp(other) >= 0
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, date):
            return self._cmp(other) > 0
        return NotImplemented

    def _cmp(self, other):
        assert isinstance(other, date)
        y, m, d = self._year, self._month, self._day
        y2, m2, d2 = other._year, other._month, other._day
        return _cmp((y, m, d), (y2, m2, d2))

    def __hash__(self):
        "Hash."
        if self._hashcode == -1:
            self._hashcode = hash(self._getstate())
        return self._hashcode

    # Computations

    def __add__(self, other):
        "Add a date to a timedelta."
        if isinstance(other, timedelta) or isinstance(other, _datetime.timedelta):
            return _date_class.fromordinal(self.toordinal()+other.days)
        return NotImplemented

    __radd__ = __add__

    def __sub__(self, other):
        """Subtract two dates, or a date and a timedelta."""
        if isinstance(other, timedelta) or isinstance(other, _datetime.timedelta):
            return self + timedelta(-other.days)
        if isinstance(other, date):
            delta_days = self.toordinal()-other.toordinal()
            return _datetime.timedelta(days=delta_days)
        return NotImplemented

    def _getstate(self):
        yhi, ylo = divmod(self._year, 256)
        return bytes([yhi, ylo, self._month, self._day]),

    def __setstate(self, string):
        yhi, ylo, self._month, self._day = string
        self._year = yhi * 256 + ylo

    def __reduce__(self):
        return self.__class__, self._getstate()


_date_class = date
date.min = date(MINYEAR, 1, 1)
date.max = date(MAXYEAR, 13, 5)
date.resolution = timedelta(days=1)
_MAXORDINAL = date.max.toordinal()

tzinfo = _datetime.tzinfo


# Decimal time class. Mostly copy-pasted from datetime.py, too, with minor edits for the decimal time format and
# conversion functions.
# The original time zone class has not been modified, as time zones are defined in the common sexagesimal time format.
# All time fields are decimal unless stated otherwise.
class time:
    """Decimal time with (sexagesimal) time zone.

    Constructors:

    __new__()
    from_sexagesimal()

    Operators:

    __repr__, __str__
    __eq__, __le__, __lt__, __ge__, __gt__, __hash__

    Methods:

    strftime()
    isoformat()
    utcoffset()
    tzname()
    dst()
    to_sexagesimal()

    Properties (readonly):
    hour, minute, second, microsecond, tzinfo, fold
    """
    __slots__ = '_hour', '_minute', '_second', '_microsecond', '_tzinfo', '_hashcode', '_fold'

    def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
        """Constructor.

        Arguments:

        hour, minute (required)
        second, microsecond (default to zero)
        tzinfo (default to None)
        fold (keyword only, default to zero)
        """
        if isinstance(hour, bytes) and len(hour) == 6 and hour[0]&0x7F < 24:
            # Pickle support
            self = object.__new__(cls)
            self.__setstate(hour, minute or None)
            self._hashcode = -1
            return self
        hour, minute, second, microsecond, fold = _check_time_fields(
            hour, minute, second, microsecond, fold)
        _check_tzinfo_arg(tzinfo)
        self = object.__new__(cls)
        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond
        self._tzinfo = tzinfo
        self._hashcode = -1
        self._fold = fold
        return self

    @classmethod
    def from_sexagesimal(cls, t):
        if not isinstance(t, _datetime.time):
            raise TypeError("t has to be a datetime.time object")
        hour, minute, second, microsecond = _convert_sexagesimal_to_decimal(t.hour, t.minute, t.second, t.microsecond)
        return cls(hour=hour, minute=minute, second=second, microsecond=microsecond, tzinfo=t.tzinfo, fold=t.fold)

    # Read-only field accessors
    @property
    def hour(self):
        """hour (0-23)"""
        return self._hour

    @property
    def minute(self):
        """minute (0-59)"""
        return self._minute

    @property
    def second(self):
        """second (0-59)"""
        return self._second

    @property
    def microsecond(self):
        """microsecond (0-999999)"""
        return self._microsecond

    @property
    def tzinfo(self):
        """timezone info object"""
        return self._tzinfo

    @property
    def fold(self):
        return self._fold

    # Standard conversions, __hash__ (and helpers)

    # Comparisons of time objects with other.

    def __eq__(self, other):
        if isinstance(other, time):
            return self._cmp(other, allow_mixed=True) == 0
        else:
            return False

    def __le__(self, other):
        if isinstance(other, time):
            return self._cmp(other) <= 0
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, time):
            return self._cmp(other) < 0
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, time):
            return self._cmp(other) >= 0
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, time):
            return self._cmp(other) > 0
        else:
            return NotImplemented

    def _cmp(self, other, allow_mixed=False):
        assert isinstance(other, time)
        mytz = self._tzinfo
        ottz = other._tzinfo
        myoff = otoff = None

        if mytz is ottz:
            base_compare = True
        else:
            myoff = self.utcoffset()
            otoff = other.utcoffset()
            base_compare = myoff == otoff

        if base_compare:
            return _cmp((self._hour, self._minute, self._second,
                         self._microsecond),
                        (other._hour, other._minute, other._second,
                         other._microsecond))
        if myoff is None or otoff is None:
            if allow_mixed:
                return 2 # arbitrary non-zero value
            else:
                raise TypeError("cannot compare naive and aware times")
        myhhmm = self._hour * 100 + self._minute - (myoff//timedelta(minutes=1))*1.44 # conversion from sexagesimal time zone offset
        othhmm = other._hour * 100 + other._minute - (otoff//timedelta(minutes=1))*1.44
        return _cmp((myhhmm, self._second, self._microsecond),
                    (othhmm, other._second, other._microsecond))

    def __hash__(self):
        """Hash."""
        if self._hashcode == -1:
            self._hashcode = hash((self.hour, self.minute, self.second, self.microsecond, self.fold))
        return self._hashcode

    # Conversion to string

    def _tzstr(self, sep="."):
        """Return formatted timezone offset (+xx.xx) or None."""
        off = self.utcoffset()
        if off is not None:
            if off.days < 0:
                sign = "-"
                off = -off
            else:
                sign = "+"
            hh, mm = divmod(off, timedelta(hours=1))
            mm, ss = divmod(mm, timedelta(minutes=1))
            assert 0 <= hh < 24
            off = "%s%02d%s%02d" % (sign, hh, sep, mm)
            if ss:
                off += sep+'%02d' % ss.seconds
        return off

    def __repr__(self):
        """Convert to formal string, for repr()."""
        if self._microsecond != 0:
            s = ", %d, %d" % (self._second, self._microsecond)
        elif self._second != 0:
            s = ", %d" % self._second
        else:
            s = ""
        s= "%s.%s(%d, %d%s)" % (self.__class__.__module__,
                                self.__class__.__qualname__,
                                self._hour, self._minute, s)
        if self._tzinfo is not None:
            assert s[-1:] == ")"
            s = s[:-1] + ", tzinfo=%r" % self._tzinfo + ")"
        if self._fold:
            assert s[-1:] == ")"
            s = s[:-1] + ", fold=1)"
        return s

    def isoformat(self):
        """Return the time formatted in an ISO-like way, substituting colons with dots.
        """
        s = "%d.%02d.%02d" % (self.hour, self.minute, self.second)
        tz = self._tzstr()
        if tz:
            s += tz
        return s

    __str__ = isoformat

    def republican_strftime(self, fmt):
        return _republican_strftime(self, fmt)

    def __format__(self, fmt):
        if not isinstance(fmt, str):
            raise TypeError("must be str, not %s" % type(fmt).__name__)
        if len(fmt) != 0:
            return self.strftime(fmt)
        return str(self)

    # Timezone functions

    def utcoffset(self):
        return timedelta.from_sexagesimal(self.to_sexagesimal().utcoffset())

    def tzname(self):
        return self.to_sexagesimal().tzname()

    def dst(self):
        return timedelta.from_sexagesimal(self.to_sexagesimal().dst())

    def replace(self, hour=None, minute=None, second=None, microsecond=None,
                tzinfo=True, *, fold=None):
        """Return a new time with new values for the specified fields."""
        if hour is None:
            hour = self.hour
        if minute is None:
            minute = self.minute
        if second is None:
            second = self.second
        if microsecond is None:
            microsecond = self.microsecond
        if tzinfo is True:
            tzinfo = self.tzinfo
        if fold is None:
            fold = self._fold
        return type(self)(hour, minute, second, microsecond, tzinfo, fold=fold)

    def to_sexagesimal(self):
        hour, minute, second, microsecond = _convert_decimal_to_sexagesimal(self.hour, self.minute, self.second,
                                                                            self.microsecond)
        return _datetime.time(hour, minute, second, microsecond, tzinfo=self.tzinfo, fold=self.fold)

    def _getstate(self, protocol=3):
        us2, us3 = divmod(self._microsecond, 256)
        us1, us2 = divmod(us2, 256)
        h = self._hour
        if self._fold and protocol > 3:
            h += 128
        basestate = bytes([h, self._minute, self._second,
                           us1, us2, us3])
        if self._tzinfo is None:
            return (basestate,)
        else:
            return (basestate, self._tzinfo)

    def __setstate(self, string, tzinfo):
        if tzinfo is not None and not isinstance(tzinfo, _tzinfo_class):
            raise TypeError("bad tzinfo state arg")
        h, self._minute, self._second, us1, us2, us3 = string
        if h > 127:
            self._fold = 1
            self._hour = h - 128
        else:
            self._fold = 0
            self._hour = h
        self._microsecond = (((us1 << 8) | us2) << 8) | us3
        self._tzinfo = tzinfo

    def __reduce_ex__(self, protocol):
        return (time, self._getstate(protocol))

    def __reduce__(self):
        return self.__reduce_ex__(2)


_time_class = time
time.min = time(0, 0, 0)
time.max = time(9, 99, 99, 999999)
time.resolution = timedelta(microseconds=1)

# Republican datetime class mostly copy-pasted from datetime.py with some minor edits for the republican/decimal
# datetime format and conversion functions.
# All datetime fields are republican and decimal unless stated otherwise.
class datetime(date):
    """datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

    The year, month and day arguments are required. tzinfo may be None, or an
    instance of a tzinfo subclass. The remaining arguments may be ints.
    """
    __slots__ = date.__slots__ + time.__slots__

    def __new__(cls, year, month=None, day=None, hour=0, minute=0, second=0,
                microsecond=0, tzinfo=None, *, fold=0):
        if isinstance(year, bytes) and len(year) == 10 and 1 <= year[2]&0x7F <= 13:
            # Pickle support
            self = object.__new__(cls)
            self.__setstate(year, month)
            self._hashcode = -1
            return self
        year, month, day = _check_date_fields(year, month, day)
        hour, minute, second, microsecond, fold = _check_time_fields(
            hour, minute, second, microsecond, fold)
        _check_tzinfo_arg(tzinfo)
        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        self._hour = hour
        self._minute = minute
        self._second = second
        self._microsecond = microsecond
        self._tzinfo = tzinfo
        self._hashcode = -1
        self._fold = fold
        return self

    # Read-only field accessors
    @property
    def hour(self):
        """hour (0-23)"""
        return self._hour

    @property
    def minute(self):
        """minute (0-59)"""
        return self._minute

    @property
    def second(self):
        """second (0-59)"""
        return self._second

    @property
    def microsecond(self):
        """microsecond (0-999999)"""
        return self._microsecond

    @property
    def tzinfo(self):
        """timezone info object"""
        return self._tzinfo

    @property
    def fold(self):
        return self._fold

    @classmethod
    def from_gregorian(cls, d):
        if not isinstance(d, _datetime.datetime):
            raise TypeError("d has to be a datetime.datetime object")
        year, month, day, hour, minute, second, microsecond = _convert_to_republican(d)
        return cls(year=year, month=month, day=day, hour=hour, minute=minute, second=second, microsecond=microsecond,
                   tzinfo=d.tzinfo, fold=d.fold)

    @classmethod
    def now(cls, tz=None):
        return cls.fromtimestamp(_time.time(), tz=tz)

    @classmethod
    def fromtimestamp(cls, t, tz=None):
        return cls.from_gregorian(_datetime.datetime.fromtimestamp(t, tz=tz))

    @classmethod
    def combine(cls, date, time, tzinfo=True):
        "Construct a datetime from a given date and a given time."
        if not isinstance(date, _date_class):
            raise TypeError("date argument must be a date instance")
        if not isinstance(time, _time_class):
            raise TypeError("time argument must be a time instance")
        if tzinfo is True:
            tzinfo = time.tzinfo
        return cls(date.year, date.month, date.day,
                   time.hour, time.minute, time.second, time.microsecond,
                   tzinfo=tzinfo, fold=time.fold)

    def to_gregorian(self):
        d = date.to_gregorian(self)
        t = self.time().to_sexagesimal()
        return _datetime.datetime.combine(d, t)

    def timestamp(self):
        return self.to_gregorian().timestamp()

    def date(self):
        "Return the date part."
        return date(self._year, self._month, self._day)

    def time(self):
        "Return the time part, with tzinfo None."
        return time(self.hour, self.minute, self.second, self.microsecond, tzinfo=self.tzinfo, fold=self.fold)

    def timetz(self):
        "Return the time part, with same tzinfo."
        return time(self.hour, self.minute, self.second, self.microsecond,
                    self._tzinfo, fold=self.fold)

    def replace(self, year=None, month=None, day=None, hour=None,
                minute=None, second=None, microsecond=None, tzinfo=True,
                *, fold=None):
        """Return a new datetime with new values for the specified fields."""
        if year is None:
            year = self.year
        if month is None:
            month = self.month
        if day is None:
            day = self.day
        if hour is None:
            hour = self.hour
        if minute is None:
            minute = self.minute
        if second is None:
            second = self.second
        if microsecond is None:
            microsecond = self.microsecond
        if tzinfo is True:
            tzinfo = self.tzinfo
        if fold is None:
            fold = self.fold
        return type(self)(year, month, day, hour, minute, second,
                          microsecond, tzinfo, fold=fold)

    def astimezone(self, tz=None):
        return datetime.from_gregorian(self.to_gregorian().astimezone(tz=tz))

    def tzstr(self):
        off = self.utcoffset()
        if off is not None:
            if off.days < 0:
                sign = "-"
                off = -off
            else:
                sign = "+"
            hh = off.total_seconds() // 10000
            mm = (off.total_seconds() // 100) % 100
            return "%s%02d:%02d" % (sign, hh, mm)
        return ""

    def isoformat(self, sep='T'):
        """Return the time formatted in an ISO-like way.

        The full format looks like 'YYYY-MM-DD HH.MM.SS.mmmmmm'.
        By default, the fractional part is omitted if self.microsecond == 0.

        If self.tzinfo is not None, the UTC offset is also attached, giving
        giving a full format of 'YYYY-MM-DD HH.MM.SS.mmmmmm+HH:MM'.

        Optional argument sep specifies the separator between date and
        time, default 'T'.
        """
        s = "%04d-%02d-%02d%c%d.%02d.%02d%s" % (self._year, self._month, self._day, sep, self._hour, self._minute,
                                                self._second, (".%06d" % self._microsecond) if self._microsecond != 0 else "")
        s += self.tzstr()
        return s

    def republican_strftime(self, fmt):
        return _republican_strftime(self, fmt)

    def __repr__(self):
        """Convert to formal string, for repr()."""
        L = [self._year, self._month, self._day,  # These are never zero
             self._hour, self._minute, self._second, self._microsecond]
        if L[-1] == 0:
            del L[-1]
        if L[-1] == 0:
            del L[-1]
        s = "%s.%s(%s)" % (self.__class__.__module__,
                           self.__class__.__qualname__,
                           ", ".join(map(str, L)))
        if self._tzinfo is not None:
            assert s[-1:] == ")"
            s = s[:-1] + ", tzinfo=%r" % self._tzinfo + ")"
        if self._fold:
            assert s[-1:] == ")"
            s = s[:-1] + ", fold=1)"
        return s

    def __str__(self):
        "Convert to string, for str()."
        return self.isoformat(sep=' ')

    def utcoffset(self):
        """Return the timezone offset in minutes east of UTC (negative west of
        UTC)."""
        return timedelta.from_sexagesimal(self.to_gregorian().utcoffset())

    def tzname(self):
        """Return the timezone name.

        Note that the name is 100% informational -- there's no requirement that
        it mean anything in particular. For example, "GMT", "UTC", "-500",
        "-5:00", "EDT", "US/Eastern", "America/New York" are all valid replies.
        """
        return self.to_gregorian().tzname()

    def dst(self):
        """Return 0 if DST is not in effect, or the DST offset (in minutes
        eastward) if DST is in effect.

        This is purely informational; the DST offset has already been added to
        the UTC offset returned by utcoffset() if applicable, so there's no
        need to consult dst() unless you're interested in displaying the DST
        info.
        """
        return timedelta.from_sexagesimal(self.to_gregorian().dst())

    # Comparisons of datetime objects with other.

    def __eq__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other, allow_mixed=True) == 0
        elif not isinstance(other, date):
            return NotImplemented
        else:
            return False

    def __le__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other) <= 0
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other) < 0
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other) >= 0
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, datetime):
            return self._cmp(other) > 0
        else:
            return NotImplemented

    def _cmp(self, other, allow_mixed=False):
        assert isinstance(other, datetime)
        mytz = self._tzinfo
        ottz = other._tzinfo
        myoff = otoff = None

        if mytz is ottz:
            base_compare = True
        else:
            myoff = self.utcoffset()
            otoff = other.utcoffset()
            # Assume that allow_mixed means that we are called from __eq__
            if allow_mixed:
                if myoff != self.replace(fold=not self.fold).utcoffset():
                    return 2
                if otoff != other.replace(fold=not other.fold).utcoffset():
                    return 2
            base_compare = myoff == otoff

        if base_compare:
            return _cmp((self._year, self._month, self._day,
                         self._hour, self._minute, self._second,
                         self._microsecond),
                        (other._year, other._month, other._day,
                         other._hour, other._minute, other._second,
                         other._microsecond))
        if myoff is None or otoff is None:
            if allow_mixed:
                return 2 # arbitrary non-zero value
            else:
                raise TypeError("cannot compare naive and aware datetimes")
        # XXX What follows could be done more efficiently...
        diff = self - other     # this will take offsets into account
        if diff.days < 0:
            return -1
        return diff and 1 or 0

    def __add__(self, other):
        "Add a datetime and a timedelta."
        if isinstance(other, _datetime.timedelta):
            other = timedelta.from_sexagesimal(other)
        if not isinstance(other, timedelta):
            return NotImplemented

        sum_days = self.toordinal()+other.days
        sum_seconds = self._hour*10000+self._minute*100+self._second+other.seconds
        sum_days += sum_seconds//100000
        sum_seconds %= 100000
        sum_microseconds = self._microsecond+other.microseconds
        sum_seconds += sum_microseconds//1000000
        sum_microseconds %= 1000000


        if 0 < sum_days <= _MAXORDINAL:
            return datetime.combine(date.fromordinal(sum_days),
                                    time(sum_seconds//10000, (sum_seconds//100)%100, sum_seconds%100,
                                         sum_microseconds,
                                         tzinfo=self._tzinfo))
        raise OverflowError("result out of range")

    __radd__ = __add__

    def __sub__(self, other):
        "Subtract two datetimes, or a datetime and a timedelta."
        if not isinstance(other, datetime):
            if isinstance(other, timedelta):
                return self + -other
            return NotImplemented

        days1 = self.toordinal()
        days2 = other.toordinal()
        secs1 = self._second + self._minute * 100 + self._hour * 10000
        secs2 = other._second + other._minute * 100 + other._hour * 10000
        base = timedelta(days1 - days2,
                         secs1 - secs2,
                         self._microsecond - other._microsecond)
        if self._tzinfo is other._tzinfo:
            return base
        myoff = self.utcoffset()
        otoff = other.utcoffset()
        if myoff == otoff:
            return base
        if myoff is None or otoff is None:
            raise TypeError("cannot mix naive and timezone-aware time")
        return base + otoff - myoff

    def __hash__(self):
        if self._hashcode == -1:
            if self.fold:
                t = self.replace(fold=0)
            else:
                t = self
            tzoff = t.utcoffset()
            if tzoff is None:
                self._hashcode = hash(t._getstate()[0])
            else:
                delta = date(year=self.year, month=self.month, day=self.day), date(year=1, month=1, day=1)
                self._hashcode = hash(delta+timedelta(days=0, hours=self.hours, minutes=self.minutes,
                                                      seconds=self.seconds, microseconds=self.microsecond)-tzoff)
        return self._hashcode

    # Pickle support.

    def _getstate(self, protocol=3):
        yhi, ylo = divmod(self._year, 256)
        us2, us3 = divmod(self._microsecond, 256)
        us1, us2 = divmod(us2, 256)
        m = self._month
        if self._fold and protocol > 3:
            m += 128
        basestate = bytes([yhi, ylo, m, self._day,
                           self._hour, self._minute, self._second,
                           us1, us2, us3])
        if self._tzinfo is None:
            return (basestate,)
        else:
            return (basestate, self._tzinfo)

    def __setstate(self, string, tzinfo):
        if tzinfo is not None and not isinstance(tzinfo, datetime.tzinfo):
            raise TypeError("bad tzinfo state arg")
        (yhi, ylo, m, self._day, self._hour,
         self._minute, self._second, us1, us2, us3) = string
        if m > 127:
            self._fold = 1
            self._month = m - 128
        else:
            self._fold = 0
            self._month = m
        self._year = yhi * 256 + ylo
        self._microsecond = (((us1 << 8) | us2) << 8) | us3
        self._tzinfo = tzinfo

    def __reduce_ex__(self, protocol):
        return (self.__class__, self._getstate(protocol))

    def __reduce__(self):
        return self.__reduce_ex__(2)


datetime.min = datetime(MINYEAR, 1, 1)
datetime.max = datetime(MAXYEAR, 13, 5, 9, 99, 99, 999999)
datetime.resolution = timedelta(microseconds=1)


_datetime_class = datetime

