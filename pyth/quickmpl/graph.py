import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd

class Person:
    def __init__(self, csv_file):
        data = pd.read_csv(csv_file)
        data["Date Received"] = pd.to_datetime(data["Date Received"])
        data.sort_values("Date Received", inplace=True)

        self.dates = data["Date Received"]
        self.money = data["Accumulation of Contributions"]
    
    def graph(self) -> None:
        """graphs time series data of {person}'s contributer's contributions over dates"""
        plt.plot_date(self.dates, self.money, linestyle="solid")
        plt.gcf().autofmt_xdate()
        
        date_format = mpl_dates.DateFormatter("%b, %d %Y")
        plt.gca().xaxis.set_major_formatter(date_format)

        plt.title("Accumulated Financial Contributions over Run")
        plt.xlabel("Timespan")
        plt.ylabel("Accumulated Money ($)")
        
        plt.tight_layout()
        plt.show()

Santos_Rowena = Person("SRStats.csv")

Santos_Rowena.graph()
