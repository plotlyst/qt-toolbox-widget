import sys

from qtpy.QtWidgets import QApplication, QLabel
from qtpy.QtWidgets import QMainWindow

from qttoolbox import ToolBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.toolbox = ToolBox(self)
        self.toolbox.currentChanged.connect(lambda i, w: print(f'{i} {w}'))
        self.setCentralWidget(self.toolbox)
        self.toolbox.addItem(QLabel('Test 1'), 'Title 1')
        self.toolbox.addItem(QLabel('Test 2'), 'Title 2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
