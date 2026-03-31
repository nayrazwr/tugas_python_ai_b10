#Nama : Nayra Zanetti Windy Rahmantya

# ======================
# 1. VARIABEL & TIPE DATA
# ======================
print("=== VARIABEL ===")

nama = "Naaay"          # string
umur = 16              # integer
tinggi = 150         # float
is_mahasiswa = True    # boolean
hobi = ["makan", "tidur", "gawe"]  # list

print(f"{nama} {umur} {tinggi} {is_mahasiswa} {hobi}")


# ======================
# 2. MANIPULASI STRING
# ======================
print("\n=== STRING ===")

teks = "nayra keren luar biasa"

print("Asli:", teks)
print("Gabung:", teks + " mantap")
print("Panjang:", len(teks))
print("Upper:", teks.upper())
print("Lower:", teks.lower())


# ======================
# 3. OPERASI MATEMATIKA
# ======================
print("\n=== MATEMATIKA ===")

a = 10
b = 5

print("Tambah:", a + b)
print("Kurang:", a - b)
print("Kali:", a * b)
print("Bagi:", a / b)
print("Modulus:", a % b)
print("Pangkat:", a ** b)


# ======================
# 4. LIST
# ======================
print("\n=== LIST ===")

data = [1, 2, 3, 4, 5]

print("List awal:", data)
print("Elemen ke-2:", data[1])

data.append(6)
print("Setelah append:", data)

data.remove(3)
print("Setelah remove:", data)


# ======================
# 5. INPUT USER
# ======================
print("\n=== INPUT USER ===")

nama_user = input("Masukkan nama: ")
hobi_user = input("Masukkan hobi: ")

print(f"Halo, saya {nama_user} dan hobi saya {hobi_user}.")