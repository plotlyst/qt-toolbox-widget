from qtpy.QtWidgets import QLabel

from qttoolbox import ToolBox


def test_add_item(qtbot):
    toolbox = ToolBox()
    qtbot.addWidget(toolbox)
    toolbox.show()

    toolbox.addItem(QLabel('Test'), 'Title 1')
