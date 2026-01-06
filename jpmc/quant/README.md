# JPMC Quantitative Research: Natural Gas Price Prediction

Financial modeling and time series analysis project for natural gas price prediction and contract pricing. This project demonstrates quantitative finance skills including statistical modeling, forecasting, and contract valuation.

## Project Overview

This project consists of two main tasks focused on natural gas commodity pricing:
1. **Time Series Forecasting**: Building a SARIMA model to predict natural gas prices
2. **Contract Pricing Model**: Creating a pricing system for natural gas storage contracts with multiple injection/withdrawal dates

**Note**: This project was part of a guided virtual experience program. The task requirements and data were provided; this documentation focuses on the implementation and modeling approaches used.

## Tech Stack

- **Python 3.x**
- **pandas**: Data manipulation and time series handling
- **numpy**: Numerical computations
- **statsmodels**: SARIMA time series modeling
- **matplotlib**: Data visualization

## Task Status

### ✅ Task 1: Natural Gas Price Prediction Model

**Status**: Completed

**Objective**: Analyze historical natural gas price data and create a forecasting model to predict prices for any date within a year in the future.

**Implementation Details**:

- **Data Loading**: Monthly natural gas price data from October 2020 to September 2024
- **Model Selection**: SARIMA (Seasonal AutoRegressive Integrated Moving Average) model
  - ARIMA order: `(1, 1, 1)` for trend component
  - Seasonal order: `(1, 1, 1, 12)` to capture monthly seasonality
- **Forecasting**: Generates 12-month price forecasts beyond historical data
- **Interpolation**: Estimates prices for any date between historical and forecasted periods using linear interpolation
- **Visualization**: Creates plots showing historical prices, forecasted prices, and confidence intervals

**Key Features**:
- Price estimation for historical dates (exact lookup)
- Price forecasting for future dates (12 months ahead)
- Date interpolation for dates between known points
- Visual representation of price trends and forecasts

### ✅ Task 2: Contract Pricing Model

**Status**: Completed

**Objective**: Create a pricing model for natural gas storage contracts that handles multiple injection and withdrawal dates with associated costs.

**Implementation Details**:

- **Contract Parameters**:
  - Storage costs (fixed)
  - Transport rate (variable cost per MMBtu)
  - Maximum storage volume
  - Injection dates (when gas is purchased and stored)
  - Withdrawal dates (when gas is sold from storage)
  
- **Pricing Logic**:
  - Calculates buy price at injection date using Task 1's price model
  - Calculates sell price at withdrawal date
  - Computes profit margin: `(sell_price - buy_price) * amount`
  - Accounts for transport costs: `transport_rate * amount`
  - Includes fixed storage costs per order
  
- **Order Management**:
  - Validates storage capacity constraints
  - Rejects unprofitable orders (negative profit)
  - Maintains ledger of cash flows by date
  - Tracks client budget and warns of insufficient funds
  
- **Contract Valuation**:
  - Calculates total contract value across all orders
  - Validates sufficient funds for all scheduled transactions
  - Returns -1 if client cannot afford the contract timeline

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
