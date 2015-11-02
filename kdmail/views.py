from django.shortcuts import render
from django.shortcuts import render, RequestContext, render_to_response, get_object_or_404
from  django.db import backends
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import *
from form import *
# from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, DetailView, ListView
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
import hashlib, datetime, random
from django.utils import timezone
import email, getpass, imaplib
import json as json
import time,datetime
import string

# from termcolor import colored
#import re


# Create your views here.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'


def date_check(x):
    if x=='Jan':
        mon=1

    elif x=='Feb':
        mon=2

    elif x=='Mar':
        mon=3

    elif x=='Apr':
        mon=4

    elif x=='May':
        mon=5

    elif x=='Jun':
        mon=6

    elif x=='Jul':
        mon=7

    elif x=='Aug':
        mon=8

    elif x=='Sep':
        mon=9

    elif x=='Oct':
        mon=10

    elif x=='Nov':
        mon=11

    else:
        mon=12

    return mon


def get_first_text_block(email_message_instance):
            NI=['jobs-noreply@cybercoders.com','applyonline@dice.com',\
                'invitations@linkedin.com','linkedin@e.linkedin.com','linkedin@e.linkedin.com']
            print "[" + email_message_instance["From"] + "] :" + email_message_instance["Subject"]
            if email_message_instance["From"] in NI or 'linkedin' in email_message_instance["From"]:
                return "cool"
            maintype = email_message_instance.get_content_maintype()
            if maintype == 'multipart':
                for part in email_message_instance.get_payload():
                    if part.get_content_maintype() == 'text':
                        print "ICE COOOOOOL"
                        return part.get_payload()

            elif maintype == 'text':
                # print "COOOOOOL"

                return "Not so COOL"


def mainfunc(statename,u,p):
    detach_dir = '.'  # directory where to save attachments (default: current)
    # user = raw_input("Enter your GMail username:")
    # pwd = getpass.getpass("Enter your password: ")
    cool = []
    count_list=[]
    c2 = []

    field = statename
    if field.isdigit():
        print "\n Please enter valid state name....\nABORTING !!"
        exit()
    user = u  #  "kunjan.dhoble@consultadd.in"  'kun2233dh@gmail.com'
    pwd = p  # "changeiscool"     "kdrocks@31"
    # anshi241215@gmail.com    ,   anscon2015


#SWAPNIL
    # "sung52me@gmail.com",   "h0907joy@gmail.com"       , "joyguru291@gmail.com",
    # "ha904ra@gmail.com"   ,        "um09bh@gmail.com"

    # pwd= consultadd505
