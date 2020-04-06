# 多線程下載任務

import threading
import os
import shutil
from pytube import YouTube

# 下載任務，傳入影片輸出路徑，以及隊列物件(物件中包含影片名稱與影片連結)
def download_job(outputPath, queueObj):
    while queueObj.qsize() != 0:
        videoInfo = queueObj.get()
        print('剩餘', queueObj.qsize(), '個任務...')
        videoName = videoInfo[0]
        videoLink = videoInfo[1]
        yt = YouTube(videoLink)

        # 檢查影片是否存在輸出路徑，若有就結束
        if video_exsit(videoName, outputPath):
            print(videoName + '已存在～')
        else:
            # 篩選影片品質
            yt = yt.streams.filter(file_extension='mp4', progressive = True).order_by('resolution')[-1]
            print(videoName + '已經開始下載...')
            yt.download(filename=videoName)
            print(videoName + '下載完成！將影片移至目標資料夾...')
            move_video(videoName, outputPath)
            print(videoName + '移動完成！')
    print('隊列物件沒有東西了！')



# 檢查影片是否存在資料夾
def video_exsit(videoName, outputPath):
    return os.path.isfile(outputPath + "\\" + videoName + ".mp4")


# 移動影片
def move_video(videoName, outputPath):
    shutil.move(videoName + ".mp4", outputPath)



if __name__ == "__main__":
    na = "01 爱前端从入门到深入Node js开发实战 01 nodejs简 开门注"
    url = "https://www.youtube.com/watch?v=sq3FAlPQEyM&list=PLE4XbebCbtzFwGFTalZIRkRgGTXoKfW-1&index=2&t=0s"
    path = "F:\\JavaScript\\downloadVideo\\"
    download_job(na, url, path)
    video_exsit(na, path)






