import requests
import json
from os.path import exists, join, dirname
from os import mkdir
from bs4 import BeautifulSoup as BS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Preparation with the list of notifications to do
informationFile =  open(join(dirname(__file__), "information.json"), "r", encoding="UTF-8")
taskList = json.load(informationFile)
informationFile.close()
    
# Notify news for each person's wanted exams
for person in taskList:
    if not exists(join(dirname(__file__), "users", person["name"])):
        mkdir(join(dirname(__file__), "users", person["name"]))
    
    for exam in person["exams"]:
        
        # Preparation with needed list
        saved_tests = []        # saved in file 
        read_tests = []         # newly read
        new_tests = []          # not in file
        
        # Get the saved dates
        if exists(join(dirname(__file__), "users", person["name"], str(exam["id"]) + ".txt")):
            readFile =  open(join(dirname(__file__), "users", person["name"], str(exam["id"]) + ".txt"), "r", encoding="UTF-8")
            saved_tests = readFile.readlines()
            readFile.close()

        # Get the new read dates and compare to saved dates to find the lately update dates
        url = "https://iigvietnam.com/lich-thi/?test_type=" + str(exam["id"]) + "&location=" + str(exam["location id"]) + "&start_date=" + exam["start date"] + "&end_date=" + exam["end date"]
        reader = BS(requests.get(url).content, "lxml").find_all("td")
        
        index = 1
        for idx_tag in range(len(reader)):
            if (reader[idx_tag].string == str(index)):
                test = str(reader[idx_tag+1].string) + ' - ' + str(reader[idx_tag+2].string) + '\n'
                if test not in saved_tests:
                    new_tests.append(test)
                    saved_tests.append(test)
                index += 1
        
        # Update the list of saved exam
        writeFile = open(join(dirname(__file__), "users", person["name"], str(exam["id"]) + ".txt"), "w", encoding="UTF-8")
        for test in saved_tests:
            writeFile.write(test)
        writeFile.close()

        # Send email
        '''
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Lately updated schedule for the exam " + str(exam["id"])
        msg['From'] = "TOEIC Notifier"
        msg['To'] = person["name"]

        content = ""
        for exam in new_exams:
            content = content + exam + "\n"

        body = MIMEText(content, 'plain', "UTF-8")
        msg.attach(body)
        s = smtplib.SMTP("localhost")
        s.sendmail("toeic-notifier@conganhluan.com", person["gmail"], msg.as_string())
        s.quit()
        '''