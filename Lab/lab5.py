import numpy as np

INNER_RADIUS = 5.83e-2 / 2  # [m]
OUTER_RADIUS = 6e-2 / 2
RADIUS = (INNER_RADIUS + OUTER_RADIUS) / 2


def tension(force):
    return force / (np.pi * 4 * RADIUS)


measurements_22 = np.array([26.8, 27.0, 27.08, 26.9, 26.8])  # T = 22.3
measurements_25 = np.array([26.6, 26.75, 26.7, 26.2, 26.6])  # T = 25
measurements_30 = np.array([26.05, 26.5, 26.7, 26.6, 26.4])  # T = 30
measurements_35 = np.array([26.0, 26.6, 26.1, 26.5, 26.3])  # T = 35
measurements_40 = np.array([25.9, 26.0, 26.1, 26.15, 26.3])  # T = 40
measurements_45 = np.array([25.3, 25.7, 25.7, 25.75, 25.9])  # T = 45
measurements_50 = np.array([25.5, 25.6, 25.4, 25.45, 25.7])  # T = 50
measurements_55 = np.array([24.7, 25.0, 25.4, 25.7, 25.2])  # T = 55


def print_results(measurements, real_value):
    print("Tension array:", tension(measurements))
    avg = np.mean(measurements)
    print("Avg tension:", tension(avg))
    print("Avg force:", avg)
    print("Std:", np.std(measurements))
    max_rel_err = (
        max(
            (np.max(tension(measurements)) - real_value) / real_value,
            (np.min(tension(measurements)) - real_value) / real_value,
        )
        * 100
    )
    print(f"Max RelErr:{max_rel_err: .3f}%")


print_results(measurements_55, 67.9)
