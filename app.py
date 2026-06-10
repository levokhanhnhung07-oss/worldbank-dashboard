import wbdata
import pandas as pd
import matplotlib.pyplot as plt

# Danh sách quốc gia
countries = {
    "Việt Nam": "VNM",
    "Mỹ": "USA",
    "Trung Quốc": "CHN",
    "Nhật Bản": "JPN",
    "Hàn Quốc": "KOR",
    "Đức": "DEU",
    "Pháp": "FRA",
    "Anh": "GBR"
}

print("Danh sách quốc gia:")
for i, country in enumerate(countries.keys(), start=1):
    print(f"{i}. {country}")

choice = int(input("\nChọn quốc gia: "))

country_name = list(countries.keys())[choice - 1]
country_code = countries[country_name]

# Chỉ số tăng trưởng GDP (%)
indicator = {
    'NY.GDP.MKTP.KD.ZG': 'GDP_Growth'
}

# Lấy dữ liệu
df = wbdata.get_dataframe(
    indicator,
    country=country_code,
    date=('2000', '2024')
)

df = df.sort_index()

print(df)

# Vẽ đồ thị
plt.figure(figsize=(12, 5))

plt.plot(
    df.index,
    df['GDP_Growth'],
    marker='o',
    linewidth=2
)

plt.title(
    f'Tăng trưởng GDP của {country_name} (2000-2024)',
    fontsize=15
)

plt.xlabel('Năm')
plt.ylabel('GDP Growth (%)')

plt.grid(True, linestyle='--', alpha=0.7)

for x, y in zip(df.index, df['GDP_Growth']):
    plt.text(x, y, f'{y:.2f}', fontsize=8)

plt.tight_layout()
plt.show()
