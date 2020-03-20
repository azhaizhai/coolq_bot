import requests
import os

async def picture_research_results(picture: str) -> str:
  sysres = os.system("wget "+picture+"-O /var/log/nginx/jay/pictures/img_search.jpg")
  if sysres != 0:
    return "获取图片资源出错，请找江叶debug"
  else:
    r = requests.post("https://trace.moe/api/search",params={'url': "https://jay.syuico.cn/pictures/img_search.jpg"})
    if r.status_code == 200:
      res = r.json()
      length = len(res['docs'])
      if length == 0:
        return "并无匹配结果"
      else:
        result = "已搜索次数:"+str(res["trial"])+"\n剩余搜索次数:"+str(res["limit"])+"\n重置搜索次数时间(s):"+str(res["limit_ttl"])
        i = 0
        for data in res['docs']:
          result += "\n********\n日文名:" +data["title_native"]+"\n中文名:"+data["title_chinese"]+"\n英文名:"+data["title_english"]+"\n时间:"+data["season"]+"\n开始集数:"+str(data["episode"])+"\n出现时间(秒):" + str(data["from"]) + " - " + str(data["to"])+ "\n可信度:" + str(round(data["similarity"] * 100, 4)) + "%\n是否里番:" + str(data["is_adult"])
          i += 1
          if i > 2:
            break
        result += "\n********\n共有" + str(length) + "个返回，输出" + str(i) + "个。(请注意，通常来讲相似度低于87%的结果并不可信，且番名有时并不准确)"
        return  result
    else:
      return "返回出错，原因如下(截图江叶debug):" + "r.text"