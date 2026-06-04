#!/usr/bin/env python3
"""
TOKEN GRENADE V7 - POWERED BY LeGend-X PRODUCTION
Owner: Muddassir-X (+923243037456)
Email: muddassirhussain75@gmail.com
"""

import random
import string
import time
import requests
import uuid
import base64
import io
import struct
import sys
import os
import warnings
from urllib.parse import quote

warnings.filterwarnings("ignore", category=DeprecationWarning)

try:
    from colorama import Fore, Style, init
    init()
except ImportError:
    os.system("pip install colorama")
    from colorama import Fore, Style, init
    init()

try:
    from Crypto.Cipher import AES
    from Crypto.Cipher import PKCS1_v1_5
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes
except ImportError:
    os.system("pip install pycryptodome")
    from Crypto.Cipher import AES
    from Crypto.Cipher import PKCS1_v1_5
    from Crypto.PublicKey import RSA
    from Crypto.Random import get_random_bytes

# --- Approval System ---
APPROVAL_URL = "https://raw.githubusercontent.com/irsalanali788-coder/Approval-/main/approval.txt"
KEY_PATH = os.path.join(os.path.expanduser("~"), ".Rul3x_v7_final.txt")

def get_henry_key():
    if os.path.exists(KEY_PATH):
        with open(KEY_PATH, "r") as f:
            return f.read().strip()
    key = "HENRY-X" + "".join(random.choices(string.digits, k=8))
    with open(KEY_PATH, "w") as f:
        f.write(key)
    return key

def bypass_check(user_key):
    os.system("clear")
    print(f"{Fore.WHITE}\u2554{'═'*48}\u2557")
    print(f"║ {Fore.YELLOW}YOUR KEY : {Fore.GREEN}{user_key}{Fore.WHITE}║")
    print(f"\u255a{'═'*48}\u255d")
    print(f"{Fore.CYAN}Hello Muddassir! Please Approve My Key: ")
    os.system(f'am start https://wa.me/+923243037456?text={quote(user_key)} >/dev/null 2>&1')
    print(f"📲 Checking Live Approval (No-Cache Mode)...")
    while True:
        try:
            r = requests.get(f"{APPROVAL_URL}?t={int(time.time())}")
            if r.status_code == 200:
                if user_key in r.text:
                    print("✅ KEY APPROVED! STARTING TOOL...")
                    return True
            print("⏳ Status: Pending Approval... Retrying in 5s ")
            time.sleep(5)
        except:
            print("⚠️ Connection Slow... Retrying.")
            time.sleep(5)


# --- Flashy Colors ---
flashy_colors = [
    Fore.LIGHTRED_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTYELLOW_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTMAGENTA_EX, Fore.LIGHTCYAN_EX
]

def get_random_color_line(text):
    return random.choice(flashy_colors) + text + Style.RESET_ALL

def animated_print(text, delay=0.03):
    for line in text.splitlines():
        sys.stdout.write(get_random_color_line(line) + "\n")
        sys.stdout.flush()
        time.sleep(delay)

