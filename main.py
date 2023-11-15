""" Mádosfokú egyenlet megoldása pythonban"""
import math


class EgyenletMegoldo():
    """ egyenlet megoldó osztály"""
    def masodfoku_egyenlet_megoldo(self, a, b, c):
        """ másodfokú egyenlet megoldó metódus"""

        if type(a) not in [int, float] or type(b) not in [int, float] or type(c) not in [int, float]:
            raise TypeError('Csak int vagy float típus elfogadható!')

        d = math.pow(b, 2) - (4 * a * c)

        if d < 0:
            return None, None

        return (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)

    def feladat_megoldo(self, a, b, c):
        """feladatmegoldó, mai a másodfokú egyenlet megoldó eredményét írja ki"""
        e = EgyenletMegoldo()
        x1, x2 = e.masodfokuEgyenletMegoldo(a, b, c)

        print(f"{a}x^2 + {b}x + {c} = 0")

        if (x1 is None) and (x2 is None):
            print("Nincs megoldás")
        elif x1 == x2:
            print(f"Egy megoldás van: {x1}")
        else:
            print(f"Két megoldás van: x1={x1}, x2={x2}")

#e = egyenletMegoldo()
#e.feladatMegoldo(1, 2, 8)
#e.feladatMegoldo(1, -14, 49)
#e.feladatMegoldo(1, 6, 8)
#e.feladatMegoldo("alma", 1, "körte")