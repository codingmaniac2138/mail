#!/usr/bin/python
import re
import json, pprint
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import *


def send_mail_func(body,toaddr):
    fromaddr = "suhas.j@consultadd.com"

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Python Requirements in NJ/NY"

    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "myid@2138")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


def get_requirements():
    consultant_data = edit_profile.objects.all()
    for idata in consultant_data:

        skill = idata.technology
        city = idata.job_location
        print idata
        print idata.requested_email
        nextUrl = '/api/rest/jobsearch/v1/simple.json?skill=' + skill + '&text=c2c&city=' + city + '&age=1&page=1'
        main_dict = {}
        while (1):

            req = requests.get('http://service.dice.com' + nextUrl)
            main_dict[str(nextUrl.split("page=")[1])] = json.loads(req.text)['resultItemList']
            try:
                nextUrl = json.loads(req.text)['nextUrl']
                # print(nextUrl)
            except:
                break
        no_c2c= 'No C2C'
        c2c = 'C2C'
        a = re.compile(r'\b%s\b' % (no_c2c))
        b = re.compile(r'\b%s\b' % (no_c2c.upper()))
        c = re.compile(r'\b%s\b' % (no_c2c.title()))
        d = re.compile(r'\b%s\b' % (c2c.upper()))
        e = re.compile(r'\b%s\b' % (c2c.title()))
        f = re.compile(r'\b%s\b' % (c2c))

        pp = pprint.PrettyPrinter(indent=4)
        a = [
            '<br><a href="{}">"jobTitle":{},"company":{},"location":{}</a>'.format(
                i['detailUrl'], i["jobTitle"], i["company"], i["location"])
            for kd in main_dict.keys() for i in main_dict[kd] if "No C2C" not in (i["jobTitle"])\
            or "no C2C" not in (i["jobTitle"]) or "NO C2C" not in (i["jobTitle"])
            ]
        pp.pprint(a)
        print(len(a))

        body = "".join(a)
        toaddr = idata.requested_email

        # send_mail_func(body,toaddr)