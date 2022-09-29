import requests,re

cookie=''

url='https://mooc1.chaoxing.com/work/selectWorkQuestionYiPiYue?courseId=227254957&workId=21782958&workAnswerId=51523740&api=1&knowledgeid=621879924&classId=61848098&oldWorkId=61b229d30442400c8dbcf1ec20a2c33d&jobid=work-61b229d30442400c8dbcf1ec20a2c33d&type=&isphone=false&submit=false&enc=15df5e74c0c2f067e828035b8d60aa26&cpi=171632656'

headers={
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Cookie": cookie,
	"Host": "mooc1.chaoxing.com",
	"Pragma": "no-cache",
	"Referer": "https://mooc1.chaoxing.com/ananas/modules/work/index.html?v=2022-0714-1515&castscreen=0",
	"sec-ch-ua": "\"Chromium\";v=\"21\", \" Not;A Brand\";v=\"99\"",
	"sec-ch-ua-mobile": "?0",
	"sec-ch-ua-platform": "\"Windows\"",
	"Sec-Fetch-Dest": "iframe",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-Site": "same-origin",
	"Upgrade-Insecure-Requests": "1",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}
res=requests.get(url=url,headers=headers)

fndtm=re.compile(r'<div class="clearfix" style="line-height: 35px; font-size: 14px;padding-right:15px;width: calc(.*?)</div>',re.S)
tm=re.findall(fndtm,res.text)

l=[]
for i in tm:
    l.append(i.replace('(100% - 60px);box-sizing: border-box;">\n\t\t\t\t\t\t\t【单选题】','').replace(':(&nbsp; &nbsp; &nbsp; )。\t\t\t\t\t\t\t','').replace('&nbsp;','').replace('(100% - 60px);box-sizing: border-box;">\n\t\t\t\t\t\t\t【多选题】','').replace('(100% - 60px);box-sizing: border-box;">\n\t\t\t\t\t\t\t【判断题】','').replace('\n','').replace('\t',''))

url='https://mooc1-2.chaoxing.com/bbscircle/grouptopic/publish'
headers={
	"Accept": "*/*",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Content-Length": "327",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"Cookie": cookie,
	"Host": "mooc1-2.chaoxing.com",
	"Origin": "https://mooc1-2.chaoxing.com",
	"Pragma": "no-cache",
	"Referer": "https://mooc1-2.chaoxing.com/bbscircle/grouptopic?courseId=227254957&hideHead=false&clazzid=61848098&ut=s&showChooseClazzId=61848098&enc=b8e7f11a153bd49b2946e3d51188b007&chapterId=0&cpi=171632656",
        "sec-ch-ua": "\"Chromium\";v=\"21\", \" Not;A Brand\";v=\"99\"",
	"sec-ch-ua-mobile": "?0",
	"sec-ch-ua-platform": "\"Windows\"",
	"Sec-Fetch-Dest": "empty",
	"Sec-Fetch-Mode": "cors",
	"Sec-Fetch-Site": "same-origin",
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
	"X-Requested-With": "XMLHttpRequest"
}
for tt in l:
    data={
            "title": tt,
            "clazzid": "61848098",
            "courseId": "227254957",
            "ut": "s",
            "folderId": "",
            "folderName": "",
            "attachmentFile": "",
            "chooseClazzId": "61848098",
            "cpi": "171632656",
            "hideHead": "false",
            "openc": "",
            "content": "",
            "file": ""
    }
    res=requests.post(url=url,headers=headers,data=data)
    print(res.text)