def loading_animation(text="PENETRATING FACEBOOK SERVERS..."):
    for char in text:
        sys.stdout.write(f"{Fore.CYAN}{Style.BRIGHT}{char}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(0.05)
    print()


# --- Facebook Password Encryptor ---
class FacebookPasswordEncryptor:
    @staticmethod
    def get_public_key():
        try:
            r = requests.get("https://b-graph.facebook.com/pwd_key_fetch", params={
                "version": "2",
                "access_token": "438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28"
            })
            data = r.json()
            return data["public_key"], data["key_id"]
        except Exception as e:
            print(f"Public key fetch error: {str(e)}")
            return None, None

    @staticmethod
    def encrypt(password):
        try:
            pub_key_str, key_id = FacebookPasswordEncryptor.get_public_key()
            if not pub_key_str:
                return None

            rand_bytes = get_random_bytes(25)
            rsa_key = RSA.import_key(pub_key_str)
            cipher_rsa = PKCS1_v1_5.new(rsa_key)
            encrypted_random = cipher_rsa.encrypt(rand_bytes)

            cipher_aes = AES.new(rand_bytes[:16], AES.MODE_GCM)
            timestamp = str(int(time.time()))
            cipher_aes.update(timestamp.encode("utf-8"))
            encrypted_pw, tag = cipher_aes.encrypt_and_digest(password.encode("utf-8"))

            buf = io.BytesIO()
            buf.write(bytes([1]))
            buf.write(struct.pack(">B", int(key_id)))
            buf.write(struct.pack(">H", len(encrypted_random)))
            buf.write(encrypted_random)
            buf.write(tag)
            buf.write(encrypted_pw)

            encoded = base64.b64encode(buf.getvalue()).decode("utf-8")
            return f"#PWD_FB4A:2:{timestamp}:{encoded}"
        except Exception as e:
            print(f"Encryption error: {str(e)}")
            return None


# --- Facebook App Tokens ---
class FacebookAppTokens:
    APPS = {
        "Facebook For Android": "350685531728",
        "Facebook Messenger For Android": "256002347743983",
        "Facebook For Lite": "275254692598279",
        "Facebook Messenger For Lite": "200424423651082",
        "Ads Manager App For Android": "438142079694454",
    }

    @staticmethod
    def extract_token_prefix(token):
        for i, c in enumerate(token):
            if c.islower():
                return token[:i]
        return token


# --- Generate IDs ---
def generate_ids():
    return {
        "adid": str(uuid.uuid4()),
        "device_id": str(uuid.uuid4()),
        "family_device_id": str(uuid.uuid4()),
        "session_id": str(uuid.uuid4()),
        "advertiser_id": str(uuid.uuid4()),
        "reg_instance": str(uuid.uuid4()),
        "machine_id": ''.join(random.choices(string.ascii_lowercase + string.digits, k=24)),
    }


# --- Facebook Login ---
class FacebookLogin:
    API_URL = "https://b-api.facebook.com/method/auth.login"
    ACCESS_TOKEN = "350685531728|62f8ce9f74b12f84c123cc23437a4a32"
    API_KEY = "882a8490361da98702bf97a021ddc14d"
    SIG = "62f8ce9f74b12f84c123cc23437a4a32"
    USER_AGENT = "Dalvik/2.1.0 (Linux; U; Android 12; SM-G998B Build/SP1A.210812.016) [FBAN/FB4A;FBAV/407.0.0.30.85;FBLC/en_US;FBBV/457696233;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G998B;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;]"

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.encrypted_password = FacebookPasswordEncryptor.encrypt(password)
        self.ids = generate_ids()
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": self.USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
        })

    def login(self):
        animated_print("[*] BYPASSING SECURITY NODES...")
        loading_animation()

        data = {
            "email": self.email,
            "password": self.encrypted_password or self.password,
            "adid": self.ids["adid"],
            "device_id": self.ids["device_id"],
            "family_device_id": self.ids["family_device_id"],
            "session_id": self.ids["session_id"],
            "advertiser_id": self.ids["advertiser_id"],
            "reg_instance": self.ids["reg_instance"],
            "machine_id": self.ids["machine_id"],
            "locale": "en_US",
            "country_code": "US",
            "client_country_code": "US",
            "cpl": "true",
            "source": "login",
            "format": "json",
            "credentials_type": "password",
            "error_detail_type": "button_with_disabled",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "tier": "regular",
            "device": "SM-G998B",
            "os_ver": "12",
            "app_id": "350685531728",
            "app_ver": "407.0.0.30.85",
            "meta_inf_fbmeta": "NO_FILE",
            "currently_logged_in_userid": "0",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
            "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
            "access_token": self.ACCESS_TOKEN,
            "api_key": self.API_KEY,
            "sig": self.SIG,
        }

        try:
            r = self.session.post(self.API_URL, data=data)
            response = r.json()

            if "access_token" in response:
                return self._parse_success(response)
            elif "error_code" in response:
                error_code = response.get("error_code", 0)
                if error_code == 406:
                    # 2FA required
                    return {"2fa_required": True, "login_first_factor": response.get("login_first_factor", ""), "uid": response.get("uid", ""), "error_msg": "2FA Required - Enter your code"}
                return {"error": f"Login failed (Code: {error_code}) {response.get('error_msg', '')}"}
            return {"error": "Unexpected response from server"}
        except Exception as e:
            return {"error": f"Network error: {str(e)}"}

    def submit_2fa(self, code, login_first_factor, uid):
        data = {
            "twofactor_code": code,
            "encrypted_msisdn": "",
            "userid": uid,
            "first_factor": login_first_factor,
            "locale": "en_US",
            "country_code": "US",
            "client_country_code": "US",
            "format": "json",
            "credentials_type": "two_factor",
            "generate_session_cookies": "1",
            "generate_analytics_claim": "1",
            "generate_machine_id": "1",
            "source": "login",
            "device": "SM-G998B",
            "os_ver": "12",
            "app_id": "350685531728",
            "app_ver": "407.0.0.30.85",
            "access_token": self.ACCESS_TOKEN,
            "api_key": self.API_KEY,
            "sig": self.SIG,
        }

        try:
            r = self.session.post(self.API_URL, data=data)
            response = r.json()
            if "access_token" in response:
                return self._parse_success(response)
            return {"error": response.get("error_msg", "2FA verification failed")}
        except Exception as e:
            return {"error": f"Network error: {str(e)}"}

    def _parse_success(self, response):
        token = response.get("access_token", "")
        result = {
            "success": True,
            "access_token": token,
            "token_prefix": FacebookAppTokens.extract_token_prefix(token),
            "uid": self.extract_user_id(token),
            "cookies": "; ".join([f"{c['name']}={c['value']}" for c in response.get("session_cookies", [])]),
        }

        # Exchange to EAAD6V7 token
        eaad_token = self.exchange_to_eaad(token)
        if eaad_token:
            result["eaad6v7_token"] = eaad_token

        # Convert to all app tokens
        converted = {}
        for app_name, app_id in FacebookAppTokens.APPS.items():
            try:
                r = requests.post("https://api.facebook.com/method/auth.getSessionforApp", data={
                    "format": "json",
                    "access_token": token,
                    "new_app_id": app_id,
                    "generate_session_cookies": "1",
                })
                td = r.json()
                if "access_token" in td:
                    converted[app_name] = td["access_token"]
            except:
                pass
        result["converted_tokens"] = converted
        return result

    def exchange_to_eaad(self, token):
        try:
            r = requests.post("https://api.facebook.com/method/auth.getSessionforApp", data={
                "format": "json",
                "access_token": token,
                "new_app_id": "275254692598279",
                "generate_session_cookies": "1",
            })
            data = r.json()
            if "access_token" in data:
                return data["access_token"]
        except:
            pass
        return None

    def extract_user_id(self, token):
        try:
            parts = token.split("|")
            first = parts[0] if parts else ""
            if first.isdigit():
                return first
            return first[:20] + "..."
        except:
            return "Unknown"


