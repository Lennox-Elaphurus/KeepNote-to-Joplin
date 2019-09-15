import os
import re
import html
print("ok")
filePath = ''   #Your path
fileList = os.listdir(filePath)
# print(fileList)
for fileName in fileList:
    realPath = filePath+'\\'+fileName
    if(re.search(".*\.html",fileName)!=None):
        htmlFile = open(realPath, "r", encoding="UTF-8")
        text = htmlFile.read()
        text=html.unescape(text)
        formattedData={}

        # getTime
        pattern = re.compile("</div>\\n+(?P<time>.*?)</div>+", re.DOTALL)
        contentMatch = re.search(pattern, text)
        formattedData = dict( formattedData, **contentMatch.groupdict())
        time=str(formattedData['time'])
        # getTitle
        pattern = re.compile(
            "<div class=\"title\">+(?P<title>.*?)</div>+", re.DOTALL)
        contentMatch = re.search(pattern, text)
        if contentMatch!=None:
            formattedData = dict(formattedData, **contentMatch.groupdict())
            title=str(formattedData['title'])
            # print(title)
        else:
            title=None

        # getContent
        pattern = re.compile(
            "<div class=\"content\">+(?P<content>.*?)</div>+", re.DOTALL)
        contentMatch = re.search(pattern, text)
        formattedData = dict( formattedData, **contentMatch.groupdict())
        content =str(formattedData['content'])
        # print(content)

        # getLabels
        pattern = re.compile(
            "<span class=\"label-name\">+(?P<labels>.*?)</span>+", re.DOTALL)
        contentMatch = re.findall(pattern, text)
        if contentMatch!=None:
            formattedData['labels'] = contentMatch
            labels = contentMatch
            # print(labels)
        else:
            labels=None
        print(formattedData)
        #finish extracting

        if title!=None:
            fileTitle=title.replace(" ","-")
            fileTitle= fileTitle.replace("\\", "-")
            fileTitle= fileTitle.replace("/", "-")
            fileTitle= fileTitle.replace(":", "-")
            fileTitle= fileTitle.replace("|", "-")
            fileTitle= fileTitle.replace("?", "")
            fileTitle= fileTitle.replace("\n", "-")
            mdFile=open(filePath+'\\md\\'+fileTitle+".md","w",encoding="utf-8")
            mdFile.write("# "+title+"\n")
            print(fileTitle+" transformed.")
        else:
            timeTitle=time.replace(" ","-")
            timeTitle = timeTitle.replace("\\", "-")
            timeTitle = timeTitle.replace("/", "-")
            timeTitle = timeTitle.replace(":", "-")
            timeTitle = timeTitle.replace("|", "-")
            timeTitle = timeTitle.replace("?", "")
            timeTitle = timeTitle.replace("\n", "-")
            mdFile = open(filePath + '\\md\\' + timeTitle + ".md", "w",encoding="utf-8")
            print(timeTitle+" transformed.")

        mdFile.write(time+"\n")

        if labels!=None:
            for label in labels:
                mdFile.write("#"+str(label)+" ")
            mdFile.write("\n")

        mdFile.write(content)

        htmlFile.close()
        mdFile.close()
