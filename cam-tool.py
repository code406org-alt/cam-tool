# python cam-tool.py
import subprocess
import sys
import os
import time
import hashlib 
import uuid    

def install_requirements():
    required = ['requests', 'colorama']
    for package in required:
        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install_requirements()

import requests, re, colorama, webbrowser
from colorama import Fore

GREEN = Fore.GREEN
WHITE = Fore.WHITE
red = "\033[1;31m"
BLUE = "\033[1;34m"
NAVY = "\033[1;34m"
SILVER_DARK = "\033[0;37m"

colorama.init()

def fade_in_banner(text, delay=0.04):
    for line in text.splitlines():
        print(line)
        time.sleep(delay)

def type_effect(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_animation(duration=7):
    chars = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{SILVER_DARK}[>] connecting to the server... {chars[i % len(chars)]}{WHITE}")
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write(f"\r{SILVER_DARK}[>] connected ✓                      {WHITE}\n")
    time.sleep(2)


def get_unique_id():
    node = uuid.getnode()
    user_id = hashlib.md5(str(node).encode()).hexdigest()[:8].upper()
    return user_id

while True:
    try:
        os.system('clear' if os.name == 'posix' else 'cls')
        
        try:
            u_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            u_ip = requests.get('https://api.ipify.org', timeout=5).text
            u_id = get_unique_id() 
        except:
            u_ip = "Unknown"
            u_id = "UNKNOWN"

        loading_animation(3)

        banner = f"""
{BLUE} @@@@@@@   @@@@@@   @@@@@@@@@@              @@@@@@@   @@@@@@    @@@@@@   @@@       
@@@@@@@@  @@@@@@@@  @@@@@@@@@@@             @@@@@@@  @@@@@@@@  @@@@@@@@  @@@       
!@@       @@!  @@@  @@! @@! @@!               @@!    @@!  @@@  @@!  @@@  @@!       
!@!       !@!  @!@  !@! !@! !@!               !@!    !@!  @!@  !@!  @!@  !@!       
!@!       @!@!@!@!  @!! !!@ @!@  @!@!@!@!@    @!!    @!@  !@!  @!@  !@!  @!!       
!!!       !!!@!!!!  !@!   ! !@!  !!!@!@!!!    !!!    !@!  !!!  !@!  !!!  !!!       
:!!       !!:  !!!  !!:     !!:               !!:    !!:  !!!  !!:  !!!  !!:       
:!:       :!:  !:!  :!:     :!:               :!:    :!:  !:!  :!:  !:!  ::!      
 ::: :::  ::   :::  :::     ::                 ::    ::::: ::  ::::: ::  ::: :: ::  
 :: :: :   :   : :   :      :                  :      : :  :    : :  :   : :: : :           
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------\033[0m"""

        fade_in_banner(banner)
        type_effect(f"{SILVER_DARK}[>] LOGIN TIME : {u_time}{WHITE}")
        type_effect(f"{SILVER_DARK}[>] YOUR IP    : {u_ip}{WHITE}")
        type_effect(f"{SILVER_DARK}[>] USER ID    : {u_id}{WHITE}") 
        type_effect(f"{WHITE}-----------------------------------------------------------")
        type_effect(f"{WHITE}[>] Mode by : MOSTAFA")
        type_effect(f"{WHITE}[>] Author  : git-blackhub and MOSTAFA")
        type_effect(f"{WHITE}[>] GitHub  : https://github.com/code406org-alt")

        print(f"""
\033[1;37m                                                                         
\033[1;37m1) \033[1;34mUnited States                \033[1;37m37) \033[1;34mMexico                \033[1;37m61) \033[1;34mMoldova
\033[1;37m2) \033[1;34mJapan                        \033[1;37m32) \033[1;34mFinland               \033[1;37m62) \033[1;34mNicaragua
\033[1;37m3) \033[1;34mItaly                        \033[1;37m33) \033[1;34mChina                 \033[1;37m63) \033[1;34mMalta
\033[1;37m4) \033[1;34mKorea                        \033[1;37m34) \033[1;34mChile                 \033[1;37m64) \033[1;34mTrinidad And Tobago
\033[1;37m5) \033[1;34mFrance                       \033[1;37m35) \033[1;34mSouth Africa          \033[1;37m65) \033[1;34mSoudi Arabia
\033[1;37m6) \033[1;34mGermany                      \033[1;37m36) \033[1;34mSlovakia              \033[1;37m66) \033[1;34mCroatia
\033[1;37m7) \033[1;34mTaiwan                       \033[1;37m34) \033[1;34mHungary               \033[1;37m67) \033[1;34mCyprus
\033[1;37m8) \033[1;34mRussian Federation           \033[1;37m38) \033[1;34mIreland               \033[1;37m68) \033[1;34mPakistan
\033[1;37m9) \033[1;34mUnited Kingdom               \033[1;37m39) \033[1;34mEgypt                 \033[1;37m69) \033[1;34mUnited Arab Emirates
\033[1;37m10) \033[1;34mNetherlands                 \033[1;37m40) \033[1;34mThailand              \033[1;37m70) \033[1;34mKazakhstan
\033[1;37m11) \033[1;34mCzech Republic              \033[1;37m41) \033[1;34mUkraine               \033[1;37m71) \033[1;34mKuwait
\033[1;37m12) \033[1;34mTurkey                      \033[1;37m42) \033[1;34mSerbia                \033[1;37m72) \033[1;34mVenezuela
\033[1;37m13) \033[1;34mAustria                     \033[1;37m43) \033[1;34mHong Kong             \033[1;37m73) \033[1;34mGeorgia
\033[1;37m14) \033[1;34mSwitzerland                 \033[1;37m44) \033[1;34mGreece                \033[1;37m74) \033[1;34mMontenegro
\033[1;37m15) \033[1;34mSpain                       \033[1;37m45) \033[1;34mPortugal              \033[1;37m75) \033[1;34mEl Salvador
\033[1;37m16) \033[1;34mCanada                      \033[1;37m46) \033[1;34mLatvia                \033[1;37m76) \033[1;34mLuxembourg
\033[1;37m17) \033[1;34mSweden                      \033[1;37m47) \033[1;34mSingapore             \033[1;37m77) \033[1;34mCuracao
\033[1;37m18) \033[1;34mIsrael                      \033[1;37m48) \033[1;34mIceland               \033[1;37m78) \033[1;34mPuerto Rico
\033[1;37m19) \033[1;34mIran                        \033[1;37m49) \033[1;34mMalaysia              \033[1;37m79) \033[1;34mCosta Rica
\033[1;37m20) \033[1;34mPoland                      \033[1;37m50) \033[1;34mColombia              \033[1;37m80) \033[1;34mBelarus
\033[1;37m21) \033[1;34mIndia                       \033[1;37m51) \033[1;34mTunisia               \033[1;37m81) \033[1;34mAlbania
\033[1;37m22) \033[1;34mNorway                      \033[1;37m52) \033[1;34mEstonia               \033[1;37m83) \033[1;34mBosnia And Herzegovia
\033[1;37m23) \033[1;34mRomania                     \033[1;37m53) \033[1;34mDominican Republic    \033[1;37m84) \033[1;34mParaguay
\033[1;37m24) \033[1;34mViet Nam                    \033[1;37m54) \033[1;34mSloveania             \033[1;37m85) \033[1;34mPhilippines
\033[1;37m25) \033[1;34mBelgium                     \033[1;37m55) \033[1;34mEcuador               \033[1;37m86) \033[1;34mFaroe Islands
\033[1;37m26) \033[1;34mBrazil                      \033[1;37m56) \033[1;34mLithuania             \033[1;37m87) \033[1;34mGuatemala
\033[1;37m27) \033[1;34mBulgaria                    \033[1;37m57) \033[1;34mPalestinian           \033[1;37m88) \033[1;34mNepal
\033[1;37m28) \033[1;34mIndonesia                   \033[1;37m58) \033[1;34mNew Zealand           \033[1;37m82) \033[1;34mLiechtenstein
\033[1;37m29) \033[1;34mDenmark                     \033[1;37m59) \033[1;34mBangladeh             \033[1;37m60) \033[1;34mPanama
\033[1;37m91) \033[1;34mExtra                       \033[1;37m92) \033[1;34mAndorra               \033[1;37m93) \033[1;34mAntigua And Barbuda
\033[1;37m94) \033[1;34mArmenia                     \033[1;37m95) \033[1;34mAngola                \033[1;37m96) \033[1;34mAustralia
\033[1;37m97) \033[1;34mAruba                       \033[1;37m98) \033[1;34mAzerbaijan            \033[1;37m99) \033[1;34mBarbados
\033[1;37m100) \033[1;34mBonaire                    \033[1;37m101) \033[1;34mBahamas              \033[1;37m102) \033[1;34mBotswana
\033[1;37m103) \033[1;34mCongo                      \033[1;37m104) \033[1;34mIvory Coast          \033[1;37m105) \033[1;34mAlgeria
\033[1;37m106) \033[1;34mFiji                       \033[1;37m107) \033[1;34mGabon                \033[1;37m108) \033[1;34mGuernsey
\033[1;37m109) \033[1;34mGreenland                  \033[1;37m110) \033[1;34mGuadeloupe           \033[1;37m111) \033[1;34mGuam
\033[1;37m112) \033[1;34mGuyana                     \033[1;37m113) \033[1;34mHonduras             \033[1;37m114) \033[1;34mJersey
\033[1;37m115) \033[1;34mJamaica                    \033[1;37m116) \033[1;34mJordan               \033[1;37m117) \033[1;34mKenya
\033[1;37m118) \033[1;34mCambodia                   \033[1;37m119) \033[1;34mSaint Kitts          \033[1;37m120) \033[1;34mCayman Islands
\033[1;37m121) \033[1;34mLaos                       \033[1;37m122) \033[1;34mLebanon              \033[1;37m123) \033[1;34mSri Lanka
\033[1;37m124) \033[1;34mMorocco                    \033[1;37m125) \033[1;34mMadagascar           \033[1;37m126) \033[1;34mMacedonia
\033[1;37m127) \033[1;34mMongolia                   \033[1;37m128) \033[1;34mMacao                \033[1;37m129) \033[1;34mMartinique
\033[1;37m130) \033[1;34mMauritius                  \033[1;37m131) \033[1;34mNamibia              \033[1;37m132) \033[1;34mNew Caledonia
\033[1;37m133) \033[1;34mNigeria                    \033[1;37m134) \033[1;34mQatar                \033[1;37m135) \033[1;34mReunion
\033[1;37m136) \033[1;34mSudan                      \033[1;37m137) \033[1;34mSenegal              \033[1;37m138) \033[1;34mSuriname
\033[1;37m139) \033[1;34mSao Tome And Principe      \033[1;37m140) \033[1;34mSyria                \033[1;37m141) \033[1;34mTanzania
\033[1;37m142) \033[1;34mUganda                     \033[1;37m143) \033[1;34mUzbekistan           \033[1;37m144) \033[1;34mSaint Vincent And The Grenadines
\033[1;37m145) \033[1;34mBenin
""")

        countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                     "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                     "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                     "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                     "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                     "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                     "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                     "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                     "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                     "-" , "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB",
                     "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
                     "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
                     "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
                     "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
                     "SY", "TZ", "UG", "UZ", "VC","BJ", ]
        
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

        num_input = input(f"{WHITE}OPTIONS : ")
        if num_input.isdigit():
            num = int(num_input)
            if num in range(1, len(countries) + 1):
                country = countries[num-1]
                res = requests.get(f"http://www.insecam.org/en/bycountry/{country}", headers=headers)
                last_page_match = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)
                last_page = int(last_page_match[0]) if last_page_match else 1

                for page in range(last_page):
                    res = requests.get(f"http://www.insecam.org/en/bycountry/{country}/?page={page}", headers=headers)
                    find_ip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)
                    for ip in find_ip:
                        print(f"{WHITE}{ip}")

        print(f"\n{SILVER_DARK}[+] Subscribe to our channel for more scripts...{WHITE}")
        time.sleep(3.5)
        
        yt_url = "https://www.youtube.com/@git-Black-Hub"
        if os.path.exists('/data/data/com.termux/files/usr/bin/termux-open'):
            os.system(f'termux-open {yt_url}')
        else:
            webbrowser.open(yt_url)
            
       
        print(f"\n{BLUE}-----------------------------------------------------------")
        print(f"{WHITE}[>] Press {BLUE}ENTER{WHITE} to restart script")
        print(f"{WHITE}[>] Press {red}Ctrl+C{WHITE} to exit")
        input(f"{BLUE}-----------------------------------------------------------{WHITE}")

    except KeyboardInterrupt:
        print(f"\n\n{red}[!] Exiting script... Goodbye!{WHITE}")
        break
    except Exception as e:
        print(f"\n{red}Error: {e}{WHITE}")
        input(f"\n{WHITE}Press Enter to restart...")
