# 獲取影片清單資訊模組

import requests
from bs4 import BeautifulSoup

# 煮湯，pt_res 表示是否將 html 結果打印
def make_soup(url, pt_res=False):
    rs = requests.get(url)
    soup = BeautifulSoup(rs.text, 'lxml')
    if pt_res:
        print(soup.prettify())
    return soup


# 獲取所有影片標題以及連結
def get_video_info(soup):
    video_info = soup.find_all(class_="pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link")
    video_name_list = []
    video_href_list = []
    base_url = 'https://www.youtube.com'
    for k, item in enumerate(video_info):
        # 提取影片名稱與連結
        name = item.text.strip()
        href = item['href']
        video_name_list.append(name)
        video_href_list.append(base_url + href)
        print('檢驗：', name, href) if k==1 else None
    return video_name_list, video_href_list


# 儲存資料，title=True 表示儲存影片標題
def save_data(video_info_list, title=True):
    if title:
        file_name = 'video_name_list' + '.txt'
    else:
        file_name = 'video_href_list' + '.txt'

    with open(file=file_name, mode='w', encoding='utf-8') as file:
        for k, content in enumerate(video_info_list, start=1):
            head_no = ('%02d' % k) if title else ''
            if k == len(video_info_list):
                file.write(head_no + content)
            else:
                file.write(head_no + content + '\n')


# 整合程式，爬取影片清單並儲存
def crawl_url_save(url, save=True):
    soup = make_soup(url)
    video_name_list, video_href_list = get_video_info(soup)
    if save:
        save_data(video_name_list)
        save_data(video_href_list, title=False)
        return video_name_list, video_href_list
    else:
        return video_name_list, video_href_list


if __name__ == "__main__":
    url = "https://www.youtube.com/playlist?list=PLE4XbebCbtzGIGHsm9ez4o9Qhn51N5HCz"
    crawl_url_save(url, True)
    