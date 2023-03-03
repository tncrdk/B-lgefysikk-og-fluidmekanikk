import numpy as np
import matplotlib.pyplot as plt
import scipy


def plot_data(x_values: np.ndarray, ys = np.ndarray) -> None:
    ax, fig = plt.figure()
frequency_rate, amplitudes_arr = scipy.io.wavfile.read()