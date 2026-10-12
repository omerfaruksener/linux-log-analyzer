import sys
import json
import argparse
from pathlib import Path
from collections import Counter

# 1.BUSINESS LOGIC
def analiz_yap(lines, filtre_seviyesi=None):
    log_levels = []
    error_messages = []

    for line in lines:
        words = line.split()
        first_word = words[0]

        
        if filtre_seviyesi and first_word != filtre_seviyesi:
            continue

        if first_word == "ERROR":
            message = " ".join(words[1:])
            error_messages.append(message)

        log_levels.append(first_word)

    numbers = Counter(log_levels)
    numberof_errors = Counter(error_messages)

    # Sadece hesaplanan veriyi bir Sözlük olarak geri döndürüyoruz
    return {   
        "total_lines": len(lines),
        "level_counts": dict(numbers),
        "top_errors": dict(numberof_errors.most_common(5))
    }

# 2. Commmand line and file exec
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Linux Log Analyzer CLI")
    parser.add_argument("files", help="Path to the log file to analyze")
    parser.add_argument("--level", help="Filter log entries by level")
    args = parser.parse_args()

    # Read file and catch error section
    try:
        lines = Path(args.files).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        print(f"Hata: '{args.files}' adinda bir dosya bulunamadi. Lütfen dosya yolunu kontrol edin.")
        sys.exit(1)

    # Step 1: prep data and call function
    rapor = analiz_yap(lines, args.level)

    # Step 2: write
    print(f"Total log entries: {rapor['total_lines']}")
    print(rapor['level_counts'])
    print("\nMost frequent errors:")
    for error, number in rapor['top_errors'].items():
        print(f"{error}: {number}")

    # Step 3: save 
    json_text = json.dumps(rapor, indent=4)
    Path("output.json").write_text(json_text, encoding="utf-8")
    print("\nSonuclar output.json dosyasina kaydedildi!")