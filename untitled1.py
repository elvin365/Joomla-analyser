# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:00:31 2019

@author: Elvin
"""
import re
from bs4 import BeautifulSoup
import requests
from requests.exceptions import ConnectionError
import urllib.request
import shutil
from urllib.request import Request, urlopen
from urllib.error import  URLError
comp=[]
comp1=[]# to get comps in proper way without duplicates
comp1_css=[] 
mod=[]
mod1=[]# get separating css and other stuff
mod_css=[]
plug=[]
plug1=[]
plug_css=[]
def get_num(x):
    return (''.join(ele for ele in x if ele.isdigit() or ele == '.'))
def version_joomla_finder(li):
    mystr=li;
    j_ver_160=('/administrator/manifests/files/joomla.xml')
    j_ver_150_26=('/language/en-GB/en-GB.xml')
    j_ver_1=('/modules/custom.xml')
#For Joomla websites >= 1.6.0
    
    print(mystr+j_ver_160)# get the url to access the xml
   #---------------------------------------------------------------------------
   # response=urllib.request.Request(mystr+j_ver_160)
    #response=urllib.request.urlopen(mystr+j_ver_160)
   # print(response.read())
#    request = requests.get(mystr+j_ver_160)
#    if request.status_code == 200:
#        print('Web site exists')
#    else:
#        print('Web site does not exist') 
   #r=requests.get(mystr+j_ver_160)
   #print(r.status_code)
    req = Request(mystr+j_ver_160)
    try:
     response = urlopen(req)
    except URLError as e:
     if hasattr(e, 'reason'):
        #print('We failed to reach a server.')
        #print('Reason: ', e.reason)
        #For Joomla websites >= 1.5.0 and <= 1.5.26
        req1 = Request(mystr+j_ver_150_26)
        try:
         response = urlopen(req1)
        except URLError as e:
         if hasattr(e, 'reason'):
             req2 = Request(mystr+j_ver_1)
             try:
              response = urlopen(req2)
             except URLError as e:
              if hasattr(e,'reason'):
                  print(e.reason)
             else:
                 with urllib.request.urlopen(mystr+j_ver_150_26) as response, open('file_name.txt', 'wb') as out_file:
                     shutil.copyfileobj(response, out_file) 
        else:
          with urllib.request.urlopen(mystr+j_ver_150_26) as response, open('file_name.txt', 'wb') as out_file:
            shutil.copyfileobj(response, out_file) 
    else:
    # everything is fine    
    # Download the file from `url` and save it locally under `file_name`:

        with urllib.request.urlopen(mystr+j_ver_160) as response, open('file_name.txt', 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
    #--------------------------------------------------------------------------
    out_file.close()
    out_file=open('file_name.txt')
    ver = '<version>'
    
    for i in out_file:
        #line = out_file.readline()
       # print (i)
        if ver in i:
            break
    out_file.close()
    
    #print(get_num(i))
    return get_num(i)
        
   # try:
   #  urllib.request.urlopen(response)
     #print(response.read())
    # response = requests.get(mystr+j_ver_160)
    # response.raise_for_status()
   # except urllib.error.HTTPError as e:
   #  print(e.code)
   #  print(e.read())    
    
    #print(response.raise_for_status())
    
    
    #r=requests.get(mystr+j_ver_160)
   # print(response.read())
    #str1=response.read()
    #print(str1)
    #print(r.status_code)
   # if r.status_code == requests.codes.ok: # everything is ok, it exists, then get a data
def saveinhtml(li):
    with urllib.request.urlopen(li) as response, open('the_site.txt', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
        out_file.close()

def strcmp(res1,res2):
    if res1 in res2:
        return True
    else:
        return False
# Just trying to find every comp on a site 
def look_for_comp(li):
    out_file=open('the_site.txt','r',encoding='Latin-1')
    mytext=out_file.read()
    #result = re.findall(r'/com_\w+\D', mytext)
    result = re.findall(r'/com_\S[^\/]+', mytext)
    #print (result)
    for x in result:
        if not x in comp:
            comp.append(x) # now we got comp directories in comp
    #additional search for componetnts
    result2 = re.findall(r'=com_\S[^&|^\"]+', mytext)
    for x in result2:
        if not x in comp:
            comp.append(x) # now we got  ALL comp directories in comp
    for i in range(len(comp)):
        if '=' in comp[i]:
            comp[i]=comp[i][1:len(comp[i])]       
    #print(comp)
    for i in range(len(comp)):
        if '/' in comp[i]:
            comp[i]=comp[i][1:len(comp[i])]
    for x in comp:
        if not x in comp1:
            comp1.append(x)
    
    #print(comp)
    # let us find .css now 
    result3 = re.findall(r'/com_\S+.css', mytext)
    #print(result3)
    for x in result3:
        if not x in comp1_css:
            comp1_css.append(x) #now we got .css directories 
    #print(comp)
    print('\n')
    out_file.close()
#    print(comp[2][0])
#    comp[2]=comp[2][1:len(comp[2])]
#    print(comp[2])
    
            #print(comp[i])
            
    print(comp1)
    print(comp1_css)        

def look_for_mod(li):
    out_file=open('the_site.txt','r',encoding='Latin-1')
    mytext=out_file.read()
    #result = re.findall(r'/com_\w+\D', mytext)
    result = re.findall(r'/mod_\S[^\.+^\/]+[^\W+^\.+]\/+', mytext)
    #print (result)
    for x in result:
        if not x in mod:
            mod.append(x) # now we got comp directories in mod
 
    #print(mod)
    # let us find .css now 
    result2 = re.findall(r'/mod_\S+.css', mytext)
    #print(result2)
    for x in result2:
        if not x in mod:
            mod.append(x) #now we got .css directories 
    print(mod)
    out_file.close()
    
def look_for_plug(li):
    out_file=open('the_site.txt','r',encoding='Latin-1')
    mytext=out_file.read()
    result = re.findall(r'/plugins/\S+?\/+\S+?\/', mytext) # looking for directories for xml
   # print(result)
    for x in result:
        if not x in plug:
            plug.append(x) # now we got comp directories in plug
#    print(plug)
    #All for xml have found 
    #now looking for .css
    result2 = re.findall(r'/plugins/\S+.css', mytext)
   # print(result2)
    for x in result2:
        if not x in plug:
            plug.append(x) # now we got comp directories in plug
    print(plug)
    out_file.close()



def info_comp(li):
    
    for i in range(len(comp1)):
        li1=li+'/administrator/components'
        buf=comp1[i]
        # fixing / and /
        buf=buf='/'+buf+'/'
        buf1=buf[5:len(buf)-1]+'.xml'
        li1=li1+buf+buf1
       # print(li1)
         # chekning the url we've got by the http response
        req = Request(li1)
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server via ', li1)
                print('Reason: ', e.reason)
                print('Continue attempts...')
                continue
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request via ', li1)
                print('Error code: ', e.code)
                print('Continue attempts...')
                continue
        else:
            with urllib.request.urlopen(li1) as response, open('the_xml.txt', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
        out_file.close()
        out_file=open('the_xml.txt','r',encoding='Latin-1')
        # searching for name , version and description
        name='<name>'
        description='<description>'
        version='<version>'
        for x in out_file:
            if name in x:
                x=x.replace("<name>","")
                x=x.replace("</name>","")
                print('The name of the component is ',x)
            if description in x:
                x=x.replace("<description>","")
                x=x.replace("</description>","")
                print('Some description of component ',x)
            if version in x:
                x=x.replace('<version>',"")
                x=x.replace('</version>',"")
                print('The version is of component ',x)
            

def info_comp_css(li):
    for i in range(len(comp1_css)):
        li1=li+'/components'
        li1=li1+comp1_css[i]
        req = Request(li1)
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server using css via',li1)
                print('Reason: ', e.reason)
                continue
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request via',li1)
                print('Error code: ', e.code)
                continue
        else:
            with urllib.request.urlopen(li1) as response, open('the_css.txt', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
        out_file.close()
        out_file=open('the_css.txt','r',encoding='Latin-1')
        print('The info from ',li1)
        author='* @author'
        package='* @package'
        version='* @version'
        copyright1='* @copyright'
        mytext=out_file.read()
        result = re.findall(r'@author', mytext)
        if not result:
            print('No info about component in there')
        else:
            out_file.seek(0)
            for j in out_file:
                if author   in j:
                    print(j)
                if package in j:
                    print(j)
                if version in j:
                    print(j)
                if copyright1 in j:
                    print(j)
        
def info_mod(li):
    for i in range(len(mod1)):
        li1=li+'/modules'+mod1[i]
        buf=mod1[i][1:len(mod1[i])-1]+'.xml'
        li1=li1+buf 
        #print(li1)
        # chekning the url we've got by the http response
        req = Request(li1)
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server via ', li1)
                print('Reason: ', e.reason)
                print('Continue attempts...')
                continue
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request via ', li1)
                print('Error code: ', e.code)
                print('Continue attempts...')
                continue
        else:
            with urllib.request.urlopen(li1) as response, open('the_xml1.txt', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
        out_file.close()
        out_file=open('the_xml1.txt','r',encoding='Latin-1')
        # searching for name , version and description
        name='<name>'
        description='<description>'
        version='<version>'
        for x in out_file:
            if name in x:
                x=x.replace("<name>","")
                x=x.replace("</name>","")
                print('The name of the module is ',x)
            if description in x:
                x=x.replace("<description>","")
                x=x.replace("</description>","")
                print('Some description of module ',x)
            if version in x:
                x=x.replace('<version>',"")
                x=x.replace('</version>',"")
                print('The version of module is ',x)
#        out_file.close()       
          
            
def info_mod_css(li):
    for i in range(len(mod_css)):
        li1=li+'/modules'
        li1=li1+mod_css[i]
        req = Request(li1)
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server using css via',li1)
                print('Reason: ', e.reason)
                continue
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request via',li1)
                print('Error code: ', e.code)
                continue
        else:
            with urllib.request.urlopen(li1) as response, open('the_css1.txt', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
        out_file.close()
        out_file=open('the_css1.txt','r',encoding='Latin-1')
        print('The info from ',li1)
        author='* @author'
        package='* @package'
        version='* @version'
        copyright1='* @copyright'
        mytext=out_file.read()
        result = re.findall(r'/\*\*', mytext)
        if not result:
            print('No info about module in there')
        else:
            out_file.seek(0)
            for j in out_file:
                if author   in j:
                    print(j)
                if package in j:
                    print(j)
                if version in j:
                    print(j)
                if copyright1 in j:
                    print(j)            
            
def cut_back(buf):
    buf=buf[1:len(buf)-1]
    r=buf[::-1]
    return(r[0:r.find('/')])

def info_plug_long(li):
       for i in range(len(plug1)):
        li1=li+plug1[i]
        buf=plug1[i]
        buf1=cut_back(buf)
        buf1=buf1[::-1]
        li1=li1+buf1+'.xml'
        print(li1)
        # chekning the url we've got by the http response
        req = Request(li1)
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server via ', li1)
                print('Reason: ', e.reason)
                print('Continue attempts...')
                continue
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request via ', li1)
                print('Error code: ', e.code)
                print('Continue attempts...')
                continue
        else:
            with urllib.request.urlopen(li1) as response, open('the_xml2.txt', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
        out_file.close()         
        out_file=open('the_xml2.txt','r',encoding='Latin-1')
        # searching for name , version and description
        name='<name>'
        description='<description>'
        version='<version>'
        for x in out_file:
            if name in x:
                x=x.replace("<name>","")
                x=x.replace("</name>","")
                print('The name of the plugin is ',x)
            if description in x:
                x=x.replace("<description>","")
                x=x.replace("</description>","")
                print('Some description of plugin ',x)
            if version in x:
                x=x.replace('<version>',"")
                x=x.replace('</version>',"")
                print('The version of plugin is ',x)    
            
  

def info_plug_short(li):
    for i in range(len(plug1)):
        plug1[i]=plug1[i][:-1]
        li1=li+plug1[i]+'.xml'
        print(li1)
        # chekning the url we've got by the http response
        req = Request(li1)
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server via ', li1)
                print('Reason: ', e.reason)
                print('Continue attempts...')
                continue
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request via ', li1)
                print('Error code: ', e.code)
                print('Continue attempts...')
                continue
        else:
            with urllib.request.urlopen(li1) as response, open('the_xml3.txt', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
        out_file.close()         
        out_file=open('the_xml3.txt','r',encoding='Latin-1')
        # searching for name , version and description
        name='<name>'
        description='<description>'
        version='<version>'
        for x in out_file:
            if name in x:
                x=x.replace("<name>","")
                x=x.replace("</name>","")
                print('The name of the plugin is ',x)
            if description in x:
                x=x.replace("<description>","")
                x=x.replace("</description>","")
                print('Some description of plugin ',x)
            if version in x:
                x=x.replace('<version>',"")
                x=x.replace('</version>',"")
                print('The version of plugin is ',x)


def info_plug_css(li):
    
    for i in range(len(plug_css)):
        li1=li+plug_css[i]
        req = Request(li1)
        try:
            response = urlopen(req)
        except URLError as e:
            if hasattr(e, 'reason'):
                print('We failed to reach a server using css via',li1)
                print('Reason: ', e.reason)
                continue
            elif hasattr(e, 'code'):
                print('The server couldn\'t fulfill the request via',li1)
                print('Error code: ', e.code)
                continue
        else:
            with urllib.request.urlopen(li1) as response, open('the_css2.txt', 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)
        out_file.close()
        out_file=open('the_css2.txt','r',encoding='Latin-1')
        print('The info from ',li1)
        author='* @author'
        package='* @package'
        version='* @version'
        copyright1='* @copyright'
        mytext=out_file.read()
        result = re.findall(r'/\*\*', mytext)
        if not result:
            print('No info about plugin in there')
        else:
            out_file.seek(0)
            for j in out_file:
                if author   in j:
                    print(j)
                if package in j:
                    print(j)
                if version in j:
                    print(j)
                if copyright1 in j:
                    print(j)
        
    





          
print("Enter the URL")
li=[]
li=input()
if li[-1]=='/':
    #li.pop()
    li=li[:-1] #say eatshit you slash 
#print(li);
#print('You entered'+li)
#r=requests.get('https://github.com')
#print(r)

print('The Joomla version is ',version_joomla_finder(li))
#------------------------------------------------------------------------------
#NOW lets see components, modules and plugs 

saveinhtml(li) # save the html of the site 

look_for_comp(li)
look_for_mod(li)
look_for_plug(li)
#------------------------------------------------------------------------------
# when we got all comps, mods and plugs , let head us to find info about them


# let's start with comps
if not comp:
    print('No components on the site')
info_comp(li) # in this func we will fix the url and get the info
info_comp_css(li)
if not mod:
    print('No modules on the site')
# separating /mod xml  and .css mod
for i in range(len(mod)):
        if '.css' in mod[i]:
            mod_css.append(mod[i])
        else:
            if not '.js' in mod[i]:
               mod1.append(mod[i])
info_mod(li)
info_mod_css(li)
if not plug:
    print('No plugins on the site')
# now plugins 
for i in range(len(plug)):
     if '.css' in plug[i]:
         plug_css.append(plug[i])
     else:
         if not '.js' in plug[i]:
             plug1.append(plug[i]) #rest
info_plug_long(li)
info_plug_short(li)
info_plug_css(li)




