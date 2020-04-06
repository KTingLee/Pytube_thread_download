# 處理檔案模組

import os
import re

# 檢查資料夾中的 mp4 檔
def mp4_in_folder(folderName="."):
    pattern = r".*\.mp4"
    reg_obj = re.compile(pattern)
    files_list = os.listdir(folderName)
    mp4_list = []

    for file_name in files_list:
        result = reg_obj.search(file_name)
        if result is not None:
            mp4_list.append(result[0])

    return mp4_list


if __name__ == "__main__":
    a = mp4_in_folder("../")
    print(a)

