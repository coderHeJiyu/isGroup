from PyQt5.QtWidgets import QTableWidget


class Calculate:
    def __init__(self, table: QTableWidget):
        self.tableWidget = table
        self.table_size = table.rowCount()
        self.ie = None
        self.wrong_str = None

    def get_ie(self):
        return str(self.ie)

    def get_wrong_str(self):
        return self.wrong_str

    def calculate(self, i, j):
        return self.tableWidget.cellWidget(i - 1, j - 1).value()

    def is_semigroup(self):
        """判断是不是半群"""
        n = self.table_size + 1
        cal = self.calculate
        for i in range(1, n):
            for j in range(1, n):
                for k in range(1, n):
                    a = cal(i, cal(j, k))
                    b = cal(cal(i, j), k)
                    if a != b:
                        self.wrong_str = "\n一个错误的例子是：\n" + str(i) + "*(" + str(j) + "*" + str(k) + ")=" + str(
                            a) + "\n而\n(" + str(i) + "*" + str(j) + ")*" + str(k) + "=" + str(b)
                        return False
        return True

    def is_monoid(self):
        """判断是不是独异点"""
        n = self.table_size + 1
        cal = self.calculate
        for i in range(1, n):
            lie = True
            for j in range(1, n):
                if cal(i, j) != j:
                    lie = False
                    break
            if lie:
                rie = True
                for j in range(1, n):
                    if cal(j, i) != j:
                        rie = False
                        break
                if rie:
                    self.ie = i
        if self.ie is not None:
            return True
        return False

    def is_group(self):
        """判断是不是群"""
        n = self.table_size + 1
        cal = self.calculate
        for i in range(1, n):
            inverse = False
            for j in range(1, n):
                if cal(i, j) == self.ie and cal(j, i) == self.ie:
                    inverse = True
                    break
            if not inverse:
                self.wrong_str = "\n比如，元素" + str(i) + "不存在逆元"
                return False
        return True
