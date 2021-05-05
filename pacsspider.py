# -*- coding: utf-8 -*-
"""
Created on Apr 21 14:21:18 2021

@author: Carsten
"""

#from crossref.restful import Works, Prefixes
from bs4 import BeautifulSoup
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import glob, os
import pickle
import time
import random

class PacsSpider:
    def __init__(self, link = "http://doctor:doctor@jarc04/transfer/transferFrame.html"):
        self.link = link
        self.driver = webdriver.Chrome()


    def set_search_parameter(self, PatientID = "", FamilyName= "", GivenName = "", BirthDateFrom="", BirthDateTo="", QryDateTimeFrom = "", QryDateTimeTo = "", Modality = ""):
        self.PatientID = PatientID
        self.FamilyName = FamilyName
        self.GivenName = GivenName
        self.BirthDateFrom = BirthDateFrom
        self.BirthDateTo = BirthDateTo
        self.QryDateTimeFrom = QryDateTimeFrom
        self.QryDateTimeTo = QryDateTimeTo
        self.Modality = Modality
        print("set search parameter") 
        print(f"QryDateTimeFrom = {self.QryDateTimeFrom}")
        print(f"QryDateTimeTo = {self.QryDateTimeTo}")

    def add_search_parameter(self, PatientID = "!!!", FamilyName= "!!!", GivenName = "!!!", BirthDateFrom="!!!", BirthDateTo="!!!", QryDateTimeFrom = "!!!", QryDateTimeTo = "!!!", Modality = "!!!"):
        if not PatientID=="!!!":
            self.PatientID = PatientID
        if not FamilyName=="!!!":
            self.FamilyName = FamilyName
        if not GivenName=="!!!":
            self.GivenName = GivenName
        if not BirthDateFrom =="!!!":
            self.BirthDateFrom = BirthDateFrom
        if not BirthDateTo=="!!!":
            self.BirthDateTo = BirthDateTo
        if not QryDateTimeFrom=="!!!":
            self.QryDateTimeFrom = QryDateTimeFrom
        if not QryDateTimeTo=="!!!":
            self.QryDateTimeTo = QryDateTimeTo
        if not Modality=="!!!":
            self.Modality = Modality
        print("add_search_parameter") 
        print(f"QryDateTimeFrom = {self.QryDateTimeFrom}")
        print(f"QryDateTimeTo = {self.QryDateTimeTo}")

    def set_link(self, link):
        self.link = link

    def open_page(self):
        self.driver.get(self.link)
        self.driver.implicitly_wait(3)
    
    def get_form_elements(self):
        self.driver.switch_to.frame(0)
        self.elem_PatientID = self.driver.find_element_by_name("PatientID")
        self.elem_FamilyName = self.driver.find_element_by_name("FamilyName")
        self.elem_GivenName = self.driver.find_element_by_name("GivenName")
        self.elem_BirthDateFrom = self.driver.find_element_by_name("BirthDateFrom")
        self.elem_BirthDateTo = self.driver.find_element_by_name("BirthDateTo")
        self.elem_QryDateTimeFrom = self.driver.find_element_by_name("QryDateTimeFrom")
        self.elem_QryDateTimeTo = self.driver.find_element_by_name("QryDateTimeTo")
        self.elem_Modality = self.driver.find_element_by_name("Modality")
        NEXT_BUTTON_XPATH = '//input[@type="SUBMIT" and @value=" Patienten und Mappen suchen "]'
        ZURUECK_BUTTON_XPATH = '//input[@type="BUTTON" and @value=" Zurücksetzen "]'
        self.submit_button = self.driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
        self.zurueck_button = self.driver.find_element_by_xpath(ZURUECK_BUTTON_XPATH)
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()

    def clear_form_elements(self):
        self.driver.switch_to.frame(0)
        self.zurueck_button.click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()

        # self.elem_PatientID.send_keys(Keys.CONTROL + "a")
        # self.elem_PatientID.send_keys(Keys.DELETE)
        # self.elem_FamilyName.send_keys(Keys.CONTROL + "a")
        # self.elem_FamilyName.send_keys(Keys.DELETE)
        # self.elem_GivenName.send_keys(Keys.CONTROL + "a")
        # self.elem_GivenName.send_keys(Keys.DELETE)        
        # self.elem_BirthDateFrom.send_keys("1850-01-01 00:00:00")
        # self.elem_BirthDateTo.send_keys("2050-01-01 00:00:00")
        # self.elem_QryDateTimeFrom.send_keys("1850-01-01 00:00:00")
        # self.elem_QryDateTimeTo.send_keys("2050-01-01 00:00:00")

        # self.elem_BirthDateFrom.send_keys(Keys.CONTROL + "a")
        # self.elem_BirthDateFrom.send_keys(Keys.DELETE)        
        # self.elem_BirthDateTo.send_keys(Keys.CONTROL + "a")
        # self.elem_BirthDateTo.send_keys(Keys.DELETE)        
        # self.elem_QryDateTimeFrom.send_keys(Keys.CONTROL + "a")
        # self.elem_QryDateTimeFrom.send_keys(Keys.DELETE)        
        # self.elem_QryDateTimeTo.send_keys(Keys.CONTROL + "a")
        # self.elem_QryDateTimeTo.send_keys(Keys.DELETE)        
        #self.driver.implicitly_wait(2)
        #self.driver.switch_to.default_content()

    def fill_form(self):
        print(f"PatientID = {self.PatientID}")
        print(f"FamilyName = {self.FamilyName}")
        print(f"GivenName = {self.GivenName}")
        print(f"BirthDateFrom = {self.BirthDateFrom}")
        print(f"BirthDateTo = {self.BirthDateTo}")
        print(f"QryDateTimeFrom = {self.QryDateTimeFrom}")
        print(f"QryDateTimeTo = {self.QryDateTimeTo}")
        print("fill form in P")
        self.driver.switch_to.frame(0)
        self.elem_PatientID.send_keys(self.PatientID)
        self.elem_FamilyName.send_keys(self.FamilyName)
        self.elem_GivenName.send_keys(self.GivenName)
        print("fill form in P 2")
        self.elem_BirthDateFrom.send_keys(self.BirthDateFrom)
        self.elem_BirthDateTo.send_keys(self.BirthDateTo)
        print("fill form in P 3")
        self.elem_QryDateTimeFrom.send_keys(self.QryDateTimeFrom)
        print("fill form in P 3.5")
        self.elem_QryDateTimeTo.send_keys(self.QryDateTimeTo)
        print("fill form in P 4")
        self.elem_Modality.send_keys(self.Modality)
        self.driver.implicitly_wait(2)
        print("fill form in P 5")
        self.driver.switch_to.default_content()
        print("fill form ende")

    def submit_form(self):
        self.driver.switch_to.frame(0)
        self.submit_button.click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()
        
    def estimate_number_of_patients_found(self):
        print(f"entering estimate_number_of_patients_found")
        self.driver.switch_to.frame(0)
        # identifying the number of rows having <tr> tag
        #try:
            # teste ob keine gefunden wurden
        rows = self.driver.find_elements_by_xpath("//table/tbody/tr/td/input")
        print(f"found {len(rows)} elements in estimate_number_of_patients")
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()
        return(len(rows)-1)

    def select_first(self):
        self.driver.switch_to.frame(0)
        select_button = self.driver.find_elements_by_xpath("//table/tbody/tr/td/input[@type='BUTTON']")
        self.driver.implicitly_wait(2)
        select_button[0].click()
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()

    def save_html(self, numframe):
        self.driver.switch_to.frame(numframe)
        with open("htmlcode1.html", "w", encoding="utf-8") as f1:
            f1.write(self.driver.page_source)
        self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()

    def select_all_studies(self):
        self.driver.switch_to.frame(0)

        # ich muss herausfinden ob der bereits gesetzt ist 
        #<img src="/multi_off.gif" name="btn0" border="0" alt="select all series of this patient">

        select_button = self.driver.find_elements_by_xpath("//table/tbody/tr/td/a/img[@name='btn0']")
        print(f"is select = {select_button[0].is_selected()}")
        self.driver.implicitly_wait(2)
        if not select_button[0].is_selected():
            select_button[0].click()
            self.driver.implicitly_wait(2)
        self.driver.switch_to.default_content()
        #<img src="/multi_off.gif" name="btn0" border="0" alt="select all series of this patient">

    def send_to_biomag(self):
        self.driver.switch_to.frame(0)
        select_button = self.driver.find_elements_by_xpath("//table/tbody/tr/td/input[@value=' Ausgewählte Serien übertragen ']")
        self.driver.implicitly_wait(2)
        select_button[0].click()
        self.driver.implicitly_wait(2)
        try:
            obj = self.driver.switch_to.alert
            obj.accept()
        except:
            #no allert message > pass
            pass
        self.driver.switch_to.default_content()
        #<input type="submit" value=" Ausgewählte Serien übertragen " onclick="return CheckForm('series')">

    def check_for_alert(self):
        #print(self.driver.switchTo().alert().getText())
        pass

    def close(self):
        self.driver.switch_to.frame(0)
        self.driver.implicitly_wait(3)
        self.driver.close()

    def transfer_data_to_orthanc(self):

        self.open_page()
        self.get_form_elements()
        self.clear_form_elements()
        self.fill_form()
        self.submit_form()
        num_rows = self.estimate_number_of_patients_found()
        print(f"number of items found = {num_rows}")
        self.select_first()
        print(f"after select the first item")
        time.sleep(1)
        print(f"now select all studies")
        self.select_all_studies()
        print(f"now send to biomag")
        #self.send_to_biomag()

