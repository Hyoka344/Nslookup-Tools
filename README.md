# 🔍 IP Inventory Lookup & nslookup Tool

Skrip Python ini digunakan untuk mengecek daftar IP terhadap inventory lokal (`InvAllComputersSummary.csv`). Jika IP tidak ditemukan, skrip akan melakukan pencarian nama host menggunakan perintah `nslookup`. Hasil akhirnya disimpan dalam file CSV.

## 📂 Struktur File

```
project-folder/
│
├── input.csv                   # File input berisi IP dan host asal
├── InvAllComputersSummary.csv # Inventory IP dan nama komputer
├── nslookup_results.csv        # Hasil output dari pemrosesan
├── script.py                   # Skrip utama
└── README.md                   # Dokumentasi proyek
```

## 📥 Format File Input

### input.csv

| Host asal      | IP            |
|----------------|---------------|
| Server Olshop  | 192.168.1.10  |
| Server Email   | 192.168.1.99  |

### InvAllComputersSummary.csv

| IP Address     | Computer Name     |
|----------------|------------------|
| 192.168.1.10   | Komputer-Olshop  |
| 192.168.1.12   | Komputer-Akuntan |

## 📤 Format Output

### nslookup_results.csv

| Host Asal     | IP            | Status     | Computer Name     |
|---------------|---------------|------------|-------------------|
| Server Olshop | 192.168.1.10  | Found      | Komputer-Olshop   |
| Server Email  | 192.168.1.99  | Not found  | host-192-168-1-99 |

> Jika IP tidak ditemukan di inventory, maka dilakukan fallback ke `nslookup`. Jika gagal, akan ditandai `Not resolved`.

## 🚀 Cara Menggunakan

1. Siapkan `input.csv` dan `InvAllComputersSummary.csv` di direktori yang sama dengan skrip.
2. Jalankan skrip:
   ```bash
   python script.py
   ```
3. File hasil akan otomatis dibuat dengan nama `nslookup_results.csv`.

## ⚠️ Catatan

- Script hanya bekerja di sistem yang mendukung perintah `nslookup` (Windows, Linux, macOS).
- File inventory harus memiliki header `IP Address` dan `Computer Name`.
- Output menggunakan encoding UTF-8.







Copyright (c) 2025 Hyoka
Permission is granted to use, modify, and distribute this software for any purpose with or without fee.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

## Developed by Hyoka
