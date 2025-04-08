import csv
import subprocess
import os

# Load daftar IP dan nama komputer dari InvAllComputersSummary.csv
def load_existing_ips(inv_file):
    existing_info = {}
    if not os.path.exists(inv_file):
        print(f"[ERROR] File inventory '{inv_file}' tidak ditemukan.")
        return existing_info
    with open(inv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ip = row.get("IP Address")
            name = row.get("Computer Name", "Unknown")
            if ip:
                existing_info[ip.strip()] = name.strip()
    return existing_info

# Jalankan nslookup

def nslookup(target):
    try:
        result = subprocess.run(["nslookup", target], capture_output=True, text=True, check=True)
        for line in result.stdout.splitlines():
            if line.strip().lower().startswith("name:"):
                return line.split("Name:")[1].strip()
        return "Not resolved"
    except subprocess.CalledProcessError as e:
        return "Not resolved"

# Proses IP dan simpan hasil

def process_ip_csv(ip_csv_file, inv_csv_file, output_file):
    existing_info = load_existing_ips(inv_csv_file)
    if not os.path.exists(ip_csv_file):
        print(f"[ERROR] File input '{ip_csv_file}' tidak ditemukan.")
        return

    results = []

    with open(ip_csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            host_asal = row.get("Host asal", "Unknown").strip()
            target_ip = row.get("IP")
            if target_ip:
                target_ip = target_ip.strip()
                if target_ip in existing_info:
                    computer_name = existing_info[target_ip]
                    print(f"[-] IP {target_ip} ditemukan di inventory. Nama Komputer: {computer_name}.")
                    results.append({
                        "Host Asal": host_asal,
                        "IP": target_ip,
                        "Status": "Found",
                        "Computer Name": computer_name
                    })
                else:
                    print(f"[+] IP {target_ip} tidak ditemukan di inventory. Menjalankan nslookup...")
                    resolved_name = nslookup(target_ip)
                    status = "Not found"
                    print(f"    Hasil nslookup: {resolved_name}")
                    results.append({
                        "Host Asal": host_asal,
                        "IP": target_ip,
                        "Status": status,
                        "Computer Name": resolved_name
                    })

    # Simpan hasil ke CSV
    if results:
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=["Host Asal", "IP", "Status", "Computer Name"])
            writer.writeheader()
            writer.writerows(results)
        print(f"\n[✓] Hasil pencarian disimpan ke: {output_file}")
    else:
        print("\n[!] Tidak ada IP untuk diproses.")

# Path
script_dir = os.path.dirname(os.path.abspath(__file__))
ip_csv = os.path.join(script_dir, "input.csv")
inventory_csv = os.path.join(script_dir, "InvAllComputersSummary.csv")
output_csv = os.path.join(script_dir, "nslookup_results.csv")

process_ip_csv(ip_csv, inventory_csv, output_csv)
