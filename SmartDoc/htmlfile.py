
# -*- coding: utf-8 -*-
#help create a html file
textFlag = 1
urlFlag = 2

class HtmlFile:
    def ChangeString(self,text):
        newStr = ""
        for c in text:
            if c == ' ':
                newStr += "&ensp;"
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
        return newStr
        
    class Node:
        def __init__(self, info, idx, flag, Id=""):  #flag=1 文本  flag=2超链接 
            self.idx=idx
            self.son = []
            self.info = info
            self.flag = flag
            self.Id=Id

    def __init__(self, title):
        self.title = title
        self.webSite = []
        self.cnt = 0

    def AddNode(self, info, flag,Id=""):
        self.webSite.append(self.Node(info, self.cnt + 1, flag, Id))
        self.cnt += 1

    def AddText(self, text, Id=False):
        #print(text)
        text = self.ChangeString(text)
      #  print("- "+text)
        self.AddNode(text, 1,Id)

    def AddUrl(self, text, url, Id=""):
        text=self.ChangeString(text)
        self.AddNode((text, url), 2,Id)
        
    def WriteHead(self, title, css):
        res = []
        res.append(r'<head>')
        res.append(r'<meta charset="utf-8">')
        res.append(r'<title>' + title + r'</title>')
        res.append(r'</head>')
        #no css
        return res

    def WriteText(self, textNode):
        res = []
        if textNode.Id==False:
            res.append(r'<span>' + textNode.info + r'</span>')
        else:
            res.append(r'<p>' + textNode.info + r'</p>')
        return res

    def WriteUrl(self, urlNode):
        #info(1)url   info(0)text
        res = []
        s = r'<a '
        if urlNode.Id!="":
            s += r'name="' + urlNode.Id + r'" '
        s +=r'href="' +urlNode.info[1] + r'">' + urlNode.info[0] + r'</a>'
        res.append(s)
        return res
    
    def Dfs(self, node, num):
        for v in node.son:
            self.Dfs(v, num + 2)
    def WriteNode(self, node):
        if node.flag == 1:
            return self.WriteText(node)
        elif node.flag==2:
            return self.WriteUrl(node)
    def WirtLinesln(self,fp,lines):
        for s in lines:
            fp.write(s+'\n')
    def CreatFile(self, fileName):
        fp = open(fileName + r'.html','w',encoding='UTF-8')
        fp.write(r'<html>' + "\n")
        
        self.WirtLinesln(fp,self.WriteHead(self.title,"myCss.css"))
        fp.write(r'<body>'+'\n')
        for node in self.webSite:
            self.WirtLinesln(fp,self.WriteNode(node))
        fp.write(r'</body>'+'\n')
        fp.write(r'</html>'+'\n')
        fp.close()
if __name__ == "__main__":
    pass


        
