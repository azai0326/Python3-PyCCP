#-*-coding:utf-8-*-
import urllib, urllib.request, http.cookiejar, re

def parseTree(string):
    
    string = string.encode('cp950')

    URL = 'http://parser.iis.sinica.edu.tw/'

    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

    opener.addheaders = [
    ('User-Agent', 'Mozilla/5.0 Gecko/20100101 Firefox/29.0'),
    ('referer', 'http://parser.iis.sinica.edu.tw/'),
    ('Host', 'parser.iis.sinica.edu.tw')
    ]

    raw = urllib.request.urlopen(URL).read().decode('cp950')
    fid = re.search('name="id" value="(\d+)"', raw).group(1)

    postdata = dict()
    postdata['myTag'] = string
    postdata['id'] = fid

    postdata = urllib.parse.urlencode(postdata).encode('cp950')

    resURL = 'http://parser.iis.sinica.edu.tw/svr/webparser.asp'

    res = opener.open(resURL, postdata).read()
    res = res.decode('cp950')
    res = re.findall('<nobr>#\d+:(.*?)</nobr>', res)

    return res