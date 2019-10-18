import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
# pyuic5 ui_file.ui -o py_form.py   - Преобразование ui-файла в py-файл

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Действие (Action) будет использоваться при нажатии на кнопку
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        # Создание кнопки в панели инструментов
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        # Установка заголовка и размеров главного окна
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