#SWAPNIL

    #SUJO

    # 2809sjt@gmail.com  ...           pwd=sushant@2814
    # 9692sjp@gmail.com
    # 2809sjp@gmail.com
    # 2196rt@gmail.com

    #SUJO


    date_list=[]
    kd=[]
    d1={}
    d={}

    count=0
    a=[]
    list_of_em=[]
    t=0


    #Today's date:
    today,today1="",""
    today+=time.strftime("%d")+" "+time.strftime("%b")
    print "TODAY: ",today
    yy=int(time.strftime("%Y"))
    mm=int(time.strftime("%m"))
    dd=int(time.strftime("%d"))
    print "Check date:",dd,mm,yy




    for l in range(len(user)):
        # print colored('USERNAME :', 'red', 'on_grey', attrs="bold")

        print color.BOLD + color.OKBLUE + "USERNAME :" + color.END + color.HEADER + color.RED + color.UNDERLINE + "\v ", (user[l]) + color.END


        # connecting to the gmail imap server

        m = imaplib.IMAP4_SSL("imap.gmail.com")

        m.login(user[l], pwd[l])


        # m.select("[Gmail]/All Mail") #SELECTS ALL THE MAILBOXES
        # here you a can choose a mail box like INBOX instead
        # use m.list() to get "LIST all the mailboxes" -"INBOX",, "[Gmail]",,"[Gmail]/All Mail"
        m.select("INBOX")  #(SELECTS ONLY INBOX)

        # print m.list()
        # resp, items = m.search(None, "ALL") # you could filter using the IMAP rules here (check http://www.example-code.com/csharp/imap-search-critera.asp)

        result, items = m.uid('search', None, "ALL")  # search and return uids instead
        # print "before",items
        items = items[0].split()  # getting the mails id
        items=items[::-1] # Reverse List to get latest EM first

        print items
        count_list.append(len(items))

        number_emails= len()

        None_list=[]
        mail_id=[]
        sender=[]
        sub=[]
        msg=[]
        date=[]
        lnth=len(items)
        nxt=[]
        final=""
        for idx, emailid in enumerate(items):
        # result, data = m.fetch(emailid, '(RFC822)')

            result, data = m.uid("fetch", emailid, '(RFC822)') # fetching the mail, "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
            email_body = data[0][1] # getting the mail content
            mail = email.message_from_string(email_body) # parsing the mail content to get a mail object
            count=0
            #CHECK DATE
            dt=""
            dt=mail["Date"].split(', ', 1)
            print mail['Date'],"kd :  ",dt

            # print "OSM"
            if len(dt)==1:
                dt=dt[0].split(' 2015')
            else:
                dt=dt[1].split(' 2015')
            dt=dt[0]
            x=dt.split()
            # yr=""
            mon=date_check(x[1])
    
            day=int(x[0])
            yr=2015
            print "mail date",day,mon,yr
    
    
            date_1 = datetime.datetime(yr,mon,day)
            date_2 = datetime.datetime(yy,mm,dd)
            diff=(date_2-date_1).days
            print "GAP: ",diff

            if diff>14:
                break

            if mail.is_multipart():
                for payload in mail.get_payload():
                    if count!=0:
                        break
                    # if payload.is_multipart(): ...
                    count+=1
                    # print "RIDDICKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK"
                    final=payload.get_payload()
            else:
                print "POSITIVE",emailid
                nxt.append(mail.get_payload())


            salutation=["Greetings","Hello","Hi","Dear"]
            for j in salutation:
    
                if j in final:
                    txt=final.split(j)
                    final=txt[1]
                    # print "salutation",j
                    break
    
    
            signoff=["Regards","regards","Thank","thank","Thanks","thanks","Best","best","Truly","truly","Sincerely","sincerely","Yours","yours"]
    
            for off in signoff:
                if off in final:
                    txt=final.split(off)
                    msg.append(txt[0])
                    t+=1
                    break
                else:
                    msg.append(final)


            if len(msg)==0:
                print "Continue", emailid,mail['From']," \t  ",mail['Date']

                continue
            sender.append(mail["From"])
            sub.append(mail["Subject"])
            em_content={}
            if "LinkedIn" not in mail["From"]:
                em_content['From']=mail["From"]
                em_content['Subject']=mail["Subject"]
                if len(msg[0])!=2:
                    em_content['Body']=msg[0]
                else:
                    st=0
                    for i in msg[0]:
                        if st==0:
                            # print i,"iiiiiiiiiiiiiiiiiiiii"
                            st+=1
                            em_content['Body']=str(i)
                            # print "em_content",em_content
                            # print "ZEROhgjghjg",len(msg[0])
                        else:
                            print "test fail"
                msg=[]
                if idx==0:
                    a.append(dt)
                    list_of_em.append(em_content)

                    d[dt]=em_content
                    print "in"
                elif idx==len(items)-1:
                    print "elif"
                    list_of_em.append(em_content)
                    d[a[0]]=list_of_em
                    if dt not in a:
                        d[dt]=em_content
                    a,list_of_em=[],[]


                else:
                    print "else"
                    if dt not in a:
                        print "else in",list_of_em
                        if len(list_of_em)==0:
                            a.append(dt)
                            list_of_em.append(em_content)
                            d[a[0]]=list_of_em


                        else:
                            d[a[0]]=list_of_em
                            a=[]
                            a.append(dt)
                            list_of_em=[]
                            list_of_em.append(em_content)
                        # print "ELSE .........ajskAJH  IF"
                    else:
                        # print "ELSE////////////ELSE"
                        list_of_em.append(em_content)

        # date.append(mail["Date"])
        # l1=['date1','date1','date1','date2','date2']#LIST OF DATES
        # lnth=len(kd)
        # for idx, val in enumerate(kd):

        # print list_of_em
        a,list_of_em,msg=[],[],[]
        if user[l]=='kun2233dh@gmail.com':
            print "Type",type(d)
        d1[user[l]]=dict(d)

        print "TypeD1",type(d1)
        with open('/home/consultadd6/Desktop/'+str(user[l])+'.json', 'wb') as out:
            json.dump(str(d1), out)
    
        # json_data=open('/home/consultadd6/Desktop/'+str(user[l])+'.json').read()
        # kd = json.loads(json_data)

        
        
        # 
        # for i in range(len(msg)):
        #     if field in msg[i]:
        #         a = ""
        # 
        #         a += "SENDER :\t" + str(sender[i]) + "\t"
        #         a += "SUBJECT:\t" + sub[i]
        #         # print "SENDER: ",sender[i]
        #         # print "SUBJECT: ",sub[i]
        #         # print "GOTCHA!!!!!!\n \n",msg[i]
        #         c1.append(a)
        #         c2.append(msg[i])
        # 
        # cool.append(c1)
        # cool.append(c2)
        # print "Length1", len(c1)
        # print "Length2", len(c2)
        # print "LIST OF IDS CONTAINING KEYWORD\n",c1
    return count_list

