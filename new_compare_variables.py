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

var_list = sorted(list(dictio.keys()))
model_list = list(dictio[var_list[0]].keys())
ws_list = list(dictio[var_list[0]][model_list[0]].keys())
metric_list = list(dictio[var_list[0]][model_list[0]][ws_list[0]].keys())
for metric in metric_list:
    dicti_mann_whitney_new = {"model": [], "ws": [], "variable1": [], "variable2": [], "u": [], "p": []}
    for model in model_list:
        for ws in ws_list:
            for var1_ix in range(len(var_list)):
                var1 = var_list[var1_ix]
                for var2_ix in range(var1_ix + 1, len(var_list)):
                    var2 = var_list[var2_ix]
                    uval, pval = stats.mannwhitneyu(dictio[var1][model][ws][metric], dictio[var2][model][ws][metric])
                    print(metric, model, ws, var1, var2, uval, pval)
                    dicti_mann_whitney_new["model"].append(model)
                    dicti_mann_whitney_new["ws"].append(ws)
                    dicti_mann_whitney_new["variable1"].append(var1)
                    dicti_mann_whitney_new["variable2"].append(var2)
                    dicti_mann_whitney_new["u"].append(uval)
                    dicti_mann_whitney_new["p"].append(pval)
    df_write = pd.DataFrame(dicti_mann_whitney_new)
    df_write.to_csv("dicti_mann_whitney_variables_" + metric + ".csv", index = False)