import xlrd as xl


class Titan(object):
    def __init__(self, file=None, progress=None):
        self.file = file
        self.progress = progress

        self.book = xl.open_workbook(self.file)
        self.sheet = self.book.sheet_by_index(0)

        self.len_column = self.sheet.ncols
        self.len_row = self.sheet.nrows

    def read_xlsx(self):
        if self.len_row == 0:
            return 0
        else:
            if self.sheet.cell(1, 12).value != 'ООО \"ТИТАН ЛОГИСТИК\"':
                return 0
            else:
                dict_column = {}
                dict_row = [0] * self.len_column
                dict_sort = {}
                for count in range(1, self.len_row):
                    for i in range(self.len_column):
                        dict_row[i] = self.sheet.cell(count, i).value
                    dict_column[count] = list(dict_row)
                    self.progress.setValue(count)

                for i in range(1, self.len_row):
                    for j in range(1, self.len_column):
                        if dict_column[i][j] == 'НАИМЕНОВАНИЕ ПРОДУКТА':
                            for col in range((i + 2), self.len_row - 2):
                                dict_sort[col] = [
                                    elem for elem in dict_column[col]
                                    if elem is not None
                                    if elem != ''
                                    if elem != 0
                                ]
                sorted_list = sorted(dict_sort.values(), key=lambda x: x[1])
                return sorted_list
