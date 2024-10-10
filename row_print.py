import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os

MAXINT = 10 ** 100

def stringify(value_round, rounding):
    if value_round == 0:
        return "0", 0
    if abs(value_round) >= 1:
        return str(np.round(value_round, rounding)), 0
    else:
        pot = 0
        while abs(value_round) < 1:
            pot += 1
            value_round *= 10
        return str(np.round(value_round, rounding)) + " \\times 10^{-" + str(pot) + "}", pot

name_list = ["data_frame_total_reverse", "data_frame_total", "data_frame_test", "data_frame_test_reverse", "data_frame_val"]
name_list_traj = [name.replace("frame_", "frame_traj_") for name in name_list]
name_list = ["data_frame_total_reverse", "data_frame_val"]
name_list_traj = ["data_frame_traj_val"]

name_list_total = []
name_list_total.extend(name_list_traj)

round_val = {"R2": (100, 2, 3), "MAE": (1, 2, 1), "euclid": (1, 2, 1), "haversine": (1, 2, 1)}
filter_add = True
cm = 1/2.54  # centimeters in inches
plot_draw = True
legend_pos = {17: 4, 4: 2.5, 5: 3.5, 7: 3.5}
legend_offset = {17: -0.1, 4: -0.05, 5: -0.05, 7: -0.05}
color_for_model = {"Att": "#6699CC", "GRU": "#004488", "LSTM": "#DDAA33", "RNN": "#BB5566", "UniTS": "#000000"}
line_for_model = {"1": "dashed", "2": "dotted", "3": "dashdot", "4": "solid", "UniTS": "solid",
                  "Linear": "dashed", "Twice": "dotted", "Third": "dashdot", "Reference": "solid"}

def color_me(name_model):
    color_use = "black"
    line_use = "solid"
    for m in sorted(color_for_model.keys()):
        if m in name_model:
            color_use = color_for_model[m]
            break
    for m in sorted(line_for_model.keys()):
        if m in name_model:
            line_use = line_for_model[m]
            break
    return color_use, line_use

for name in name_list_total:
    df_dictio = pd.read_csv(name + ".csv", index_col = False)

    min_max_for_metric_for_ws = dict()
    dictio = dict()
    use_stdev = False
    used_metric = set()
    for ix in range(len(df_dictio["variable"])):
        var = df_dictio["variable"][ix]
        model = df_dictio["model"][ix]
        ws = df_dictio["ws"][ix]
        test = df_dictio["test"][ix]
        val = df_dictio["val"][ix]
        if var not in dictio:
            dictio[var] = dict()
        if model not in dictio[var]:
            dictio[var][model] = dict()
        if ws not in dictio[var][model]:
            dictio[var][model][ws] = dict()
        for metric in round_val:
            if metric not in df_dictio:
                continue
            used_metric.add(metric)
            if metric not in dictio[var][model][ws]:
                dictio[var][model][ws][metric] = []
            else:
                use_stdev = True
            dictio[var][model][ws][metric].append(df_dictio[metric][ix])

    for ws in [2, 3, 4, 5, 10, 20, 30]:
        for var in ["no abs"]:
            for metric in ["R2"]:
                for model in ["UniTS"]:
                        print(ws, var, metric)
                        averages = []
                        for ps in range(5):
                            list_new = dictio[var][model][ws][metric][ps*5:(ps+1)*5]
                            averages.append(np.average(list_new))
                        if "R2" in metric:
                            print(averages, np.argmax(averages) + 1)
                        else:
                            print(averages, np.argmin(averages) + 1)