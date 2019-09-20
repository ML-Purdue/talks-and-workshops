import requests

PURDUE_CTLG_XML_URL = "https://selfservice.mypurdue.purdue.edu/prod/bwckctlg.xml"


headers = {
    "origin": "https://selfservice.mypurdue.purdue.edu",
    "upgrade-insecure-requests": "1",
    "dnt": "1",
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "sec-fetch-site": "same-origin",
    "cache-control": "no-cache",
}

def download_subj_xml(subj):
    payload = {
        "attr_in": "%",
        "coll_in": "%",
        "cred_from_in": "",
        "cred_to_in": "",
        "crse_end_in": "",
        "crse_strt_in": "",
        "dept_in": "%",
        "divs_in": "%",
        "last_updated": "",
        "levl_in": "%",
        "schd_in": "%",
        "subj_in": f"\t{subj}\t",
        "term_in": "202010",
        "title_in": "%%",
    }

    res = requests.post(PURDUE_CTLG_XML_URL, data=payload, headers=headers)
    return res.text


print(download_subj_xml('CS'))
