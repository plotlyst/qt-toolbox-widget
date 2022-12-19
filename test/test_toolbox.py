from qttoolbox import ToolBox


def test_add_item(qtbot):
    toolbox = ToolBox()
    qtbot.addWidget(toolbox)
    toolbox.show()
