#Nama : Nayra Zanetti Windy Rahmantya

import numpy as np
import pandas as pd

np.random.seed(42)

# ======================
# NUMPY
# ======================
print("=== NUMPY ===")

nilai = np.random.randint(50, 100, 10)

print("Nilai:", nilai)
print("Rata-rata:", np.mean(nilai))
print("Median:", np.median(nilai))
print("Std Dev:", np.std(nilai))
print("Min:", np.min(nilai))
print("Max:", np.max(nilai))


# ======================
# PANDAS
# ======================
print("\n=== PANDAS ===")

nama = ["Nayra", "Frans", "Firman", "Upi", "Elzan", "Jocelyn", "Amel", "Reza", "Kelin", "Ratna"]
nim = [101,102,103,104,105,106,107,108,109,110]

df = pd.DataFrame({
    "nama": nama,
    "nim": nim,
    "nilai": nilai
})

df["status"] = df["nilai"].apply(lambda x: "LULUS" if x >= 70 else "TIDAK LULUS")

print(df.head())


# ======================
# OOP
# ======================
class GradeBook:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def average(self) -> float:
        return self.df["nilai"].mean()

    def pass_rate(self, threshold: float = 70.0) -> float:
        return (self.df["nilai"] >= threshold).mean() * 100

    def save_summary(self, path: str):
        with open(path, "w") as f:
            f.write("=== RINGKASAN ===\n")
            f.write(f"Total Data: {len(self.df)}\n")
            f.write(f"Rata-rata: {self.average():.2f}\n")

            lulus = (self.df["status"] == "LULUS").sum()
            tidak = (self.df["status"] == "TIDAK LULUS").sum()

            f.write(f"Lulus: {lulus}\n")
            f.write(f"Tidak Lulus: {tidak}\n")

    def __str__(self):
        return f"Jumlah data: {len(self.df)}, Rata-rata: {self.average():.2f}"


# ======================
# DEMO
# ======================
if __name__ == "__main__":
    print("\n=== OOP: GRADEBOOK ===")

    gb = GradeBook(df)

    print(gb)
    print("Average:", gb.average())
    print("Pass Rate:", gb.pass_rate())

    gb.save_summary("ringkasan_tugas6.txt")