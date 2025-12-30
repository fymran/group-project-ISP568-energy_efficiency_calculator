from fuzzy_membership import FuzzyMembership
import numpy as np
import matplotlib.pyplot as plt

class FuzzyPlotter:
    @staticmethod
    def plot_live_fuzzy(value, m_off, m_low, m_med, m_high, max_val, label_type):
        start_val = 16 if label_type == "AC" else 0
        x_plot = np.linspace(start_val, max_val, 200)
        fig, ax = plt.subplots(figsize=(6, 1.8))
        if label_type == "Plug":
            y_low = [FuzzyMembership.trimf(i, [0.1, 40, 80]) for i in x_plot]
            y_med = [FuzzyMembership.trimf(i, [60, 120, 180]) for i in x_plot]
            y_high = [FuzzyMembership.trimf(i, [160, 240, 240.1]) for i in x_plot]
            ax.set_xlabel("Voltage (V)", fontsize=8)
        elif label_type == "Lamp":
            y_low = [FuzzyMembership.trimf(i, [0.1, 16.5, 33]) for i in x_plot]
            y_med = [FuzzyMembership.trimf(i, [25, 50, 75]) for i in x_plot]
            y_high = [FuzzyMembership.trimf(i, [66, 100, 100.1]) for i in x_plot]
            ax.set_xlabel("Intensity (%)", fontsize=8)
        elif label_type == "Fan":
            y_low = [FuzzyMembership.trimf(i, [0.1, 1.5, 3.0]) for i in x_plot]
            y_med = [FuzzyMembership.trimf(i, [2.0, 3.5, 5.0]) for i in x_plot]
            y_high = [FuzzyMembership.trimf(i, [4.0, 5.0, 5.1]) for i in x_plot]
            ax.set_xlabel("Speed Level", fontsize=8)
        elif label_type == "Efficiency":
            y_vlow = [FuzzyMembership.trimf(i, [-0.1, 0, 25]) for i in x_plot]
            y_low = [FuzzyMembership.trimf(i, [20, 40, 60]) for i in x_plot]
            y_med = [FuzzyMembership.trimf(i, [40, 60, 80]) for i in x_plot]
            y_high = [FuzzyMembership.trimf(i, [75, 100, 100.1]) for i in x_plot]
            ax.set_xlabel("Score (%)", fontsize=8)
        else: # AC
            y_low = [FuzzyMembership.trimf(i, [25, 27, 29]) for i in x_plot]
            y_med = [FuzzyMembership.trimf(i, [22, 24, 26]) for i in x_plot]
            y_high = [FuzzyMembership.trimf(i, [15.9, 16, 23]) for i in x_plot]
            ax.set_xlabel("Temperature (°C)", fontsize=8)
        if label_type == "Efficiency":
            ax.fill_between(x_plot, y_vlow, color="#e74c3c", alpha=0.2, label="V.Low")
            ax.fill_between(x_plot, y_low, color="#e67e22", alpha=0.2, label="Low")
            ax.fill_between(x_plot, y_med, color="#f1c40f", alpha=0.2, label="Med")
            ax.fill_between(x_plot, y_high, color="#2ecc71", alpha=0.2, label="High")
        else:
            ax.fill_between(x_plot, y_low, color="#2ecc71", alpha=0.2, label="Low")
            ax.fill_between(x_plot, y_med, color="#f39c12", alpha=0.2, label="Med")
            ax.fill_between(x_plot, y_high, color="#c0392b", alpha=0.2, label="High")
        current_y = max(m_off, m_low, m_med, m_high)
        ax.scatter([value], [current_y], color="#2980b9", zorder=5, s=30, edgecolors='white')
        ax.axvline(x=value, color="#2980b9", linestyle=":", linewidth=1.5, alpha=0.6)
        ax.set_ylim(0, 1.1)
        ax.set_yticks([0, 0.5, 1])
        ax.tick_params(axis='both', which='major', labelsize=7)
        if label_type == "AC":
            ax.set_xlim(15, 29)
            ax.invert_xaxis() 
        else:
            ax.set_xlim(start_val, max_val)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(True, axis='y', linestyle='--', alpha=0.3)
        ax.legend(loc='upper right', fontsize=6, frameon=False, ncol=4)
        plt.tight_layout()
        return fig
