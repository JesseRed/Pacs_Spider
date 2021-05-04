#download_orthanc

from pyorthanc import Orthanc

orthanc = Orthanc('http://localhost:8042')
# #orthanc.setup_credentials('username', 'password')  # If needed

# # To get patients identifier and main information
patients_identifiers = orthanc.get_patients()
idx = 0
for patient_identifier in patients_identifiers:
    print(idx)
    patient_information = orthanc.get_patient_information(patient_identifier)
    print(patient_information)

    bytes_content = orthanc.get_patient_zip(patient_identifier)
    filename= patient_information['MainDicomTags']['PatientName'] + patient_information['MainDicomTags']['PatientID']
    with open(filename+'.zip', 'wb') as file_handler:
        file_handler.write(bytes_content)

#     with open(idx+'.zip', 'wb') as z:
#         z.write(orthanc.get_patient_zip(patient_identifier))
#         orthanc.get_patient_zip()

#     >>> from pyorthanc import Orthanc
# >>> orthanc = Orthanc('http://localhost:8042')
# >>> a_patient_identifier = orthanc.get_patients()[0]
# >>> bytes_content = orthanc.get_patient_zip(a_patient_identifier)
# >>> with open('patient_zip_file_path.zip', 'wb') as file_handler:
# ...     file_handler.write(bytes_content)

#        orthanc.get_patient_zip(patient_identifier)
        # for patarch in orthanc.get_patient_zip(patient_identifier):
        # #for chunk in orthanc.get_study_archive(patient_identifier):
        #     z.write(patarch)
#     patient_name = patient_information['MainDicomTags']['name']
#     #...
#     study_identifiers = patient_information['Studies']    

# # To get patient's studies identifier and main information
# for study_identifier in study_identifiers:
#     study_information = orthanc.get_study_information(study_identifier)

#     study_date = study_information['MainDicomTags']['StudyDate']
#     #...
#     series_identifiers = study_information['Series']

# # To get study's series identifier and main information
# for series_identifier in series_identifiers:
#     series_information = orthanc.get_series_information(series_identifier)

#     modality = series_information['MainDicomTags']['Modality']
#     #...
#     instance_identifiers = series_information['Instances']

# # and so on ...
# for instance_identifier in instance_identifiers:
#     instance_information = orthanc.get_instance_information(instance_identifier)
#     #...

# from orthanc_rest_client import Orthanc
# orthanc = Orthanc('http://localhost:8042')
# # Patient endpoints
# patients = orthanc.get_patients()
# for patient in patients:
#     print(patient)
# #orthanc.get_patient(id)


# with open('test.zip', 'wb') as z:
#     for chunk in orthanc.get_study_archive(id):
#         z.write(chunk)