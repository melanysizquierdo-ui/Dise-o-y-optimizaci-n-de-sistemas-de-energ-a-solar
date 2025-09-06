# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 17:39:32 2025

@author: melany sanchez
"""

# Simulador de Producción de Energía Fotovoltaica ☀️🔋

Este proyecto es una aplicación educativa en **Python** que permite modelar y visualizar el rendimiento de un panel fotovoltaico en función de la ubicación, fecha, inclinación y orientación. Utiliza la biblioteca `pvlib` para cálculos solares precisos y permite comparar resultados con datos reales.

---

## ✨ Funcionalidades

- **Parámetros de entrada**:
  - Latitud y longitud de la ubicación
  - Fecha de simulación
  - Inclinación y azimut del panel fotovoltaico
  - Área y eficiencia del panel
- **Cálculo de posición solar**: altitud y azimut del sol a lo largo del día.
- **Modelo de irradiancia solar**:
  - Irradiancia directa normal (DNI)
  - Irradiancia difusa horizontal (DHI)
  - Irradiancia global horizontal (GHI)
  - Irradiancia sobre el plano inclinado (POA)
- **Simulación de producción de energía**:
  - Potencia instantánea por intervalo
  - Energía total diaria en Wh
- **Visualización**:
  - Gráfico de altitud solar vs hora del día
  - Gráfico de potencia FV vs hora del día

---

## 📦 Dependencias

La aplicación requiere **Python 3.8+** y las siguientes librerías:

- `numpy`
- `pandas`
- `matplotlib`
- `pvlib`

Instálalas con:

```bash
pip install numpy pandas matplotlib pvlib 

 Ejecución
- Clona el repositorio:
git clone https://github.com/tu-usuario/solar-simulation.git
cd solar-simulation


- Ejecuta el script principal:
python src/solar_model.py


- Ingresa los datos solicitados en consola:
- Latitud y longitud del sitio
- Fecha de simulación
- Inclinación y orientación del panel
- Área y eficiencia del módulo

- El programa mostrará en consola:
- Energía diaria estimada (Wh)
- Potencia pico del panel (W)

Y generará gráficos de:
- Altitud solar durante el día
- Potencia fotovoltaica estimada durante el día












