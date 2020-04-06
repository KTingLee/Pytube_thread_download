# 下載影片主程式

from models import file
from models import videoInfo
from models import threadJob
import os
import queue
import threading

# 提供要下載的影片"清單"，名稱以及連結。 樣板如下
# video_list.append({ "no":, "name":"", "link":""})
video_list = []
video_list.append({ "no":0, "name":"愛前端 Node.js 從入門到深入", "link":"https://www.youtube.com/playlist?list=PLE4XbebCbtzFwGFTalZIRkRgGTXoKfW-1"})
video_list.append({ "no":1, "name":"愛前端 Ajax 教學", "link":"https://www.youtube.com/playlist?list=PLE4XbebCbtzGIGHsm9ez4o9Qhn51N5HCz"})
video_list.append({ "no":2, "name":"愛前端 jQuery 教學", "link":"https://www.youtube.com/playlist?list=PLE4XbebCbtzG9FHaeMYRmLoiMZxuNS5fI"})
video_list.append({ "no":3, "name":"愛前端 React 教學", "link":"https://www.youtube.com/playlist?list=PLE4XbebCbtzGI4MQALa2yce1XQifXmB9n"})
video_list.append({ "no":4, "name":"愛前端 Cancas 教學", "link":"https://www.youtube.com/playlist?list=PLE4XbebCbtzHBTKXC0k7LQm6RGRFd-fwx"})
video_list.append({ "no":5, "name":"愛前端 JavaScript 教學", "link":"https://www.youtube.com/playlist?list=PLE4XbebCbtzHj1J_Ig_yZpFfMOqvIH0yR"})

# 基本參數
td_max = 10  # 線程數量
list_num = 5 # 清單號碼


# 建立影片資料夾與檔案輸出路徑
folder_name = video_list[list_num]["name"]
if folder_name not in os.listdir():
    os.mkdir(folder_name)
outputPath = os.getcwd() + '\\' + folder_name


# 獲得要下載的影片標題以及連結，並微調影片名稱
videoURL = video_list[list_num]["link"]
name_li, href_li = videoInfo.crawl_url_save(videoURL, save=False)
for k, name in enumerate(name_li, start=1):
    name = ('%02d %s' % (k, name))
    name_li[k-1] = name


# 多線程下載
threads=[]  # 用以存放線程的容器
q = queue.Queue()  # 建立Queue物件，用來存放線程結果

for i in range(0, len(name_li)):
    item = [name_li[i], href_li[i]]
    q.put(item)

for n in range(td_max):
    td = threading.Thread(target=threadJob.download_job, args=(outputPath, q))
    threads.append(td)
    td.start()

for td in threads:
    td.join()

print('下載完成！')
