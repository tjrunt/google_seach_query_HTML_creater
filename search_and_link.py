#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python 3.4.3


import sys, os, random, shutil 


#google = 'https://www.google.com/'


Opening_htmlTags = "<!DOCTYPE html><html><head></head><Body>"
Closing_htmlTags = "</body></html>"


#example tag
#  <a href="http://www.w3schools.com/html/">Visit our HTML tutorial</a>

p_tag_o = "<p>"
p_tag_c = "</p>"
links_o = '<a href="'
links_o_2= '">'
links_c = '</a>'
url= ''
linkText = ''

#file = '_____wesites.txt'
file = 'AUG-14-dataEntry1.txt'



def readFile(linkPath):
    # read product links
    filename=open(linkPath,'r')
    f=filename.readlines()
    filename.close()
    return f

# add affilate id and choose between ? or &
def formatlink(f, google):
    posts = []
    for i in f:
        #print(i[0:-2])
        i = google + '\"' + i[0:-2] +'\"' + ' intext:EMAIL'
        posts.append(i) 
    return posts

def writeFile(text, url,):
    # read product links
    filename=open(linkPath,'w')
    for i in textToWrite:
        filename.write(i +'\n')
    filename.close()
    return


myText =readFile(file)
#myLinks = formatlink(myText, google)
myLinks = formatlink(myText, '')

htlm_links = 'AUG-14-dataEntry1.html'

filename=open(htlm_links,'w')
filename.write(Opening_htmlTags)


#example tag
#  <a href="http://www.w3schools.com/html/">Visit our HTML tutorial</a>
count = 0
rows = len(myText)
while count < rows:
    filename.write(p_tag_o)
    filename.write(links_o)
    filename.write(myLinks[count])
    filename.write(links_o_2)
    filename.write(myText[count])
    filename.write(links_c)
    filename.write(p_tag_c)
    count = count + 1

filename.write(Closing_htmlTags)


filename.close()






