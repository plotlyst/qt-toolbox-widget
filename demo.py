import sys

from qtpy.QtWidgets import QApplication, QLabel
from qtpy.QtWidgets import QMainWindow

from qttoolbox import ToolBox


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.widget = ToolBox(self)
        self.setCentralWidget(self.widget)
        self.widget.addItem(QLabel('Test 1'), 'Title 1')
        self.widget.addItem(QLabel('Test 2'), 'Title 2')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    sys.exit(app.exec())
