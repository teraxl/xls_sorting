import xlrd
import xlwt
import openpyxl


def main():
    ee_dic = {
        1: [10, 'name', '23-332', 'model_name'],
        2: [20, 'sename', '22-343', 'model_sename'],
        3: [30, 'age', '44-212', 'model_age']
    }

    mass = [[0] * 4] * 3
    maa = list(ee_dic.values())

    for i in range(maa.__len__()):
        for j in range(maa[i].__len__()):
            print(maa[i][j], end=' ')
        print()

    print(mass[0][0])
    print(maa[0][0])

    print(mass)
    print(maa)

if __name__ == '__main__':
    main()
