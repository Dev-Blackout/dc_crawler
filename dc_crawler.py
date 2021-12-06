import requests
from bs4 import BeautifulSoup
import operator, time, re, os

def request(url):
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'utf-8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'gall.dcinside.com',
        'Upgrade-Insecure-Requests': '10',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.76 Whale/3.12.129.34 Safari/537.36'
    }
    try:
        url_get = requests.get(url, headers=header)
    except:
        url_get = requests.get(url, headers=header)
    return url_get

def gall_check(gall_type: str, gall: str):
    if gall_type == "1":
        recept = request("http://gall.dcinside.com/board/lists/?id=%s" %gall)
    if gall_type == "2":
        recept = request("http://gall.dcinside.com/mgallery/board/lists/?id=%s" %gall)
    if gall_type == "3":
        recept = request("http://gall.dcinside.com/mini/board/lists/?id=%s" %gall)
    soup = BeautifulSoup(recept.text, "html.parser")
    meta_data = soup.find_all("meta", {"name": "title"})
    comp = re.findall("\"(.*갤러리)", str(meta_data))
    if comp == []:
        return (gall_type, "no_gallery")
    else:
        gall_name = comp[0]
        tuple = (gall_type, gall_name)
        return tuple

def main():
    gall = input("Gallery ID : ")
    print("Types = (정식:1 마이너:2 미니:3)")
    gall_type = input("Gallery Type : ")
    (gall_type, gall_name) = gall_check(gall_type, gall)

    if gall_name != "no_gallery":
        print("Gallery Name = %s" %gall_name)
    else:
        print("Wonrg Gallery")
        main()
    init_page = int(input("First Page : "))
    final_page = int(input("Last Page : "))
    nick_dic = dict()

    for page in range(init_page, final_page + 1):
        print("\rProcessing Page = {}/{}".format(page, final_page), end="")
        if gall_type == "1":
            recept = request("http://gall.dcinside.com/board/lists/?id=%s&page=%d" %(gall, page))
        if gall_type == "2":
            recept = request("http://gall.dcinside.com/mgallery/board/lists/?id=%s&page=%d" %(gall, page))
        if gall_type == "3":
            recept = request("http://gall.dcinside.com/mini/board/lists/?id=%s&page=%d" %(gall, page))
        soup = BeautifulSoup(recept.text, "html.parser")
        nick_list = soup.find_all('td', {'class': "gall_writer ub-writer"})

        for nicks in nick_list:
            try:
                nick = nicks.attrs['data-nick']
                uid = nicks.attrs['data-uid']
                ip = nicks.attrs['data-ip']
            except:
                nick = "운영자"
            if nick == "운영자":
                continue
            nick_str = nick + "(" + uid + ip + ")"
            if nick_str in nick_dic:
                nick_dic[nick_str] += 1
            else:
                nick_dic[nick_str] = 1
    nick_list = dict_sorter(nick_dic)
    file_writer(gall_name, nick_list)
    main()

def dict_sorter(nick_dic):
    sorted_dic = sorted(nick_dic.items(), key=operator.itemgetter(1))
    sorted_dic.reverse()
    return sorted_dic

def file_writer(gall_name, nick_list):
    timestr = time.strftime("%Y_%m_%d-%H_%M")
    file_path = os.getcwd()
    file_name = "%s-%s.txt" %(gall_name, timestr)
    print('')
    print("File Path = %s" %file_path)
    print("Saving File = %s" %file_name)
    print("End of Process \n")
    f = open(file_name, 'w', encoding="utf-8")
    total = 0
    for i in range(len(nick_list)):
        total += nick_list[i][1]
    f.write("총 글수: %d\n" %total)
    f.write("랭킹\t닉네임\t\t글\t지분(%)\n")
    error = 0
    for i in range(len(nick_list)):
        if nick_list[i][1] == 0:
            continue
        string = "%d\t%s\t%d\t%.2f\n" %((i+1), nick_list[i][0], nick_list[i][1], (nick_list[i][1] / total * 100))
        try:
            f.write(string)
        except:
            error += nick_list[i][1]
            f.write(str(error))
    f.close()

if __name__ == "__main__":
    main()