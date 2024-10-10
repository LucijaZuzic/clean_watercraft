import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
import scipy.stats as stats

round_val = ["R2", "MAE", "euclid", "haversine"]

df_dictio = pd.read_csv("data_frame_traj_val.csv", index_col = False)

dictio = dict()
for ix in range(len(df_dictio["variable"])):
    var = df_dictio["variable"][ix]
    if "time" in var:
        continue
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
        if metric not in dictio[var][model][ws]:
            dictio[var][model][ws][metric] = []
        else:
            use_stdev = True
        dictio[var][model][ws][metric].append(df_dictio[metric][ix])

var_list = list(dictio.keys())
model_list = sorted(list(dictio[var_list[0]].keys()))
ws_list = list(dictio[var_list[0]][model_list[0]].keys())
metric_list = list(dictio[var_list[0]][model_list[0]][ws_list[0]].keys())
for metric in dictio[var][model][ws]:
    dicti_mann_whitney_traj_new = {"variable": [], "ws": [], "model1": [], "model2": [], "u": [], "p": []}
    for var in var_list:
        for ws in ws_list:
            for model1_ix in range(len(model_list)):
                model1 = model_list[model1_ix]
                for model2_ix in range(model1_ix + 1, len(model_list)):
                    model2 = model_list[model2_ix]
                    uval, pval = stats.mannwhitneyu(dictio[var][model1][ws][metric], dictio[var][model2][ws][metric])
                    print(metric, var, ws, model1, model2, uval, pval)
                    dicti_mann_whitney_traj_new["variable"].append(var)
                    dicti_mann_whitney_traj_new["ws"].append(ws)
                    dicti_mann_whitney_traj_new["model1"].append(model1)
                    dicti_mann_whitney_traj_new["model2"].append(model2)
                    dicti_mann_whitney_traj_new["u"].append(uval)
                    dicti_mann_whitney_traj_new["p"].append(pval)
    df_write = pd.DataFrame(dicti_mann_whitney_traj_new)
    df_write.to_csv("dicti_mann_whitney_traj_" + metric + ".csv", index = False)