# Sites Monitoring Utility

This script check all sites listed in a txt file by checking their status (response code = 200 ) and registration expiration dates of their domain names.


### How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

### How to use
```bash

$ python check_sites_health.py -h
usage: check_sites_health.py [-h] -f FILE

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to file with sites list

```

### Sample output
```bash
$ python python check_sites_health.py -f sites.txt
Domain name: google.com                     Response code: 200 Expires date: 2020-09-14 04:00:00 Test results: OK
Domain name: youtube.com                    Response code: 200 Expires date: 2018-02-15 05:13:12 Test results: OK
Domain name: facebook.com                   Response code: 200 Expires date: 2025-03-30 04:00:00 Test results: OK
Domain name: baidu.com                      Response code: 200 Expires date: 2026-10-11 11:05:17 Test results: OK
Domain name: yahoo.com                      Response code: 200 Expires date: 2023-01-19 05:00:00 Test results: OK
Domain name: amazon.com                     Response code: 503 Expires date: 2022-10-31 04:00:00 Test results: ATTENTION !!!
Domain name: wikipedia.org                  Response code: 200 Expires date: 2023-01-13 00:12:14 Test results: OK
Domain name: qq.com                         Response code: 200 Expires date: 2027-07-27 02:09:19 Test results: OK
Domain name: google.co.in                   Response code: 200 Expires date: 2018-06-23 14:02:33 Test results: OK
Domain name: twitter.com                    Response code: 200 Expires date: 2020-01-21 16:28:17 Test results: OK
Domain name: live.com                       Response code: 200 Expires date: 2017-12-27 05:00:00 Test results: OK
Domain name: taobao.com                     Response code: ERR Expires date: 2018-04-21 03:50:05 Test results: ATTENTION !!!
Domain name: msn.com                        Response code: 200 Expires date: 2022-06-04 16:44:29 Test results: OK
Domain name: sina.com.cn                    Response code: 200 Expires date: None Test results: ATTENTION !!!
Domain name: yahoo.co.jp                    Response code: 200 Expires date: None Test results: ATTENTION !!!
Domain name: google.co.jp                   Response code: 200 Expires date: None Test results: ATTENTION !!!
Domain name: linkedin.com                   Response code: 200 Expires date: 2020-11-02 15:38:11 Test results: OK
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

