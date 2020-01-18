import xlrd as xl


class Titan(object):
    def __init__(self, file=None, progress=None):
        self.file = file
        self.progress = progress
        self.progress.setStyleSheet(
            "border: 2px solid grey;"
            "border-radius: 5px;"
            "text-align: center;"
            "}"
            "QProgressBar::chunk {"
            "background-color: #05B8CC;"
            "width: 20px;}"
            "QProgressBar::chunk[urgent=true] {"
            "background-color: red;"
            "}"
        )

        self.book = xl.open_workbook(self.file)
        self.sheet = self.book.sheet_by_index(0)

        self.len_column = self.sheet.ncols
        self.len_row = self.sheet.nrows

        self.dict_row = [0] * self.len_column
        self.dict_column = {}
        self.sorted_list = []

    def read_xlsx(self):
        if self.sheet.cell(1, 12).value != 'ООО \"ТИТАН ЛОГИСТИК\"':
            Exception.with_traceback('')
        else:
            dict_sort = {}
            for count in range(1, self.len_row):
                for i in range(self.len_column):
                    self.dict_row[i] = self.sheet.cell(count, i).value
                self.dict_column[count] = list(self.dict_row)
                self.progress.setValue(count)

            for i in range(1, self.len_row):
                for j in range(1, self.len_column):
                    if self.dict_column[i][j] == 'НАИМЕНОВАНИЕ ПРОДУКТА':
                        for col in range((i + 2), self.len_row - 2):
                            dict_sort[col] = [
                                elem for elem in self.dict_column[col]
                                if elem is not None
                                if elem != ''
                                if elem != 0
                            ]
            self.sorted_list = sorted(dict_sort.values(), key=lambda x: x[1])
            return self.sorted_list

    def get_data(self):
        return self.sorted_list
