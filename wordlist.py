import argparse
import itertools
import string
import os
import time

def generate_wordlist(combinations, min_length, max_length):
    wordlist = set()

    # Kombinasi dasar tanpa modifikasi
    for combo in combinations:
        if min_length <= len(combo) <= max_length:
            wordlist.add(combo)
            wordlist.add(combo.upper())  # Tambah huruf kapital
            wordlist.add(combo.capitalize())  # Kapital awal

    # Kombinasi antar kata
    for r in range(2, 4):  # Kombinasi 2 dan 3 kata
        for comb in itertools.permutations(combinations, r):
            combo = ''.join(comb)
            if min_length <= len(combo) <= max_length:
                wordlist.add(combo)
                wordlist.add(combo.upper())  # Kapital semua
                wordlist.add(combo.capitalize())  # Kapital awal

    # Kombinasi karakter berulang (aa, bb, cc, dll.)
    for combo in combinations:
        double_combo = combo * 2
        if min_length <= len(double_combo) <= max_length:
            wordlist.add(double_combo)
            wordlist.add(double_combo.upper())  # Kapital semua
            wordlist.add(double_combo.capitalize())  # Kapital awal

    # Kombinasi dua karakter dari kombinasi awal
    for comb in itertools.combinations(combinations, 2):
        combo = ''.join(comb)
        if min_length <= len(combo) <= max_length:
            wordlist.add(combo)
            wordlist.add(combo.upper())  # Kapital semua
            wordlist.add(combo.capitalize())  # Kapital awal

    # Kombinasi dengan angka 1-100
    for combo in wordlist.copy():
        if min_length <= len(combo) + 2 <= max_length:
            for i in range(1, 101):
                wordlist.add(f"{combo}{i}")
                wordlist.add(f"{i}{combo}")

    # Kombinasi dengan karakter khusus
    special_chars = ['#', '@', '%', '&', '*']
    for combo in wordlist.copy():
        if min_length <= len(combo) + 1 <= max_length:
            for char in special_chars:
                wordlist.add(f"{combo}{char}")
                wordlist.add(f"{char}{combo}")

    # Kombinasi penggantian karakter
    replacements = {'a': '4', 'e': '3', 'g': '9'}
    for combo in wordlist.copy():
        if min_length <= len(combo) <= max_length:
            new_combo = ''.join(replacements.get(c, c) for c in combo)
            wordlist.add(new_combo)

    # Memfilter berdasarkan panjang
    wordlist = {word for word in wordlist if min_length <= len(word) <= max_length}

    return wordlist

def save_wordlist(wordlist, output_file):
    with open(output_file, 'w') as file:
        for word in sorted(wordlist):
            file.write(f"{word}\n")

def main():
    parser = argparse.ArgumentParser(description="Generate a wordlist with various combinations.")
    parser.add_argument('-k', '--kombinasi', required=True, help="Comma-separated list of base combinations.")
    parser.add_argument('-o', '--output', required=True, help="Output file path for the wordlist.")
    parser.add_argument('--min', type=int, default=1, help="Minimum length of combinations to include (default: 1).")
    parser.add_argument('--max', type=int, default=100, help="Maximum length of combinations to include (default: 100).")

    args = parser.parse_args()

    combinations = [x.strip() for x in args.kombinasi.split(',')]
    min_length = args.min
    max_length = args.max
    output_file = args.output

    start_time = time.time()
    wordlist = generate_wordlist(combinations, min_length, max_length)
    end_time = time.time()

    # Menyimpan wordlist
    save_wordlist(wordlist, output_file)

    # Menampilkan proses pembuatan
    total_words = len(wordlist)
    file_size = os.path.getsize(output_file) / 1024  # Ukuran file dalam KB

    elapsed_time = end_time - start_time
    days = int(elapsed_time // (24 * 3600))
    elapsed_time %= (24 * 3600)
    hours = int(elapsed_time // 3600)
    elapsed_time %= 3600
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)

    print(f"Wordlist berhasil dibuat dengan {total_words} baris.")
    print(f"Ukuran file: {file_size:.2f} KB")
    print(f"Estimasi waktu penyelesaian: {days} hari, {hours} jam, {minutes} menit, {seconds} detik")

if __name__ == "__main__":
    main()
