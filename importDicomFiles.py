#!/usr/bin/env python

# Orthanc - A Lightweight, RESTful DICOM Store
# Copyright (C) 2012-2016 Sebastien Jodogne, Medical Physics
# Department, University Hospital of Liege, Belgium
# Copyright (C) 2017-2019 Osimis S.A., Belgium
#
# This program is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import os
import sys
import os.path
import os
from os.path import dirname, realpath
import httplib2
import base64
import shutil
import logging

logging.basicConfig(filename='importDicomFiles.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file at start')
if len(sys.argv) != 4 and len(sys.argv) != 6:
    print("""
Sample script to recursively import in Orthanc all the DICOM files
that are stored in some path. Please make sure that Orthanc is running
before starting this script. The files are uploaded through the REST
API.

Usage: %s [hostname] [HTTP port] [path]
Usage: %s [hostname] [HTTP port] [path] [username] [password]
For instance: %s 127.0.0.1 8042 .
""" % (sys.argv[0], sys.argv[0], sys.argv[0]))
    exit(-1)

URL = 'http://%s:%d/instances' % (sys.argv[1], int(sys.argv[2]))
print(URL)
success_count = 0
total_file_count = 0


# This function will upload a single file to Orthanc through the REST API
def UploadFile(path):
    global success_count
    global total_file_count

    f = open(path, "rb")
    content = f.read()
    #content.co
    f.close()
    total_file_count += 1
    #print(f"count of content: {content.count}")
    try:
        #sys.stdout.write("Importing %s" % path)

        h = httplib2.Http()

        headers = { 'content-type' : 'application/dicom' }

        if len(sys.argv) == 6:
            username = sys.argv[4]
            password = sys.argv[5]
            #print(f"unsername = {username}")
            #print(f"password = {password}")
            # h.add_credentials(username, password)

            # This is a custom reimplementation of the
            # "Http.add_credentials()" method for Basic HTTP Access
            # Authentication (for some weird reason, this method does
            # not always work)
            # http://en.wikipedia.org/wiki/Basic_access_authentication
            headers['authorization'] = 'Basic ' + base64.b64encode((username + ':' + password).encode('UTF-8')).decode('ascii')       
        #print(f"content = {content}")
        resp, content = h.request(URL, 'POST', 
                                    body = content,
                                    headers = headers)
        #print(f"URL = {URL}")
        #print(f"body = {content}")
        #print(f"headers = {headers}")
        #print(f"resp = {resp}")
        #print(f"content = {content}")
        if resp.status == 200:
            #sys.stdout.write(" => success\n")
            success_count += 1
        else:
            sys.stdout.write(" => failure (Is it a DICOM file? Is there a password?)\n")

    except Exception as e:
        print(f"error during handling of file {path}")
        print(f"this file was not successfully included")
        print(f"error = {e}")
        logging.warning(f"error during handling of file {path} , this file was not included")
        logging.warning(f"error = {e}")

    #    sys.stdout.write(" => unable to connect (Is Orthanc running? Is there a password?)\n")

zaehler = 0
root_target = os.path.join(dirname(dirname(dirname(realpath(__file__)))),"imported")
if not os.path.exists(root_target):
    os.makedirs(root_target)
    
if os.path.isfile(sys.argv[3]):
    # Upload a single file
    UploadFile(sys.argv[3])
else:
    # 
    d = sys.argv[3] # das Startdirctory
    dirlist = [os.path.join(d, o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))] # alle Verzeichnisse im aktuellen Verzeichnis
    for dir_to_upload in dirlist:
        print(f"start importing directory {dir_to_upload}")
        # Recursively upload a directory
        for root, dirs, files in os.walk(dir_to_upload):
            for f in files:
                UploadFile(os.path.join(root, f))
                zaehler += 1
                if (zaehler % 1000)==0:
                    #print(f"{zaehler} images imported (last = {os.path.join(root,f)})")
                    logging.warning(f"{zaehler} images importet (last = {os.path.join(root,f)})")
        #nun move das Directory
        print(f"import of directory {dir_to_upload} successful ")
        print(f"... now moving directory to  from {dir_to_upload} -> {os.path.join(root_target,os.path.basename(dir_to_upload))}")
        shutil.move(dir_to_upload,os.path.join(root_target,os.path.basename(dir_to_upload)))
        print(f"moving directory finished")
if success_count == total_file_count:
    print("\nSummary: all %d DICOM file(s) have been imported successfully" % success_count)
else:
    print("\nSummary: %d out of %d files have been imported successfully as DICOM instances" % (success_count, total_file_count))
