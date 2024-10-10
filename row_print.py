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
name_list_traj = ["data_frame_traj_total_reverse", "data_frame_traj_val"]

name_list_total = []
name_list_total.extend(name_list)
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

    dictio_stdev = dict()
    for var in dictio:
        for model in dictio[var]:
            for ws in dictio[var][model]:
                for metric in dictio[var][model][ws]:
                    if var not in dictio_stdev:
                        dictio_stdev[var] = dict()
                    if model not in dictio_stdev[var]:
                        dictio_stdev[var][model] = dict()
                    if ws not in dictio_stdev[var][model]:
                        dictio_stdev[var][model][ws] = dict()
                    if not use_stdev:
                        dictio[var][model][ws][metric] = dictio[var][model][ws][metric][0]
                        dictio_stdev[var][model][ws][metric] = 0
                    else:
                        dictio_stdev[var][model][ws][metric] = np.std(dictio[var][model][ws][metric])
                        dictio[var][model][ws][metric] = np.average(dictio[var][model][ws][metric])
                    if var not in min_max_for_metric_for_ws:
                        min_max_for_metric_for_ws[var] = dict()
                    if ws not in min_max_for_metric_for_ws[var]:
                        min_max_for_metric_for_ws[var][ws] = dict()
                    if metric not in min_max_for_metric_for_ws[var][ws]:
                        min_max_for_metric_for_ws[var][ws][metric] = (dictio[var][model][ws][metric], model, dictio[var][model][ws][metric], model)
                    else:    
                        metric_min, model_min, metric_max, model_max = min_max_for_metric_for_ws[var][ws][metric]
                        if dictio[var][model][ws][metric] > metric_max:
                            metric_max = dictio[var][model][ws][metric]
                            model_max = model
                        if dictio[var][model][ws][metric] < metric_min:
                            metric_min = dictio[var][model][ws][metric]
                            model_min = model
                        min_max_for_metric_for_ws[var][ws][metric] = (metric_min, model_min, metric_max, model_max)

    for metric in used_metric:
        for var in dictio:
            if var == "time":
                continue
            print(metric, var)
            ix_best = round_val[metric][2]
            string_latex = ""
            set_of_best = set()
            for model in dictio[var]:
                for ws in dictio[var][model]:
                    if model == min_max_for_metric_for_ws[var][ws][metric][ix_best] or not filter_add:
                        set_of_best.add(model)
            how_to_round = round_val[metric][1]
            found_error = True
            while how_to_round < 7 and found_error:
                set_str = set()
                found_error = False
                max_times = 0
                for model in set_of_best:
                    for ws in dictio[var][model]:
                        val_round, times_part = stringify(dictio[var][model][ws][metric] * round_val[metric][0], how_to_round)
                        max_times = max(times_part, max_times)
                        if val_round not in set_str:    
                            set_str.add(val_round)
                        else:
                            found_error = True
                how_to_round += 1
            if round_val[metric][0] == 100:
                max_times = 0
            how_to_round -= 1
            for model in set_of_best:
                row_str = model.replace("_", " ") + " & "
                for ws in dictio[var][model]:
                    str_val_round, times_part = stringify(dictio[var][model][ws][metric] * round_val[metric][0] * (10 ** max_times), how_to_round)
                    if round_val[metric][0] == 100:
                        str_val_round += "\%"
                    if model == min_max_for_metric_for_ws[var][ws][metric][ix_best]:
                        row_str += "$\\mathbf{" + str_val_round + "}$ & "
                    else:
                        row_str += "$" + str_val_round + "$ & "
                string_latex += row_str[:-2] + "\\\\ \\hline\n"
                if use_stdev:
                    row_str = model.replace("_", " ") + " & "
                    for ws in dictio_stdev[var][model]:
                        str_val_round, times_part = stringify(dictio_stdev[var][model][ws][metric] * round_val[metric][0] * (10 ** max_times), how_to_round)
                        if round_val[metric][0] == 100:
                            str_val_round += "\%"
                        if model == min_max_for_metric_for_ws[var][ws][metric][ix_best]:
                            row_str += "\\textbf{(}$\\mathbf{" + str_val_round + "}$\\textbf{)} & "
                        else:
                            row_str += "($" + str_val_round + "$) & "
                    string_latex += row_str[:-2] + "\\\\ \\hline\n"
            print(max_times, how_to_round)
            print(string_latex)