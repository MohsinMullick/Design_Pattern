from abc import ABC, abstractmethod
class Internet(ABC):
    @abstractmethod
    def connect_to(self, server_host: str):
        pass
class RealInternet(Internet):
    def connect_to(self, server_host: str):
        print(f"Connecting to {server_host}")
class ProxyInternet(Internet):
    banned_sites = {"abc.com", "xyz.com", "banned.com"}
    def __init__(self):
        self.real_internet = RealInternet()
    def connect_to(self, server_host: str):
        lower_server_host = server_host.lower()
        if lower_server_host in self.banned_sites:
            raise RuntimeError(f"Access Denied to {server_host}")
        self.real_internet.connect_to(server_host)
def attempt_connection(internet: Internet, site: str):
    try:
        internet.connect_to(site)
        print(f"Successfully connected to {site}!")
    except Exception as e:
        print(e)
if __name__ == "__main__":
    proxy_internet = ProxyInternet()
    attempt_connection(proxy_internet, "example.com")
    attempt_connection(proxy_internet, "abc.com")  # This site is banned.
    attempt_connection(proxy_internet, "stackoverflow.com")
