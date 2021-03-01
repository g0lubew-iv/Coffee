import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class CoffeeWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.con = sqlite3.connect("coffee.db")
        self.load_results()

    def load_results(self):
        cur = self.con.cursor()
        try:
            result = cur.execute(f"SELECT * FROM Drinks").fetchall()
        except Exception as error:
            self.statusBar().showMessage(error.__str__())
            self.tableWidget.setRowCount(0)
            return
        result.insert(0, ("ID", "Название сорта", "Степень обжарки (в градусах по Цельсию)", "Молотый",
                          "Дополнительное описание вкуса", "Цена", "Объем упаковки"))
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeWidget()
    ex.show()
    sys.exit(app.exec())