def retrieve_em(statename,gm_id):
    # state=statename
    state_l=statename.lower()
    state_u=statename.upper()
    state_t=statename.title()
    sender_list, sub_list, em_body_list, cool=[], [], [], []
    for i in gm_id:
        json_data=open('/home/consultadd6/Desktop/'+i+'.json').read()
        kd = json.loads(json_data)
        # print kd['anshi241215@gmail.com']['27 Oct'][1]['From']  #This is OSM ABOUT PYTHON :D:D:D
        kd=eval(kd)

        for it,val in kd.iteritems():
            for it1,val1 in val.iteritems():
                for i in val1:
                    # print i['Body'],"BBBBBBBBBBBBBBBBBBBBBBBBBBBBB\n"
                    if statename in i['Body'] or state_l in i['Body']\
                            or state_u in i['Body'] or state_t in i['Body']:
                        sender,sub,em_body="","",""
                        sender+=str(i['From'])
                        sub+=str(i['Subject'])
                        em_body+=str(i['Body'])
                        sender_list.append(sender)
                        sub_list.append(sub)
                        em_body_list.append(em_body)

    #
    # print kd['anshi241215@gmail.com']['27 Oct'][1]['From']  #This is OSM ABOUT PYTHON :D:D:D



    cool.append(sender_list)
    cool.append(sub_list)
    cool.append(em_body_list)
    return cool




def filter_res_view(request):
    if request.GET:
        print "GETTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT"

 # URL hit to avoid loss of data on refresh
    if request.POST:
        print "POSTTTTTTTTTTTTTTTT"
    form1 = request.POST
    print form1
    userid=request.user.id
    print userid

    a=edit_profile.objects.get(user_id=userid)


    b=a.id_field
    c=a.pass_field
    ids=b.split(',')
    pwd=c.split(',')
    print ids
    print pwd
    if form1 is not None and len(form1) == 3 and form1.has_key('state'):
        print "FORM INPUTS : \n", form1
        res = str(form1['state'])
        # k=mainfunc(res,ids,pwd)
        res=retrieve_em(res,ids)
        sndr= res[0]
        hdr = res[1]
        msg = res[2]
        print "\v\nSENDER:",sndr

        ln = len(msg)
    else:
        # print "FORM INPUTS : \n",form1
        # form1['state']='New Jersey'
        # res=str(form1['state'])
        # res=mainfunc(res)
        # hdr=res[0]
        # msg=res[1]

        # ln=len(msg)
        sndr,hdr, msg, ln = 0, 0, 0, 0

        # print "USERNAME: ",form1['username']
        # print "STATE : ",form1['state']
    return render_to_response('kdmail/filter_res.html',
                                  {'form': form1,'res_sender':sndr, 'res_header': hdr, 'res_msg': msg, 'size': ln},
                                  context_instance=RequestContext(request))
    # else:
    #     return HttpResponseRedirect('/getmail/results/')

def welcome(request):
    if request.POST:
        print "cool"
        form2 = request.POST
        print form2
        return HttpResponseRedirect('/getmail/results/')
    # var doughnutData = [
    #     {
    #         value: 3000,
    #         color:"#F7464A",
    #         highlight: "#FF5A5E",
    #         label: "Mobile"
    #     },

    a={}
    b=[]
    a['value']=1000
    a['color']="#46BFBD"
    a['highlight']= "#5AD3D1"
    a['label']= "Kitchen"

    b.append(a)
    a={}
    a['value']=2000
    a['color']="#46BFBD"
    a['highlight']= "#5AD3D1"
    a['label']= "Mobile"

    b.append(a)
    a={}
    a['value']=6000
    a['color']="#46BFBD"
    a['highlight']= "#5AD3D1"
    a['label']= "Home"


    b.append(a)
    b_json=json.dumps(str(b))
    b_json=json.loads(b_json)
    b_json=eval(b_json)

    print type(b_json)

    #     {
    #         value: 1000,
    #         color: "#FDB45C",
    #         highlight: "#FFC870",
    #         label: "Home"
    #     },
    # {
    #         value: 1000,
    #         color: "#FDB45C",
    #         highlight: "#FFC870",
    #         label: "Home"
    #     }

    return render_to_response('kdmail/welcome.html',{'b_json':b_json},
                              context_instance=RequestContext(request))


