from functools import partial
from typing import List

from qthandy import hbox, transparent, vbox, vspacer, margins
from qtpy.QtCore import Signal, QEvent, QObject
from qtpy.QtGui import QIcon, QMouseEvent
from qtpy.QtWidgets import QWidget, QToolButton, QLineEdit


class ToolBoxHeader(QWidget):
    selected = Signal(bool)

    def __init__(self, text: str = '', parent=None):
        super(ToolBoxHeader, self).__init__(parent)
        self._selected: bool = False

        hbox(self, margin=0)
        self.icon = QToolButton(self)
        transparent(self.icon)
        self.icon.setHidden(True)
        self.title = QLineEdit(self)
        transparent(self.title)
        self.title.setText(text)
        self.title.setReadOnly(True)
        self.title.editingFinished.connect(lambda: self.title.setReadOnly(True))
        self.title.installEventFilter(self)

        self.layout().addWidget(self.icon)
        self.layout().addWidget(self.title)

    def setIcon(self, icon: QIcon):
        self.icon.setIcon(icon)
        self.icon.setVisible(True)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.MouseButtonDblClick and self.title.isReadOnly():
            self.mouseDoubleClickEvent(event)
        elif event.type() == QEvent.Type.MouseButtonRelease and self.title.isReadOnly():
            self.mouseReleaseEvent(event)

        return super(ToolBoxHeader, self).eventFilter(watched, event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if not self._selected:
            self.selected.emit(True)
        self.setSelected(True)

    def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
        self.title.setReadOnly(False)
        self.title.setFocus()

    def setSelected(self, selected: bool):
        self._selected = selected


class ToolBoxItem(QWidget):
    def __init__(self, widget: QWidget, title: str, icon: QIcon = None, parent=None):
        super(ToolBoxItem, self).__init__(parent)
        self._header = ToolBoxHeader(title)
        self._center = QWidget()
        vbox(self._center, 0, 0).addWidget(widget)
        margins(self._center, left=4)
        self._center.setHidden(True)
        if icon:
            self._header.setIcon(icon)

        vbox(self)
        self.layout().addWidget(self._header)
        self.layout().addWidget(self._center)
        self._header.selected.connect(self._center.setVisible)

    def header(self) -> ToolBoxHeader:
        return self._header

    def setSelected(self, selected: bool):
        self._center.setVisible(selected)
        self._header.setSelected(selected)


class ToolBox(QWidget):
    def __init__(self, parent=None):
        super(ToolBox, self).__init__(parent)
        vbox(self)
        self._items: List[ToolBoxItem] = []
        self.layout().addWidget(vspacer())

    def addItem(self, widget, title: str, icon: QIcon = None):
        item = ToolBoxItem(widget, title, icon)
        self._items.append(item)
        item.header().selected.connect(partial(self._itemToggled, item))
        self.layout().insertWidget(self.layout().count() - 1, item)

    def _itemToggled(self, selectedItem: ToolBoxItem, toggled: bool):
        for item in self._items:
            if item is not selectedItem:
                item.setSelected(False)
