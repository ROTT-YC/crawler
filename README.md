# crawler 

一些爬蟲小模組

### Install

- [x] bs4
- [x] Pillow
- [x] requests
- [x] openai
- [x] pymysql

於 setting.py 中填入 Openai API Key，並在 main.py 中設定 host，微調資料庫設定後即可使用



### 功能:

get_webdata() - 爬取**文章標題、內文、圖片與原文連結**

currentime() - 依據當下時間分配文章統一發布在12/16/22點整(台北時間)

genereate_content() - 串接OpenAI API產生文章摘要

draw_icon() - 可對圖片進行水印(圖片/文字)備註

status_num - 標題或內文缺失異常檢查

increase_db() - 新增至資料庫
