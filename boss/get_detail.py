from selenium import webdriver
import time
from lxml import etree
import random


class parse(object):
    def __init__(self):
        self.drive = webdriver.Chrome(executable_path=r"C:\Users\WDXCQ\Desktop\Learning\spiderTool/chromedriver.exe")
        self.start_url = "https://www.zhipin.com/c101210100/?query=python&page="
        self.items = []
        self.second = random.randint(1, 4)

    def run(self, i):
        url = self.start_url + str(i)
        self.drive.get(url)
        response = self.drive.page_source
        self.parse_detail(response)

    def parse_detail(self, response):
        i = 0
        html = etree.HTML(response)
        lis = html.xpath('//div[@class="job-list"]/ul/li')
        for li in lis:
            try:
                item = {}
                position_name = html.xpath('.//div[@class="job-title"]/text()')[i]
                position_salary = html.xpath('.//span[@class="red"]/text()')[i]
                position_company = html.xpath('.//div[@class="company-text"]/h3[@class="name"]/a/text()')[i]
                position_place = html.xpath('.//div[@class="info-primary"]/p/text()')[3*i]
                item["position_name"] = position_name
                item["position_salary"] = position_salary
                item["position_conpany"] = position_company
                item["position_place"] = position_place
                self.items.append(item)
                i += 1
            except:
                print("error")
        time.sleep(self.second)

    def write_data(self):
        fp = open("./doc/position.txt", "w", encoding="utf-8")
        for data in self.items:
            fp.write(str(data) + "\n")


if __name__ == '__main__':
    p = parse()
    for i in range(1, 11):
        p.run(i)
    p.drive.quit()
    p.write_data()
