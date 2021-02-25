# from selenium import webdriver
import requests
from bs4 import BeautifulSoup
# import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 강남/강북의 각 지역을 숫자로 표시한 리스트
seoul_list = [218]  # , 201, 202, 203, 217, 204, 205, 206,
# 207, 209, 210, 211, 212, 213, 214, 215, 216, 208, 'a', 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 218,
# 223, 219, 217, 211, 216, 222, 224, 220, 212, 213, 214, 215, 221]

# 강남/강북 지역 url
seoul_url = ['https://www.menupan.com/restaurant/bestrest/bestrest.asp?pt=wk&areacode=ss',
             'https://www.menupan.com/restaurant/bestrest/bestrest.asp?pt=wk&areacode=sn']
num = 0

data = {'res_name': [], 'res_type': [], 'res_address': [], 'hompage': [],
        'score': [], 'feature': [], 'parking': [], 'intro': [], 'review': []}

# 지역별 음식점 리스트 출력
for gu in seoul_list:
    if type(gu) == int:
        data = requests.get(seoul_url[num] + str(gu), headers=headers)
    else:
        num += 1

    soup = BeautifulSoup(data.text, 'html.parser')

    # body > div > div.container > div.bestRest > div.ranking > div.rankingList > ul > li:nth-child(1) > p.listName > span.restName > a
    restaurant = soup.select(
        'body > div > div.container > div.bestRest > div.ranking > div.rankingList > ul > li')

    # print(restaurant)

    # 음식점 i의 상세 페이지 진입
    for i in restaurant:

        res_name = i.select_one('p.listName > span.restName > a')

        # 상세 페이지 url 추출
        detail_page = requests.get(
            'http://menupan.com' + res_name['href'], headers=headers)
        soup_2 = BeautifulSoup(detail_page.text, 'html.parser')
        ajax_code = res_name['href'][-7:]
        reviews = soup_2.select_one(
            'body > center > div.WrapMain > div.mainArea02 > div.tabReview > div.reviewWrap > div.memberReview')
# body > center > div.WrapMain > div.mainArea02 > div.tabReview > div.reviewWrap > div.memberReview

        print(ajax_code)
        # details = soup_2.select(
        #     'body > center > div.WrapMain > div.mainArea01')

        # for detail in details:
        #     name = detail.select_one('div.areaBasic > dl.restName > dd').text
        #     type = detail.select_one('div.areaBasic > dl.restType > dd')
        #     address = detail.select_one('div.areaBasic > dl.restAdd > dd')
        #     homepage = detail.select_one(
        #         'div.areaBasic > dl.restHome > dd > a')
        #     res_score = detail.select_one(
        #         'div.areaBasic > dl.restGrade > dd.rate > p.score > span.total')
        #     parking = detail.select_one(
        #         'div.infoTable > ul.tableLR > li:nth-child(4) > dl:nth-child(1) > dd')
        #     info = detail.select_one(
        #         'div.tabInfo > div.infoTable > ul.tableBottom > li > dl > dd > div')
        #     amenity = detail.select_one(
        #         'div.tabInfo > div.infoTable > ul.tableLR > li:nth-child(4) > dl:nth-child(2) > dd')
        #     # print(homepage.text)
        #     if homepage != None:
        #         print(name.split('[')[0], type.text, address.text, homepage.text, res_score.text, parking.text.strip(), info.text.strip(), amenity.text
        #               )
        #     else:
        #         print(name.split('[')[0], type.text, address.text, 'None', res_score.text, parking.text.strip(), info.text.strip(), amenity.text
        #   )
# score.text, parking.text, info.text
# body > center > div.WrapMain > div.mainArea02 > div.tabReview
# body > center > div.WrapMain > div.mainArea01 > div.areaBasic > dl.restHome > dd > a
# body > center > div.WrapMain > div.mainArea01 > div.areaBasic > dl.restName > dd
# body > center > div.WrapMain > div.mainArea01 > div.areaBasic > dl.restType > dd
# body > center > div.WrapMain > div.mainArea01 > div.areaBasic > dl.restAdd > dd.add1 > a
# body > center > div.WrapMain > div.mainArea01 > div.areaBasic > dl.restHome > dd > a
# body > center > div.WrapMain > div.mainArea01 > div.areaBasic > dl.restGrade > dd.rate > p.score > span.total
# body > center > div.WrapMain > div.mainArea01 > div.areaBasic > dl.restTheme > dd > a:nth-child(1)
# body > center > div.WrapMain > div.mainArea01 > div.areaBasic > dl.restTheme > dd > a:nth-child(2)
# body > center > div.WrapMain > div.mainArea01 > div.tabInfo > div.infoTable > ul.tableLR > li:nth-child(4) > dl:nth-child(1) > dd
# body > center > div.WrapMain > div.mainArea01 > div.tabInfo > div.infoTable > ul.tableLR > li:nth-child(4) > dl:nth-child(1) > dd
# body > center > div.WrapMain > div.mainArea01 > div.tabInfo > div.infoTable > ul.tableBottom > li > dl > dd > div
# body > center > div.WrapMain > div.mainArea01 > div.tabInfo > div.infoTable > ul.tableLR > li:nth-child(4) > dl:nth-child(2) > dd
# ajax_comment > ul > li:nth-child(1) > dl > dd.content
# body > center > div.WrapMain > div.mainArea02 > div.tabReview > h3 > img
# ajax_comment > ul > li:nth-child(1) > dl > dd.rate > p.score

# https://www.menupan.com/restaurant/onepage_201401/include/ajax_comment.asp?ac=R106699&pg=2&pz=5&ord=1
# https://www.menupan.com/restaurant/onepage_201401/include/ajax_comment.asp?ac=R106699&pg=1&pz=5&ord=1

# https://www.menupan.com/restaurant/onepage_201401/include/ajax_comment.asp?ac=D102366&pg=1&pz=5&ord=1
# https://www.menupan.com/restaurant/onepage_201401/include/ajax_comment.asp?ac=D102366&pg=2&pz=5&ord=1
# https://www.menupan.com/restaurant/onepage_201401/include/ajax_comment.asp?ac=D102366&pg=3&pz=5&ord=1
# https://www.menupan.com/restaurant/onepage_201401/include/ajax_comment.asp?ac=D102366&pg=4&pz=5&ord=1
