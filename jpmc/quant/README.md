# David Hu JPMC Quant Job Sim Code Description + Instructions Given

## Task 1 (Commodity Price Prediction)

After asking around for the source of the existing data, you learn that the current process is to take a monthly snapshot of prices from a market data provider, which represents the market price of natural gas delivered at the end of each calendar month. This data is available for roughly the next 18 months and is combined with historical prices in a time series database. After gaining access, you are able to download the data in a CSV file.

You should use this monthly snapshot to produce a varying picture of the existing price data, as well as an extrapolation for an extra year, in case the client needs an indicative price for a longer-term storage contract.

### Instructions

1. **Download the Data**  
   Download the monthly natural gas price data. Each point in the data set corresponds to the purchase price of natural gas at the end of a month, from 31st October 2020 to 30th September 2024.

2. **Analyze and Extrapolate**  
   Analyze the data to estimate the purchase price of gas at any date in the past and extrapolate it for one year into the future. Your code should take a date as input and return a price estimate.

3. **Visualization**  
   Try to visualize the data to find patterns and consider what factors might cause the price of natural gas to vary. This can include looking at months of the year for seasonal trends that affect the prices, but market holidays, weekends, and bank holidays need not be accounted for.

## Task 2 (Contract Pricing Model)

You need to create a prototype pricing model that can go through further validation and testing before being put into production. Eventually, this model may be the basis for fully automated quoting to clients, but for now, the desk will use it with manual oversight to explore options with the client. 

### Instructions

1. **Write a Pricing Function**  
   Write a function that is able to use the data you created previously to price the contract. The client may want to choose multiple dates to inject and withdraw a set amount of gas, so your approach should generalize the explanation from before. Consider all the cash flows involved in the product.

2. **Input Parameters**  
   The input parameters that should be taken into account for pricing are:
   - **Injection Dates**: Dates when gas is injected.
   - **Withdrawal Dates**: Dates when gas is withdrawn.
   - **Prices**: The prices at which the commodity can be purchased/sold on those dates.
   - **Injection/Withdrawal Rate**: The rate at which the gas can be injected/withdrawn.
   - **Maximum Volume**: The maximum volume that can be stored.
   - **Storage Costs**: Costs associated with storing the gas.

3. **Function Requirements**  
   Write a function that takes these inputs and gives back the value of the contract. You can assume there is no transport delay and that interest rates are zero. Market holidays, weekends, and bank holidays need not be accounted for.

4. **Testing**  
   Test your code by selecting a few sample inputs.