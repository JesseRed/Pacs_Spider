import sys
from qtpy import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import qtpy
from ui.mainwindow import Ui_MainWindow
import subprocess, os, time
from pyorthanc import Orthanc
from myorthanc import MyOrthanc
from pacsspider import PacsSpider
import pandas as pd
import os
# & C:/Users/CKlingner/Desktop/WPy64-3890/python-3.8.9.amd64/python.exe c:/Users/CKlingner/Desktop/WPy64-3890/Pacs_Spider-main/main.py

#orthanc = Orthanc('http://localhost:8042')
app = QtWidgets.QApplication(sys.argv)
base_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(base_path)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        print(f"version of qtpy: {qtpy.__version__}")
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
        command = base_path + "\orthanc\orthanc.exe"
#        os.system(command)
        os.startfile(command)
        #res = subprocess.call(command, shell = True)
        #print("Returned Value: ", res)

        
    def getwebsitetoenter(self):
        print(f"getwegsitetoenter")

    def select_excel_file(self):
        print(f"select_excel_file with {self.ui.lineEdit_excel_absolute_file_path.text()}")
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.\\')
        if fname[0]:
            self.ui.lineEdit_excel_absolute_file_path.setText(fname[0])

    def load_into_orthanc_by_excel(self):
        #lineEdit_excel_absolute_file_path
        print(f"load_into_orthanc_by_excel with {self.ui.lineEdit_excel_absolute_file_path.text()}")
        df = pd.read_excel(self.ui.lineEdit_excel_absolute_file_path.text())
        # lege eine neue Spalte an die den ERfolg darstellt 
        df['found'] = "NA"
        df['numberOfFindings'] = "NA"
        df['success'] = "NA"

        print(df)
        P=PacsSpider()
        time.sleep(1)
        print("now transfering data from Pacs to orthanc")
        #P.set_search_parameter(PatientID = "*11031488")
        for index, row in df.iterrows():
            # setze nur in der Klasse es wird hier noch nicht auf der website eingetragen
            # setze alle search Parameter auf Blank
            P.set_search_parameter()
            if self.ui.checkBox_PatientID.isChecked():
                P.add_search_parameter(PatientID = ("*"+str(row["PatientID"])))
            if self.ui.checkBox_FamilyName.isChecked():
                P.add_search_parameter(FamilyName = row["FamilyName"])
            if self.ui.checkBox_GivenName.isChecked():
                P.add_search_parameter(GivenName = row["GivenName"])
            if self.ui.checkBox_BirthDate.isChecked():
                P.add_search_parameter(BirthDateFrom = row["BirthDate"], BirthDateTo = row["BirthDate"])
            if self.ui.checkBox_5.isChecked():
                P.add_search_parameter(QryDateTimeFrom = row["StudyDate"],QryDateTimeTo = row["StudyDate"])
            # if self.ui.checkBox_Modality.isChecked():
            #     P.add_parameter(Modality = row["Modality"])
            
            # PatientID = ""
            # FamilyName= ""
            # GivenName = ""
            # BirthDateFrom=""
            # BirthDateTo=""
            # QryDateTimeFrom = ""
            # QryDateTimeTo = ""
            # Modality = ""
            # print(f"search for PatientID = {patid} FamilyName = {fname}")
            # if self.ui.checkBox_PatientID.isChecked():
            #     PatientID = "*"+str(row["PatientID"])
            # if self.ui.checkBox_FamilyName.isChecked():
            #     FamilyName = row["FamilyName"]
                

            # P.set_search_parameter(PatientID = PatientID, 
            #                        FamilyName = FamilyName,
            #                        GivenName=GivenName,
            #                        BirthDateFrom= BirthDateFrom, 
            #                        BirthDateTo=BirthDateTo,
            #                        QryDateTimeFrom=QryDateTimeFrom, 
            #                        QryDateTimeTo=QryDateTimeTo,
            #                        Modality=Modality)

            #P.set_search_parameter()
            #P.set_search_parameter(GivenName = "*"+row["GivenName"])
            #P.set_search_parameter(BirthDateFrom = "*"+row["BirthDate"])
            #P.set_search_parameter(BirthDateTo = "*"+row["BirthDate"])
            #P.set_search_parameter(QryDateTimeFrom = "*"+row["StudyDate"])
            #P.set_search_parameter(QryDateTimeTo = "*"+row["StudyDate"])
            try:
                print("open page")
                P.open_page()
                print("get form elements")
                P.get_form_elements()
                print("clear form elements")
                P.clear_form_elements()
                print("fill form")
                P.fill_form()
                print(f"submit form")
                P.submit_form()
                num_findings = P.estimate_number_of_patients_found()
                df.loc[index,'numberOfFindings'] = num_findings
                if num_findings == 1:
                    df.loc[index,'found'] = 'yes'
                else:
                    df.loc[index,'found'] = 'no'
                P.select_first()
                print(f"after select the first item")
                #time.sleep(1)
                print(f"now select all studies")
                P.select_all_studies()
                print(f"now send to biomag")
                #P.send_to_biomag()
                row["success"] = "success"
                df.loc[index,"success"]="success"

            except:
                row["success"] = "failure"
                df.loc[index,"success"]="failure"
                #df.iloc[index,df.columns.get_loc("success")]="failure"
            
        print(df)
                #         P.set_search_parameter(FamilyName = "Wagner", GivenName="Franziska")
            #P.transfer_data_to_orthanc()
        #self.ui.lineEdit_excel_absolute_file_path.text()
        with pd.ExcelWriter('output.xlsx') as writer:  
            df.to_excel(writer)
        time.sleep(3)
        P.close()
        

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
#        fname = QFileDialog.getOpenFileName(self, 'Open file', '.\\')
        fname = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if fname:
            self.ui.lineEdit_absolute_download_dir_path.setText(fname)

    ##### downlaod from orthanc
    def download_from_orthanc_to_drive(self):
        #lineEdit_absolute_download_dir_path
        print(f"download_from_orthanc_to_drive with {self.ui.lineEdit_absolute_download_dir_path.text()}")
        myorthanc = MyOrthanc()
        download_dir = self.ui.lineEdit_absolute_download_dir_path.text()
        #myorthanc.download_patient_by_identifier(download_dir, patient_identifier)
        myorthanc.download_all_patients(download_dir)
        print(f"fertig")

    def init_gui(self):
        print("gui will be initialized")
        self.ui.lineEdit_absolute_download_dir_path.setText("C:\\Users\\CKlingner\\Desktop")
        self.ui.lineEdit_excel_absolute_file_path.setText("C:\\Users\\CKlingner\\Desktop\\Infarkte_PONTOS.xlsx")


ui_window = MainWindow()
ui_window.show()
sys.exit(app.exec_())


#window = QtWidgets.QMainWindow()
#window.setWindowTitle("Pacs Spider")

#ui_window = Ui_MainWindow()
#ui_window.setupUi(window)
#window.show()

#sys.exit(app.exec())