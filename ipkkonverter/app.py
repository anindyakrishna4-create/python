import streamlit as st

def main():
    st.title("Aplikasi Konversi Nilai")
    st.markdown("Masukkan nilai Anda (0-100) untuk mengetahui hasilnya.")

    # 1. Input Nilai menggunakan Streamlit
    # min_value dan max_value digunakan sebagai batasan awal
    nilai = st.number_input(
        "Masukkan nilai Anda:",
        min_value=0.0,
        max_value=100.0,
        value=50.0,  # Nilai default
        step=0.01    # Langkah input
    )

    # st.button untuk memicu logika, jika nilai sudah dimasukkan
    if st.button("Cek Nilai"):
        hasil = ""

        # 2. Logika Penilaian
        # Cek nilai tidak valid (di luar rentang 0-100)
        if nilai > 100 or nilai < 0:
            hasil = "Nilai Anda **TIDAK VALID** (di luar rentang 0-100)"
            st.error(hasil)  # Tampilkan sebagai pesan error
        # Cek Nilai A (85-100)
        elif nilai >= 85:
            hasil = "Nilai Anda **A** (Sangat Baik)"
            st.success(hasil) # Tampilkan sebagai pesan sukses/terbaik
        # Cek Nilai B (70-84.99...)
        elif nilai >= 70:
            hasil = "Nilai Anda **B** (Baik)"
            st.info(hasil) # Tampilkan sebagai pesan info
        # Cek Nilai C (55-69.99...)
        elif nilai >= 55:
            hasil = "Nilai Anda **C** (Cukup)"
            st.info(hasil)
        # Cek Nilai D (40-54.99...)
        elif nilai >= 40:
            hasil = "Nilai Anda **D** (Kurang)"
            st.warning(hasil) # Tampilkan sebagai pesan warning
        # Sisanya adalah Nilai E (0-39.99...)
        else:
            hasil = "Nilai Anda **E** (Gagal)"
            st.error(hasil) # Tampilkan sebagai pesan error

if __name__ == "__main__":
    main()
