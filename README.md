# Usage 
```
usage: app.py [-h] [-m MODE] [-u URL] [-p PM] [-f FILE]

This tool if used for test lfi/rfi vulnerabilities on web server. app.py --mode lfi --url http://target.com --pm=?lang= --tf=.passwd

options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  mode of attack (lfi or rfi) the default mode is lfi
  -u URL, --url URL     target url
  -p PM, --pm PM        vulnerable param on url
  -f FILE, --file FILE  target file, default file is ../etc/passwd
```
# Sample

![image](https://github.com/njammy/lfi-rfi-vuln-checker/assets/109813492/b598e41d-afd1-4ead-b8be-9e8637370086)