# --- Permission Checker ---
class PermissionChecker:
    PERMISSIONS = [
        "email", "public_profile", "user_friends", "user_posts",
        "user_photos", "user_videos", "user_likes", "user_birthday",
        "user_location", "user_hometown", "user_gender", "user_age_range",
        "user_link", "user_events", "user_groups", "pages_show_list",
        "pages_read_engagement", "pages_manage_posts", "publish_actions",
        "publish_pages", "manage_pages", "ads_management", "ads_read",
        "business_management", "instagram_basic", "instagram_content_publish",
        "instagram_manage_comments", "instagram_manage_insights",
        "whatsapp_business_management", "groups_access_member_info",
    ]

    @staticmethod
    def check(token):
        results = {}
        for perm in PermissionChecker.PERMISSIONS:
            try:
                r = requests.get(f"https://graph.facebook.com/me?access_token={token}&fields=id,name")
                if r.status_code == 200:
                    results[perm] = "✅"
                else:
                    results[perm] = "❌"
            except:
                results[perm] = "❌"
        return results


# --- Main ---
if __name__ == "__main__":
    os.system("clear")

    # Approval check
    user_key = get_henry_key()
    bypass_check(user_key)

    os.system("clear")

    # UI
    border_color = Fore.MAGENTA
    print(f"{border_color}╔════════════════════════════════════════════════════════════╗")
    print(f"║ {Fore.WHITE}SYSTEM STATUS: {Fore.GREEN}PREMIUM TOOL (ACTIVE)           {border_color}    ║")
    print(f"║ {Fore.WHITE}PRICE: {Fore.YELLOW}200₹ / MONTHLY                          {border_color}║")
    print(f"║ {Fore.WHITE}OWNER: {Fore.CYAN}LeGend-X (Muddassir)                    {border_color}║")
    print(f"║ {Fore.WHITE}WHATSAPP: {Fore.GREEN}+923243037456                        {border_color}║")
    print(f"║ {Fore.WHITE}EMAIL: {Fore.CYAN}muddassirhussain75@gmail.com           {border_color}║")
    print(f"{border_color}╚════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    print("<<==============================================================>>")
    print("          TOKEN GRENADE V7 - POWERED BY LeGend-X PRODUCTION")
    print()

    u = input(f"{Fore.YELLOW}ENTER GMAIL/PHONE NUMBER ➠ {Style.RESET_ALL}").strip()
    p = input(f"{Fore.YELLOW}ENTER PASSWORD ➠ {Style.RESET_ALL}").strip()

    fb = FacebookLogin(u, p)
    result = fb.login()

    if result.get("2fa_required"):
        print(f"\n{Fore.YELLOW}[⚠️] 2FA REQUIRED!")
        code = input(f"{Fore.YELLOW}ENTER 2FA CODE ➠ {Style.RESET_ALL}").strip()
        result = fb.submit_2fa(code, result.get("login_first_factor", ""), result.get("uid", ""))

    if result.get("success"):
        print(f"\n {Fore.GREEN}[✅] TOKEN GENERATED SUCCESSFULLY!")
        print(f"{Fore.WHITE}UID: {Fore.CYAN}{result.get('uid', '')}")
        print(f"{Fore.WHITE}TOKEN PREFIX: {Fore.GREEN}{result.get('token_prefix', '')}")
        print(f"{Fore.WHITE}ACCESS TOKEN: {Fore.YELLOW}{result.get('access_token', '')}")

        if result.get("eaad6v7_token"):
            print(f"\n{Fore.WHITE}EAAD6V7 TOKEN: {Fore.GREEN}{result['eaad6v7_token']}")

        if result.get("converted_tokens"):
            print(f"\n{Fore.WHITE}CONVERTED TOKENS:")
            for app, data in result["converted_tokens"].items():
                print(f"  {Fore.CYAN}APP: {Fore.WHITE}{app}")
                print(f"  {Fore.GREEN}TOKEN: {data}")
                print()

        if result.get("cookies"):
            print(f"\n {Fore.YELLOW}[🍪] SESSION COOKIES ")
            print(f"  {result['cookies']}")
    else:
        print(f"\n {Fore.RED}[!] LOGIN FAILED: {result.get('error', '')}")

    print(f"\n{Fore.MAGENTA}OFFICIAL LeGend-X PRODUCTION TOOL{Style.RESET_ALL}")
  
