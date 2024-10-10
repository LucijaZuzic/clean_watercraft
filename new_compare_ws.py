import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os
import scipy.stats as stats

round_val = ["R2", "MAE"]

df_dictio = pd.read_csv("data_frame_val.csv", index_col = False)

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
model_list = list(dictio[var_list[0]].keys())
ws_list = sorted(list(dictio[var_list[0]][model_list[0]].keys()))
metric_list = list(dictio[var_list[0]][model_list[0]][ws_list[0]].keys())
for metric in metric_list:
    dicti_mann_whitney_new = {"variable": [], "model": [], "ws1": [], "ws2": [], "u": [], "p": []}
    for var in var_list:
        for model in model_list:
            for ws1_ix in range(len(ws_list)):
                ws1 = ws_list[ws1_ix]
                for ws2_ix in range(ws1_ix + 1, len(ws_list)):
                    ws2 = ws_list[ws2_ix]
                    uval, pval = stats.mannwhitneyu(dictio[var][model][ws1][metric], dictio[var][model][ws2][metric])
                    print(metric, var, model, ws1, ws2, uval, pval)
                    dicti_mann_whitney_new["variable"].append(var)
                    dicti_mann_whitney_new["model"].append(model)
                    dicti_mann_whitney_new["ws1"].append(ws1)
                    dicti_mann_whitney_new["ws2"].append(ws2)
                    dicti_mann_whitney_new["u"].append(uval)
                    dicti_mann_whitney_new["p"].append(pval)
    df_write = pd.DataFrame(dicti_mann_whitney_new)
    df_write.to_csv("dicti_mann_whitney_ws_" + metric + ".csv", index = False)