import requests
import json
from bs4 import BeautifulSoup

header = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
}


address=[]
top = []
dict = {}
tops=[]

def topAccounts():

    apitoken="NGWWN6MTCVMFGY2Y871WQHURNQS6X465ZM"

    for i in range(1,5):
        r = requests.get("https://etherscan.io/accounts/{i}", headers=header)
        soup = BeautifulSoup(r.content, "lxml")
        for el in soup.find("tbody").find_all("a"):
            address.append(el.get_text())

    for i in range(0,len(address)-90):
        link = "https://api.etherscan.io/api?module=account&action=balance&address=" + address[i] + "&tag=latest&apikey="+apitoken
        r = requests.get(link, headers=header)
        soup = BeautifulSoup(r.content, "lxml")
        # top.append(soup.find("body").get_text())
        # print(i)
        dict[i] = json.loads(soup.find("body").get_text())

    

    for i in range(0,len(address)-90):
        tops.append({
            "category":address[i],
            "num_of_products":dict[i]['result']
        })

    # fixedTop = []
    # for i in range(0, len(dict)):
    #     fixedTop.append(["Rank - " + str(i + 1) +"、Address - " + address[i] + "、 Balance - ", dict[i]["result"] + " Ether"])
    # print(fixedTop)
    # print(dict)

    # print(tops)
    return tops