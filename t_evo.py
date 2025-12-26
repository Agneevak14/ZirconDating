import numpy as np
import matplotlib.pyplot as plt

def eHF_DM(e, m, t):
    x = e - (m*t)
    return x

def eHF_crust(e, mDM, mcrust, t, s):
    x = eHF_DM(e, mDM, s) - (mcrust * (t - s))
    return x

lambda_1 = 1.867E-2  # Ga^-1

lu_depleted = float(input("Lu/Hf ratio (Depleted Mantle): "))
lu_chur     = float(input("Lu/Hf ratio (CHUR): "))
lu_crust    = float(input("Lu/Hf ratio (Crust): "))

ts    = float(input("Time of separation (Ga): "))

e_DM_0    = float(input("eHfDM(0) value: "))

n = int(round((ts - 0) / 0.01)) + 1     # number of points so step ≈ 0.01
t = np.linspace(0, ts, n)
print(t)
age_Ga = ts - t

m_DM     = lambda_1 * (lu_depleted - lu_chur) * 10000
m_crust  = lambda_1 * (lu_crust - lu_chur) * 10000

E_dm = eHF_DM(e_DM_0, m_DM, t)
E_crust = eHF_crust(e_DM_0, m_DM, m_crust, t, ts)


t_plot = t[::-1]
print(t_plot)
E_dm_plot = E_dm[::-1]
E_crust_plot = E_crust[::-1]

plt.figure(figsize=(8, 4.5))
plt.plot(t_plot, E_dm_plot, label="E_dm", color="C0")
plt.plot(t_plot, E_crust_plot, label="E_crust", color="C1")
plt.xlabel("Time (Ga)")
plt.ylabel("epsilon_Hf")
plt.title("Epsilon evolution: Depleted Mantle vs Crust")
plt.legend()
plt.grid(True)
plt.xlim(0, t_plot.max())
plt.tight_layout()
plt.show()



