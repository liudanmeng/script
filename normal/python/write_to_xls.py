import xlwt

workbook = xlwt.Workbook(encoding='utf-8')
booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

with open('result_analysis', 'r') as f:
    line = f.readline()
    index = 0
    while line:
        tmp = line.split('"""')
        entity = tmp[0].strip()
        categories = eval(tmp[1].strip())

        booksheet.write(index, 0, entity)
        for i in range(len(categories)):
            booksheet.write(index, i + 1, categories[i][0] + ':' + str(categories[i][1]))

        line = f.readline()
        index += 1

    workbook.save('test_xlwt.xls')
