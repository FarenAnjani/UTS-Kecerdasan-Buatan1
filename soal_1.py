# -*- coding: utf-8 -*-
"""Soal_1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1e_eBNRG0wrWU3j_7PJzxNCgE13Wdu3dC
"""

def deteksi_hama(gejala):
    if "daun menguning" in gejala:
        return "Kuning"
    elif "bercak hitam" in gejala:
        return "Hitam"
    elif "daun berlubang" in gejala:
        return "Ulat"
    elif "tanaman layu" in gejala:
        return "Bakteri"
    else:
        return "Tidak diketahui"

# Contoh input gejala
gejala_input = ["daun menguning", "daun berlubang"]

for g in gejala_input:
    print(f"gejala: {g} -> diagnosis {deteksi_hama(g)}")

"""1. Kasus:
 Seorang Petani ingin sistem AI yang bisa membantu menentukan jenis hama tanaman berdasarkan gejala seperti berikut:
 1. Daun menguning
 2. Terdapat bercak hitam
 3. Daun berlubang
 4. Tanaman layu

Jawaban:
1. IF - THEN RULES
* IF daun menguning THEN hama kuning
* IF terdapat bercak hitam THEN hama hitam
* IF daun berlubang THEN hama ulat
* IF tanaman layu THEN bakteri tanaman

2. Logika Proposisional
* P1: Daun menguning
* P2: Terdapat bercak hitam
* P3: Daun berlubang
* P4: Tanaman layu
* H1: Serangan Kuning
* H2: Serangan Hitam
* H3: Serangan Ulat
* H4: Serangan Bakteri

1. P1 -> H1 (jika daun menguning, maka kemungkinan sernagan kuning)
2. P2 -> H2 (jika terdapat bercak hitam, maka kemungkinan serangan hitam)
3. P3 -> H3 (jika daun berlubang, maka kemungkinan serangan ulat)
4. P4 -> H4 (jika tanaman layu, maka kemungkinan serangan bakteri)
5. (
𝑃
1
∧
𝑃
2
)
→
(
𝐻
1
∧
𝐻
2
)
(P
1
​
 ∧P
2
​
 )→(H
1
​
 ∧H
2
​
 )
(Jika daun menguning dan terdapat bercak luka, maka ada kemungkinan serangan virus kuning dan jamur.)

6. (
𝑃
4
∧
¬
𝑃
1
∧
¬
𝑃
2
∧
¬
𝑃
3
)
→
𝐻
4
(P
4
​
 ∧¬P
1
​
 ∧¬P
2
​
 ∧¬P
3
​
 )→H
4
​

(Jika tanaman layu dan tidak ada gejala lain, maka kemungkinan besar serangan bakteri.)

3. Penjelasan Sistem Inferensi:

Input: Data gejala dari tanaman.

Inferensi: Sistem akan memeriksa aturan secara berurutan, dan mencocokkan gejala yang diberikan dengan aturan yang ada (rule-based inference menggunakan forward chaining).

Output: Diagnosis hama atau penyakit tanaman.


"""