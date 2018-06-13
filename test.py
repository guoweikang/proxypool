from proxypool.utils import get_page
from pyquery import PyQuery as pq
import re
from time import sleep

def test():
    for page in range(1, 4):
        # 国内高匿代理
        sleep(2)
        start_url = 'https://www.kuaidaili.com/free/inha/{}/'.format(page)
        html = get_page(start_url)
        ip_adress = re.compile('<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>')
        if html == None:
            continue
        re_ip_adress = ip_adress.findall(html)

        for adress, port in re_ip_adress:
            result = adress + ':' + port
            print(result)
test()