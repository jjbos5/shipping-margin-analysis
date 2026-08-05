import matplotlib.pyplot as plt

def bleed_chart(free_bleed, paid_bleed):
    plt.bar(["Free lane", "Paid lane"], [free_bleed, paid_bleed])
    plt.title("Shipping Bleed by Lane")
    plt.ylabel("Net bleed ($)")
    plt.savefig("assets/bleed_breakdown.png")
    plt.close()

if __name__ == "__main__":
    bleed_chart(-95.0, -15.0)

def chart_bleed_by_year(bleed_series):
    plt.bar(bleed_series.index.astype(str), bleed_series.values)
    plt.title("Bleed by year")
    plt.xlabel("Years")
    plt.ylabel("Net bleed ($)")
    plt.savefig("assets/bleed_by_year.png")
    plt.close()
