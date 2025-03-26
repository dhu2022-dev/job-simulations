from Task1 import NaturalGasPriceModel
import pandas as pd

class ContractPricingModel:
    def __init__(self, storage_cost, transport_rate, max_volume, model):
        self.storage_cost = storage_cost
        self.transport_rate = transport_rate
        self.max_volume = max_volume
        self.model = model
        self.order_dict = {}
        self.current_stored = 0
        self.client_budget = 100000000

    def price_order(self, injection_date, withdrawal_date, amount):
        # Get buy price for the injection date
        buy_price = self.model.estimate_price(injection_date)
        sell_price = self.model.estimate_price(withdrawal_date)

        # Calculate profit
        revenue_margin = sell_price - buy_price
        revenue = revenue_margin * amount
        transport_cost = self.transport_rate * amount
        profit = revenue - transport_cost - self.storage_cost

        # Update current storage and ledger
        self.current_stored += amount
        self._update_ledger(injection_date, withdrawal_date, buy_price, sell_price, amount, transport_cost)

        return profit

    def _update_ledger(self, injection_date, withdrawal_date, buy_price, sell_price, amount, transport_cost):
        """Update ledger with net revenue or cost by date, reflecting the balance of gas bought and sold."""
        # Convert dates to datetime objects
        injection_date = pd.to_datetime(injection_date)
        withdrawal_date = pd.to_datetime(withdrawal_date)

        # Total cost for injection date (buy price + transport + storage)
        injection_total_cost = (buy_price * amount) + transport_cost + self.storage_cost

        # Total revenue for withdrawal date (sell price * amount)
        withdrawal_revenue = sell_price * amount

        # Update ledger: on injection date, subtract the total cost (costs are negative)
        if injection_date in self.order_dict:
            self.order_dict[injection_date] -= injection_total_cost
        else:
            self.order_dict[injection_date] = -injection_total_cost

        # Update ledger: on withdrawal date, add the revenue (revenue is positive)
        if withdrawal_date in self.order_dict:
            self.order_dict[withdrawal_date] += withdrawal_revenue
        else:
            self.order_dict[withdrawal_date] = withdrawal_revenue

    def process_orders(self):
        """Process orders from user input."""
        while True:
            # Get order parameters from client
            injection_date = input("Enter the client's desired injection date (YYYY-MM-DD): ")
            withdrawal_date = input("Enter the client's withdrawal date (YYYY-MM-DD): ")
            amount = float(input("How much (in MMBtu) would the client like to purchase? "))

            # Check if the order exceeds storage capacity
            if (self.current_stored + amount) > self.max_volume:
                print("This order would exceed storage capacity. Order canceled. Try again.")
                continue

            # Calculate order price and check if it is profitable
            order_price = self.price_order(injection_date, withdrawal_date, amount)
            if order_price < 0:
                print("This order will lose the client money. Order canceled. Try again.")
                continue

            print("Placing an order.")
            response = input("Are there more orders to place? (yes/no): ").strip().lower()
            if response != "yes":
                print("No more orders to place. Exiting.")
                break

    def calculate_contract_value(self):
        """Calculate the total contract value based on all orders."""
        sorted_keys = sorted(self.order_dict.keys())
        contract_value = 0
        for key in sorted_keys:
            self.client_budget += self.order_dict[key]  # Update client budget with net cash flow on each date
            contract_value += self.order_dict[key]
            if self.client_budget < 0:
                print(f"Your client will have insufficient funds to execute the orders occurring on: {key}")
                return -1
        
        return contract_value

def main():
    # Market fees for the sake of example
    storage_cost = 100000  # Fixed cost
    transport_rate = 0.1  # Variable cost (cost to transport 1 MMBtu of Nat Gas)
    max_volume = 1000000  # Maximum volume that can be stored at a time

    # Create an instance of the natural gas price model (from Task1)
    model = NaturalGasPriceModel('Nat_Gas.csv')
    model.load_data()
    model.fit_model()
    model.forecast_price()

    # Create the contract pricing model
    contract_model = ContractPricingModel(storage_cost, transport_rate, max_volume, model)

    # Process orders and calculate the total contract value
    contract_model.process_orders()
    contract_value = contract_model.calculate_contract_value()

    if contract_value != -1:
        print(f"The total value of the contract is: {contract_value}")

if __name__ == "__main__":
    main()