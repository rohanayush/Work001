import urllib.request
with urllib.request.urlopen('https://python.org') as response:
     html = response.read()
#print(html)
html1=html + "iiitA5".encode("ascii")
html2=" "
for i in html1:
	if(i == ord('<')):
		html2= html2+" "+chr(i)
		html2=html2+" "
	if(i == ord('>')):
		html2=html2+ " "+chr(i)+" "
	if(i == ord('"')):
		html2=html2+ " "+chr(i)+" "
	if(i == ord('/')):
		html2=html2+ " "+chr(i)+" "

	else:
		html2=html2 + chr(i)



