import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.statespace.sarimax import SARIMAX

class NaturalGasPriceModel:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.dates = None
        self.prices = None
        self.future_dates = None
        self.forecast_prices = None
        self.model = None
        self.forecast = None

    def load_data(self):
        # Load the data
        data = pd.read_csv(self.csv_file, parse_dates=['Dates'])
        self.dates = pd.to_datetime(data['Dates'])
        self.prices = data['Prices']

    def fit_model(self):
        # Fit SARIMA model
        sarima_model = SARIMAX(self.prices, 
                            order=(1, 1, 1),            # ARIMA(p, d, q)
                            seasonal_order=(1, 1, 1, 12),  # Seasonal ARIMA(P, D, Q, m)
                            enforce_stationarity=False, 
                            enforce_invertibility=False)
        self.model = sarima_model.fit()

    def forecast_price(self):
        # Forecast the next 12 months
        forecast = self.model.get_forecast(steps=12)
        self.forecast_prices = forecast.predicted_mean
        self.forecast = forecast

        # Generate future dates for the next 12 months
        self.future_dates = pd.date_range(start=self.dates.iloc[-1] + pd.DateOffset(months=1), periods=12, freq='M')

    def plot_data(self):
        forecast_conf_int = self.forecast.conf_int()

        # Plot historical and forecasted data
        plt.figure(figsize=(10, 6))
        plt.plot(self.dates, self.prices, label='Historical Prices')
        plt.plot(self.future_dates, self.forecast_prices, label='Predicted Prices (Next 12 Months)', linestyle='--')
        plt.fill_between(self.future_dates, forecast_conf_int.iloc[:, 0], forecast_conf_int.iloc[:, 1], color='gray', alpha=0.2)

        # Connect the last historical price to the first predicted price
        plt.plot([self.dates.iloc[-1], self.future_dates[0]], [self.prices.iloc[-1], self.forecast_prices.iloc[0]], 'k--', label='Transition Line')

        # Add title and labels
        plt.title('Natural Gas Price Prediction using SARIMA (statsmodels)')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.show()

        # Concatenate historical and forecasted data
        combined_dates = pd.concat([self.dates, pd.Series(self.future_dates)], ignore_index=True)
        combined_prices = pd.concat([self.prices, pd.Series(self.forecast_prices)], ignore_index=True)

        # Create a DataFrame with the combined data
        result_table = pd.DataFrame({
            'Date': combined_dates,
            'Price': combined_prices
        })

        # Print the table of dates and prices
        print("\nDates and Prices displayed in the plot:\n", result_table)

    def estimate_price(self, date_str):
        date = pd.to_datetime(date_str)

        # Define the full range of dates
        full_range_start = self.dates.iloc[0]
        full_range_end = self.future_dates[-1]

        if date < full_range_start or date > full_range_end:
            return (f"Your inputted date {date.date()} is out of range ({full_range_start.date()} to {full_range_end.date()}). "
                    "Please enter a date within the range.")

        # Check for exact historical price
        if date in self.dates.values:
            historical_price = self.prices[self.dates == date].values[0]
            return historical_price

        # Prepare extended data
        extended_dates = pd.concat([pd.Series(self.dates), pd.Series(self.future_dates)])
        extended_prices = pd.concat([pd.Series(self.prices), pd.Series(self.forecast_prices)])

        # Drop duplicates and align prices
        extended_dates = extended_dates.drop_duplicates().reset_index(drop=True)
        extended_prices = extended_prices.reindex(extended_dates.index).reset_index(drop=True)
        extended_prices = extended_prices.fillna(method='ffill')

        # Convert dates to ordinal values
        extended_dates_numeric = extended_dates.map(pd.Timestamp.toordinal)
        target_date_numeric = date.toordinal()

        # Perform interpolation
        if target_date_numeric < extended_dates_numeric.min() or target_date_numeric > extended_dates_numeric.max():
            return "Date is out of interpolation bounds."

        interpolated_price = np.interp(target_date_numeric, extended_dates_numeric, extended_prices)
        return round(interpolated_price, 2)


        
def main():
    model = NaturalGasPriceModel('Nat_Gas.csv')
    model.load_data()
    model.fit_model()
    model.forecast_price()
    model.plot_data()
    client_date = input("Enter a date to predict on within a year. (YYYY-MM-DD): ")
    print(model.estimate_price(client_date))

main()