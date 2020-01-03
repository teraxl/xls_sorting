# coding=utf-8
import openpyxl
from openpyxl import Workbook


class UnionReport(object):
    def __init__(self, ar_karton=None, titan=None):
        self._ar_karton = ar_karton
        self._titan = titan
        self.ak = self._titan.__len__()
        self.tl = self._ar_karton.__len__()
        self.len_m = 0
        self.file_name = 'Отчет__.xlsx'

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
                if (self._titan[elem][3] - self._ar_karton[elem][3]) != 0:
                    if (self._titan[elem][3] - self._ar_karton[elem][3]) > 0:
                        self.full_massiv[elem] = self._titan[elem]
                        self.m_result[1] = self._titan[elem][3] - self._ar_karton[elem][3]
                        self.full_massiv[elem] += self.m_result
                        self.full_massiv[elem] += self._ar_karton[elem]
                    else:
                        self.full_massiv[elem] = self._titan[elem]
                        self.m_result[1] = self._titan[elem][3] - self._ar_karton[elem][3]
                        self.full_massiv[elem] += self.m_result
                        self.full_massiv[elem] += self._ar_karton[elem]
                else:
                    continue
            else:
                if self._titan[elem][2] == self._ar_karton[elem + 1][2]:
                    del self._ar_karton[elem]

        # for i in self.full_massiv.keys():
        #     print(self.full_massiv[i])

    def create_xls(self):
        wb = Workbook(write_only=False)
        ws = wb.active
        ws.title = 'Общий отчет'

        r_mass = [[0] * self.full_massiv.keys().__len__()] * 15
        split_list = list(self.full_massiv.values())

        ws.merge_cells('A1:F1')
        ws.merge_cells('J1:O1')
        ws['A1'] = 'Титан Логистик'
        ws['H1'] = 'Результат'
        ws['J1'] = 'АР Картон'

        column_count = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,
            'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14
        }

        for c_key, c_values in column_count.items():
            ws.column_dimensions[c_key].width = int(self.max_value(split_list, c_values))

        ws.column_dimensions['G'].width = 0.83
        ws.column_dimensions['I'].width = 0.83

        # Заполнение данных Титан-Логистик
        for i in range(split_list.__len__()):
            for j in range(split_list[i].__len__()):
                ws.cell(i + 2, j + 1).value = split_list[i][j]

        wb.save(self.file_name)

    def max_value(self, array, val_c):
        value_max = len(str(array[1][val_c]))
        for i in range(1, array.__len__()):
            for j in range(array[i - 1].__len__()):
                if value_max < len(str(array[i][val_c])):
                    value_max = len(str(array[i][val_c]))
                else:
                    continue
        return value_max + 3
