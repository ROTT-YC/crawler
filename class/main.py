# pip install bs4, Pillow, requests, openai, pymysql
from bs4 import BeautifulSoup
from PIL import Image
import requests, os, openai, pymysql, package, time, threading, concurrent.futures
import setting

# Globals
setting.env_str()
openai.api_key = setting.ai_key

# Database connect
db = pymysql.connect(host='xxx.xxx.x.xxx', port=3306, user='', passwd='', db='', charset='utf8mb4')
cur = db.cursor()

# Remove duplicates
db_urls = []
cur.execute("SELECT DISTINCT origin_url FROM datasheet")
for i in cur:
    i = str(i).strip("(),'")
    db_urls.append(i)

def get_res(link):
    headers = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"}
    re = requests.get(link, headers=headers, timeout=65)
    re.encoding = 'UTF-8'
    time.sleep(3)
    return BeautifulSoup(re.text, features='html.parser')

def get_webdata(link):
    data = get_res(link)
    link_data = list(set([i["href"] for i in data.select("h2 a")]))
    dict_data = []
    for ori_link in link_data:
        if ori_link not in db_urls:
            arti_data = get_res(ori_link)
            if arti_data.find('h1') is not None:
                title = arti_data.find('h1').text.strip()
                content = arti_data.find("article",{"class":""}).select('div p')
                # Cull the element you dont want
                filtered_content = [p.text.strip() for p in content if 'breadcrumbs' not in p.get('class', [])]
                cont = "\n ".join(filtered_content)
                if arti_data.select('picture img'):
                    img_link = arti_data.select('picture img')[0].get('src')
                    dict_data.append([title, cont, img_link, ori_link])
                    # Data will equal or less than 5
                    if len(dict_data) == 5 : return dict_data
            else : continue
    return dict_data

def increase_db(dict_data, id_num, cate_num, wm_num):
    sql = "INSERT INTO datasheet(title, content, image_path, status, post_time, pf_id, pf_category, watermark, origin_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    
    for l in (range(len(dict_data))):
        dict_title, dict_content, dict_img, dict_link = dict_data[l]
        img_title = dict_title.translate(str.maketrans("", "", """\/:*?!,.'"<>|""")).strip()
        img_path = str("/root/news" + img_title + ".jpg")
        package.load_pic(dict_img, img_path) # Download pic
        package.draw_icon(img_path, wm_num) # Watermark

        article_con = package.genereate_content(dict_title, dict_content, "gpt-4-1106-preview")
        title = article_con[0].replace(",", "").replace("/", "").strip()
        public_time = package.currentime()

        if dict_title and dict_content and dict_img:
            status_num = "Completed"
        else: status_num = "Undone"

        try:
            cur.executemany(sql,[[title, article_con[1], img_path, status_num, public_time, id_num, cate_num, wm_num, dict_link]])
            db.commit()
            print("Database increase sucessful!")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    
    print(setting.today_date)

    start_time = time.time()
    link = ""
    increase_db(get_webdata(link), "1", "1", "1")
    print("--- %s seconds ---" % (time.time() - start_time))