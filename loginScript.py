from requests import Session
from bs4 import BeautifulSoup as bs

with Session() as s:
    site = s.get("https://portal.smktarunabhakti.net/login/index.php", verify=False)
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name": "logintoken"})["value"]
    login_data = {"username": "18191146", "password": "1234567*", "logintoken": token}
    s.post("https://portal.smktarunabhakti.net/login/index.php", login_data)
    home_page = s.get("https://portal.smktarunabhakti.net/")
    print(home_page.content)
