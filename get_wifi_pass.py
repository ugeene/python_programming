import subprocess
import re
def get_wifi_password():
    try:

        profiles_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
        profies = [line.split(":")[1].strip() for line in profiles_data.split('\n') if "All User Profiles" in line]

        for profiles in profies:
            try:
                profile_info = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profiles, 'key=clear']).decode('utf-8')
                password = re.search(r'Key Content\s+:\s+(.+)', profile_info)
                if password:
                    print(f"Wifi SSID: {profile}\nPassword: {password.group(1)}\n")
                else:
                    print("Wifi SSID: {profile}\nPassword: NOT FOUND\n")
            except subprocess.CalledProcessError:
                print(f"WiFi SSID: {profile}\nError retriving password\n")
    except subprocess.CalledProcessError:
        print("Error Retriving WIFI profiles. Run as Administrator.")
if __name__ == '__main__':
    get_wifi_password()

