import sys
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableView, QLineEdit,
                             QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLabel)
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

class AstronautModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.query = QSqlQuery()
        self.query.prepare("SELECT * FROM astronaut")
        self.query.exec_()

    def rowCount(self, parent=None):
        return self.query.size()

    def columnCount(self, parent=None):
        return 5

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            self.query.seek(index.row())
            return QVariant(self.query.value(index.column()))
        return QVariant()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Astronaut Database")
        self.resize(800, 600)

        # Add a table view and set the model
        self.table_view = QTableView(self)
        self.model = AstronautModel(self)
        self.table_view.setModel(self.model)

        # Add widgets for inserting, deleting, and editing records
        self.first_name_edit = QLineEdit(self)
        self.last_name_edit = QLineEdit(self)
        self.birthdate_edit = QLineEdit(self)
        self.country_edit = QLineEdit(self)
        self.insert_button = QPushButton("Insert", self)
        self.insert_button.clicked.connect(self.insert_record)
        self.delete_button = QPushButton("Delete", self)
        self.delete_button.clicked.connect(self.delete)
