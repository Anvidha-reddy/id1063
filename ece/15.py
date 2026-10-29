import numpy as np
import matplotlib.pyplot as plt
import subprocess
import os

# Given sampling frequency
Fs = 40
Ts = 1 / Fs

# First ten samples, starting at t = 0
n = np.arange(10)
t_samples = n * Ts

# Continuous-time axis for detailed plots
t = np.linspace(0, t_samples[-1], 5000)

# Original analog signals
x1 = np.cos(20 * np.pi * t)
x2 = np.cos(100 * np.pi * t)

# Sampled signals
x1_samples = np.cos(20 * np.pi * t_samples)
x2_samples = np.cos(100 * np.pi * t_samples)

# Differences between corresponding samples
difference = x1_samples - x2_samples

# Print sample table
print("Sampling frequency =", Fs, "Hz")
print("Sampling interval =", Ts, "seconds")
print("\n n       t(n)       x1[n]       x2[n]      Difference")
for i in range(10):
    print(f"{n[i]:2d}   {t_samples[i]:.4f}     "
          f"{x1_samples[i]: .4f}      "
          f"{x2_samples[i]: .4f}      "
          f"{difference[i]: .4f}")

print("\nAll samples equal:",
      np.allclose(x1_samples, x2_samples))

# Create detailed plots
fig, ax = plt.subplots(3, 1, figsize=(12, 13))

# Plot 1: Continuous signals
ax[0].plot(t, x1, label=r'$x_1(t)=\cos(20\pi t)$',
           linewidth=2)
ax[0].plot(t, x2, label=r'$x_2(t)=\cos(100\pi t)$',
           linewidth=1.5, alpha=0.85)

ax[0].scatter(t_samples, x1_samples, s=55,
              marker='o', label=r'$x_1[n]$ samples',
              zorder=5)
ax[0].scatter(t_samples, x2_samples, s=90,
              marker='x', label=r'$x_2[n]$ samples',
              zorder=6)

ax[0].set_title("Continuous Signals and Their Sampling Points")
ax[0].set_xlabel("Time (seconds)")
ax[0].set_ylabel("Amplitude")
ax[0].set_xticks(t_samples)
ax[0].tick_params(axis='x', labelrotation=45)
ax[0].set_ylim(-1.3, 1.3)
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].legend()
ax[0].text(0.02, 0.08,
           "The continuous signals differ, but their samples coincide.",
           transform=ax[0].transAxes)

# Plot 2: Discrete-time samples
markerline1, stemlines1, baseline1 = ax[1].stem(
    n, x1_samples, linefmt='C0-', markerfmt='C0o',
    basefmt='k-', label=r'$x_1[n]$'
)
markerline2, stemlines2, baseline2 = ax[1].stem(
    n, x2_samples, linefmt='C1--', markerfmt='C1x',
    basefmt=' '
)

ax[1].set_title("First Ten Samples: Both Sequences Overlap")
ax[1].set_xlabel("Sample index n")
ax[1].set_ylabel("Sample amplitude")
ax[1].set_xticks(n)
ax[1].set_yticks([-1, 0, 1])
ax[1].set_ylim(-1.4, 1.4)
ax[1].grid(True, linestyle='--', alpha=0.6)
ax[1].legend([markerline1, markerline2],
             [r'$x_1[n]$', r'$x_2[n]$'])

# Label each sample
for i in range(10):
    ax[1].annotate(f"{x1_samples[i]:.0f}",
                   (n[i], x1_samples[i]),
                   xytext=(0, 10 if x1_samples[i] >= 0 else -18),
                   textcoords='offset points',
                   ha='center', fontsize=9)

# Plot 3: Difference between samples
ax[2].stem(n, difference, linefmt='C3-',
           markerfmt='C3o', basefmt='k-')
ax[2].set_title(r"Difference: $x_1[n]-x_2[n]$")
ax[2].set_xlabel("Sample index n")
ax[2].set_ylabel("Difference")
ax[2].set_xticks(n)
ax[2].set_yticks([-1, 0, 1])
ax[2].set_ylim(-0.5, 0.5)
ax[2].grid(True, linestyle='--', alpha=0.6)
ax[2].text(0.5, 0.75, "All differences are zero",
           transform=ax[2].transAxes, ha='center')

plt.tight_layout()

# Save and automatically open the plot
filename = os.path.abspath("sampling_verification.png")
plt.savefig(filename, dpi=250, bbox_inches='tight')
plt.close()

subprocess.run(["termux-open", filename])
