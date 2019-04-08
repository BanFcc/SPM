
# -*- coding: utf-8 -*-
#help create a html file
class HtmlFile:
    def changeString(self,str):
        newStr=""
        for c in str:
            if c == ' ':
                newStr += "&nbsp;"
            elif c=='"':
                newStr += "&quot;"
            elif c == "&":
                newStr += "&amp;"
            elif c=='<':
                newStr += "&lt;"
            elif c == '>':
                newStr += "&gt;"
            else:
                newStr+=c
        str=newStr
    class Node:
        def __init__(self, info, idx, flag):  
            self.idx=idx
            self.son = []
            self.info = info
            self.flag = flag
    def __init__(self, title):
        self.title = title
        self.webSite = []
        self.cnt = 0
    def addNode(self, info, flag):
        self.webSite.append(self.Node(info, self.cnt + 1, 1))
        self.cnt+=1
    def addText(self, text):
        self.changeString(text)
        self.addNode(text, 1)
    def writeHead(self, title, css):
        res = []
        res.append("<head>")
        res.append("<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />")
        res.append("<title>" + title + "</title>")
        res.append("<link rel=\"stylesheet\" type=\"text/css\" href=\"materials/"+css+"\" />")
    def creatFile(self, fileName):
        fp = open(fileName + ".html", w)
        fp.write("<html xmlns=\" http: // www.w3.org / 1999 / xhtml \">" + "\n")
        fp.writelines(self.writeHead(self.title, "myCss.css"))
        
        fp.close()
        
        


        
