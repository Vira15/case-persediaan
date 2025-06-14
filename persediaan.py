import streamlit as st
import math

st.title("📦 Model Persediaan Tahunan - EOQ (Economic Order Quantity)")

st.markdown("""
Model EOQ digunakan untuk menentukan jumlah pemesanan optimal yang meminimalkan total biaya persediaan.
""")

# Input user
D = st.number_input("Permintaan tahunan (unit/tahun)", min_value=1.0, value=1000.0)
S = st.number_input("Biaya pemesanan per kali (Rp)", min_value=0.0, value=50000.0)
H = st.number_input("Biaya penyimpanan per unit per tahun (Rp)", min_value=0.0, value=1000.0)

if st.button("📊 Hitung EOQ"):
    if H == 0:
        st.error("❌ Biaya penyimpanan tidak boleh nol.")
    else:
        eoq = math.sqrt((2 * D * S) / H)
        frekuensi_pemesanan = D / eoq
        total_biaya_pemesanan = S * frekuensi_pemesanan
        total_biaya_penyimpanan = (eoq / 2) * H
        total_biaya_persediaan = total_biaya_pemesanan + total_biaya_penyimpanan

        st.success("✅ Hasil Perhitungan:")
        st.write(f"Jumlah EOQ optimal: *{eoq:.2f} unit*")
        st.write(f"Frekuensi pemesanan per tahun: *{frekuensi_pemesanan:.2f} kali*")
        st.write(f"Total biaya pemesanan: *Rp {total_biaya_pemesanan:,.2f}*")
        st.write(f"Total biaya penyimpanan: *Rp {total_biaya_penyimpanan:,.2f}*")
        st.write(f"Total biaya persediaan tahunan: *Rp {total_biaya_persediaan:,.2f}*")