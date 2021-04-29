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
        self.ui.pushButton_select_excel_file.clicked.connect(self.select_excel_file)
        self.ui.pushButton_load_into_orthanc_by_excel.clicked.connect(self.load_into_orthanc_by_excel)
        self.ui.pushButton_select_download_dir.clicked.connect(self.select_download_dir)
        self.ui.pushButton_download_from_orthanc_to_drive.clicked.connect(self.download_from_orthanc_to_drive)
        self.ui.pushButton_start_orthanc.clicked.connect(self.start_orthanc)
        self.ui.pushButton_load_into_orthanc_by_notion.clicked.connect(self.load_into_orthanc_by_notion)
        self.ui.pushButton_getwebsitetoenter.clicked.connect(self.getwebsitetoenter)
        self.init_gui()

    def start_orthanc(self):
        print(f"starting orthanc")
        
    def getwebsitetoenter(self):
        print(f"getwegsitetoenter")

    def select_excel_file(self):
        print(f"select_excel_file with {self.ui.lineEdit_excel_absolute_file_path.text()}")

    def load_into_orthanc_by_excel(self):
        #lineEdit_excel_absolute_file_path
        print(f"load_into_orthanc_by_excel with {self.ui.lineEdit_excel_absolute_file_path.text()}")


    def load_into_orthanc_by_notion(self):
        print(f"load_into_orthanc_by_notion with")
        print(f"Column PatientID = {self.ui.lineEdit_ncn_patientid.text()}")
        print(f"Column FamiliyName = {self.ui.lineEdit_ncn_familyname.text()}")
        print(f"Column GivenName = {self.ui.lineEdit_ncn_givenname.text()}")
        print(f"Column BirthDateFrom {self.ui.lineEdit_ncn_birthdatefrom.text()} - {self.ui.lineEdit_ncn_birthdateto.text()}")
        print(f"Column StudyDateFrom {self.ui.lineEdit_ncn_studydatefrom.text()} -  {self.ui.lineEdit_ncn_studydateto.text()}")
        print(f"Load rows from {self.ui.spinBox_loadrowsfrom.text()} - {self.ui.spinBox_loadrowsto.text()} ")
        print(f"type=  {type(self.ui.spinBox_loadrowsfrom.text())} ")

    ##### downlaod from orthanc
    def select_download_dir(self):
        #lineEdit_absolute_download_dir_path
        print(f"select_download_dir with {self.ui.lineEdit_absolute_download_dir_path.text()}")

    ##### downlaod from orthanc
    def download_from_orthanc_to_drive(self):
        #lineEdit_absolute_download_dir_path
        print(f"download_from_orthanc_to_drive with {self.ui.lineEdit_absolute_download_dir_path.text()}")

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