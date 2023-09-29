
# USD/INR Exchange Rate Simulation

This project simulates the dynamics of the USD/INR exchange rate. The stochastic differential equation used for the simulation has been derived by the repository owner from the book "Brownian Motion Calculus", specifically problem 4.10.8.

## Model

The specifics of the equation are derived from the mentioned book. For a clear representation, it's advisable to refer to problem 4.10.8 of the book.

## Simulation Results

The simulation was carried out with the following parameters:
- Initial exchange rate: 1 USD = 83 INR
- Drift rate: 1% annual appreciation of USD against INR
- Volatility: 15% annual volatility
- Time horizon: 1 year
- Time step: 1/252 (assuming 252 trading days in a year)

The next-day forecasted average exchange rate is approximately INR 83.01 per USD, with a standard deviation of approximately INR 0.78.

The results are visually represented in the plot provided in this repository.

![Simulated USD/INR Exchange Rate Paths](simulation_plot.png)

## Usage

To run the simulation, execute the `exchange_rate_simulation.py` script.

## Reference

The dynamics and methodology are based on:
- Wiersema, Ubbo F. *Brownian Motion Calculus*. Wiley, 2008.

## License

MIT License.

