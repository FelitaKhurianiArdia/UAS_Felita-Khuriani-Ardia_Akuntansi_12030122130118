import pandas as pd
import matplotlib.pyplot as plt

# Membaca data dari file CSV dengan pemisah titik koma
data = pd.read_csv('Datapenjualan.csv', delimiter=';')

# Menampilkan 5 baris pertama dari dataset
print("5 Baris Pertama dari Dataset:")
print(data.head())

# Fungsi untuk menghilangkan koma dari string dan mengonversinya ke integer
def remove_commas_and_convert(value):
    return int(value.replace(',', ''))

# Menghilangkan koma dan mengonversi kolom penjualan ke integer
data['Total Penjualan Kalung (Rp)'] = data['Total Penjualan Kalung (Rp)'].apply(remove_commas_and_convert)
data['Total Penjualan Gelang (Rp)'] = data['Total Penjualan Gelang (Rp)'].apply(remove_commas_and_convert)
data['Total Penjualan Anting (Rp)'] = data['Total Penjualan Anting (Rp)'].apply(remove_commas_and_convert)

# Membuat diagram garis untuk jumlah barang terjual per bulan
plt.figure(figsize=(12, 6))

# Plot untuk kalung
plt.plot(data['Bulan'], data['Jumlah Kalung Terjual'], marker='o', linestyle='-', color='r', label='Kalung')

# Plot untuk gelang
plt.plot(data['Bulan'], data['Jumlah Gelang Terjual'], marker='o', linestyle='-', color='g', label='Gelang')

# Plot untuk anting
plt.plot(data['Bulan'], data['Jumlah Anting Terjual'], marker='o', linestyle='-', color='b', label='Anting')

# Menambahkan label dan judul
plt.xlabel('Bulan', fontweight='bold')
plt.ylabel('Jumlah Terjual', fontweight='bold')
plt.xticks(rotation=45)
plt.title('Tren Penjualan Barang per Bulan')

# Menambahkan legenda
plt.legend()

# Menampilkan diagram garis
plt.tight_layout()
plt.grid(True)
plt.show()
