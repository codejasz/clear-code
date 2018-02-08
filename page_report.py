import csv
import re
import operator

import sys

logs = """
10.4.180.222 [28/Jan/2018:10:02:32 +0100] "GET http://clearcode.cc/ HTTP/1.1" 200 1080
10.4.180.222 [28/Jan/2018:10:03:31 +0100] "GET http://www.clearcode.cc HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:05:30 +0100] "GET http://clearcode.cc/careers HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:08:29 +0100] "GET http://clearcode.cc/careers/ HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:13:29 +0100] "GET http://clearcode.cc/careers? HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:21:27 +0100] "GET http://clearcode.cc/careers/? HTTP/1.1" 200 3056
10.4.180.222 [28/Jan/2018:10:34:26 +0100] "GET
http://clearcode.cc/careers?offer=internship&type=python HTTP/1.1" 200 4545

10.4.180.222 [28/Jan/2018:10:55:25 +0100] "GET
http://clearcode.cc/careers?type=frontend&offer=internship HTTP/1.1" 200 5454
https://www.google.pl/
https://www.google.pl/
https://docs.python.org/3/library/
https://docs.python.org/3/library/
https://docs.python.org/3/library/

"""

urls = re.findall(r'(?P<url>[a-z]*[a-z]+\.[a-z]+/*[a-z]*\.*[a-z]+)', logs)

dict = {}
for url in urls:
    if url not in dict:
        dict.setdefault(url, 1)
    else:
        dict[url] += 1

spamwriter = csv.writer(sys.stdout, quoting=csv.QUOTE_NONNUMERIC)

spamwriter.writerows(sorted(dict.items(),
                            key=operator.itemgetter(1), reverse=True))
