# -*- coding: utf-8 -*-
import htmlfile
Requirement = []
Rationale = []
TestCase = []
def RemoveSpace(s):
    res=""
    for c in s:
        if c==' ':
            continue
        res+=c
    return res
def WriteToCodeHtml(s, html, link):
    le = len(s)
    lst = -1
    ve = []
    for i in range(le):
        if s[i] == '{':
            lst = i
        elif s[i] == '}':
            if s[lst + 1:lst + 4] == 'see': 
                ve.append((lst, i))
                lst=-1
                
    lst=-1
    for rg in ve:
        html.AddText(s[lst + 1:rg[0]])
        name = RemoveSpace(s[rg[0] + 4:rg[1]])
        html.AddUrl(s[rg[0]:rg[1] + 1], link + r'#' + name, name)
    if len(ve) == 0:
        html.AddText(s,True)
    else:
        html.AddText(s[ve[-1][1] + 1:-1], True)
def WriteToSrsHtml(s,html,link):
    le=len(s)
    srq='@Requirement'
    sra='Rationale'
    stc='TestCase'
    frq = False
    fra = False
    ftc = False
    lst=-1
    rq=[]
    ra=[]
    tc=[]
   # print(s)
    for i in range(le):
        if i+len(srq)<le and s[i:i+len(srq)]==srq:
            frq=True
        if i+len(sra)<le and s[i:i+len(sra)]==sra:
            fra=True
        if i+len(stc)<le and s[i:i+len(stc)]==stc:
            ftc=True
        if s[i]=='[':
            lst=i
        elif s[i]==']':
            if s[lst+1:lst+4]=='id=':
                if frq:
                    rq.append((lst, i))
                    frq = False
                elif fra:
                    ra.append((lst, i))
                    fra = False 
                elif ftc:
                    tc.append((lst, i))
                    ftc = False
                lst=-1      
    lst=-1
    for rg in rq:
        html.AddText(s[lst + 1:rg[0]])
        name = RemoveSpace(s[rg[0] + 4:rg[1]])
        Requirement.append(name)
        html.AddUrl(s[rg[0]:rg[1]+1],link+r'#'+name,name)
    if len(rq) == 0:
        html.AddText(s,False)
    else:
        html.AddText(s[rq[-1][1] + 1:-1], False)
    for rg in ra:
        name = RemoveSpace(s[rg[0] + 4:rg[1]])
        Rationale.append(name)
    for rg in tc:
       # print(rg)
        name = RemoveSpace(s[rg[0] + 4:rg[1]])
        TestCase.append(name)
    
    html.AddText("", True)
def CreatSrsHtml(fileName, html, link):
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

def GetMatrix(row,col):
    tmp=[""]
    tmp.extend(row)
    matrix=[]
    matrix.append(tmp)
 #   print(len(row))
    for i in range(len(col)):
        tmp = []
        tmp.append(col[i])
        for j in range(len(row)):
            tmp.append(" ")
        matrix.append(tmp)
  #  for r in matrix:
  #      print(r)
    return matrix

if __name__ == '__main__':
    srsName = input()
    codeName = input()
  #  srsName='srs.txt'
  #  codeName='code.py'
    codeHtml = htmlfile.HtmlFile("code")
    srsHtml = htmlfile.HtmlFile("srs")
    CreatSrsHtml(srsName, srsHtml, GetName(codeName) + ".html")
    CreatCodeHtml(codeName, codeHtml, GetName(srsName) + ".html")
    srsHtml.CreatMatrix(GetMatrix(Requirement, Requirement))
    srsHtml.CreatMatrix(GetMatrix(Rationale, Requirement))
    srsHtml.CreatMatrix(GetMatrix(TestCase, Requirement))
    codeHtml.CreatFile(GetName(codeName))
    srsHtml.CreatFile(GetName(srsName))
