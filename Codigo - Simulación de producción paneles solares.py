# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 17:02:31 2025

@author: melany sanchez
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pvlib.location import Location
from pvlib.irradiance import get_total_irradiance

# Entrada de usuario
lat_deg = float(input("Ingresa los grados de latitud: "))
lat_min = float(input("Ingresa los minutos de latitud: "))
lon_deg = float(input("Ingresa la longitud (en grados negativos para oeste): "))
fecha = input("Ingresa la fecha (YYYY-MM-DD): ")
offset_min = float(input("Ingresa la corrección horaria en minutos (por longitud y horario): "))
tilt = float(input("Ingresa la inclinación del panel (grados): "))
azimuth_panel = float(input("Ingresa el azimut del panel (0 = norte, 180 = sur): "))
area_panel = float(input("Ingresa el área del panel en m²: "))
efficiency = float(input("Ingresa la eficiencia del panel (ej. 0.18 para 18%): "))

# Ubicación y tiempo
lat = lat_deg + lat_min / 60
location = Location(latitude=lat, longitude=lon_deg, tz='America/Bogota')
times = pd.date_range(f'{fecha} 05:30', f'{fecha} 20:00', freq='15min', tz='America/Bogota')

#  Posición solar
solar_position = location.get_solarposition(times)
zenith = solar_position['zenith']
azimuth = solar_position['azimuth']
elevation = solar_position['elevation']

#  Irradiancia simplificada (modelo claro)
dni = 1.4883 * np.maximum(np.sin(np.radians(elevation)), 0)  # irradiancia directa
ghi = dni * np.cos(np.radians(zenith))  # aproximación de GHI
dhi = ghi * 0.2  # estimación difusa (20%)

#  Irradiancia total sobre el plano inclinado
irradiancia = get_total_irradiance(
    surface_tilt=tilt,
    surface_azimuth=azimuth_panel,
    solar_zenith=zenith,
    solar_azimuth=azimuth,
    dni=dni,
    ghi=ghi,
    dhi=dhi
)

# ⚡ Producción energética
poa = irradiancia['poa_global']  # irradiancia sobre el plano del panel
power_output = poa * area_panel * efficiency  # potencia instantánea
energy_daily = power_output.sum() * (15 / 60)  # energía total diaria en Wh

# 📊 Gráficos
plt.figure(figsize=(10, 5))
plt.plot(times, elevation, label='Altura solar (°)', color='orange')
plt.xlabel('Hora')
plt.ylabel('Altura solar')
plt.title('Ángulo de altitud solar')
plt.grid(True)
plt.legend()

plt.figure(figsize=(10, 5))
plt.plot(times, power_output, label='Potencia estimada (W)', color='green')
plt.xlabel('Hora')
plt.ylabel('Potencia (W)')
plt.title('Producción fotovoltaica estimada')
plt.grid(True)
plt.legend()

plt.show()

# 📢 Resultado final
print(f"\nProducción total estimada para el {fecha}: {energy_daily:.2f} Wh")