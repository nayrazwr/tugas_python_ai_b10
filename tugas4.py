#Nama : Nayra Zanetti Windy Rahmantya

# ======================
# LIST
# ======================
print("=== LIST ===")

data = [10, "A", 20, "B", 30, "C"]

print("List awal:", data)
print("Elemen pertama:", data[0])
print("Elemen terakhir:", data[-1])
print("Slicing:", data[1:4])

# operasi
data.append("D")
data.insert(1, "Z")
data.extend([100, 200])
data.pop()
data.remove("A")

print("List setelah operasi:", data)


# ======================
# TUPLE
# ======================
print("\n=== TUPLE ===")

t = (1, 2, 3, 4, 5)

print("Tuple:", t)
print("Panjang:", len(t))
print("Index ke-2:", t[2])

a, b, *c = t
print("Unpacking:", a, b, c)


# ======================
# SET
# ======================
print("\n=== SET ===")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

# duplikat hilang
set_duplikat = {1, 1, 2, 2, 3}
print("Set tanpa duplikat:", set_duplikat)


# ======================
# DICTIONARY
# ======================
print("\n=== DICTIONARY ===")

mhs = {
    "nama": "Windy",
    "nim": "2308561041",
    "angkatan": 2023,
    "kota": "Denpasar"
}

# tambah & ubah
mhs["jurusan"] = "Informatika"
mhs["kota"] = "Bali"

# hapus
del mhs["angkatan"]

print("Keys:", mhs.keys())
print("Values:", mhs.values())
print("Items:", mhs.items())

for k, v in mhs.items():
    print(k, ":", v)


# ======================
# NESTED STRUCTURE
# ======================
print("\n=== NESTED STRUCTURE ===")

buku = [
    {"judul": "Alo Alo Bandung", "penulis": "X", "tahun": 2010},
    {"judul": "Balonku Ada 1", "penulis": "Y", "tahun": 2015},
    {"judul": "Cintaku Terhalang Agama", "penulis": "Z", "tahun": 2020},
    {"judul": "Diam-Diam Aku Diam", "penulis": "W", "tahun": 2022},
]

print("Judul buku:")
for b in buku:
    print(b["judul"])

# filter
buku_baru = [b for b in buku if b["tahun"] > 2015]
print("Buku setelah 2015:", buku_baru)


# ======================
# COMPREHENSION
# ======================
print("\n=== COMPREHENSION ===")

angka = list(range(1, 21))

genap = [x for x in angka if x % 2 == 0]
kuadrat = [x**2 for x in angka]

print("Genap:", genap)
print("Kuadrat:", kuadrat)

# dict comprehension
mapping = {x: "genap" if x % 2 == 0 else "ganjil" for x in range(1, 11)}
print("Mapping:", mapping)

# set comprehension
kalimat = "Aku Keren Sekali"
huruf_unik = {c.lower() for c in kalimat if c.isalpha()}
print("Huruf unik:", huruf_unik)


# ======================
# KEANGGOTAAN
# ======================
print("\n=== KEANGGOTAAN ===")

print("Apakah 10 ada di list?", 10 in data)
print("Posisi 'B':", data.index("B") if "B" in data else "Tidak ada")

print("Apakah 3 ada di set?", 3 in set1)