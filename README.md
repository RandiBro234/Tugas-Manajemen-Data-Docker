# Tugas 1: Analisis Quiz Mnajemen Data
# Tugas 2: Analisis Data Sederhana dengan Docker

Aplikasi Python Flask sederhana untuk mengunggah file CSV dan menghitung statistik deskriptif (mean, median, std).

## Cara Menjalankan

```bash
docker build -t statistik-app .
docker run -p 5000:5000 statistik-app