if __name__ == "__main__":

    P=PacsSpider()
    time.sleep(1)
    print("set_search_parameter")
    P.set_search_parameter(FamilyName = "Wagner", GivenName="Franziska")
    P.transfer_data_to_orthanc()

    time.sleep(5)
    P.close()

# elem_FamilyName.send_keys("Klingner")
# driver.implicitly_wait(5)
# #elem = driver.find_element_by_class_name("INPUT")
# #submit_button = driver.find_element_by_xpath("//td[@name='continue'][@type='button']")


#         self.driver.implicitly_wait(2)
#         self.driver.switch_to.default_content()
# #elem.send_keys("0011031488")

# elem_FamilyName.send_keys(Keys.CONTROL + "a")
# elem_FamilyName.send_keys(Keys.DELETE)
# driver.implicitly_wait(2)
# elem_FamilyName.send_keys("Klingner")
# driver.implicitly_wait(5)
# #elem = driver.find_element_by_class_name("INPUT")
# #submit_button = driver.find_element_by_xpath("//td[@name='continue'][@type='button']")
# NEXT_BUTTON_XPATH = '//input[@type="SUBMIT" and @value=" Patienten und Mappen suchen "]'
# submit_button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
# submit_button.click()

# #<td class="INPUT"><input type="SUBMIT" value=" Patienten und Mappen suchen " onclick="document.form_qry.QryLevel.value='PATIENT'"></td>

