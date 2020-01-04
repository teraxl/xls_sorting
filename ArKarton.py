import xlrd as xl


class ArKarton(object):
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

        self.sorted_list = None

    def read_xls(self):
        if not self.sheet.cell(1, 1).value in 'Company:':
            return 0
        else:
            dict_column = {}
            dict_row = [0] * self.len_column
            dict_sort = {}
            for count in range(self.len_row):
                for i in range(self.len_column):
                    dict_row[i] = self.sheet.cell_value(count, i)
                dict_column[count] = list(dict_row)
                self.progress.setValue(count)

            for i in range(self.len_row):
                for j in range(self.len_column):
                    if dict_column[i][j] == 'EACH':
                        dict_sort[i] = [
                            elem for elem in dict_column[i]
                            if elem != ' '
                            if elem != ''
                            if elem != 'EACH'
                            if elem != 'TOTAL'
                        ]

            self.sorted_list = sorted(dict_sort.values(), key=lambda x: x[1])
            return self.sorted_list

    def get_data(self):
        return self.sorted_list

