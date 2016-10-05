from math import sqrt, floor
"""Övningar på iterators."""


class Cubes():
    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """
    def __init__(self):
        self.c = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.c += 1
        return self.c ** 3


class Primes():
    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """

    def __init__(self):
        self.p = 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.p += 1

            if self._is_prime(self.p):
                return self.p

    @staticmethod
    def _is_prime(x):
        n_max = floor(sqrt(x))
        n = 2
        while n <= n_max:
            if x % n == 0:
                return False
            else:
                n += 1
        return True


class Fibonacci():
    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """

    def __init__(self):
        self.tal1 = 0
        self.tal2 = 1
        self.i = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < 1:
            self.i += 1
            return self.i
        self.tal1, self.tal2 = self.tal2, self.tal1 + self.tal2
        return self.tal2


class Alphabet():
    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    def __init__(self):
        self.list = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin',
                     'Het', 'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun',
                     'Samekh', 'Ayin', 'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin',
                     'Tav']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        return char

    def char(self):
        for char in list:
            self.index += 1


class Permutations():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    pass


class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    pass