# driver.implicitly_wait(2)
# pageSource1 = driver.page_source
# driver.switch_to.default_content()


#     def fill_form():



# <input type="text" name="QryDateTimeFrom" value="" size="11" onchange="completeDate(this.form,QryDateTimeFrom,QryDateTimeTo, true)">

# print("working")
# link = "http://doctor:doctor@jarc04/pacs_servlet/com.imagedev.web.servlets.transfer.query_retrieve.PatientStudySelect"
# link = "http://jarc04/pacs_servlet/com.imagedev.web.servlets.main.navigation.Navigation?NavFeature=transfer"
# link = "http://doctor:doctor@jarc04/transfer/transferFrame.html"
# #link = "http://doctor:doctor@jarc04/pacs_servlet/com.imagedev.web.servlets.main.navigation.Navigation?NavFeature=transfer"
# #fname_html = "pageinhalt.html"
# #idx = 0
# #browser = webdriver.Firefox()
# #C:\Users\CKlingner\AppData\Local\Google\Chrome\Application
# #browser = webdriver.Chrome('C:/Users/CKlingner/AppData/Local/Google/Chrome/Application')
# #link = "http://doctor:doctor@jarc04"
# driver = webdriver.Chrome()
# #driver = webdriver.Ie()
# #driver = webdriver.Edge()
# driver.get(link)

# #<table cellspacing="0" cellpadding="3" id="searchControl">

# # </th><td align="LEFT" colspan="4"><input type="text" name="PatientID" value="0011031488" size="36"><input type="hidden" name="a_PatientID" value="true" size="36"></td>
# # </th><td align="LEFT" colspan="4"><input type="text" name="FamilyName" value="" size="36"><input type="hidden" name="a_FamilyName" value="true" size="36"></td>
# # <th class="RIGHTAL"><nobr>Vorname</nobr>
# # </th><td align="LEFT" colspan="4"><input type="text" name="GivenName" value="" size="36"><input type="hidden" name="a_GivenName" value="true" size="36"></td>
# # <td align="LEFT" class="INPUT"><input type="text" name="BirthDateFrom" value="" size="11" onchange="completeDate(this.form,BirthDateFrom,BirthDateTo)"></td>
# # <td align="LEFT" class="INPUT"><input type="text" name="BirthDateTo" value="" size="11" onchange="completeDate(this.form,BirthDateFrom,BirthDateTo)"></td>
# # <th class="INPUT" align="LEFT">[yyyy-mm-dd &nbsp;&nbsp; hh:mm:ss]
# # <th class="RIGHTAL"><nobr>Study Date</nobr></th>


