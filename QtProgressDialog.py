#!/usr/bin/env python
# --*--codig: utf8 --*--

from PyQt5 import QtWidgets, QtCore

class BaseProgressDialog(QtWidgets.QWidget):
    updateProgress = QtCore.pyqtSignal(int)
    def __init__(self, text='', parent=None):
        super(BaseProgressDialog, self).__init__(parent)
        self.setFixedHeight(50)
        self.text  = text
        self.progressbar = QtWidgets.QProgressBar( )
        self.progressbar.setTextVisible(True)
        self.updateProgress.connect(self.addValue)

        self.bottomBorder = QtWidgets.QWidget( )
        self.bottomBorder.setStyleSheet("""
            background: palette(shadow);
        """)
        self.bottomBorder.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed))
        self.bottomBorder.setMinimumHeight(1)

        self.label  = QtWidgets.QLabel(self.text)
        self.label.setStyleSheet("""
            font-weight: bold;
        """)
        self.layout = QtWidgets.QVBoxLayout( )
        self.layout.setContentsMargins(10,0,10,0)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.progressbar)

        self.mainLayout = QtWidgets.QVBoxLayout( )
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.addLayout(self.layout)
        self.mainLayout.addWidget(self.bottomBorder)
        self.setLayout(self.mainLayout)
        self.totalValue = 0

    def addValue(self, value):
        self.totalValue += value
        self.progressbar.setValue(self.totalValue)

    def setValue(self, value):
        self.totalValue = value
        self.progressbar.setValue(self.totalValue)
        
    def setMax(self, value):
        self.progressbar.setMaximum(value)

    def getMax(self):
        return self.progressbar.maximum()
        
class DownloadProgressBar(BaseProgressDialog):
    def __init__(self, text='Downloading', parent=None):
        super(self.__class__, self).__init__(text, parent)
        style ="""
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: #37DA7E;
            width: 20px;
        }"""
        self.progressbar.setStyleSheet(style)


class UploadProgressBar(BaseProgressDialog):
    def __init__(self, text='Uploading', parent=None):
        super(self.__class__, self).__init__(text, parent)
        style ="""
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }

        QProgressBar::chunk {
            background-color: #88B0EB;
            width: 20px;
        }"""
        self.progressbar.setStyleSheet(style)

class ProgressDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(self.__class__, self).__init__(parent)
        self.resize(500, 250)
        self.scrollArea = QtWidgets.QScrollArea( )
        self.scrollArea.setWidgetResizable(True)
        self.setCentralWidget(self.scrollArea)

        self.centralWidget = QtWidgets.QWidget( )
        self.scrollArea.setWidget(self.centralWidget)

        self.layout = QtWidgets.QVBoxLayout( )
        self.layout.setAlignment(QtCore.Qt.AlignTop)
        self.layout.setContentsMargins(0,10,0,0)
        self.centralWidget.setLayout(self.layout)

    def addProgressbar(self, progressbar):
        self.layout.addWidget(progressbar)

if __name__ == "__main__":
    import random

    app = QtWidgets.QApplication([])
    progressNumbers = [x for x in range(1, 101)]
    progressItems = []

    while len(progressItems) <= 20:
        progressItems.append(random.choice(progressNumbers))

    progressDialog = ProgressDialog()

    for progressItem in progressItems:
        progressBar = DownloadProgressBar(text="download")
        progressBar.setMax(100)
        progressBar.setValue(' ' * progressItem)
        progressDialog.addProgressbar(progressBar)

    for progressItem in progressItems:
        progressBar = UploadProgressBar(text="Upload")
        progressBar.setMax(100)
        progressBar.setValue(' ' * progressItem)
        progressDialog.addProgressbar(progressBar)

    progressDialog.show()
    app.exec_()
