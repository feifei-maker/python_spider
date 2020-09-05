# @Time : 2020/9/3 13:54 
# @Author : fei_fei
# @File : news_requests_data.py
# @Software: PyCharm
import requests, bs4, re;


# 网页请求
def request_url(url):
    r = requests.get(url);
    r.encoding = r.apparent_encoding;  # 自动检测编码
    soup = bs4.BeautifulSoup(r.text, "html.parser");  # 设置解析器
    return soup;


# 获取单条新闻数据
def get_single_data(url):
    soup = request_url(url);
    # 获取p标签里面的内容
    news_p = soup.find(name="div", attrs={"class": "wy_contMain fontSt"}).find(name="p")
    news_line_data = "";
    # 由于新闻网中span的格式内容不一致，所以分情况处理
    if len(news_p) == 1:
        news_line_data = news_p.find(name="span").get_text().split("。")[1].strip();
    elif len(news_p) > 1:
        new_span = news_p.find_all(name="span");
        for i in range(0, len(new_span)):
            new_line_text = new_span[i].get_text().strip();
            # 获取以"截至"开头的文本信息
            if new_line_text.startswith("截至"):
                news_line_data = new_line_text;
    # 获取内容中特定的字段
    news_data_line_re = re.compile(r"\d+").findall(news_line_data);
    if len(news_data_line_re) > 3:
        for i in range(0, 3):
            news_data_line_re.pop(0);
    return news_data_line_re;


# 获取单个页面信息
def get_page_data(url):
    soup = request_url(url);
    # 获取页面上所有的新闻连接
    new_line = soup.find(name="div", attrs={"class": "contMain fontSt"}).find(name="ul").find_all(name="li");
    page_data = list();
    for i in range(0, len(new_line)):
        # 获取满足条件的每一页新闻标题
        title = new_line[i].find(name="a").get_text();
        title_need = title.startswith("四川省新型冠状病毒肺炎疫情最新情况") & title.endswith("发布）");
        if title_need:
            # 获取每个新闻时间
            news_data_time = re.compile(r"\d+").findall(str(title));
            # news_data_time =
            # 获取每个新闻的url
            single_news_url = new_line[i].find(name="a")["href"];
            really_news_url = "http://wsjkw.sc.gov.cn/" + single_news_url;
            # 获取每个新闻的数据
            news_data_people = get_single_data(really_news_url);
            # 将新闻的时间和数据放在一个集合中
            page_data.append(news_data_time + news_data_people);
        else:
            continue;
    return page_data;


# 获取所有页面的信息
def get_all_page_data():
    # 获取所有页面的url
    all_page_url = ["http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl.shtml", ];
    for i in range(2, 11):  # 11
        single_page_url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd01/ztwzlmgl_" + str(i) + ".shtml";
        all_page_url.append(single_page_url);
    # 获取所有页面的信息
    all_page_data = list();
    for j in range(0, len(all_page_url)):
        single_page_data = get_page_data(all_page_url[j]);
        all_page_data.append(single_page_data);
    return all_page_data;

