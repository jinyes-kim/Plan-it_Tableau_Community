from bs4 import BeautifulSoup
from selenium import webdriver

# 에이펙스 인벤 자유 게시판 크롤링


class Apex_inven:

    def __init__(self, page, filename):
        self.page = page
        self.filename = filename

    def apex_legned(self):
        page = self.page
        filename = self.filename

        f = open(filename, 'w', encoding='utf-8')
        driver = webdriver.Chrome("C:/Study_Python/Chromedriver")

        Apex_dict = {}
        word_list = []

        for a in range(1, page):                # 게시판 페이지 1 ~ X 페이지
            for b in range(2, 52):              # 게시판 페이지당 글 50개 존재
                if a == 1 and b < 9:            # 공지글 1페이지 8개 존재
                    continue

                driver.get('http://www.inven.co.kr/board/apexlegends/5404?category=%EC%9E%A1%EB%8B%B4&sort=PID&p=' +str(a))
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')

                posts = soup.select("#powerbbsBody > table > tbody > tr > td > div > table > tbody > tr > td > table > tbody > tr:nth-of-type(3) > td > form > table > tbody > tr:nth-of-type(" +str(b) + ") > td.bbsSubject > a")

                for c in posts:
                    c = c.text.strip()
                    c = c[6:]

                f.write(str(c) + '\n')
        f.close()

firstC = Apex_inven(2, "Testcode1.txt")

firstC.apex_legned()