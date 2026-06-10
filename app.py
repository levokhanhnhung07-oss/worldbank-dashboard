import streamlit as st
import wbdata
import matplotlib.pyplot as plt

st.title("📊 World Bank Data Viewer")

countries = {
    "Vietnam": "VNM",
    "United States": "USA",
    "China": "CHN",
    "Japan": "JPN",
    "South Korea": "KOR"
}

indicators = {
    "GDP Growth (%)": "NY.GDP.MKTP.KD.ZG",
    "Population": "SP.POP.TOTL",
    "Inflation (%)": "FP.CPI.TOTL.ZG",
    "Unemployment (%)": "SL.UEM.TOTL.ZS"
}

country = st.selectbox(
    "Chọn quốc gia",
    list(countries.keys())
)

indicator_name = st.selectbox(
    "Chọn chỉ số",
    list(indicators.keys())
)

if st.button("Hiển thị biểu đồ"):

    data = wbdata.get_dataframe(
        {indicators[indicator_name]: "Value"},
        country=countries[country],
        date=("2000", "2024")
    )

    data = data.sort_index()

    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        data.index,
        data["Value"],
        marker="o"
    )

    ax.set_title(
        f"{indicator_name} - {country}"
    )

    ax.grid(True)

    st.pyplot(fig)

    st.dataframe(data)
