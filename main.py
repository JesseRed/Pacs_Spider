import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.setWindowTitle("Pacs Spider")
        self.ui.setupUi(self)
        #self.ui.pushButton.clicked.connect(self.press)
        self.init_gui()

    def press(self):
        print("Button 1 was pressed")

    def init_gui(self):
        print("gui will be initialized")

ui_window = MainWindow()
ui_window.show()
sys.exit(app.exec_())


#window = QtWidgets.QMainWindow()
#window.setWindowTitle("Pacs Spider")

#ui_window = Ui_MainWindow()
#ui_window.setupUi(window)
#window.show()

#sys.exit(app.exec())