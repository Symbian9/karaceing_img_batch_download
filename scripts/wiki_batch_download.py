#! /usr/bin/env python
try:
    # For Python 3.0 and later
    from urllib.request import Request
    from urllib.request import urlopen
    from urllib.error import HTTPError

    def raw_input(x):
        return input(x)

except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import HTTPError
try:
    import base64
    from bs4 import BeautifulSoup
    import os.path
    from sys import version_info
    import getpass
    import errno
except ImportError as err:
    print("Couldn't import all necessary modules!")
    print(err)
    exit()

url_list = []
userinput = raw_input("Please enter wiki-path: \n"
                      "e.g.: infovault:bilder:fsuk_2015\n")
site_url = "https://wiki.ka-raceing.de/" + userinput
print("Querying site: {}".format(site_url))

if False:
    username = "YOUR USERNAME"
    password = "YOUR PASSWORD"
else:
    username = raw_input("Please enter username: \n")
    password = getpass.getpass("Please enter password: \n")

request = Request(site_url)
base64string = base64.encodestring(('%s:%s' % (username, password)).encode()).decode().replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)

urlpath = urlopen(request)
string = urlpath.read().decode('utf-8')
bs = BeautifulSoup(string, 'lxml')

for row in bs.findAll('img'):
    if ".jpg" in str(row):
        src = row.get('src')
        idx = src.index('.jpg?')
        src = src[0:idx] + '.jpg'
        url_list.append('https://wiki.ka-raceing.de'+src)
if len(url_list) < 1:
    print("No Pictures found at: {}".format(site_url))
    exit()

elmts = len(url_list)

for i, url in enumerate(url_list):
    split = url.split(':')
    file_name = split[-2] + "/" + split[-1]
    if not os.path.exists(os.path.dirname(file_name)):
        try:
            os.makedirs(os.path.dirname(file_name))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    if os.path.isfile(file_name):
        print("File already exists -> skipping: {}".format(file_name))
        continue

    print("Querying site: {}".format(url))
    try:
        request = Request(url)
        base64string = base64.encodestring(('%s:%s' % (username, password)).encode()).decode().replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)

        u = urlopen(request)

    except HTTPError as err:
        print(err)
        continue

    f = open(file_name, 'wb')
    meta = u.info()
    if version_info[0] >= 3:
        file_size = int(meta.get_all("Content-Length")[0])
    else:
        file_size = int(meta.getheaders("Content-Length")[0])
    print("Downloading: {} Size: {}".format(file_name, file_size/1e6))

    file_size_dl = 0
    block_sz = 8192

    count = 0
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        count += 1
        if count % 50 == 0:
            status = r"Image [{0}/{1}]: {2:^.2f}/{3:^.2f} MB  [{4:^.2f}%]".format(i+1, elmts,
                                                                                  file_size_dl/1e6, file_size/1e6,
                                                                                  file_size_dl * 100. / file_size)
            print(status)
            count = 0
    f.close()
