from getmac import get_mac_address
from socket import gethostname, gethostbyname
from urllib.request import getproxies


def check_proxies():
    proxy = getproxies()
    if len(proxy) == 0:
        return 'No proxy configured'
    return f'Proxy: {proxy}'


def get_cpu_info():
    hostname = gethostname()
    mac_address = get_mac_address()
    ip_address = gethostbyname(hostname)
    proxy = check_proxies()

    print(f'Hostname is: {hostname}')
    print(f'Ip Address is: {ip_address}')
    print(f'Mac Address is: {mac_address}')
    print(f'{proxy}')


if __name__ == "__main__":
    get_cpu_info()
