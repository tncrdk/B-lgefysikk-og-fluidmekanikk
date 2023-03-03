from enum import Enum
import numpy as np

diameter = 2.5e-2
err_diameter = 0.1e-2
massetetthet_vann = 997  # kg/m^3
volum_kule = 4 / 3 * np.pi * (diameter / 2) ** 3


class Kule(Enum):
    Brun_kule = 0
    Stål_kule = 1
    Liten_kule = 2


analytisk_losning_tråd = massetetthet_vann * volum_kule

kule_vekt = {Kule.Brun_kule: 76e-3, Kule.Stål_kule: 68e-3, Kule.Liten_kule: 58e-3}

kule_måling_bunn = {
    Kule.Brun_kule: 76e-3,
    Kule.Stål_kule: 68e-3,
    Kule.Liten_kule: 59e-3,
}

kule_måling_tråd = {Kule.Brun_kule: 7e-3, Kule.Stål_kule: 8e-3, Kule.Liten_kule: 6e-3}

for kule in Kule:
    måling_tråd = kule_måling_tråd[kule]
    måling_bunn = kule_måling_bunn[kule]
    print("Tråd")
    print(f"Måling: {måling_tråd}")
    print(f"Analytisk: {analytisk_losning_tråd}")
    print(f"Differanse: {måling_tråd - analytisk_losning_tråd}")
    print("-" * 10)
    print(f"Bunn")
    print(f"Måling: {måling_bunn}")
    print(f"Analytisk: {kule_vekt[kule]}")
    print(f"Differanse: {måling_bunn - kule_vekt[kule]}")
    print()
    print()
