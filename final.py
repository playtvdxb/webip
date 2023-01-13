from cgitb import text
import json
import sys
import requests
cookies = {
    'mac': '00%3A1A%3A79%3A4f%3Aea%3A0c', 
    'stb_lang': 'en',
    'timezone': 'Europe%2FParis',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
    'Referrer': 'http://92.204.40.153/stalker_portal/c/',
    'X-User-Agent': 'Model: MAG250; Link: WiFi',
    'Cache-Control': 'no-cache',
    'Host': '92.204.40.153',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}

params = (
    ('type', 'stb'),
    ('action', 'handshake'),
    ('token', ''),
    ('JsHttpRequest', '1-xml'),
)

response = requests.get('http://92.204.40.153/stalker_portal/server/load.php', headers=headers, params=params, cookies=cookies)
json_object = json.loads(response.text)
json_object2=json_object["js"]
token=json_object2["token"]
random=json_object2["random"]
# print(token,random)
Bearer=c='Bearer'+ " "+token
metrics='{"mac":"00:1A:79:4f:ea:0c","sn":"","model":"MAG250","type":"STB","uid":"","random":"'+random+'"}'

headers = {
    'Accept': '/',
    'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3',
    'Referer': 'http://92.204.40.153/stalker_portal/c/',
    'Accept-Language': 'en-US,',
    'Accept-Charset': 'UTF-8,;q=0.8',
    'X-User-Agent': 'Model: MAG254; Link: WiFi',
    'Authorization': c,
    'Host': '92.204.40.153',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
}
params = (
    ('', ''),
    ('action', 'get_profile'),
    ('random', random),
    ('mac', '00:1A:79:4f:ea:0c'),
    ('type', 'stb'),
    ('hd', '1'),
    ('sn', ''),
    ('stb_type', 'MAG250'),
    ('client_type', 'STB'),
    ('image_version', '218'),
    ('device_id', ''),
    ('hw_version', '1.7-BD-00'),
    ('hw_version_2', '1.7-BD-00'),
    ('auth_second_step', '1'),
    ('video_out', 'hdmi'),
    ('num_banks', '2'),
    ('metrics', metrics),
    ('ver', 'ImageDescription: 0.2.18-r14-pub-250; ImageDate: Fri Jan 15 15:20:44 EET 2016; PORTAL version: 5.6.1; API Version: JS API version: 328; STB API version: 134; Player Engine version: 0x566'),
)
response = requests.get('http://92.204.40.153/stalker_portal/server/load.php', headers=headers, params=params, cookies=cookies)

params = (
    ('type', 'itv'),
    ('action', 'create_link'),
    ('forced_storage', 'undefined'),
    ('download', '0'),
    ('cmd', 'ffrt http://localhost/ch/'+sys.argv[1]),
)
response = requests.get('http://92.204.40.153/stalker_portal/server/load.php', headers=headers, params=params, cookies=cookies)
json_object = json.loads(response.text)
# print(response.text)
json_object2=json_object["js"]
# print(json_object2)
channel_link=json_object2["cmd"]
t=channel_link.replace("\\/","/")
URL = t
t+='"'
print(t)
