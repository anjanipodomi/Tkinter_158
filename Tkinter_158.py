import tkinter as tk  # Mengimpor modul tkinter dan memberinya alias 'tk'
from tkinter import messagebox  # Mengimpor kotak pesan dari tkinter untuk menampilkan peringatan

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    # Mengecek apakah ada input yang kosong
    for entry in entries:
        if entry.get() == "":  # Jika ada entry yang kosong
            messagebox.showwarning("Peringatan", "Semua nilai mata pelajaran harus diisi!")
            return  # Keluar dari fungsi jika ada input kosong

    # Jika semua input terisi, tampilkan hasil prediksi
    label_hasil.config(text="Prediksi Prodi: Teknologi Informasi")  # Menampilkan prediksi di label hasil

# Membuat jendela utama
root = tk.Tk()  # Inisialisasi objek utama jendela
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menetapkan judul jendela
root.geometry("400x500")  # Menentukan ukuran jendela

# Label judul
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16))  # Membuat label judul
label_judul.pack(pady=10)  # Memposisikan label judul dengan padding atas dan bawah 10

# Membuat frame untuk menampung input nilai
frame_input = tk.Frame(root)  # Membuat frame sebagai wadah untuk input nilai
frame_input.pack(pady=20)  # Memposisikan frame dengan padding vertikal 20

# Membuat 10 input nilai mata pelajaran
entries = []  # Menyimpan entri input nilai
for i in range(10):  # Mengulangi untuk membuat 10 entri
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i+1}")  # Label untuk setiap mata pelajaran
    label.grid(row=i, column=0, padx=5, pady=5)  # Memposisikan label pada grid
    entry = tk.Entry(frame_input)  # Membuat entri input
    entry.grid(row=i, column=1, padx=5, pady=5)  # Memposisikan entri input pada grid
    entries.append(entry)  # Menambahkan entri ke daftar entries

# Button untuk menampilkan hasil prediksi
btn_prediksi = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)  # Membuat tombol untuk hasil prediksi
btn_prediksi.pack(pady=10)  # Memposisikan tombol dengan padding vertikal 10

# Label untuk menampilkan hasil prediksi
label_hasil = tk.Label(root, text="", font=("Arial", 12))  # Membuat label kosong untuk hasil prediksi
label_hasil.pack(pady=10)  # Memposisikan label hasil dengan padding vertikal 10

# Menjalankan aplikasi
root.mainloop()  # Memulai loop utama aplikasi untuk menjalankan GUI
