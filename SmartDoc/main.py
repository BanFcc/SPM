import htmlfile
def WriteToHtml(s, html,link):
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
        html.AddUrl(s[rg[0]:rg[1]+1],link+r'/'+s[rg[0]+4:rg[1]],s[rg[0]+4:rg[1]])
    if len(ve)==0:
        html.AddText(s,True)
    else:
        html.AddText(s[ve[-1][1]+1:-1],True)

def CreatSrsHtml(fileName, html,link):
    f = open(fileName, "r", encoding='UTF-8')
    info = f.readlines()
    f.close()
    for s in info:
        WriteToHtml(s, html,link)      

def CreatCodeHtml(codeName, html,link):
    f = open(codeName, "r", encoding='UTF-8')
    info = f.readlines()
    f.close()
    
    
    for s in info:
        #print(s)
        WriteToHtml(s, html,link)
   


if __name__ == '__main__':
    srsName = input()
    codeName = input()
    codeHtml = htmlfile.HtmlFile("code")
    srsHtml = htmlfile.HtmlFile("srs")
    CreatSrsHtml(srsName, srsHtml,"code.html")
    CreatCodeHtml(codeName, codeHtml,"srs.html")
    codeHtml.CreatFile("code")
    srsHtml.CreatFile("srs")