from PyQt5.QtWidgets import QTableWidget


class Example:
    def __init__(self, table: QTableWidget):
        self.tableWidget = table

    def set_demo(self, e: list[list[int]]):
        size = 4
        for i in range(0, size):
            for j in range(0, size):
                self.tableWidget.cellWidget(i, j).setValue(e[i][j])

    def set_demo_1(self):
        e = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [3, 4, 4, 4]]
        self.set_demo(e)

    def set_demo_2(self):
        e = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
        self.set_demo(e)

    def set_demo_3(self):
        e = [[4, 3, 2, 1], [2, 2, 2, 2], [3, 3, 3, 3], [1, 2, 3, 4]]
        self.set_demo(e)

    def set_demo_4(self):
        e = [[1, 2, 3, 4], [2, 3, 4, 1], [3, 4, 1, 2], [4, 1, 2, 3]]
        self.set_demo(e)
