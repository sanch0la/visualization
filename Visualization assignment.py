import numpy as np
import matplotlib.pyplot as plt

def prepare_country_data(years, area, yld, prod):
    return {
        "Year": np.array(years),
        "Area harvested": np.array(area),
        "Yield": np.array(yld),
        "Production": np.array(prod),
    }

def plot_scatter(country_data: dict, country: str):
    plt.figure(figsize=(8, 5))
    plt.scatter(country_data["Year"], country_data["Yield"], color="green", marker="o")
    plt.title(f"Yield of Cocoa in {country}")
    plt.xlabel("Year")
    plt.ylabel("Yield (hg/ha)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()

def plot_bar(country_data: dict, country: str):
    plt.figure(figsize=(10, 6))
    plt.bar(country_data["Year"], country_data["Area harvested"], color="saddlebrown")
    plt.title(f"Area Harvested of Cocoa in {country}")
    plt.xlabel("Year")
    plt.ylabel("Area Harvested (ha)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    ghana = prepare_country_data(
        years=[2018, 2019, 2020, 2021, 2022],
        area=[1500000, 1520000, 1550000, 1570000, 1600000],
        yld=[450, 470, 460, 480, 490],
        prod=[675000, 714400, 713000, 753600, 784000]
    )

    ivory_coast = prepare_country_data(
        years=[2018, 2019, 2020, 2021, 2022],
        area=[2200000, 2250000, 2300000, 2320000, 2350000],
        yld=[500, 520, 510, 530, 540],
        prod=[1100000, 1170000, 1173000, 1230000, 1269000]
    )

    print("Ghana Cocoa Data:")
    for i in range(len(ghana["Year"])):
        print(ghana["Year"][i], ghana["Area harvested"][i], ghana["Yield"][i], ghana["Production"][i])

    print("\nIvory Coast Cocoa Data:")
    for i in range(len(ivory_coast["Year"])):
        print(ivory_coast["Year"][i], ivory_coast["Area harvested"][i], ivory_coast["Yield"][i], ivory_coast["Production"][i])

    plot_scatter(ghana, "Ghana")
    plot_bar(ghana, "Ghana")
    plot_scatter(ivory_coast, "Ivory Coast")
    plot_bar(ivory_coast, "Ivory Coast")

if __name__ == "__main__":
    main()
