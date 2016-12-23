#!/usr/bin/python
import json, pprint
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from models import *
def get_requirements():

    consultant_data = edit_profile.objects.all()
    for idata in consultant_data:

        skill = idata.technology
        city = idata.job_location
        print idata
        print idata.requested_email
        nextUrl = '/api/rest/jobsearch/v1/simple.json?skill=' + skill + '&city='+city+'&age=1&page=1'
        main_dict = {}
        while (1):
            try:

                req = requests.get('http://service.dice.com' + nextUrl)
                main_dict[str(nextUrl.split("page=")[1])] = json.loads(req.text)['resultItemList']
                # print(json.loads(req.text)['resultItemList'])
                nextUrl = json.loads(req.text)['nextUrl']
                # print(nextUrl)
            except:
                break

        pp = pprint.PrettyPrinter(indent=4)
        a = [
            '<br><a href="{}">"jobTitle":{},"company":{},"location":{}</a>'.format(
                i['detailUrl'], i["jobTitle"], i["company"], i["location"])
            for kd in main_dict.keys() for i in main_dict[kd]
            ]
        # pp.pprint(a)
        print(len(a))

        fromaddr = "suhas.j@consultadd.com"

        toaddr = idata.requested_email
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Python Requirements in NJ/NY"

        body = "".join(a)
        msg.attach(MIMEText(body, 'html'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "myid@2138")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
