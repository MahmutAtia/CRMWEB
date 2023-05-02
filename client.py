import requests
#url  ="http://127.0.0.1:8000/api/accounts/login/"
url = "http://127.0.0.1:8000/api/companies/"
puturl = "http://127.0.0.1:8000/api/companies/contact/86"
token = "e6d2335a2e4261ca032b10f65b71f55de6483cd2"
res = requests.put(puturl,json={ "company": "Orhan bey",
"contact_time"
: 
"0",
"contact_type"
: 
"ARAMA",
"contact_url"
: 
"http://127.0.0.1:8000/api/companies/contact/91",
"date"
: 
"2023-02-20",
"result"
: 
"CEVAP YOK  WP",
}, 
                #   headers={"Authorization":"Token "+token}
                     )

print(res.json())