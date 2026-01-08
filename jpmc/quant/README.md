# JPMC Quantitative Research: Natural Gas Price Prediction

Quantitative research project focused on natural gas commodity price analysis and storage contract pricing. This project involves analyzing monthly price data, creating forecasting models, and developing a prototype pricing model for storage contracts.

## Project Overview

This project consists of two main tasks:
1. **Commodity Price Prediction**: Analyze monthly natural gas price data and create a model to estimate prices at any date, with extrapolation for one year into the future
2. **Contract Pricing Model**: Create a prototype pricing model for natural gas storage contracts that considers injection/withdrawal dates, rates, storage costs, and capacity constraints

**Note**: This project was part of a guided virtual experience program. The task requirements and data were provided; this documentation focuses on the implementation and modeling approaches used.

## Tech Stack

- **Python 3.x**
- **pandas**: Data manipulation and time series handling
- **numpy**: Numerical computations
- **statsmodels**: SARIMA time series modeling
- **matplotlib**: Data visualization

## Task Status

### ✅ Task 1: Commodity Price Prediction

**Status**: Completed

**Objective**: Analyze monthly natural gas price data and create a model to estimate prices at any date in the past and extrapolate for one year into the future.

**Task Description**: 
The task involves working with monthly snapshots of natural gas prices from a market data provider, representing the market price of natural gas delivered at the end of each calendar month. This data is available for roughly the next 18 months and is combined with historical prices.

**Implementation**:
- Analyzed monthly natural gas price data from October 31, 2020 to September 30, 2024
- Created a model that takes a date as input and returns a price estimate
- Implemented extrapolation for one year into the future for longer-term storage contract pricing
- Added visualization to identify patterns and seasonal trends in price data
- Used SARIMA time series model for forecasting and linear interpolation for date-based price estimates

### ✅ Task 2: Contract Pricing Model

**Status**: Completed

**Objective**: Create a prototype pricing model for natural gas storage contracts that can be used with manual oversight to explore options with clients.

**Task Description**: 
The model is a prototype that will go through further validation and testing before being put into production. Eventually, it may be the basis for fully automated quoting to clients, but for now, it's used with manual oversight.

**Implementation**:
- **Pricing Function**: Takes multiple injection and withdrawal dates with set amounts of gas
- **Input Parameters**:
  - Injection dates: Dates when gas is injected
  - Withdrawal dates: Dates when gas is withdrawn
  - Prices: Prices at which the commodity can be purchased/sold on those dates (using Task 1's price model)
  - Injection/Withdrawal rate: Rate at which gas can be injected/withdrawn
  - Maximum volume: Maximum volume that can be stored
  - Storage costs: Costs associated with storing the gas
- **Function Output**: Returns the value of the contract
- **Assumptions**: No transport delay, zero interest rates, market holidays/weekends/bank holidays not accounted for
- Includes testing with sample inputs to validate the pricing logic

## Project Structure

```
jpmc/quant/
├── README.md
├── requirements.txt
├── Nat_Gas.csv              # Historical natural gas price data
├── Task1.py                 # Natural gas price prediction model
└── Task2.py                 # Contract pricing model
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Navigate to the project directory:
```bash
cd jpmc/quant
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Task 1: Price Prediction Model

Run the price prediction model:
```bash
python Task1.py
```

The script will:
1. Load historical data from `Nat_Gas.csv`
2. Fit the SARIMA model to the data
3. Generate 12-month forecasts
4. Display a plot showing historical and forecasted prices
5. Prompt you to enter a date to estimate the price

**Example Usage**:
```python
from Task1 import NaturalGasPriceModel

# Initialize and load the model
model = NaturalGasPriceModel('Nat_Gas.csv')
model.load_data()
model.fit_model()
model.forecast_price()

# Estimate price for a specific date
price = model.estimate_price('2024-12-15')
print(f"Estimated price: ${price}")
```

**Key Methods**:
- `load_data()`: Loads and parses the CSV data
- `fit_model()`: Trains the SARIMA model on historical data
- `forecast_price()`: Generates 12-month price forecasts
- `plot_data()`: Visualizes historical and forecasted prices
- `estimate_price(date_str)`: Returns price estimate for any date (YYYY-MM-DD format)

### Task 2: Contract Pricing Model

Run the contract pricing model:
```bash
python Task2.py
```

The script will:
1. Initialize the contract pricing model with market parameters
2. Load and fit the price prediction model from Task 1
3. Prompt you to enter contract orders interactively:
   - Injection date (when to buy gas)
   - Withdrawal date (when to sell gas)
   - Amount to purchase (in MMBtu)
4. Validate each order (storage capacity, profitability)
5. Calculate total contract value after all orders

**Example Usage**:
```python
from Task1 import NaturalGasPriceModel
from Task2 import ContractPricingModel

# Setup price model
model = NaturalGasPriceModel('Nat_Gas.csv')
model.load_data()
model.fit_model()
model.forecast_price()

# Setup contract pricing with market parameters
storage_cost = 100000  # Fixed storage cost
transport_rate = 0.1   # Cost per MMBtu to transport
max_volume = 1000000   # Maximum storage capacity

contract_model = ContractPricingModel(
    storage_cost, transport_rate, max_volume, model
)

# Price a single order
profit = contract_model.price_order(
    injection_date='2024-06-01',
    withdrawal_date='2024-12-01',
    amount=50000
)
print(f"Expected profit: ${profit}")
```

**Key Methods**:
- `price_order(injection_date, withdrawal_date, amount)`: Prices a single order and returns profit
- `process_orders()`: Interactive method to process multiple orders
- `calculate_contract_value()`: Calculates total contract value and validates budget

## Data Format

The `Nat_Gas.csv` file contains monthly natural gas price data with the following structure:
- **Dates**: End-of-month dates from October 2020 to September 2024
- **Prices**: Market price of natural gas for delivery at the end of each calendar month

## Key Skills Demonstrated

- **Time Series Analysis**: SARIMA modeling for forecasting with seasonality
- **Financial Modeling**: Contract pricing with multiple cash flows
- **Statistical Forecasting**: 12-month ahead predictions with confidence intervals
- **Data Interpolation**: Linear interpolation for date-based price estimates
- **Risk Management**: Budget validation and capacity constraints
- **Data Visualization**: Time series plots with historical and forecasted data

## Model Details

### SARIMA Model Parameters

The SARIMA model uses:
- **Order (p, d, q)**: `(1, 1, 1)`
  - `p=1`: One autoregressive term
  - `d=1`: First-order differencing for stationarity
  - `q=1`: One moving average term

- **Seasonal Order (P, D, Q, m)**: `(1, 1, 1, 12)`
  - `P=1`: One seasonal autoregressive term
  - `D=1`: First-order seasonal differencing
  - `Q=1`: One seasonal moving average term
  - `m=12`: Monthly seasonality (12 periods per year)

### Pricing Model Assumptions

- No transport delays (instantaneous injection/withdrawal)
- Zero interest rates
- Market holidays and weekends are not accounted for
- Fixed storage cost per order
- Linear transport cost per unit volume

## Limitations and Future Improvements

- Model assumes stationarity after differencing; may need refinement for longer-term forecasts
- Linear interpolation may not capture all price dynamics between data points
- Contract pricing model uses simple profit calculation; could incorporate more sophisticated financial metrics
- No validation for unrealistic dates or edge cases in user input

---

*This project is part of the J.P. Morgan Chase Quantitative Research Virtual Experience program.*
