import os
from ftplib import error_perm
from ftplib import error_temp, error_reply
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

def find_articles(category,date):
    request = requests.head('https://www.thenews.com.pk/latest/category/'+ category +'/'+ date +'')
    # print(request.status_code)
    if request.status_code == 307:
        return
    all_data = []
    r = requests.get('https://www.thenews.com.pk/latest/category/'+ category +'/'+ date +'')
    soup = BeautifulSoup(r.text, "lxml")
    main_content = soup.findAll("div", {"class": "siteContent"})
    urls = []
    for div in main_content:
        links = div.findAll('a')
        for a in links:
            urls.append(a['href'])
    for i in urls:

        r = requests.get(str(i))
        soup = BeautifulSoup(r.text, "lxml")

        heading = str(i)
        heading = heading.strip('https://www.thenews.com.pk/latest/')
        heading = heading.replace('-',' ')
        heading = heading.split(' ', 1)[1]
        heading = heading.lstrip()
        # print(heading)

        main_content = soup.findAll("div", {"class": "story-detail"})
        # print(main_content)
        # print(main_content)
        content = ""
        for div in main_content:
            # links = re.sub("<p>|</p>","",main_content[i])
            links = div.findAll('p')
            if links:
                for a in links:
                    a = str(a).strip('<p>')
                    a = str(a).strip('/>')
                    a = str(a).strip('<')
                    a = str(a).strip('<br>')
                    content = content + a
            else:
                content = soup.find("div", {"class": "story-detail"}).text
                content = str(content)
                # content = content.strip('<p>')
                # content = content.strip('/>')
                # content = content.strip('<')

                content = content.split("Advertisement", 1)[0]
                content = content.strip('<br>')
        # print(content)
        content = content.lstrip()
        # if ':' in content:
        #     k = content.split(':')
        #     location = k[0].strip('strong')
        #     location = location.strip('<')
        #     location = location.strip('>')
        #     content = k[1].lstrip()
        # else:
        #     k = content.split(" ", 1)
        #     location = k[0].strip('strong')
        #     location = location.strip('<')
        #     location = location.strip('>')
        #     content = k[1].lstrip()
        #
        all_data.append({'NewsType': category, 'Date': date, 'Article':content, 'Heading':heading})

    all_data = pd.DataFrame(all_data)
    if not os.path.isfile('Articles1.csv'):
        all_data.to_csv('Articles1.csv', header='column_names',index=False)
    else:  # else it exists so append without writing the header
        all_data.to_csv('Articles1.csv', mode='a', header=False,index=False)
    # all_data.to_csv("Articles.csv")
    # print(all_data)


def all_2015_sports_data():
    for i in range(1,13):
        if i%2!=0:
            for j in range(1,32):
                print(i,j)
                find_articles("sports", "2015-" + str(i) + "-" + str(j) + "")
        elif i==2:
            for j in range(1,29):
                print(i, j)
                find_articles("sports", "2015-" + str(i) + "-" + str(j) + "")
        elif i%2==0:
            for j in range(1,31):
                print(i, j)
                find_articles("sports", "2015-" + str(i) + "-" + str(j) + "")

def all_2016_sports_data():
    for i in range(1,13):
        if i%2!=0:
            for j in range(1,32):
                print(i,j)
                find_articles("sports", "2016-" + str(i) + "-" + str(j) + "")
        elif i==2:
            for j in range(1,30):
                print(i, j)
                find_articles("sports", "2016-" + str(i) + "-" + str(j) + "")
        elif i%2==0:
            for j in range(1,31):
                print(i, j)
                find_articles("sports", "2016-" + str(i) + "-" + str(j) + "")

def all_2017_sports_data():

    for i in range(1,4):

        if i==3:
            for j in range(1,27):
                print(i,j)
                find_articles("sports", "2017-" + str(i) + "-" + str(j) + "")


        if i%2!=0:
            for j in range(1,32):
                print(i,j)
                find_articles("sports", "2017-" + str(i) + "-" + str(j) + "")
        elif i==2:
            for j in range(1,29):
                print(i, j)
                find_articles("sports", "2017-" + str(i) + "-" + str(j) + "")
        elif i%2==0:
            for j in range(1,31):
                print(i, j)
                find_articles("sports", "2017-" + str(i) + "-" + str(j) + "")

def all_2015_business_data():
    for i in range(1, 13):
        if i % 2 != 0:
            for j in range(1, 32):
                print(i, j)
                find_articles("business", "2015-" + str(i) + "-" + str(j) + "")
        elif i == 2:
            for j in range(1, 29):
                print(i, j)
                find_articles("business", "2015-" + str(i) + "-" + str(j) + "")
        elif i % 2 == 0:
            for j in range(1, 31):
                print(i, j)
                find_articles("business", "2015-" + str(i) + "-" + str(j) + "")

def all_2016_business_data():
    for i in range(10, 13):
        if i % 2 != 0:
            for j in range(1, 32):
                print(i, j)
                find_articles("business", "2016-" + str(i) + "-" + str(j) + "")
        elif i == 2:
            for j in range(1, 30):
                print(i, j)
                find_articles("business", "2016-" + str(i) + "-" + str(j) + "")
        elif i % 2 == 0:
            for j in range(1, 31):
                print(i, j)
                find_articles("business", "2016-" + str(i) + "-" + str(j) + "")

def all_2017_business_data():

    for i in range(1, 4):

        if i == 3:
            for j in range(1, 27):
                print(i, j)
                find_articles("business", "2017-" + str(i) + "-" + str(j) + "")

        if i % 2 != 0:
            for j in range(1, 32):
                print(i, j)
                find_articles("business", "2017-" + str(i) + "-" + str(j) + "")
        elif i == 2:
            for j in range(1, 29):
                print(i, j)
                find_articles("business", "2017-" + str(i) + "-" + str(j) + "")
        elif i % 2 == 0:
            for j in range(1, 31):
                print(i, j)
                find_articles("business", "2017-" + str(i) + "-" + str(j) + "")


#
# all_2015_business_data()
all_2016_business_data()
all_2017_business_data()
# all_2015_sports_data()
