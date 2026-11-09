import json
import urllib.request

def get_ip_info():
    try:
        # Mengambil data dari API ipinfo.io
        with urllib.request.urlopen("https://ipinfo.io/json") as response:
            data = json.load(response)
        
        print("\n--- Informasi IP Publik Anda ---")
        print(f"IP Address : {data.get('ip', 'Tidak tersedia')}")
        print(f"Kota       : {data.get('city', 'Tidak tersedia')}")
        print(f"Wilayah    : {data.get('region', 'Tidak tersedia')}")
        print(f"Negara     : {data.get('country', 'Tidak tersedia')}")
        print(f"ISP        : {data.get('org', 'Tidak tersedia')}")
        print("--------------------------------\n")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    get_ip_info()