# driver.implicitly_wait(3)

# #search_form = driver.find_element_by_xpath("//table[@id='searchControl']")
# #<input type="text" name="PatientID" value="0011031488" size="36">
# #elem = driver.find_element_by_name("PatientID")
# #elem = driver.find_element_by_name("form_qry")
# #elem = driver.find_element_by_xpath("/html/head")
# #elem = driver.find_element_by_xpath("//input[@name='PatientID']")
# #print(f"now the element")
# #print(elem)
# #print(f"after element printing")

# driver.get(link)
# driver.implicitly_wait(3)

# driver.switch_to.frame(0)
# elem_PatientID = driver.find_element_by_name("PatientID").clear()
# elem_FamilyName = driver.find_element_by_name("FamilyName")
# elem_GivenName = driver.find_element_by_name("GivenName").clear()
# elem_BirthDateFrom = driver.find_element_by_name("BirthDateFrom").clear()
# elem_BirthDateTo = driver.find_element_by_name("BirthDateTo").clear()
# driver.implicitly_wait(2)
# #elem.send_keys("0011031488")

# elem_FamilyName.send_keys(Keys.CONTROL + "a")
# elem_FamilyName.send_keys(Keys.DELETE)
# driver.implicitly_wait(2)
# elem_FamilyName.send_keys("Klingner")
# driver.implicitly_wait(5)
# #elem = driver.find_element_by_class_name("INPUT")
# #submit_button = driver.find_element_by_xpath("//td[@name='continue'][@type='button']")
# NEXT_BUTTON_XPATH = '//input[@type="SUBMIT" and @value=" Patienten und Mappen suchen "]'
# submit_button = driver.find_element_by_xpath(NEXT_BUTTON_XPATH)
# submit_button.click()

# #<td class="INPUT"><input type="SUBMIT" value=" Patienten und Mappen suchen " onclick="document.form_qry.QryLevel.value='PATIENT'"></td>

# driver.implicitly_wait(2)
# pageSource1 = driver.page_source
# driver.switch_to.default_content()

# #print(pageSource)
# #driver.get(link)
# driver.implicitly_wait(3)
# #driver.switch_to.frame(1)
# pageSource2 = driver.page_source
# #print(pageSource2)

# #fname_html = "htmlcode.html"      

# with open("htmlcode1.html", "w", encoding="utf-8") as f1:
#     f1.write(pageSource1)
# with open("htmlcode2.html", "w", encoding="utf-8") as f2:
#     f2.write(pageSource2)
# #f1.close()
# #elem = driver.find_element_by_name(" Patienten und Mappen suchen ")
# time.sleep(3)

#search_form = browser.find_element_by_name('PatientID')
#search_form.send_keys("0011031488")
#search_form.submit()
#all_html = browser.page_source
#<input type="SUBMIT" value=" Patienten und Mappen suchen " onclick="document.form_qry.QryLevel.value='PATIENT'">

#<input type="SUBMIT" value=" Patienten und Mappen suchen " onclick="document.form_qry.QryLevel.value='PATIENT'">
#try:  
#    browser.get(link)
#    browser.implicitly_wait(5)
#    time.sleep(random.randint(7,15))
#    all_html = browser.page_source

    #with open(fname_html, "w", encoding="utf-8") as f1:
    #    f1.write(all_html)
    #f1.close()
    #idx +=1
#    print('downloaded paper: abgeschlossen')
#except:
#    print('something went wrong')

#             break
# all from NeuroImage
# idx = 0
# browser = webdriver.Firefox()
# p = './Elsevier_html_files/'
# for journal, issn_c in journal_issn.items():
#     works = works.query(publisher_name='Elsevier BV').filter(issn=[issn_c])
#     print('Analyse Journal: ' + journal + ' ' +issn_c)
#     for i in works: #.select('title'):
#         idx +=1    

#         if (idx%2000)==2
#             print('start downloading paper number: ' +str(idx))
#           #  if i['language']=='en' and i['type']=='journal_article':
#         try:  
#             if i['type']=='journal-article':
#                 alternative_id = i['alternative-id'][0]
#                 link = 'https://www.sciencedirect.com/science/article/pii/' + alternative_id
#                 fname_html = p + 'HTML_' + journal + '_' + alternative_id + '.html'
#                 fname_crossref = p +'XML_' + journal + '_' + alternative_id + '.xml'
                  
