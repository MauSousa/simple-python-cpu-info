from getmac import get_mac_address
from socket import gethostname, gethostbyname
from urllib.request import getproxies


def check_proxies():
    proxy = getproxies()
    if len(proxy) == 0:
        return 'No proxy configured'
    return f'Proxy: {proxy}'


def write_info_to_file(hostname, ip, mac, proxy):
    filename = 'pc_info.txt'
    with open(filename, "w") as file:
        file.write("Hostname: ")
        file.write(hostname)
        file.write("\n")
        file.write("Ip address: ")
        file.write(ip)
        file.write("\n")
        file.write("Mac address: ")
        file.write(mac)
        file.write("\n")
        file.write(proxy)
    print(f'Todos los datos están en el archivo {filename}')


def get_cpu_info():
    hostname = gethostname()
    mac_address = get_mac_address()
    ip_address = gethostbyname(hostname)
    proxy = check_proxies()

    write_info_to_file(hostname, ip_address, mac_address, proxy)


if __name__ == "__main__":
    get_cpu_info()
