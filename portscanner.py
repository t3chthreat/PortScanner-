import socket 
import termcolor



# this will allow the user to san the number of a targets port set by the code user  
def scan(target, ports):
    print('\n'+ 'Starting Scan For ' + str(target))
    for port in range (1, ports):
        scan_port(target,port)

#this is the code main line that allow the code to scan the ports  
def scan_port(ipaddress, port):
    try:
        sock = socket.scoket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened" + str(port))
        sock.close()    
    except:
        pass

# this sets the variables that targets and ports that we will be scanning that are vunerable 
targets = input("[*] Enter Target To Scan: ")
ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
if ',' in targets:
    print (termcolor.colored("[*] Scanning Multiple Targets"), 'green'), 
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
else:
    scan(targets,ports)