def register_view(request):
    args = {}
    args.update(csrf(request))
    if request.method == 'POST':
        form = MyForm(request.POST)
        args['form'] = form
        if form.is_valid():
            form.save()  # save user to database if form is valid

            username = form.cleaned_data['username']
            a=(username).upper
            # password=form.cleaned_data['password']
            # print "PASSWORD", password
            email = form.cleaned_data['email']
            salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
            activation_key = hashlib.sha1(salt + email).hexdigest()
            key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by username
            user = User.objects.get(username=username)

            # Create and save user profile
            new_profile = EmailUser(user=user, activation_key=activation_key,
                                    key_expires=key_expires)
            new_profile.save()

            # Send email with activation key
            email_subject = 'Account confirmation'
            email_body = "Hey %s, thanks for signing up. We are pleased to welcome you in our small family which is growing big every minute thanks to people like you.\n\nTo activate your account, click this link within 48hours http://127.0.0.1:8000/getmail/confirm/%s" % (
                a, activation_key)

            send_mail(email_subject, email_body, 'myemail@example.com',
                      [email], fail_silently=False)

            return HttpResponseRedirect('/getmail/register/')
    else:
        args['form'] = MyForm()

    return render_to_response('kdmail/register.html', args, context_instance=RequestContext(request))


def auth_view(request):
    # args = {}
    # args.update(csrf(request))
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    print "COOL",username,password
    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)

        # d=1
        # -----------------------------------my test-----------------------------------------

        userid = request.user.id
        print "USERID : ",userid
        my_test = edit_profile.objects.get(user_id=userid)
        my_data = my_test.id_field
        print my_data, "mydata"
        if my_data == "Enter comma separated Gmail Ids":

            return HttpResponseRedirect('/getmail/add_ids/')


        else:

            return HttpResponseRedirect('/getmail/results/')



            # --------------------------------------end test----------------------------------------------
            # return HttpResponseRedirect('/fmar/locate/')

    else:
        return HttpResponseRedirect('/getmail/invalid/')



def register_confirm(request, activation_key):
    #check if user is already logged in and if he is redirect him to some other url, e.g. home
    if request.user.is_authenticated():
        HttpResponseRedirect('')

    # check if there is UserProfile which matches the activation key (if not then display 404)
    user_profile = get_object_or_404(EmailUser, activation_key=activation_key)

    #check if the activation key has expired, if it hase then render confirm_expired.html
    if user_profile.key_expires < timezone.now():
        return render_to_response('kdmail/invalid.html')
    #if the key hasn't expired save user and set him as active and render some template to confirm activation
    user = user_profile.user
    user.is_active = True
    user.save()
    # username=request.POST.get('username','')
    # print"user",username
    # password=request.POST.get('password','')
    # user=auth.authenticate(username=username,password=password)
    #
    # if user is not None and user.is_active:
    #     auth.login(request,user)
    # auth_view(request);
    return render_to_response('kdmail/register_confirm.html')
    # username=request.POST.get('username','')
    # password=request.POST.get('password','')
    # user=auth.authenticate(username=username,password=password)
    #
    # if user is not None and user.is_active:
    #     auth.login(request,user)
    #     return render_to_response('shwekd/profile.html')


def login_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('kdmail/login.html', c)


def invalid_view(request):
    return render_to_response('kdmail/invalid.html')


def logout_view(request):
    auth.logout(request)
    return render_to_response('kdmail/logout.html')

@login_required
def add_ids_view(request):
    try:
        instance = edit_profile.objects.get(user=request.user)
    except edit_profile.DoesNotExist:
        instance = None

    if request.method == 'POST':

        form = edit_profile_form(request.POST or None, request.FILES, instance=instance)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()

            # if form1 is not None and len(form1) == 3 and form1.has_key('state'):
            #     print "FORM INPUTS : \n", form1
            #     res = str(form1['state'])
            #     res = mainfunc(res)
            #     hdr = res[0]
            #     msg = res[1]
            #
            #     ln = len(msg)
            # else:
            #     # print "FORM INPUTS : \n",form1
            #     # form1['state']='New Jersey'
            #     # res=str(form1['state'])
            #     # res=mainfunc(res)
            #     # hdr=res[0]
            #     # msg=res[1]
            #
            #     # ln=len(msg)
            #     hdr, msg, ln = 0, 0, 0
            #
            # # print "USERNAME: ",form1['username']
            # # print "STATE : ",form1['state']
            # return render_to_response('kdmail/filter_res.html',
            #                       {'form': form, 'res_header': hdr, 'res_msg': msg, 'size': ln},
            #                       context_instance=RequestContext(request))


                    # message.succes('SAVED')
            # print form.pass_field

            return HttpResponseRedirect('/getmail/results/')

        else:
            print form.errors
    else:

        form = edit_profile_form(instance=instance)





    return render(request, 'kdmail/add_ids.html', {'form': form}, context_instance=RequestContext(request))

