import requests
from connection.MagicWords import *
from bs4 import BeautifulSoup

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# ----------------------------------------------------------------------GLOBAL IMPORTS IN HERE------------------------------------------------------------------------#

global HEADERS, PAYLOAD, WEBSOC

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------#

formDataRequest = {"Submit": None, }


def web_connection(attempt: int = 0):
    if (attempt == 100):
        print("ATTENTION!!!! Couldn't enstablis connection to the webPage! Application shutting down !!!!ATTENTION")
        exit()

    r = requests.get(WEBSOC)
    if (r.status_code != 200):
        print(f"ERROR: WebReg SEEMS TO NOT BE ONLINE: NewAttempt #{attempt}/100")
        web_connection(attempt + 1)

    scrapper()


def scrapper():
    with requests.session() as session:
        _form = session.post(WEBSOC, data=PAYLOAD)
        soup = BeautifulSoup(_form.content, "html.parser")
        print(soup.prettify())




