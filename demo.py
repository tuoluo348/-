import requests,re



url='https://mooc1.chaoxing.com/work/selectWorkQuestionYiPiYue?courseId=227254957&workId=21782958&workAnswerId=51523740&api=1&knowledgeid=621879924&classId=61848098&oldWorkId=61b229d30442400c8dbcf1ec20a2c33d&jobid=work-61b229d30442400c8dbcf1ec20a2c33d&type=&isphone=false&submit=false&enc=15df5e74c0c2f067e828035b8d60aa26&cpi=171632656'

headers={
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Accept-Encoding": "gzip, deflate, br",
	"Accept-Language": "zh-CN,zh;q=0.9",
	"Cache-Control": "no-cache",
	"Connection": "keep-alive",
	"Cookie": "k8s=ce48016bd48a1133f3361f8c8850612b90f0af6f; route=1ab934bb3bbdaaef56ce3b0da45c52ed; source=\"\"; lv=2; fid=2322; _uid=62344227; uf=da0883eb5260151ed0e6b313eef9e6d6af18e3ade52b01cdacd6cb2d5e04b5a9ced162a04da0f153950650979b36c843c49d67c0c30ca5047c5a963e85f110991f5ef0b3e62067f5ce71fc6e59483dd3f69ef4b99e86e7c73bb92551d2c298de2adea3c5d6bae2c8; _d=1664472767285; UID=62344227; vc=7165AFB4103CCEDE03AFBC41AD25538F; vc2=3E6BEC3A858E7FAC6192C6660B62C7A7; vc3=WXn8%2FyD93sZPuWw4PhwRrNhNo3H%2B8jpUjNPNAVOMPEL3j%2F2S1Zlg2UGTuS19d0gjb4rx6jasKIEUwQqGDpBZvaBCpyKJbmJQ2VF21EBZwT2rhOqGq1rapS1eEKmZufszXTqkSoloP3rBIaOFvoZD%2F4qppfU7f2kwb%2F1KJSkjon8%3D33295492d6e661d1c188447e5f2b5c2b; xxtenc=a2086b78a5afc3684d540f46c5a6ea54; DSSTASH_LOG=C_43-UN_941-US_62344227-T_1664472767286; spaceFid=2322; spaceRoleId=\"\"; thirdRegist=0; jrose=8D8DC24C1FB9C97F1978DE9EB153EC53.mooc-1820963910-qw8ts",
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
	"Cookie": "k8s=87f03d0bf9bb9989b8e1fd887f48bae2967dbda7; route=6c7e83002ce2cc0e78a680d806381539; source=\"\"; lv=2; fid=2322; _uid=62344227; uf=da0883eb5260151ed0e6b313eef9e6d6af18e3ade52b01cdacd6cb2d5e04b5a9ced162a04da0f153950650979b36c843c49d67c0c30ca5047c5a963e85f110991f5ef0b3e62067f5ce71fc6e59483dd3f69ef4b99e86e7c73bb92551d2c298de2adea3c5d6bae2c8; _d=1664472767285; UID=62344227; vc=7165AFB4103CCEDE03AFBC41AD25538F; vc2=3E6BEC3A858E7FAC6192C6660B62C7A7; vc3=WXn8%2FyD93sZPuWw4PhwRrNhNo3H%2B8jpUjNPNAVOMPEL3j%2F2S1Zlg2UGTuS19d0gjb4rx6jasKIEUwQqGDpBZvaBCpyKJbmJQ2VF21EBZwT2rhOqGq1rapS1eEKmZufszXTqkSoloP3rBIaOFvoZD%2F4qppfU7f2kwb%2F1KJSkjon8%3D33295492d6e661d1c188447e5f2b5c2b; xxtenc=a2086b78a5afc3684d540f46c5a6ea54; DSSTASH_LOG=C_43-UN_941-US_62344227-T_1664472767286; spaceFid=2322; spaceRoleId=\"\"; jrose=A076D26846863AE99D6AD9201A7FA7B2.mooc-1820963910-kcvdz; thirdRegist=0",
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
