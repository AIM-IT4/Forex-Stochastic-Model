
# USD/INR Exchange Rate Simulation

This project simulates the dynamics of the USD/INR exchange rate based on a given stochastic differential equation (SDE).

## Model

The exchange rate dynamics are modeled as:

\[ dQ(t) = \mu_Q Q(t) dt + \sigma_Q Q(t) dB(t) \]

where:
- \( Q(t) \) is the exchange rate at time \( t \).
- \( \mu_Q \) is the drift rate.
- \( \sigma_Q \) is the volatility.
- \( dB(t) \) is a Wiener process.

## Simulation Results

The simulation was carried out with the following parameters:
- Initial exchange rate: 1 USD = 83 INR
- Drift rate (\( \mu_Q \)): 1% annual appreciation of USD against INR
- Volatility (\( \sigma_Q \)): 15% annual volatility
- Time horizon: 1 year
- Time step: 1/252 (assuming 252 trading days in a year)

![Simulated USD/INR Exchange Rate Paths](simulation_plot.png)

## Usage

To run the simulation, execute the `exchange_rate_simulation.py` script.

## License

MIT License.

