import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os

MAXINT = 10 ** 100
cm = 1/2.54  # centimeters in inches

def plot_dict(dict_use, save_name, subtitle, use_ws = []):
    plt.figure(figsize=(21*cm, 29.7/2.1*len(use_ws)*cm), dpi = 300)
    
    plt.rcParams["svg.fonttype"] = "none"
    rc('font',**{'family':'Arial'})
    #plt.rcParams.update({"font.size": 7})
    SMALL_SIZE = 7
    MEDIUM_SIZE = 7
    BIGGER_SIZE = 7

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    ix_var = 0
    if len(use_ws) == 0:
        use_ws = list(dict_use.keys())
    for ws in use_ws:
        ix_ws = ix_var
        for model in dict_use[ws]:
            ix_ws += 1
            plt.subplot(5 * len(use_ws), 4, ix_ws)
            stepx = 1
            stepy = 1
            x = 0
            for m1 in sorted(dict_use[ws][model]):
                y = 0
                for m2 in sorted(dict_use[ws][model]):
                    xarr = [x - stepx / 2, x + stepx / 2]
                    ymin = y - stepy / 2
                    ymax = y + stepy / 2
                    valu = 1 - dict_use[ws][model][m1][m2][1]
                    hexcode = "#" + str(hex(int(np.round(valu * 255, 0)))).replace("0x", "") * 3
                    plt.fill_between(xarr, ymin, ymax, color = hexcode)
                    y += stepy
                x += stepx
            range_vals = np.arange(- stepx / 2, x, stepx)
            for x2 in range_vals:
                plt.axvline(x2, color = "k")
                plt.axhline(x2, color = "k")
            plt.xticks(rotation = 90)
            plt.xlim(- stepx / 2, x - stepx / 2)
            plt.ylim(- stepy / 2, y - stepy / 2)
            ticks_use = [ix * stepx for ix in range(len(dict_use[ws][model]))]
            labs_use = []
            for var in dict_use[ws][model]:
                varnew = var.replace("_", " ").replace("longitude no abs", "$x$ offset").replace("direction", "heading")
                varnew = varnew.replace("latitude no abs", "$y$ offset").replace("no abs", "$x$ and $y$ offset")
                varnew = varnew.replace("speed actual dir", "speed, heading, and time")
                labs_use.append(varnew.capitalize())
            modelnew = model.replace("_", " ")
            if ix_ws % 20 == 1 and len(use_ws) > 1:
                plt.ylabel("Forecasting time $" + str(ws) + "$ $s$" + "\n" + subtitle)
            else:
                if ix_ws % 20 == 2 and len(use_ws) == 1:
                    plt.title("Forecasting time $" + str(ws) + "$ $s$" + "\n" + subtitle)
            plt.xlabel(modelnew)
            if ix_ws % 20 == 17 and ix_var == 20 * (len(use_ws) - 1):
                plt.yticks(ticks_use, labs_use)
                plt.gca().yaxis.tick_right()
            else:
                plt.yticks([])
            plt.xticks([])
        ix_var += 20
    if not os.path.isdir("stats_dir_var_reverse"):
        os.makedirs("stats_dir_var_reverse")
    plt.savefig("stats_dir_var_reverse/" + save_name + ".svg", bbox_inches = "tight")
    plt.savefig("stats_dir_var_reverse/" + save_name + ".png", bbox_inches = "tight")
    plt.savefig("stats_dir_var_reverse/" + save_name + ".pdf", bbox_inches = "tight")
    plt.close()

for metric in ["R2", "MAE"]:
    df_dictio = pd.read_csv("dicti_mann_whitney_variables_" + metric + ".csv", index_col = False)

    model_list = set(df_dictio["model"])
    var_list1 = set(list(df_dictio["variable1"]))
    var_list2 = set(list(df_dictio["variable2"]))
    var_list = set()
    for m in var_list1:
        var_list.add(m)
    for m in var_list2:
        var_list.add(m)
    ws_list = set(df_dictio["ws"])

    dicti_mann_whitney = dict()

    for ws in ws_list:
        dicti_mann_whitney[ws] = dict()
        for model in model_list:
            dicti_mann_whitney[ws][model] = dict()
            for var1 in var_list:
                dicti_mann_whitney[ws][model][var1] = dict()
                for var2 in var_list:
                    dicti_mann_whitney[ws][model][var1][var2] = (1.0, 1.0)

    for ix in range(len(df_dictio["model"])):
        var1 = df_dictio["variable1"][ix]
        var2 = df_dictio["variable2"][ix]
        ws = df_dictio["ws"][ix]
        model = df_dictio["model"][ix]
        u = df_dictio["u"][ix] 
        p = df_dictio["p"][ix]
        dicti_mann_whitney[ws][model][var1][var2] = (u, p)
        dicti_mann_whitney[ws][model][var2][var1] = (u, p)

    metricnew = metric.replace("R2", "$R^{2}$ (%)")
    metricnew = metricnew.replace("euclid", "Euclidean distance")
    metricnew = metricnew.replace("haversine", "Haversine distance")
    for ws in set(list(df_dictio["ws"])):
        plot_dict(dicti_mann_whitney, "var_" + str(ws) + "_" + metric, metricnew, [ws])

for metric in ["R2", "MAE", "euclid", "haversine"]:
    df_dictio_traj = pd.read_csv("dicti_mann_whitney_traj_variables_" + metric + ".csv", index_col = False)

    model_list = set(df_dictio_traj["model"])
    var_list1 = set(list(df_dictio_traj["variable1"]))
    var_list2 = set(list(df_dictio_traj["variable2"]))
    var_list = set()
    for m in var_list1:
        var_list.add(m)
    for m in var_list2:
        var_list.add(m)
    ws_list = set(df_dictio_traj["ws"])

    dicti_mann_whitney_traj = dict()

    for ws in ws_list:
        dicti_mann_whitney_traj[ws] = dict()
        for model in model_list:
            dicti_mann_whitney_traj[ws][model] = dict()
            for var1 in var_list:
                dicti_mann_whitney_traj[ws][model][var1] = dict()
                for var2 in var_list:
                    dicti_mann_whitney_traj[ws][model][var1][var2] = (1.0, 1.0)

    for ix in range(len(df_dictio_traj["model"])):
        var1 = df_dictio_traj["variable1"][ix]
        var2 = df_dictio_traj["variable2"][ix]
        ws = df_dictio_traj["ws"][ix]
        model = df_dictio_traj["model"][ix]
        u = df_dictio_traj["u"][ix] 
        p = df_dictio_traj["p"][ix]
        dicti_mann_whitney_traj[ws][model][var1][var2] = (u, p)
        dicti_mann_whitney_traj[ws][model][var2][var1] = (u, p)

    metricnew = metric.replace("R2", "$R^{2}$ (%)")
    metricnew = metricnew.replace("euclid", "Euclidean distance")
    metricnew = metricnew.replace("haversine", "Haversine distance")
    for ws in set(list(df_dictio_traj["ws"])):
        plot_dict(dicti_mann_whitney_traj, "traj_" + str(ws) + "_" + metric, metricnew, [ws])