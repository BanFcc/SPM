# -*- coding: utf-8 -*-
import htmlfile
def RemoveSpace(s):
    res=""
    for c in s:
        if c==' ':
            continue
        res+=c
    return res
def WriteToCodeHtml(s, html,link):
    le=len(s)
    lst=-1
    ve=[]
    for i in range(le):
        if s[i]=='{':
            lst=i
        elif s[i]=='}':
            if s[lst+1:lst+4]=='see':
                ve.append((lst,i))
    lst=-1
    for rg in ve:
        html.AddText(s[lst+1:rg[0]])
        name=RemoveSpace(s[rg[0]+4:rg[1]])
        html.AddUrl(s[rg[0]:rg[1]+1],link+r'#'+name,name)
    if len(ve)==0:
        html.AddText(s,True)
    else:
        html.AddText(s[ve[-1][1]+1:-1],True)
def WriteToSrsHtml(s,html,link):
    le=len(s)
    flag=False
    lst=-1
    ve=[]
    for i in range(le):
        if i+12<le and s[i:i+12]=='@Requirement':
            flag=True
        if s[i]=='[':
            lst=i
        elif s[i]==']':
            if s[lst+1:lst+4]=='id=' and flag:
                ve.append((lst,i))
    lst=-1
    for rg in ve:
        html.AddText(s[lst+1:rg[0]])
        name=RemoveSpace(s[rg[0]+4:rg[1]])
        html.AddUrl(s[rg[0]:rg[1]+1],link+r'#'+name,name)
    if len(ve)==0:
        html.AddText(s,False)
    else:
        html.AddText(s[ve[-1][1]+1:-1],False)
    html.AddText("",True)
def CreatSrsHtml(fileName, html,link):
    f = open(fileName, "r", encoding='UTF-8')
    info = f.readlines()
    f.close()
    for s in info:
        WriteToSrsHtml(s, html,link)      

def CreatCodeHtml(codeName, html,link):
    f = open(codeName, "r", encoding='UTF-8')
    info = f.readlines()
    f.close()
    
    
    for s in info:
       # print(s)
        WriteToCodeHtml(s, html,link)
        
def GetName(fileName):
    pos = fileName.find('.')
    if pos >= 0:
        fileName = fileName[:pos]
    return fileName
        

if __name__ == '__main__':
    srsName = input()
    codeName = input()
    codeHtml = htmlfile.HtmlFile("code")
    srsHtml = htmlfile.HtmlFile("srs")
    CreatSrsHtml(srsName, srsHtml, GetName(codeName) + ".html")
    CreatCodeHtml(codeName, codeHtml, GetName(srsName) + ".html")
    codeHtml.CreatFile( GetName(codeName))
    srsHtml.CreatFile(GetName(srsName))