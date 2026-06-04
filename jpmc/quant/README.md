# Quantitative Research

Two of four tasks from JPMC's [Forage](https://www.theforage.com/simulations/jpmorgan/quantitative-research-11oc) quant research sim: forecast monthly natural gas prices, then price storage contracts from those estimates. Code and data live in this folder (`Nat_Gas.csv`, `Task1.py`, `Task2.py`).

[← Job Simulations](../../README.md)

---

## Task 1: Natural gas price forecasting

**The task.** Work from monthly end-of-month natural gas prices (roughly Oct 2020 through Sep 2024 in the provided CSV). Explore the series for patterns, build a model that returns a price for any date in range, and extrapolate about one year ahead for longer-dated storage quotes. [Official task on Forage ↗](https://www.theforage.com/simulations/jpmorgan/quantitative-research-11oc/task/1)

**How I solved it.** I plotted the history first to confirm clear yearly seasonality (winter demand vs. summer), then fit a SARIMA model with order `(1, 1, 1)` and seasonal order `(1, 1, 1, 12)` in `statsmodels`. `forecast_price()` projects the next 12 months; `plot_data()` overlays the forecast with a confidence band and prints the combined date/price table. For ad hoc dates, `estimate_price()` returns an exact monthly observation when the date matches the CSV, otherwise linear interpolation on ordinal dates across historical plus forecast points (with an out-of-range message if the date falls outside that span). The sim left model choice open; SARIMA was my pick for monthly seasonality rather than a simpler trend-only fit.

**Demo.** From this folder:

```bash
python Task1.py
```

Loads `Nat_Gas.csv`, fits the model, shows the chart, then prompts for a date (`YYYY-MM-DD`).

---

## Task 2: Storage contract pricing

**The task.** Build a prototype pricer for natural gas storage contracts: clients specify injection and withdrawal dates, volumes, and market parameters; the model should support manual review before anything production-grade. Assumptions in the brief included no transport lag, zero interest, and no holiday calendar. [Official task on Forage ↗](https://www.theforage.com/simulations/jpmorgan/quantitative-research-11oc/task/2)

**How I solved it.** `ContractPricingModel` pulls buy and sell prices from Task 1's `estimate_price()` on each leg. Per order, profit is `(sell − buy) × volume − transport_rate × volume − fixed storage_cost`. I track cumulative stored volume against `max_volume`, skip orders that would breach capacity or show negative per-order profit, and maintain a date ledger (cash out on injection, cash in on withdrawal). `calculate_contract_value()` walks sorted ledger dates and stops if the running client budget goes negative. `process_orders()` is interactive CLI over multiple legs, then prints total contract value when feasible. This is a prototype spread-and-costs model, not a full options-style storage optimizer.

**Demo.** From this folder (Task 1 model is initialized inside the script):

```bash
python Task2.py
```

Enter injection date, withdrawal date, and MMBtu per order; answer `yes`/`no` when asked for more orders.

---

## Setup

**Stack:** Python 3, pandas, numpy, statsmodels, matplotlib (`requirements.txt`).

```bash
cd jpmc/quant
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Files:** `Nat_Gas.csv` (monthly dates and prices), `Task1.py` (`NaturalGasPriceModel`), `Task2.py` (`ContractPricingModel`).

[View on Forage ↗](https://www.theforage.com/simulations/jpmorgan/quantitative-research-11oc)
