# TOEIC NOTIFIIER
Đây là một chương trình giúp bạn nhận thông báo về những lịch thi được IIG cập nhật mỗi ngày đối với những kì thi mà bạn quan tâm.  
  
## Điều kiện tiên quyết/ Presiquites:
Để chạy được các code này, máy tính cần có Python. Ngoài các thư viện đã có sẵn, bạn cũng cần phải cài đặt những thư viện riêng mà chương trình đã sử dụng bao gồm `requests`, `emails`, `beautifulsoup4` nếu máy bạn chưa có. 
Theo mặc định, chương trình sẽ sử dụng *localhost* cho SMTP (dịch vụ gửi thư), vậy nên máy tính của bạn cần phải được cài đặt dịch vụ SMTP trước. Nếu bạn sử dụng dịch vụ SMTP của các trang web như Gmail, Outlook,... thì bạn phải mở khóa dòng 66 `s.login(SMTP_user, SMTP_password)` để có thể đăng nhập vào dịch vụ đó.  
  
## Cách cài đặt và sử dụng/ How to install and use
Các bạn tải (hoặc nhân bản) mã nguồn về, sau đó tạo 1 file **information.json** ở cùng thư mục của file **main.py** và có dạng như sau:  
  
```
[
    {
        "name": "",
        "gmail": "",
        "exams": [
            {
                "id": "",
                "location id": "",
                "start date": "",
                "end date": ""
            },
            {
                "id": "",
                "location id": "",
                "start date": "",
                "end date": ""
            }
        ]
    },
    {
        "name": "",
        "gmail": "",
        "exams": [
            {
                "id": "",
                "location id": "",
                "start date": "",
                "end date": ""
            }
        ]
    }
]
```
Hãy lưu ý những điều sau đây để tệp **information.json** có ý nghĩa và chương trình có thể chạy được:  
1. Các id của exam sẽ bao gồm:
    - TOEFL iBT - 88
    - TOEFL ITP - 89
    - TOEFL Junior - 90
    - TOEFL Primary - 91
    - TOEIC - 92
    - TOEIC Bridge - 93
    - TOEIC SW - 94
    - MOS - 251
    - IC3 - 255
    - SAT - 259
    - GRE - 272
2. Các location id của exam sẽ bao gồm:
    - Trường Đại học Kỹ Thuật Công nghiệp Thái Nguyên - 53
    - Trụ sở chính của IIG Việt Nam - 55
    - Trường Đại học CNTT & Truyền thông Thái Nguyên - 57
    - Văn phòng Trung Yên - Hà nội - 59
    - Trường Đại học Nha Trang - 61
    - Trung tâm Phát triển Phần mềm Đai học Đà Nẵng - 63
    - IIG Việt Nam chi nhánh Đà Nẵng - 65
    - Trường Đại học Kinh tế TP.HCM - 67
    - Trường Đại học Kinh tế Quốc dân Hà Nội - 118
    - Trường Cao đẳng Kinh tế TP.HCM - 124
    - Trường Trung cấp Kỹ thuật Công Nghệ Hùng Vương - 126
    - Trường Đại học Văn Hiến - 128
    - Trường Cao đẳng Quốc tế TP.HCM - 130
    - Trường Đại học Nguyễn Tất Thành - 132
    - IIG Việt Nam chi nhánh Hồ Chí Minh - 205
    - Trường Đại học Hàng Hải Việt Nam - 465
    - Trường Đại học Bách Khoa - ĐHQG-HCM - 476
3. Các id phải được viết trong dấu **" "**
4. *start date* và *end date* phải được viết dưới dạng mm/dd/yyyy (ví dụ: 12/31/2023)
5. Không được để trống hai trường dữ liệu *id* và *location id* của exam, nếu không có thể dẫn đến kết quả không mong muốn
6. Mỗi trường dữ liệu id (*id* và *location id*) chỉ điền một id mà mình muốn, nếu có nhiều hơn một kì thi hoặc một địa điểm cố định cho cùng một kì thi thì phải tách ra thành 2 exam khác nhau
7. Phải tạo một thư mục **user** trong cùng thư mục với **main.py** để không bị lỗi  
  
Để sử dụng chương trình, bạn chỉ cần đặt lệnh `python /path/to/main.py` cho crontab chạy mỗi ngày là hoàn thành . Nếu có bất kì lỗi phát sinh nào thì xin vui lòng liên hệ với mình để mình có thể sửa chữa một cách sớm nhất!
