import requests
import sys
from bs4 import BeautifulSoup as BS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Read information about TOEIC (Reading and Listening)
response = requests.get("https://iigvietnam.com/lich-thi/?test_type=&location=&start_date=09/01/2023&end_date=10/01/2023")
content = BS(response.content, "lxml")

    # Read and find desired information
finder = content.find_all("td")
read_dates = []
for index in range(len(finder)):
    if finder[index].string == "TOEIC":
        read_dates.append(finder[index+1].string)
        index += 1

    # Read saved dates from file
with open("TOEIC_dates.txt", "r", encoding="UTF-8") as file:
    saved_dates = file.readlines()
    file.close()

    # Compare the read dates with saved dates, update with new dates
new_dates_TOEIC = []
for date in read_dates:
    if date not in saved_dates:
        new_dates_TOEIC.append(date)
        saved_dates.append(date)

    # Update the file
with open("TOEIC_dates.txt", "w", encoding="UTF-8") as file:
    for line in saved_dates:
        file.write(line + "\n")
    file.close()

# Read information about TOEIC SW (Reading and Listening)
response = requests.get("https://iigvietnam.com/lich-thi/?test_type=94&location=205&start_date=09/01/2023&end_date=10/01/2023")
content = BS(response.content, "lxml")

    # Read and find desired information
finder = content.find_all("td")
read_dates = []
for index in range(len(finder)):
    if finder[index].string == "TOEIC SW":
        read_dates.append(finder[index+1].string)
        index += 1

    # Read saved dates from file
with open("TOEIC_SW_dates.txt", "r", encoding="UTF-8") as file:
    saved_dates = file.readlines()
    file.close()

    # Compare the read dates with saved dates, update with new dates
new_dates_TOEIC_SW = []
for date in read_dates:
    if date not in saved_dates:
        new_dates_TOEIC_SW.append(date)
        saved_dates.append(date)

    # Update the file
with open("TOEIC_SW_dates.txt", "w", encoding="UTF-8") as file:
    for line in saved_dates:
        file.write(line + "\n")
    file.close()

