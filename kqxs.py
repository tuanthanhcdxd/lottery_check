from html.parser import HTMLParser
import urllib.request


class KQParser(HTMLParser):
    found = False
    result = None

    def handle_starttag(self, tag, attrs):
        if tag == "div" and dict(attrs).get("id") == "rs_0_0":
            self.found = True

    def handle_data(self, data):
        if self.found:
            self.result = data
            self.found = False


req = urllib.request.Request(
    "http://ketqua.net",
    method="GET",
    # sites nowaday block python default user-agent, fake it
    headers={"User-Agent": "python-requests/2.18.2"},
)

with urllib.request.urlopen(req, timeout=5) as f:
    p = KQParser()
    p.feed(f.read().decode("utf-8"))
    print("Giai dac biet", p.result)

