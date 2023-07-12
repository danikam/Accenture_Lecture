import plotly.graph_objects as go
import matplotlib.pyplot as plt


######################## Sources ########################
# ~80-90% battery system efficiency: https://www.pnnl.gov/sites/default/files/media/file/Final%20-%20ESGC%20Cost%20Performance%20Report%2012-11-2020.pdf
# ~55-75% hydrogen electrolyzer system efficiency: https://www.nrel.gov/docs/fy04osti/36705.pdf
# 33.6 kWh per kg of hydrogen: https://rmi.org/run-on-less-with-hydrogen-fuel-cells/
# 53% FT efficiency: https://www.sciencedirect.com/science/article/abs/pii/S2212982021000263
# DAC energy efficiency of 1.7-2.5 kWh / kg CO2: https://www.iea.org/energy-system/carbon-capture-utilisation-and-storage/direct-air-capture
#########################################################

############# Calculation of CO2 efficiency #############
C_KG_PER_MOLE=0.012
O2_KG_PER_MOLE=0.032
H2_KG_PER_MOLE=0.002

H2_ENERGY_PER_KG = 33.6         # Usable hydrogen energy per kg H2
H2_ENERGY_PER_MOLE = H2_ENERGY_PER_KG * H2_KG_PER_MOLE # Energy needed to produce one mole of H2
CO2_ENERGY_PER_KG_DAC = 2    # Energy needed to produce 1 kg of CO2 using liquid DAC
CO2_ENERGY_PER_MOLE_DAC = CO2_ENERGY_PER_KG_DAC * (C_KG_PER_MOLE + O2_KG_PER_MOLE)

DAC_ENERGY_EFFICIENCY = H2_ENERGY_PER_MOLE / (H2_ENERGY_PER_MOLE+CO2_ENERGY_PER_MOLE_DAC)    # For each mole of H2 energy, also need to provide energy to produce 1 mole of CO2 from DAC (since long-chain hydrocarbons have a H:C ration of 2:1)

print('Efficiency of FT hydrocarbon after producing CO2 from DAC and before performing FT: %f%%'%(100*DAC_ENERGY_EFFICIENCY))

#########################################################

# Lithium ion battery waterfall plot

fig = go.Figure(go.Waterfall(
    name = "", orientation = "v",
    measure = ["absolute", "relative"],
    x = ["Initial", "Li Ion Battery"],
    textposition = "outside",
    text = ["", "-15%"],
    y = [100, -15],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
        title = "",
        font=dict(size=24),
        yaxis_title="Energy (kWh)",
        showlegend = False
)

fig.write_image('battery_waterfall.png')

# Hydrogen waterfall plot

fig = go.Figure(go.Waterfall(
    name = "", orientation = "v",
    measure = ["absolute", "relative"],
    x = ["Initial", "H2 Electrolysis"],
    textposition = "outside",
    text = ["", "-35%"],
    y = [100, -35],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
        title = "",
        font=dict(size=24),
        yaxis_title="Energy (kWh)",
        showlegend = False
)


fig.write_image('h2_waterfall.png')

# Hydrocarbon waterfall plot

fig = go.Figure(go.Waterfall(
    name = "", orientation = "v",
    measure = ["absolute", "relative", "relative"],
    x = ["Initial", "H2 Electrolysis", "CO2 from DAC", "Fischer-TropschProcess"],
    textposition = "outside",
    text = ["", "-35%", "-55%", "-50%"],
    y = [100, -35, -35, -18],
    connector = {"line":{"color":"rgb(63, 63, 63)"}},
))

fig.update_layout(
        title = "",
        font=dict(size=22),
        yaxis_title="Energy (kWh)",
        showlegend = False
)


fig.write_image('hydrocarbon_waterfall.png')
