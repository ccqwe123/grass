import requests
import time

url = "https://api.bigdatacloud.net/data/client-ip"
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "__Host-next-auth.csrf-token=35ebcbee5972769e7c3f4b7edb0dda28d859c6784e0f1cd3b36259235eb9fa0d%7C44b02128e710d452f02b227cda9c6cbe8f97106862b29fa8db82d258220a020f; _id=67c84ae4b12df4279c48dc1d; __Secure-next-auth.callback-url=https%3A%2F%2Fquest.aidenlabs.ai%2Fpost-signin%2F67c82f11b12df4279c487b7c; cf_clearance=RE5O4P7xWev8alUf_T21SQeSGq_c3exAXdvIjCfMrmM-1741179822-1.2.1.1-AId0yFED908likzfNDpOsKBNMxjEXNHAB19BI8De2De27aT1h9RHemSxxeCWTsEgFdjBQZDL1tG2WvziKNmst3R1hv5IPAdsg_2rsArx9fy.b1Xe31y71fEwnc_vfAmcfYj7hCc0kLl2qYjdNh_6hpHLVfgioAK6iEt1dZHmYVJafmjwHQjynTB6lEY6sQ1.FgtCBLiiKCmQGQJhVGF45W7.s2y6_z3MD8zo5q6SOCJ98KW9KfQJliPEd_f7k5B9DVFdNOlWSgwqmaEsksON4puJWG8581RCRxCihmdwpWaP752bi32NklDR9duLGf0qyJdbFNaryxEVm8I1K7PhTC9_qNhiKA_GaJiS226P74uwms34zfuUwrn2AC6WYPjpoGerp4KLqedotWvAbrng4Ct0E49qDrHuJAWeKmerjvC7OS5jzD4w8Y_apudiif0bLt_vdAo1rN3roIj3fFehNA; __Secure-next-auth.session-token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..xzFlFH9EXJb7cIcb.5fm6gAQrCnIPNxDrrFZygzsuy6qXg-vCakiQKW5EMPVux5WRG1SCTigxEpza-ebMGsUrTrl46fibKSFiqTlN0SbPkd69qLhj7cRwryKKHyNjaVrX5YKYhFl1EOp2hCJt2z1mUveTv0cryE3EElX_AZFIroJqwrU72KUfkxUBgeeFPsgwY5QIBTQ5dX3KlIgnumAHwh-eq_gAB00bPWszGG7W2DZEF-XHCMADowGpm2T_RYxq9RtF2mu0NwncsWkxHEBOt8ePVY0I7x7JIWabwh3F5a3LF600NviuCxabHSlmOg.axfg_S3acVwiSQ6ismZ3DA",
    "Priority": "u=1, i",
    "Referer": "https://quest.aidenlabs.ai/",
    "Sec-Ch-Ua": "\"Not(A:Brand\";v=\"99\", \"Brave\";v=\"133\", \"Chromium\";v=\"133\"",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Ch-Ua-Platform-Version": "\"10.0.0\"",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Gpc": "1",
}

try:
    with open('token.txt', 'r') as f:
        token = f.read().strip()
        headers['Authorization'] = f'Bearer {token}'
except FileNotFoundError:
    print("token.txt file not found.")
    exit()

while True:
    try:
        response = requests.get(url, headers=headers)
        print("Ping Success!")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    time.sleep(10)