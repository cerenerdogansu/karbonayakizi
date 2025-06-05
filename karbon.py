import streamlit as st

st.set_page_config(page_title="Karbon Ayak İzi Hesaplayıcı 🌱", page_icon="🌍")

st.title("🌍 Karbon Ayak İzi Hesaplayıcı")
st.markdown("Dünya Çevre Günü için küçük bir farkındalık adımı atalım. Günlük alışkanlıklarınızın doğaya etkisini keşfedin.")

st.sidebar.header("Verilerinizi Girin")

km = st.sidebar.slider("Günde araba ile kaç km yol kat ediyorsunuz?", 0, 100, 10)
et = st.sidebar.slider("Haftada kaç gün kırmızı et tüketiyorsunuz?", 0, 7, 3)
elektrik = st.sidebar.number_input("Aylık elektrik faturanız (TL)", min_value=0.0, value=150.0)

karbon_km = km * 0.21 * 30
karbon_et = et * 2.5 * 4
karbon_elektrik = elektrik * 0.5
toplam_karbon = karbon_km + karbon_et + karbon_elektrik

st.subheader("🌿 Sonuçlar")
st.write(f"**Toplam Aylık Karbon Ayak İzi:** `{toplam_karbon:.2f} kg CO₂`")

if toplam_karbon > 500:
    st.warning("⚠️ Karbon ayak iziniz yüksek! Sürdürülebilir yaşam alışkanlıkları edinmeye ne dersiniz?")
else:
    st.success("✅ Karbon ayak iziniz ortalamanın altında. Harika bir başlangıç!")

st.markdown("---")
st.markdown("### 💡 Sürdürülebilirlik İpuçları")
st.markdown("""
- 🚶 Mümkünse yürüyün veya bisiklet kullanın  
- 🥦 Bitki bazlı öğünleri artırın  
- 💡 Enerji tasarruflu ampuller tercih edin  
- 🔌 Elektronik cihazları kullanmadığınızda prizden çekin  
""")

st.markdown("---")
st.caption("Hazırlayan: Ceren Erdoğan | #DünyaÇevreGünü #Python #Streamlit #YBS")
