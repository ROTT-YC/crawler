# pip install bs4, Pillow, requests, openai, pymysql
from bs4 import BeautifulSoup
from PIL import Image
import requests, os, openai, pymysql, package, time
import setting

# Globals
setting.env_str()
openai.api_key = setting.ai_key

# Database connect
db = pymysql.connect(host='xxx.xxx.x.xxx', port=3306, user='', passwd='', db='', charset='utf8mb4')
cur = db.cursor()

def get_res(link):
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    re = requests.get(link, headers=headers, timeout=65)
    re.encoding = 'UTF-8'
    time.sleep(3)
    return BeautifulSoup(re.text, features='html.parser')


if __name__ == "__main__":
    print(setting.today_date)
    