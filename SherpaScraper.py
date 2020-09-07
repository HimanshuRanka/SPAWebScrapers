import requests
from bs4 import BeautifulSoup
import re
import xlwings as xw


@xw.func
def sherpa(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    results = []

    # This is to find the publisher info (ISSN and Publisher)
    articleInfo = soup.find_all('div', class_='summary_page_box')[0]
    colNine = articleInfo.find_all('div', class_='col span-9')

    for i in range(1, len(colNine), 2):
        results.append(colNine[i].get_text())
        
    # Ths is to find all the embargos
    embargos = soup.find_all('div', class_='ac')

    colNine = embargos[0].find_all('div', class_='col span-9')
    colThree = embargos[0].find_all('div', class_='col span-3')

    for div in colThree:
        stepFour = div.find_all('h4')
        for h4 in stepFour:
            text = re.sub('\t', '', (h4.get_text()))
            text = re.sub('\n', '', text)
            results.append(text)

    count = 2
    for div in colNine:
        colTwelve = div.find_all('div', class_='col span-12')
        if len(colTwelve) > 0:
            text = re.sub('\t', '', (colTwelve[0].get_text()))
            text = re.sub('\n', '', text)
            results[count] = results[count] + ": " + text
            count = count + 1

    return results
