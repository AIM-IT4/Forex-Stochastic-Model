
import numpy as np
import matplotlib.pyplot as plt

def simulate_exchange_rate(Q0, mu_Q, sigma_Q, T, dt, n_simulations):
    n_steps = int(T/dt)
    Q_paths = np.zeros((n_simulations, n_steps))
    Q_paths[:, 0] = Q0
    for i in range(n_simulations):
        for j in range(1, n_steps):
            dB = np.sqrt(dt) * np.random.normal(0, 1)
            dQ = mu_Q * Q_paths[i, j-1] * dt + sigma_Q * Q_paths[i, j-1] * dB
            Q_paths[i, j] = Q_paths[i, j-1] + dQ
    return Q_paths

def plot_simulation(Q_paths):
    plt.figure(figsize=(10, 6))
    for i in range(Q_paths.shape[0]):
        plt.plot(Q_paths[i, :], lw=1)
    plt.title('Simulated USD/INR Exchange Rate Paths')
    plt.xlabel('Trading Days')
    plt.ylabel('Exchange Rate (USD/INR)')
    plt.grid(True)
    plt.savefig("simulation_plot.png")
    plt.show()

if __name__ == "__main__":
    # Parameters
    Q0 = 83  # Initial exchange rate (1 USD = 83 INR)
    mu_Q = 0.01  # Drift rate (1% annual appreciation of USD against INR)
    sigma_Q = 0.15  # Volatility (15% annual volatility)
    T = 1  # Time horizon (1 year)
    dt = 1/252  # Time step (assuming 252 trading days in a year)
    n_simulations = 10  # Number of simulation paths

    # Simulate and plot
    Q_paths = simulate_exchange_rate(Q0, mu_Q, sigma_Q, T, dt, n_simulations)
    plot_simulation(Q_paths)

