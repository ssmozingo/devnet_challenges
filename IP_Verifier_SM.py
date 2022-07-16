import ipaddress

def checkIpAdd():
    ipadd = input("Enter IP address (Press x to exit.): ")
    if ipadd == "x":
        return print("Thanks for using the IP Verifier")
    try:
        ip = (ipaddress.ip_address(ipadd))
        print("IP address is valid.")
        checkIpAdd()
    except:
        print("IP address is not valid.") 
        checkIpAdd()
        
checkIpAdd()