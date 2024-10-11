import pandas as pd
import numpy as np

MAXINT = 10 ** 100

def stringify(value_round, rounding, skip_mul):
    if value_round == 0:
        return "0", 0
    if abs(value_round) >= 1 or skip_mul:
        return str(np.round(value_round, rounding)), 0
    else:
        pot = 0
        while abs(value_round) < 1:
            pot += 1
            value_round *= 10
        return str(np.round(value_round, rounding)) + " \\times 10^{-" + str(pot) + "}", pot

name_list = ["data_frame_total_reverse", "data_frame_total", "data_frame_test", "data_frame_test_reverse", "data_frame_val"]
name_list_traj = [name.replace("frame_", "frame_traj_") for name in name_list]
name_list = ["data_frame_val"]
name_list_traj = ["data_frame_traj_val"]

name_list_total = []
name_list_total.extend(name_list)
name_list_total.extend(name_list_traj)

round_val = {"R2": (100, 2, 3), "MAE": (1, 2, 1), "euclid": (1, 2, 1), "haversine": (1, 2, 1)}

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
    dictio_avg = dict()
    for var in dictio:
        for model in dictio[var]:
            for ws in dictio[var][model]:
                for metric in dictio[var][model][ws]:
                    if var not in dictio_avg:
                        dictio_avg[var] = dict()
                    if model not in dictio_avg[var]:
                        dictio_avg[var][model] = dict()
                    if ws not in dictio_avg[var][model]:
                        dictio_avg[var][model][ws] = dict()
                    if var not in dictio_stdev:
                        dictio_stdev[var] = dict()
                    if model not in dictio_stdev[var]:
                        dictio_stdev[var][model] = dict()
                    if ws not in dictio_stdev[var][model]:
                        dictio_stdev[var][model][ws] = dict()
                    if not use_stdev:
                        dictio_stdev[var][model][ws][metric] = 0
                        dictio_avg[var][model][ws][metric] = dictio[var][model][ws][metric][0]
                    else:
                        dictio_stdev[var][model][ws][metric] = np.std(dictio[var][model][ws][metric])
                        dictio_avg[var][model][ws][metric] = np.average(dictio[var][model][ws][metric])

                    if var not in min_max_for_metric_for_ws:
                        min_max_for_metric_for_ws[var] = dict()
                    if ws not in min_max_for_metric_for_ws[var]:
                        min_max_for_metric_for_ws[var][ws] = dict()
                    if metric not in min_max_for_metric_for_ws[var][ws]:
                        min_max_for_metric_for_ws[var][ws][metric] = (dictio_avg[var][model][ws][metric], model, dictio_avg[var][model][ws][metric], model)
                    else:    
                        metric_min, model_min, metric_max, model_max = min_max_for_metric_for_ws[var][ws][metric]
                        if dictio_avg[var][model][ws][metric] > metric_max:
                            metric_max = dictio_avg[var][model][ws][metric]
                            model_max = model
                        if dictio_avg[var][model][ws][metric] < metric_min:
                            metric_min = dictio_avg[var][model][ws][metric]
                            model_min = model
                        min_max_for_metric_for_ws[var][ws][metric] = (metric_min, model_min, metric_max, model_max)

    if "no abs" in dictio:
        for ws in [2, 3, 4, 5, 10, 20, 30]:
            for var in ["no abs"]:
                for metric in ["R2"]:
                    for model in ["UniTS"]:
                            #print(ws, var, metric)
                            averages = []
                            for ps in range(5):
                                list_new = dictio[var][model][ws][metric][ps*5:(ps+1)*5]
                                averages.append(np.average(list_new))
                            continue
                            if "R2" in metric:
                                print(averages, np.argmax(averages) + 1)
                            else:
                                print(averages, np.argmin(averages) + 1)

    for metric in round_val:
        if metric not in df_dictio:
            continue
        if "euclid" in metric:
            continue
        for var in min_max_for_metric_for_ws:
            if "time" in var:
                continue
            model_best_for = dict()
            for model in dictio[var]:
                model_best_for[model] = []
            for ws in min_max_for_metric_for_ws[var]:
                metric_min, model_min, metric_max, model_max = min_max_for_metric_for_ws[var][ws][metric]
                model_best = model_min
                if "R2" in metric:
                    model_best = model_max
                model_best_for[model_best].append(ws)
            for model in model_best_for:
                if len(model_best_for[model]) > 0:
                    model_best_for[model] = sorted(model_best_for[model])
                    mul_val = 0
                    direction_use = "lowest"
                    if metric == "R2":
                        mul_val = 2
                        direction_use = "highest"
                    if metric == "MAE" and "no_abs" in var:
                        mul_val = 5
                    if metric == "MAE" and ("no abs" in var or "actual" in var):
                        mul_val = 3
                    if metric == "haversine" and "speed" in var:
                        mul_val = 1
                    rnd_val = 2
                    if metric == "MAE" and "latitude" in var:
                        rnd_val = 3
                    if "speed" in var and "actual" in var:
                        rnd_val = 3
                    mul_str = ""
                    if mul_val > 0:
                        mul_str = " \\times 10^{-" + str(mul_val) + "}"
                    avg_arr = [np.round(dictio_avg[var][model][ws][metric] * (10 ** mul_val), rnd_val) for ws in model_best_for[model]]
                    std_arr = [np.round(dictio_stdev[var][model][ws][metric] * (10 ** mul_val), rnd_val) for ws in model_best_for[model]]
                    varnew = var.replace("_", " ").replace("longitude no abs", "$x$ offset").replace("direction", "heading")
                    varnew = varnew.replace("latitude no abs", "$y$ offset").replace("no abs", "$x$ and $y$ offset")
                    varnew = varnew.replace("speed actual dir", "speed, heading, and time")
                    if "actual" in var or "no abs" in var:
                        varnew = "trajectories estimated using " + varnew
                    str_ws = ""
                    for ws in model_best_for[model]:
                        str_ws += "$" + str(ws) + "$, "
                    str_ws = str_ws[:-2]    
                    if "," in str_ws:
                        str_ws = str_ws.replace(", $" + str(model_best_for[model][-1]) + "$", ", and $" + str(model_best_for[model][-1]) + "$")
                    str_avg_std = ""
                    last_part = ""
                    for ix in range(len(model_best_for[model])):
                        unit_str = "\\%"
                        if "haversine" in metric:
                            unit_str = " $km$"
                        if "euclid" in metric or ("MAE" in metric and ("heading" in varnew or "offset" in varnew)):
                            unit_str = "$\\degree$"
                        if "MAE" in metric and "speed" == varnew:
                            unit_str = " $km/h$"
                        last_part = " $" + str(avg_arr[ix]) + mul_str + "$" + unit_str + " ($" + str(std_arr[ix]) + mul_str + "$" + unit_str + ")"
                        str_avg_std += last_part + ","
                    str_avg_std = str_avg_std[1:-1]
                    if "," in str_avg_std:
                        str_avg_std = str_avg_std.replace(last_part, " and" + last_part)
                    metricnew = metric.replace("R2", "$R^{2}$ (\%)")
                    metricnew = metricnew.replace("euclid", "Euclidean distance")
                    metricnew = metricnew.replace("haversine", "haversine distance")
                    sentence_use = "The " + model.replace("_", " ") + " model achieved the " + direction_use + " " + metricnew + " for " + varnew + ", and a forecasting time of " + str_ws + " seconds with average values and standard deviation (in brackets) that equal " + str_avg_std
                    if "," not in str_ws:
                        sentence_use = sentence_use.replace("average values", "an average value")
                        sentence_use = sentence_use.replace("equal", "equals")
                    if "," in str_ws:
                        sentence_use = sentence_use + " respectively"
                    sentence_use = sentence_use.replace("$$", "") + "."
                    print(sentence_use)