#                 browser.get(link)
#                 browser.implicitly_wait(5)
#                 time.sleep(random.randint(7,15))
#                 all_html = browser.page_source
                
#                 with open(fname_html, "w", encoding="utf-8") as f1:
#                     f1.write(all_html)
#                 f1.close()
#                 with open(fname_crossref, "w", encoding="utf-8") as f2:
#                     f2.write(str(i))
#                 f2.close()
#                 idx +=1
                
#                 print('downloaded paper: ' + str(idx)+ 'abgeschlossen')
#         except:
#             print('something went wrong')
#             print(i)
#             break
# print('all downloaded')
# """ 

# <th class="RIGHTAL"><nobr>Modality</nobr></th>
# <td align="LEFT" class="INPUT" colspan="4"><select name="Modality" size="5" multiple="">
# <option value="">&lt;all&gt;
# </option><option value="AS">AS, Angioscopy
# </option><option value="BI">BI, Biomagnetic Imaging
# </option><option value="CD">CD, Color flow Doppler
# </option><option value="CF">CF, Cinefluorography (retired)
# </option><option value="CP">CP, Culposcopy (retired)
# </option><option value="CR">CR, Computed Radiography
# </option><option value="CS">CS, Cystoscopy (retired)
# </option><option value="CT">CT, Computed Tomography
# </option><option value="DD">DD, Duplex Doppler
# </option><option value="DF">DF, Digital fluoroscopy (retired)
# </option><option value="DG">DG, Diaphanography
# </option><option value="DM">DM, Digital Microscopy (retired)
# </option><option value="DR">DR, Direct Radiography
# </option><option value="DS">DS, Digital Substraction Angiography (retired)
# </option><option value="DX">DX, Digital Radiography
# </option><option value="EC">EC, Echocardiography (retired)
# </option><option value="ECG">ECG, ECG Waveform
# </option><option value="EPS">EPS, Cardiac Electrophysiology
# </option><option value="ES">ES, Endoscopy
# </option><option value="FA">FA, Fluorescein Angiography (retired)
# </option><option value="FID">FID, Spatial Fiducials
# </option><option value="FS">FS, Fundoscopy (retired)
# </option><option value="GM">GM, General Microscopy
# </option><option value="HC">HC, Hard Copy
# </option><option value="HD">HD, Hemodynamic ECG Waveform
# </option><option value="IO">IO, Intra-oral Radiography
# </option><option value="KO">KO, Key Object Selection Document
# </option><option value="LP">LP, Laparoscopy (retired)
# </option><option value="LS">LS, Laser surface scan
# </option><option value="MA">MA, Magnetic res. Angiography (retired)
# </option><option value="MG">MG, Mammography
# </option><option value="MR">MR, Magnetic Resonance
# </option><option value="MS">MS, Magnetic res. Spectroscopy (retired)
# </option><option value="NM">NM, Nuclear Medicine
# </option><option value="OP">OP, Ophthalmic Photography
# </option><option value="OT">OT, Other
# </option><option value="PR">PR, Softcopy Presentation State
# </option><option value="PT">PT, Positron em. tomography (PET)
# </option><option value="PX">PX, Panoramic X-Ray
# </option><option value="REG">REG, Spatial Registration
# </option><option value="RF">RF, Radio Fluoroscopy
# </option><option value="RG">RG, Radiographic imaging (conventional film/screen)
# </option><option value="RTDOSE">RTDOSE, Radiotherapy Dose
# </option><option value="RTIMAGE">RTIMAGE, Radiotherapy Image
# </option><option value="RTPLAN">RTPLAN, Radiotherapy Plan
# </option><option value="RTRECORD">RTRECORD, RT Treatment Record
# </option><option value="RTSTRUCT">RTSTRUCT, Radiotherapy Structure Set
# </option><option value="RWV">RWV, Real World Value Mapping
# </option><option value="SC">SC, Secondary Capture
# </option><option value="SM">SM, Slide Microscopy
# </option><option value="SMR">SMR, Stereometric Relationship Storage
# </option><option value="SR">SR, Structured Report
# </option><option value="ST">ST, Single-photon em. computed tomography (SPECT)
# </option><option value="TG">TG, Thermography
# </option><option value="US">US, Ultrasound
# </option><option value="VF">VF, Videofluorography (retired)
# </option><option value="XA">XA, X-Ray Angiography
# </option><option value="XC">XC, External-camera Photography
# </option></select></td>
# </tr>
# </tbody></table> """