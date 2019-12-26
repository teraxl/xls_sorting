# coding=utf-8


class UnionReport(object):
    def __init__(self, ar_karton=None, titan=None):
        self._ar_karton = ar_karton
        self._titan = titan
        self.ak = self._titan.__len__()
        self.tl = self._ar_karton.__len__()
        self.len_m = 0

    def Union(self):

        for i in range(self._titan.__len__()):
            self._titan[i][0] = i + 1
            temp = self._titan[i][1]
            self._titan[i][1] = self._titan[i][2]
            self._titan[i][2] = temp
            del self._titan[i][3]
            del self._titan[i][4]
            del self._titan[i][5]

        for i in range(self._titan.__len__()):
            temp = self._titan[i][3]
            self._titan[i][3] = self._titan[i][5]
            self._titan[i][5] = temp

        for i in range(self._ar_karton.__len__()):
            self._ar_karton[i][0] = i + 1
            temp = self._ar_karton[i][1]
            self._ar_karton[i][1] = self._ar_karton[i][2]
            self._ar_karton[i][2] = temp

        if (self.tl - self.ak) > 0:
            self.len_m = self.tl - (abs(self.tl - self.ak))
        else:
            self.len_m = self.ak - (abs(self.tl - self.ak))

        self.full_massiv = {}
        self.m_result = ['', '', '']

        for elem in range(self.len_m - 1):
            if self._titan[elem][2] == self._ar_karton[elem][2]:
                self.full_massiv[elem] = self._titan[elem]
                if (self._titan[elem][3] - self._ar_karton[elem][3]) != 0:
                    if (self._titan[elem][3] - self._ar_karton[elem][3]) > 0:
                        self.m_result[1] = 1
                        self.full_massiv[elem] += self.m_result
                        self.full_massiv[elem] += self._ar_karton[elem]
                    else:
                        self.m_result[1] = -1
                        self.full_massiv[elem] += self.m_result
                        self.full_massiv[elem] += self._ar_karton[elem]
                else:
                    del self._titan[elem]
                    del self._ar_karton[elem]
                    self.len_m -= 1
                    continue
            else:
                if self._titan[elem][2] == self._ar_karton[elem + 1][2]:
                    del self._ar_karton[elem]

        for i in self.full_massiv.keys():
            print(self.full_massiv[i])




