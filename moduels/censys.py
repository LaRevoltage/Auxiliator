import requests
import re
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
def SearchByIp(target):
    infos=[]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Cache-Control': 'max-age=0',
        'TE': 'trailers',
    }
    i=0
    response = requests.get(f'''https://search.censys.io/hosts/{target}''', headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find(id="content")
    ports = results.find_all("div", class_="protocol-details")
    for port in ports:
        soup = BeautifulSoup(str(port), features="lxml")
        results = soup.h2
        results = str(results.text)
        results = results.replace(" ", "")
        results = results.split('\n')
        infos.append("Protocol:"+" "+results[1].split("/")[1]+" "+"is on port:"+" "+results[1].split("/")[0])
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find(id="content")
    try:
        dl_data = results.find('dt', string='OS').find_next_siblings('dd')
        infos.append("OS:"+dl_data[0].string.replace("\n", ""))
    except:
        infos.append("OS Can't be specified!")
    try:
        dl_data = results.find('dt', string='Network').find_next_siblings('dd')
        infos.append("Network:"+dl_data[0].text.replace(" ", "").replace("\n", ""))
    except:
        infos.append("Network Can't be specified!")
    try:
        dl_data = results.find('dt', string='Routing').find_next_siblings('dd')
        infos.append("Routing:"+dl_data[0].text.replace(" ", "").replace("\n", ""))
    except:
        infos.append("Routing Can't be specified!")
    ports=results.find_all("div", class_="protocol-details")
    for portservice in ports:
        portlist=(portservice.find_next_siblings("div", class_="host-section"))
        port=re.sub('\n\n', '\n', portlist[0].text)
        port=re.sub(' +', ' ', port)
        port=port.split("\n")
        infos.append(portservice.text.split("\n")[2].replace(" ", "")+":")
        for el in port:
            if el!='' and el!=' ' and "\r" not in el and "\n" not in el:
                if(el.startswith(" ")==True):
                    infos.append(el.replace(" ", "-", 1))
                if(el.startswith(" ")==False):
                    infos.append(el+":")
            elif(el!=' '):
                infos.append(el)
    return(infos)
def SearchByDomain(target):
    addr=[]
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Accept': '*/*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'X-Requested-With': 'XMLHttpRequest',
        'Connection': 'keep-alive',
        'Referer': 'https://search.censys.io/search?resource=hosts&q=artscp.com',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Cache-Control': 'max-age=0',
    }
    params = (
        ('resource', 'hosts'),
        ('q', f''' services.tls.certificates.leaf_data.names: {target}''')
    )
    response = requests.get('https://search.censys.io/_search', headers=headers, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    results=soup.text.replace("\n", "")
    results=re.sub(' +', ' ', results)
    results=results.split(" ")
    for result in results:
        preresult=str(result).replace("\n", "")
        preresult=preresult.replace(" ", "")
        resultis=(preresult.split("\n"))
        if(any(c.isalpha() for c in resultis[0])==False and ")" not in resultis[0] and resultis[0]!=""):
            addr.append(resultis[0])
    return(addr)
if __name__ == "__main__":
    SearchByDomain(target)
    SearchByIp(target)