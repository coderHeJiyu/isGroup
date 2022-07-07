import sys
import datetime
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QSpinBox, QApplication
from PyQt5.QtCore import Qt
from mainWindow import Ui_MainWindow
from Calculate import Calculate as Cal
from Example import Example as Exp


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.table_size = 5
        self.set_table()

    def set_table(self):
        # TODO 设置表格
        self.table_size = self.spinBox.value()
        self.tableWidget.setRowCount(self.table_size)
        self.tableWidget.setColumnCount(self.table_size)
        for i in range(0, self.table_size):
            self.tableWidget.setColumnWidth(i, 100)
            for j in range(0, self.table_size):
                box = QSpinBox(self.centralwidget)
                box.setMinimum(1)
                box.setMaximum(self.table_size)
                box.setAlignment(Qt.AlignCenter)
                self.tableWidget.setCellWidget(i, j, box)

    def program_run(self):
        c = Cal(self.tableWidget)
        self.textEdit.setText(str(datetime.datetime.now())+"\n")
        if c.is_semigroup():
            self.textEdit.append("1. 该代数满足结合律，因此是半群。")
            if c.is_monoid():
                self.textEdit.append("\n2. 该半群含么元，是含么半群，其么元为" + c.get_ie() + "。")
                if c.is_group():
                    self.textEdit.append("\n3. 该含么半群的每一个元素都有逆元，因此是群。")
                else:
                    self.textEdit.append("\n3. 该含么半群的某些元素没有逆元，因此是不是群。")
            else:
                self.textEdit.append("\n2. 该半群不含么元，因此不是含么半群，也不是群。")
        else:
            self.textEdit.append("1. 该代数不满足结合律，因此不是半群，也不是含么半群或群。")
        wrong_str = c.get_wrong_str()
        if wrong_str is not None:
            self.textEdit.append(wrong_str)

    def q_action(self, q):
        if q == self.action_help:
            str_help = "1. 在界面左侧设置代数的基数，点击确定。\n2. 在界面右侧的表格中填写运算a*b的结果，点击运行。\n3. " \
                       "在界面左侧下方查看运行结果。\n\n注意：用户输入被严格限制，以此保证用户的输入一定是代数。\n此外，软件里自带" \
                       "了测试用例，可以在界面的左上角示例菜单里找到"
            QMessageBox.about(self, "使用说明", str_help)
        elif q == self.action_about:
            QMessageBox.about(self, "作者信息", "X02014155  何济宇\n\n        离散作业")
        else:
            exp = Exp(self.tableWidget)
            self.spinBox.setValue(4)
            self.set_table()
            if q == self.action1:
                exp.set_demo_1()
            elif q == self.action2:
                exp.set_demo_2()
            elif q == self.action3:
                exp.set_demo_3()
            else:
                exp.set_demo_4()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
