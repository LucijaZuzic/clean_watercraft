import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import os

MAXINT = 10 ** 100
cm = 1/2.54  # centimeters in inches

def plot_dict(begin_name, dict_use, save_name, subtitle, use_ws = []):
    plt.figure(figsize=(5.25*len(dict_use[list(dict_use.keys())[0]])*cm, 29.7/6*len(use_ws)*cm), dpi = 300)
    
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
        for var in dict_use[ws]:
            if var == "time":
                continue
            ix_ws += 1
            plt.subplot(len(use_ws), len(dict_use[ws]), ix_ws)
            stepx = 1
            stepy = 1
            x = 0
            for m1 in sorted(dict_use[ws][var]):
                y = 0
                for m2 in sorted(dict_use[ws][var]):
                    xarr = [x - stepx / 2, x + stepx / 2]
                    ymin = y - stepy / 2
                    ymax = y + stepy / 2
                    valu = 1 - dict_use[ws][var][m1][m2][1]
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
            ticks_use = [ix * stepx for ix in range(len(dict_use[ws][var]))]
            labs_use = [m.replace("_", " ") for m in sorted(dict_use[ws][var])]
            varnew = var.replace("_", " ").replace("longitude no abs", "$x$ offset").replace("direction", "heading")
            varnew = varnew.replace("latitude no abs", "$y$ offset").replace("no abs", "$x$ and $y$ offset")
            varnew = varnew.replace("speed actual dir", "speed, heading, and time")
            if ix_ws % len(dict_use[ws]) == 1 and len(use_ws) > 1:
                plt.ylabel("Forecasting time $" + str(ws) + "$ $s$" + "\n" + subtitle)
            else:
                if ix_ws % len(dict_use[ws]) == len(dict_use[ws]) // 2 and len(use_ws) == 1:
                    plt.title("Forecasting time $" + str(ws) + "$ $s$" + "\n" + subtitle)
            plt.xlabel(varnew.capitalize())
            if ix_ws % len(dict_use[ws]) == 0 and ix_var == len(dict_use[ws]) * (len(use_ws) - 1):
                plt.yticks(ticks_use, labs_use)
                plt.gca().yaxis.tick_right()
            else:
                plt.yticks([])
            plt.xticks([])
        ix_var += len(dict_use[ws])
    new_dir_name = "stats_dir_reverse/"    
    if begin_name == "dicti_wilcoxon":
        new_dir_name += "wilcoxon/"
    if not os.path.isdir(new_dir_name):
        os.makedirs(new_dir_name)
    plt.savefig(new_dir_name + save_name + ".svg", bbox_inches = "tight")
    plt.savefig(new_dir_name + save_name + ".png", bbox_inches = "tight")
    plt.savefig(new_dir_name + save_name + ".pdf", bbox_inches = "tight")
    plt.close()

for start_name in ["dicti_mann_whitney", "dicti_wilcoxon"]:

    for metric in ["R2", "MAE"]:
        df_dictio = pd.read_csv(start_name + "_" + metric + ".csv", index_col = False)

        var_list = set(df_dictio["variable"])
        model_list1 = set(list(df_dictio["model1"]))
        model_list2 = set(list(df_dictio["model2"]))
        model_list = set()
        for m in model_list1:
            model_list.add(m)
        for m in model_list2:
            model_list.add(m)
        ws_list = set(df_dictio["ws"])

        dicti_mann_whitney = dict()

        for ws in ws_list:
            dicti_mann_whitney[ws] = dict()
            for var in var_list:
                dicti_mann_whitney[ws][var] = dict()
                for model1 in model_list:
                    dicti_mann_whitney[ws][var][model1] = dict()
                    for model2 in model_list:
                        dicti_mann_whitney[ws][var][model1][model2] = (1.0, 1.0)

        for ix in range(len(df_dictio["variable"])):
            var = df_dictio["variable"][ix]
            ws = df_dictio["ws"][ix]
            model1 = df_dictio["model1"][ix]
            model2 = df_dictio["model2"][ix]
            u = df_dictio["u"][ix] 
            p = df_dictio["p"][ix]
            dicti_mann_whitney[ws][var][model1][model2] = (u, p)
            dicti_mann_whitney[ws][var][model2][model1] = (u, p)

        metricnew = metric.replace("R2", "$R^{2}$ (%)")
        metricnew = metricnew.replace("euclid", "Euclidean distance")
        metricnew = metricnew.replace("haversine", "Haversine distance")
        for ws in set(list(df_dictio["ws"])):
            plot_dict(start_name, dicti_mann_whitney, "var_" + str(ws) + "_" + metric, metricnew, [ws])

    for metric in ["R2", "MAE", "euclid", "haversine"]:
        df_dictio_traj = pd.read_csv(start_name + "_traj_" + metric + ".csv", index_col = False)

        var_list = set(df_dictio_traj["variable"])
        model_list1 = set(list(df_dictio_traj["model1"]))
        model_list2 = set(list(df_dictio_traj["model2"]))
        model_list = set()
        for m in model_list1:
            model_list.add(m)
        for m in model_list2:
            model_list.add(m)
        ws_list = set(df_dictio_traj["ws"])

        dicti_mann_whitney_traj = dict()

        for ws in ws_list:
            dicti_mann_whitney_traj[ws] = dict()
            for var in var_list:
                dicti_mann_whitney_traj[ws][var] = dict()
                for model1 in model_list:
                    dicti_mann_whitney_traj[ws][var][model1] = dict()
                    for model2 in model_list:
                        dicti_mann_whitney_traj[ws][var][model1][model2] = (1.0, 1.0)

        for ix in range(len(df_dictio_traj["variable"])):
            var = df_dictio_traj["variable"][ix]
            ws = df_dictio_traj["ws"][ix]
            model1 = df_dictio_traj["model1"][ix]
            model2 = df_dictio_traj["model2"][ix]
            u = df_dictio_traj["u"][ix] 
            p = df_dictio_traj["p"][ix] 
            dicti_mann_whitney_traj[ws][var][model1][model2] = (u, p)
            dicti_mann_whitney_traj[ws][var][model2][model1] = (u, p)

        metricnew = metric.replace("R2", "$R^{2}$ (%)")
        metricnew = metricnew.replace("euclid", "Euclidean distance")
        metricnew = metricnew.replace("haversine", "Haversine distance")
        for ws in set(list(df_dictio_traj["ws"])):
            plot_dict(start_name, dicti_mann_whitney_traj, "traj_" + str(ws) + "_" + metric, metricnew, [ws])