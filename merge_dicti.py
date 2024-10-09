from utilities import load_object, save_object
import numpy as np
import matplotlib.pyplot as plt
import os
MAXVALTOTAL = 10 ** 200
TOPOFPLOT = 10 ** 100
dicti_all = load_object("dicti_all")
dicti_all_ws = load_object("dicti_all_ws")
dicti_all_latest = dict()
dicti_all_traj = load_object("dicti_all_traj")
dicti_all_traj_ws = load_object("dicti_all_traj_ws")
dicti_all_traj_latest = dict()

ord_metric_traj = dicti_all_traj[0][0]["long no abs"].keys()
ord_metric = dicti_all[0][0]["speed"].keys()
metric_dicti_traj = {"Euclid": 0, "R2": 2, "MAE": 0, "RMSE": 0, "R2_wt": 2, "MAE_wt": 0, "RMSE_wt": 0}
metric_dicti = {"NRMSE": 2, "R2": 2, "MAE": 0, "RMSE": 0}
metric_translate_traj = {"Euclid": "Euclidean distance", "R2": "$R^{2}$ (%)", "MAE": "MAE", "RMSE": "RMSE", "R2_wt": "$R^{2}$ (%) (time)", "MAE_wt": "MAE (time)", "RMSE_wt": "RMSE (time)"}
metric_translate = {"NRMSE": "NRMSE (%)", "R2": "$R^{2} (%)$", "MAE": "MAE", "RMSE": "RMSE"}

list_ws = [2, 3, 4, 5, 10, 20, 30] 
list_ws_short = [2, 5, 10, 20, 30]
 
sf1, sf2 = 5, 5
for nf1 in range(sf1):
    dicti_all_latest[nf1] = dict()
    for nf2 in range(sf2):
        dicti_all_latest[nf1][nf2] = dict()
        for varname in dicti_all[nf1][nf2]:
            dicti_all_latest[nf1][nf2][varname] = dict()
            for model_name_use in ord_metric:
                dicti_all_latest[nf1][nf2][varname][model_name_use] = dict()
                for val_ws in list_ws:
                    dicti_all_latest[nf1][nf2][varname][model_name_use][str(val_ws)] = dict()
                    for metric_name_use in list(metric_dicti.keys()):
                        vv = dicti_all[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use]
                        if model_name_use in dicti_all_ws[nf1][nf2][varname]:
                            vv = dicti_all_ws[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use]
                        dicti_all_latest[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use] = vv
                      
save_object("dicti_all_latest", dicti_all_latest)

for nf1 in range(sf1):
    dicti_all_traj_latest[nf1] = dict()
    for nf2 in range(sf2):
        dicti_all_traj_latest[nf1][nf2] = dict()
        for varname in dicti_all_traj[nf1][nf2]:
            dicti_all_traj_latest[nf1][nf2][varname] = dict()
            for model_name_use in ord_metric_traj:
                dicti_all_traj_latest[nf1][nf2][varname][model_name_use] = dict()
                for val_ws in list_ws:
                    dicti_all_traj_latest[nf1][nf2][varname][model_name_use][str(val_ws)] = dict()
                    for metric_name_use in list(metric_dicti_traj.keys()):
                        vv = dicti_all_traj[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use]
                        if model_name_use in dicti_all_traj_ws[nf1][nf2][varname]:
                            vv = dicti_all_traj_ws[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use]
                        dicti_all_traj_latest[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use] = vv

save_object("dicti_all_traj_latest", dicti_all_traj_latest)

dicti_all_latest_short = dict()
dicti_all_traj_latest_short = dict()

dicti_all_latest_avg = dict()
dicti_all_traj_latest_avg = dict()

dicti_all_latest_std = dict()
dicti_all_traj_latest_std = dict()

dicti_all_latest_by_test_short = dict()
dicti_all_traj_latest_by_test_short = dict()

dicti_all_latest_by_test_avg = dict()
dicti_all_traj_latest_by_test_avg = dict()

dicti_all_latest_by_test_std = dict()
dicti_all_traj_latest_by_test_std = dict()

for varname in dicti_all[0][0]:
    dicti_all_latest_short[varname] = dict()
    dicti_all_latest_avg[varname] = dict()
    dicti_all_latest_std[varname] = dict()
    dicti_all_latest_by_test_short[varname] = dict()
    dicti_all_latest_by_test_avg[varname] = dict()
    dicti_all_latest_by_test_std[varname] = dict()
    for model_name_use in ord_metric:
        dicti_all_latest_short[varname][model_name_use] = dict()
        dicti_all_latest_avg[varname][model_name_use] = dict()
        dicti_all_latest_std[varname][model_name_use] = dict()
        dicti_all_latest_by_test_short[varname][model_name_use] = dict()
        dicti_all_latest_by_test_avg[varname][model_name_use] = dict()
        dicti_all_latest_by_test_std[varname][model_name_use] = dict()
        for val_ws in list_ws:
            dicti_all_latest_short[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_latest_avg[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_latest_std[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_latest_by_test_short[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_latest_by_test_std[varname][model_name_use][str(val_ws)] = dict()
            for metric_name_use in list(metric_dicti.keys()):
                arr = []
                dicti_all_latest_by_test_short[varname][model_name_use][str(val_ws)][metric_name_use] = dict()
                dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use] = dict()
                dicti_all_latest_by_test_std[varname][model_name_use][str(val_ws)][metric_name_use] = dict()
                for nf1 in range(sf1):
                    arr_test = []
                    for nf2 in range(sf2):
                        arr.append(dicti_all_latest[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use])
                        arr_test.append(dicti_all_latest[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use])
                    dicti_all_latest_by_test_short[varname][model_name_use][str(val_ws)][metric_name_use][nf1] = arr_test
                    dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][nf1] = np.mean(arr_test)
                    dicti_all_latest_by_test_std[varname][model_name_use][str(val_ws)][metric_name_use][nf1] = np.std(arr_test)
                dicti_all_latest_short[varname][model_name_use][str(val_ws)][metric_name_use] = arr
                dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use] = np.mean(arr)
                dicti_all_latest_std[varname][model_name_use][str(val_ws)][metric_name_use] = np.std(arr)

save_object("dicti_all_latest_short", dicti_all_latest_short)
save_object("dicti_all_latest_avg", dicti_all_latest_avg)
save_object("dicti_all_latest_std", dicti_all_latest_std)
save_object("dicti_all_latest_by_test_short", dicti_all_latest_by_test_short)
save_object("dicti_all_latest_by_test_avg", dicti_all_latest_by_test_avg)
save_object("dicti_all_latest_by_test_std", dicti_all_latest_by_test_std)

for varname in dicti_all_traj[0][0]:
    dicti_all_traj_latest_short[varname] = dict()
    dicti_all_traj_latest_avg[varname] = dict()
    dicti_all_traj_latest_std[varname] = dict()
    dicti_all_traj_latest_by_test_short[varname] = dict()
    dicti_all_traj_latest_by_test_avg[varname] = dict()
    dicti_all_traj_latest_by_test_std[varname] = dict()
    for model_name_use in ord_metric_traj:
        dicti_all_traj_latest_short[varname][model_name_use] = dict()
        dicti_all_traj_latest_avg[varname][model_name_use] = dict()
        dicti_all_traj_latest_std[varname][model_name_use] = dict()
        dicti_all_traj_latest_by_test_short[varname][model_name_use] = dict()
        dicti_all_traj_latest_by_test_avg[varname][model_name_use] = dict()
        dicti_all_traj_latest_by_test_std[varname][model_name_use] = dict()
        for val_ws in list_ws:
            dicti_all_traj_latest_short[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_traj_latest_std[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_traj_latest_by_test_short[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)] = dict()
            dicti_all_traj_latest_by_test_std[varname][model_name_use][str(val_ws)] = dict()
            for metric_name_use in list(metric_dicti_traj.keys()):
                arr = []
                dicti_all_traj_latest_by_test_short[varname][model_name_use][str(val_ws)][metric_name_use] = dict()
                dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use] = dict()
                dicti_all_traj_latest_by_test_std[varname][model_name_use][str(val_ws)][metric_name_use] = dict()
                for nf1 in range(sf1):
                    arr_test = []
                    for nf2 in range(sf2):
                        arr.append(dicti_all_traj_latest[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use])
                        arr_test.append(dicti_all_traj_latest[nf1][nf2][varname][model_name_use][str(val_ws)][metric_name_use])
                    dicti_all_traj_latest_by_test_short[varname][model_name_use][str(val_ws)][metric_name_use][nf1] = arr_test
                    dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][nf1] = np.mean(arr_test)
                    dicti_all_traj_latest_by_test_std[varname][model_name_use][str(val_ws)][metric_name_use][nf1] = np.std(arr_test)
                dicti_all_traj_latest_short[varname][model_name_use][str(val_ws)][metric_name_use] = arr
                dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use] = np.mean(arr)
                dicti_all_traj_latest_std[varname][model_name_use][str(val_ws)][metric_name_use] = np.std(arr)

save_object("dicti_all_traj_latest_short", dicti_all_traj_latest_short)
save_object("dicti_all_traj_latest_avg", dicti_all_traj_latest_avg)
save_object("dicti_all_traj_latest_std", dicti_all_traj_latest_std)
save_object("dicti_all_traj_latest_by_test_short", dicti_all_traj_latest_by_test_short)
save_object("dicti_all_traj_latest_by_test_avg", dicti_all_traj_latest_by_test_avg)
save_object("dicti_all_traj_latest_by_test_std", dicti_all_traj_latest_by_test_std)

dicti_my_title = {0: "",
                  1: "$1^{st}$",
                  2: "$2^{nd}$",
                  3: "$3^{rd}$",
                  4: "$4^{th}$",
                  5: "$5^{th}$"}

def my_table_print(use_table = True, use_plot = True, use_sizes = True, use_outliers = True, use_minmax = True, use_detail = True, use_single = True, use_vertical = True, use_horizontal = True, use_all = True, use_merged = True, use_test = 0, use_val = 0, use_std = True, use_var = True, use_traj = True):
    if use_val > 0 and use_test == 0:
        return
    print(use_test, use_val)
    metrictouse_traj = ["Euclid", "MAE", "R2"]
    vartouse_traj = ["long speed actual dir", "long no abs"]
    translate_varname_traj = {"long speed ones dir": "speed, heading, a fixed one-second time interval",
                        "long speed dir": "speed, heading, time intervals",
                        "long speed actual dir": "speed, heading, the actual time interval",
                        "long no abs": "$x$ and $y$ offset"}
    
    metrictouse_var = ["MAE", "R2"]
    vartouse_var = ["direction", "speed", "longitude_no_abs", "latitude_no_abs"]
    translate_varname_var = {"direction": "heading", "speed": "speed", "longitude_no_abs": "$x$ offset", "latitude_no_abs": "$y$ offset", "time": "time intervals"}
        
    if use_table:
        total_errs = set()
        total_errs2 = dict()
        supposed_val = dict()

        my_title_replace = "k-fold testing datasets"
        if use_val == 0:
            if use_test > 0:
                my_title_replace = dicti_my_title[use_test] + " k-fold testing dataset"
        else:
            use_std = False
            my_title_replace = dicti_my_title[use_test] + " testing dataset, using the " + dicti_my_title[use_val] + " validation dataset,"

        if use_var:
            start_of_table = "\\begin{table}[!ht]\n\t\\centering\n\t\\resizebox{\linewidth}{!}{"
            end_of_table = "\t\t\\end{tabular}\n\t}\n\t\\caption{The average METRICNAME across k-fold validation datasets, with standard deviation in brackets, for the VARNAME estimated on the MYTITLE by different RNN models, and forecasting times.}\n\t\\label{tab:val_VARNAME_METRICNAME}\n\\end{table}\n"
            end_of_table = end_of_table.replace("MYTITLE", my_title_replace)
            if not use_std:
                end_of_table = end_of_table.replace(",with standard deviation in brackets,", "")
            if use_val > 0 and use_test > 0:
                end_of_table = end_of_table.replace("The average ", "")
                end_of_table = end_of_table.replace(" across k-fold validation datasets, with standard deviation in brackets,", "")
            all_metric_str = ""
            for metric_name_use in metrictouse_var:
                all_var_str = ""
                for varname in vartouse_var:
                    duplicate_val_all = True
                    duplicate_val = True
                    too_small = True
                    mul_metric = 0
                    rv_metric = 2
                    while too_small or duplicate_val_all:
                        errs = set()
                        set_values_all = set()
                        set_values = dict()
                        for val_ws in list_ws:
                            set_values[val_ws] = set()
                        max_col = dict()
                        for val_ws in list_ws:
                            max_col[val_ws] = (-MAXVALTOTAL, 0, metric_name_use)
                        min_col = dict()
                        for val_ws in list_ws:
                            min_col[val_ws] = (MAXVALTOTAL, 0, metric_name_use)
                        duplicate_val_all = False
                        duplicate_val = False
                        too_small = False
                        str_pr = ""
                        first_line = metric_name_use + " " + varname + " 10^{" + str(mul_metric) + "} " + str(rv_metric)
                        first_line = "\t\t\\begin{tabular}{|c|} \\hline\n\t\t\tModel"
                        longc = "c"
                        for model_name_use in ord_metric:
                            for val_ws in list_ws:
                                first_line += " & $" + str(val_ws) + "$s"
                                longc += "|c"
                            break
                        first_line = first_line.replace("{|c|}", "{|"+ longc + "|}")
                        for model_name_use in ord_metric:
                            if "offsets" in model_name_use:
                                continue
                            if use_std:
                                str_pr += "\t\t\t\multirow{2}{*}{"
                            else:
                                str_pr += "\t\t\t"
                            str_pr += model_name_use.replace("_", " ").replace(" 256", "").replace(" longlat speed direction", "")
                            if use_std:
                                str_pr += "}"
                            for val_ws in list_ws:
                                if use_val == 0:
                                    if use_test == 0:
                                        vv = dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]  
                                        vv2 = dicti_all_latest_std[varname][model_name_use][str(val_ws)][metric_name_use]  
                                    else:
                                        vv = dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1]
                                        vv2 = dicti_all_latest_by_test_std[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1] 
                                else:
                                    vv = dicti_all_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]
                                    vv2 = dicti_all_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]
                                vv = np.round(vv * (10 ** metric_dicti[metric_name_use]) * (10 ** mul_metric), rv_metric)
                                vv2 = np.round(vv2 * (10 ** metric_dicti[metric_name_use]) * (10 ** mul_metric), rv_metric)
                                old_str = vv
                                if "e+" in str(vv):
                                    parts_12 = str(vv).split("e+")
                                    main_part = float(parts_12[0])
                                    exp_part = int(parts_12[1])
                                    vv = str(np.round(main_part, rv_metric)) + " \\times 10^{" + str(exp_part) + "}"
                                    errs.add((varname, model_name_use, str(val_ws), metric_name_use, old_str, vv))
                                if "e+" in str(vv2):
                                    old_str2 = vv2
                                    parts_12 = str(vv2).split("e+")
                                    main_part = float(parts_12[0])
                                    exp_part = int(parts_12[1])
                                    vv2 = str(np.round(main_part, rv_metric)) + " \\times 10^{" + str(exp_part) + "}"
                                    errs.add((varname, model_name_use, str(val_ws), metric_name_use, old_str2, vv2))
                                str_pr += " & $" + str(vv) + "$"
                                vv = old_str
                                if vv in set_values[val_ws]:
                                    duplicate_val = True
                                if vv in set_values_all:
                                    duplicate_val_all = True
                                if "$0." in str_pr:
                                    too_small = True
                                set_values[val_ws].add(vv)
                                set_values_all.add(vv)
                                if vv > max_col[val_ws][0]:
                                    max_col[val_ws] = (vv, vv2, model_name_use)
                                if vv < min_col[val_ws][0]:
                                    min_col[val_ws] = (vv, vv2, model_name_use)
                            if use_std:
                                str_pr += " \\\\\n"
                                str_pr += "\t\t\t"
                                for val_ws in list_ws: 
                                    if use_val == 0:
                                        if use_test == 0:
                                            vv = dicti_all_latest_std[varname][model_name_use][str(val_ws)][metric_name_use]  
                                        else:
                                            vv = dicti_all_latest_by_test_std[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1]
                                    else:
                                        vv = dicti_all_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]                            
                                    vv = np.round(vv * (10 ** metric_dicti[metric_name_use]) * (10 ** mul_metric), rv_metric)
                                    if "e+" in str(vv):
                                        old_str = vv
                                        parts_12 = str(vv).split("e+")
                                        main_part = float(parts_12[0])
                                        exp_part = int(parts_12[1])
                                        vv = str(np.round(main_part, rv_metric)) + " \\times 10^{" + str(exp_part) + "}"
                                        errs.add((varname, model_name_use, str(val_ws), metric_name_use, old_str, vv))
                                    str_pr += " & ($" + str(vv) + "$)"
                            str_pr += " \\\\ \\hline\n"
                        if "R2" not in metric_name_use and "NRMSE" not in metric_name_use:
                            if too_small:
                                mul_metric += 1
                                rv_metric = 2
                            elif duplicate_val_all:
                                rv_metric += 1
                        else: 
                            rv_metric += 1
                        if ("R2" in metric_name_use or "NRMSE" in metric_name_use) and (rv_metric > 3 or mul_metric > 3):
                            break
                        if rv_metric > 3 or mul_metric > 6:
                            break
                    supposed_val[metric_name_use + "_" + varname] = 0
                    if "R2" in metric_name_use:
                        for val_ws in list_ws:
                            print(metric_name_use + " " + varname.replace("_", " "), val_ws, max_col[val_ws], str_pr.count("$" + str(max_col[val_ws][0]) + "$"))
                            supposed_val[metric_name_use + "_" + varname] += 1 + use_std * 1
                            str_pr = str_pr.replace("$" + str(max_col[val_ws][0]) + "$", "$\\mathbf{" + str(max_col[val_ws][0]) + "}$") 
                            str_pr_by_rows = str_pr.split("\n")
                            old_next_row = ""
                            new_next_row = ""
                            for r_ix in range(len(str_pr_by_rows) - 1):
                                curr_row = str_pr_by_rows[r_ix]
                                next_row = str_pr_by_rows[r_ix + 1]
                                if "$\\mathbf{" + str(max_col[val_ws][0]) + "}$" in curr_row:
                                    old_next_row = next_row
                                    new_next_row = next_row.replace("($" + str(max_col[val_ws][1]) + "$)", "\\textbf{(}$\\mathbf{" + str(max_col[val_ws][1]) + "}$\\textbf{)}")
                            str_pr = str_pr.replace(old_next_row, new_next_row) 
                    else:
                        for val_ws in list_ws:
                            print(metric_name_use + " " + varname.replace("_", " "), val_ws, min_col[val_ws], str_pr.count("$" + str(min_col[val_ws][0]) + "$"))
                            supposed_val[metric_name_use + "_" + varname] += 1 + use_std * 1
                            str_pr = str_pr.replace("$" + str(min_col[val_ws][0]) + "$", "$\\mathbf{" + str(min_col[val_ws][0]) + "}$")
                            str_pr_by_rows = str_pr.split("\n")
                            old_next_row = ""
                            new_next_row = ""
                            for r_ix in range(len(str_pr_by_rows) - 1):
                                curr_row = str_pr_by_rows[r_ix]
                                next_row = str_pr_by_rows[r_ix + 1]
                                if "$\\mathbf{" + str(min_col[val_ws][0]) + "}$" in curr_row:
                                    old_next_row = next_row
                                    new_next_row = next_row.replace("($" + str(min_col[val_ws][1]) + "$)", "\\textbf{(}$\\mathbf{" + str(min_col[val_ws][1]) + "}$\\textbf{)}")
                            str_pr = str_pr.replace(old_next_row, new_next_row) 
                    newend = end_of_table.replace("METRICNAME", metric_name_use).replace("VARNAME_", varname + "_").replace("NRMSE ", "NRMSE (\%) ").replace("R2 ", "$R^{2}$ (\%) ").replace("VARNAME ", translate_varname_var[varname] + " ")
                    if "R2" not in metric_name_use and "NRMSE" not in metric_name_use and mul_metric != 0:
                        newend = newend.replace(metric_name_use + " ", metric_name_use + " ($\\times 10^{-" + str(mul_metric) + "}$) ")
                    #print(start_of_table)
                    #print(first_line + " \\\\ \\hline")
                    #print(str_pr + newend)
                    file_open = open("latest_plot/all_var_" + metric_name_use + "_" + varname + "_test.tex", "w")
                    file_open.write(start_of_table + "\n" + first_line + " \\\\ \\hline\n" + str_pr + newend[:-1])
                    file_open.close()
                    all_var_str += start_of_table + "\n" + first_line + " \\\\ \\hline\n" + str_pr + newend + "\n"
                    for e in errs:
                        total_errs.add(e)
                    total_errs2[metric_name_use + "_" + varname] = str_pr.count("mathbf")
                file_open = open("latest_plot/all_var_" + metric_name_use + "_test.tex", "w")
                file_open.write(all_var_str[:-2])
                file_open.close()
                all_metric_str += all_var_str
            file_open = open("latest_plot/all_var_all_metric_test.tex", "w")
            file_open.write(all_metric_str[:-2])
            file_open.close()

        if use_traj:
            start_of_table = "\\begin{table}[!ht]\n\t\\centering\n\t\\resizebox{\linewidth}{!}{"
            end_of_table = "\t\t\\end{tabular}\n\t}\n\t\\caption{The average METRICNAME across k-fold validation datasets, with standard deviation in brackets, for the trajectories in the MYTITLE estimated using VARNAME, different RNN models, and forecasting times.}\n\t\\label{tab:val_VARNAME_METRICNAME}\n\\end{table}\n"
            end_of_table = end_of_table.replace("MYTITLE", my_title_replace)
            if not use_std:
                end_of_table = end_of_table.replace(",with standard deviation in brackets,", "")
            if use_val > 0 and use_test > 0:
                end_of_table = end_of_table.replace("The average ", "")
                end_of_table = end_of_table.replace(" across k-fold validation datasets, with standard deviation in brackets,", "")
            all_metric_str = ""
            for metric_name_use in metrictouse_traj:
                all_var_str = ""
                for varname in vartouse_traj:
                    duplicate_val_all = True
                    duplicate_val = True
                    too_small = True
                    mul_metric = 0
                    rv_metric = 2
                    while too_small or duplicate_val_all:
                        errs = set()
                        set_values_all = set()
                        set_values = dict()
                        for val_ws in list_ws:
                            set_values[val_ws] = set()
                        max_col = dict()
                        for val_ws in list_ws:
                            max_col[val_ws] = (-MAXVALTOTAL, 0, metric_name_use)
                        min_col = dict()
                        for val_ws in list_ws:
                            min_col[val_ws] = (MAXVALTOTAL, 0, metric_name_use)
                        duplicate_val_all = False
                        duplicate_val = False
                        too_small = False
                        str_pr = ""
                        first_line = metric_name_use + " " + varname + " 10^{" + str(mul_metric) + "} " + str(rv_metric)
                        first_line = "\t\t\\begin{tabular}{|c|} \\hline\n\t\t\tModel"
                        longc = "c"
                        for model_name_use in ord_metric:
                            for val_ws in list_ws:
                                first_line += " & $" + str(val_ws) + "$s"
                                longc += "|c"
                            break
                        first_line = first_line.replace("{|c|}", "{|"+ longc + "|}")
                        for model_name_use in ord_metric_traj:
                            if "offsets" in model_name_use:
                                continue
                            if use_std:
                                str_pr += "\t\t\t\multirow{2}{*}{"
                            else:
                                str_pr += "\t\t\t"
                            str_pr += model_name_use.replace("_", " ").replace(" 256", "").replace(" longlat speed direction", "")
                            if use_std:
                                str_pr += "}"
                            for val_ws in list_ws: 
                                if use_val == 0:
                                    if use_test == 0:
                                        vv = dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]  
                                        vv2 = dicti_all_traj_latest_std[varname][model_name_use][str(val_ws)][metric_name_use]  
                                    else:
                                        vv = dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1]
                                        vv2 = dicti_all_traj_latest_by_test_std[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1] 
                                else:
                                    vv = dicti_all_traj_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]
                                    vv2 = dicti_all_traj_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]
                                vv = np.round(vv * (10 ** metric_dicti_traj[metric_name_use]) * (10 ** mul_metric), rv_metric)
                                vv2 = np.round(vv2 * (10 ** metric_dicti_traj[metric_name_use]) * (10 ** mul_metric), rv_metric)
                                old_str = vv
                                if "e+" in str(vv):
                                    parts_12 = str(vv).split("e+")
                                    main_part = float(parts_12[0])
                                    exp_part = int(parts_12[1])
                                    vv = str(np.round(main_part, rv_metric)) + " \\times 10^{" + str(exp_part) + "}"
                                    errs.add((varname, model_name_use, str(val_ws), metric_name_use, old_str, vv))
                                if "e+" in str(vv2):
                                    old_str2 = vv2
                                    parts_12 = str(vv2).split("e+")
                                    main_part = float(parts_12[0])
                                    exp_part = int(parts_12[1])
                                    vv2 = str(np.round(main_part, rv_metric)) + " \\times 10^{" + str(exp_part) + "}"
                                    errs.add((varname, model_name_use, str(val_ws), metric_name_use, old_str2, vv2))
                                str_pr += " & $" + str(vv) + "$"
                                vv = old_str
                                if vv in set_values[val_ws]:
                                    duplicate_val = True
                                if vv in set_values_all:
                                    duplicate_val_all = True
                                if "$0." in str_pr:
                                    too_small = True
                                set_values[val_ws].add(vv)
                                set_values_all.add(vv)
                                if vv > max_col[val_ws][0]:
                                    max_col[val_ws] = (vv, vv2, model_name_use)
                                if vv < min_col[val_ws][0]:
                                    min_col[val_ws] = (vv, vv2, model_name_use)
                            if use_std:
                                str_pr += " \\\\\n"
                                str_pr += "\t\t\t"
                                for val_ws in list_ws: 
                                    if use_val == 0:
                                        if use_test == 0:
                                            vv = dicti_all_traj_latest_std[varname][model_name_use][str(val_ws)][metric_name_use]  
                                        else:
                                            vv = dicti_all_traj_latest_by_test_std[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1]
                                    else:
                                        vv = dicti_all_traj_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]                            
                                    vv = np.round(vv * (10 ** metric_dicti_traj[metric_name_use]) * (10 ** mul_metric), rv_metric)
                                    if "e+" in str(vv):
                                        old_str = vv
                                        parts_12 = str(vv).split("e+")
                                        main_part = float(parts_12[0])
                                        exp_part = int(parts_12[1])
                                        vv = str(np.round(main_part, rv_metric)) + " \\times 10^{" + str(exp_part) + "}"
                                        errs.add((varname, model_name_use, str(val_ws), metric_name_use, old_str, vv))
                                    str_pr += " & ($" + str(vv) + "$)"
                            str_pr += " \\\\ \\hline\n"
                        if "R2" not in metric_name_use and "NRMSE" not in metric_name_use:
                            if too_small:
                                mul_metric += 1
                                rv_metric = 2
                            elif duplicate_val_all:
                                rv_metric += 1
                        else: 
                            rv_metric += 1
                        if ("R2" in metric_name_use or "NRMSE" in metric_name_use) and (rv_metric > 3 or mul_metric > 3):
                            break
                        if rv_metric > 3 or mul_metric > 6:
                            break
                    supposed_val[metric_name_use + "_" + varname] = 0
                    if "R2" in metric_name_use:
                        for val_ws in list_ws:
                            print(metric_name_use + " " + varname.replace("_", " "), val_ws, max_col[val_ws], str_pr.count("$" + str(max_col[val_ws][0]) + "$"))
                            supposed_val[metric_name_use + "_" + varname] += 1 + use_std * 1
                            str_pr = str_pr.replace("$" + str(max_col[val_ws][0]) + "$", "$\\mathbf{" + str(max_col[val_ws][0]) + "}$") 
                            str_pr_by_rows = str_pr.split("\n")
                            old_next_row = ""
                            new_next_row = ""
                            for r_ix in range(len(str_pr_by_rows) - 1):
                                curr_row = str_pr_by_rows[r_ix]
                                next_row = str_pr_by_rows[r_ix + 1]
                                if "$\\mathbf{" + str(max_col[val_ws][0]) + "}$" in curr_row:
                                    old_next_row = next_row
                                    new_next_row = next_row.replace("($" + str(max_col[val_ws][1]) + "$)", "\\textbf{(}$\\mathbf{" + str(max_col[val_ws][1]) + "}$\\textbf{)}")
                            str_pr = str_pr.replace(old_next_row, new_next_row) 
                    else:
                        for val_ws in list_ws:
                            print(metric_name_use + " " + varname.replace("_", " "), val_ws, min_col[val_ws], str_pr.count("$" + str(min_col[val_ws][0]) + "$"))
                            supposed_val[metric_name_use + "_" + varname] += 1 + use_std * 1
                            str_pr = str_pr.replace("$" + str(min_col[val_ws][0]) + "$", "$\\mathbf{" + str(min_col[val_ws][0]) + "}$")
                            str_pr_by_rows = str_pr.split("\n")
                            old_next_row = ""
                            new_next_row = ""
                            for r_ix in range(len(str_pr_by_rows) - 1):
                                curr_row = str_pr_by_rows[r_ix]
                                next_row = str_pr_by_rows[r_ix + 1]
                                if "$\\mathbf{" + str(min_col[val_ws][0]) + "}$" in curr_row:
                                    old_next_row = next_row
                                    new_next_row = next_row.replace("($" + str(min_col[val_ws][1]) + "$)", "\\textbf{(}$\\mathbf{" + str(min_col[val_ws][1]) + "}$\\textbf{)}")
                            str_pr = str_pr.replace(old_next_row, new_next_row)
                    newend = end_of_table.replace("METRICNAME", metric_name_use).replace("VARNAME_", varname.replace(" ", "_") + "_").replace("NRMSE ", "NRMSE (\%) ").replace("R2 ", "$R^{2}$ (\%) ").replace("VARNAME", translate_varname_traj[varname])
                    if "R2" not in metric_name_use and "NRMSE" not in metric_name_use and mul_metric != 0:
                        newend = newend.replace(metric_name_use + " ", metric_name_use + " ($\\times 10^{-" + str(mul_metric) + "}$) ")
                    if "wt" in metric_name_use:
                        newend = newend.replace("_wt", "").replace("trajectories", "trajectories and time stamps")
                    #print(start_of_table)
                    #print(first_line + " \\\\ \\hline")
                    #print(str_pr + newend.replace("Euclid ", "Euclidean distance "))
                    file_open = open("latest_plot/all_traj_" + metric_name_use + "_" + varname + "_test.tex", "w")
                    file_open.write(start_of_table + "\n" + first_line + " \\\\ \\hline\n" + str_pr + newend.replace("Euclid ", "Euclidean distance ")[:-1])
                    file_open.close()
                    all_var_str += start_of_table + "\n" + first_line + " \\\\ \\hline\n" + str_pr + newend.replace("Euclid ", "Euclidean distance ") + "\n"
                    for e in errs:
                        total_errs.add(e)
                    total_errs2[metric_name_use + "_" + varname] = str_pr.count("mathbf")
                file_open = open("latest_plot/all_traj_" + metric_name_use + "_test.tex", "w")
                file_open.write(all_var_str[:-2])
                file_open.close()
                all_metric_str += all_var_str
            file_open = open("latest_plot/all_traj_all_metric_test.tex", "w")
            file_open.write(all_metric_str[:-2])
            file_open.close()

        errs2 = set()
        errs3 = set()
        errs4 = dict()
        for e in total_errs:
            errs2.add((e[1], e[2]))
            errs3.add((e[0], e[1], e[2]))
            if (e[0], e[1], e[2], e[3]) not in errs4:
                errs4[(e[0], e[1], e[2], e[3])] = set()
            errs4[(e[0], e[1], e[2], e[3])].add((e[4], e[5]))
        #print(errs4)

        for model_name_use_val_ws in errs2:
            model_name_use, val_ws = model_name_use_val_ws
            print(model_name_use, val_ws)
            for varname in dicti_all_traj_latest_avg:
                #if (varname, model_name_use, val_ws) not in errs3:
                    #continue
                for metric_name_use in dicti_all_traj_latest_avg[varname][model_name_use][val_ws]:
                    if (varname, model_name_use, val_ws, metric_name_use) not in errs4:
                        continue
                    print(varname, metric_name_use, dicti_all_traj_latest_avg[varname][model_name_use][val_ws][metric_name_use], dicti_all_traj_latest_std[varname][model_name_use][val_ws][metric_name_use])
                    for v in errs4[(varname, model_name_use, val_ws, metric_name_use)]:
                        print(v)
                    #print(dicti_all_traj_latest_short[varname][model_name_use][val_ws][metric_name_use])
            for varname in dicti_all_latest_avg:
                #if (varname, model_name_use, val_ws) not in errs3:
                    #continue
                for metric_name_use in dicti_all_latest_avg[varname][model_name_use][val_ws]:
                    if (varname, model_name_use, val_ws, metric_name_use) not in errs4:
                        continue
                    print(varname, metric_name_use, dicti_all_latest_avg[varname][model_name_use][val_ws][metric_name_use], dicti_all_latest_std[varname][model_name_use][val_ws][metric_name_use])
                    for v in errs4[(varname, model_name_use, val_ws, metric_name_use)]:
                        print(v)
                    #print(dicti_all_latest_short[varname][model_name_use][val_ws][metric_name_use])

        for v in total_errs2:
            if total_errs2[v] != supposed_val[v]:
                print(v, total_errs2[v], supposed_val[v])
  
    lnc = ["#000000", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
    lns = ["solid", "dotted", "dashed", "dashdot"]
                
    if use_plot:

        if not os.path.isdir("latest_plot/" + str(use_test) + "/" + str(use_val) + "/"):
            os.makedirs("latest_plot/" + str(use_test) + "/" + str(use_val) + "/")

        if use_var:
            if use_single:
                lims_for_plt = dict()
                for varname in vartouse_var:
                    for metric_name_use in metric_dicti:
                        lims_for_plt[varname + metric_name_use] = (MAXVALTOTAL, -MAXVALTOTAL)
                        for model_name_use in ord_metric:
                            for val_ws in list_ws:
                                if use_val == 0:
                                    if use_test == 0:
                                        val_use = dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]
                                    else:
                                        val_use = dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1]
                                else:
                                    val_use = dicti_all_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]
                                if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                     val_use = val_use * 100
                                if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use][0]:
                                    lims_for_plt[varname + metric_name_use] = (val_use, lims_for_plt[varname + metric_name_use][1])
                                if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use][1]:
                                    lims_for_plt[varname + metric_name_use] = (lims_for_plt[varname + metric_name_use][0], val_use)  
                for varname in vartouse_var:
                    for metric_name_use in metric_dicti:
                        plt.figure(figsize = (8, 6), dpi = 600)
                        newvar = varname
                        if varname in translate_varname_var:
                            newvar = translate_varname_var[varname]
                        if varname in translate_varname_traj:
                            newvar = translate_varname_traj[varname]
                        newmetric = metric_name_use
                        if metric_name_use in metric_translate:
                            newmetric = metric_translate[metric_name_use]
                        if metric_name_use in metric_translate_traj:
                            newmetric = metric_translate_traj[metric_name_use]
                        title_use = newvar.capitalize() + " " + newmetric
                        if use_val == 0:
                            if use_test > 0:
                                title_use += "\n" + dicti_my_title[use_test] + " testing dataset"
                        else:
                            title_use += "\n" + dicti_my_title[use_test] + " testing dataset " + dicti_my_title[use_val] + " validation dataset"
                        plt.title(title_use)
                        cix = 0
                        six = 0
                        for model_name_use in ord_metric:
                            plt_dict = []
                            for val_ws in list_ws:
                                if use_val == 0:
                                    if use_test == 0:
                                        plt_dict.append(dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use])
                                    else:
                                        plt_dict.append(dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1])
                                else:
                                    plt_dict.append(dicti_all_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use])
                            if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                plt_dict = [x * 100 for x in plt_dict]
                            plt.plot(list_ws, plt_dict, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                            cix += 1
                            if cix == len(lnc):
                                cix = 0
                                six += 1
                                if six == len(lns):
                                    six = 0
                        plt.xlim(min(list_ws), max(list_ws))
                        plt.ylim(lims_for_plt[varname + metric_name_use][0], lims_for_plt[varname + metric_name_use][1])
                        plt.xticks(list_ws)
                        ytick_vals = []
                        stepval = (lims_for_plt[varname + metric_name_use][1] - lims_for_plt[varname + metric_name_use][0]) / 10
                        for ytick_val in np.arange(lims_for_plt[varname + metric_name_use][0], lims_for_plt[varname + metric_name_use][1] + stepval, stepval):
                            ytick_vals.append(ytick_val)
                        plt.yticks(ytick_vals)
                        plt.xlabel("Forecasting time")
                        plt.ylabel(newmetric)
                        plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -0.35))
                        plt.savefig("latest_plot/" + str(use_test) + "/" + str(use_val) + "/" + varname + "_" + metric_name_use + "_" + str(use_test) + "_" + str(use_val) + ".png", bbox_inches = "tight")
                        plt.close()

            if use_test == 0 and use_val == 0:
                if use_merged:
                    lims_for_plt = dict()
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            lims_for_plt[varname + metric_name_use] = (MAXVALTOTAL, -MAXVALTOTAL)
                            for model_name_use in ord_metric:
                                for val_ws in list_ws:
                                    val_use = dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]
                                    if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                            val_use = val_use * 100
                                    if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use][0]:
                                        lims_for_plt[varname + metric_name_use] = (val_use, lims_for_plt[varname + metric_name_use][1])
                                    if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use][1]:
                                        lims_for_plt[varname + metric_name_use] = (lims_for_plt[varname + metric_name_use][0], val_use)  
                    for metric_name_use in metric_dicti:
                        tx = 0
                        plt.figure(figsize = (8, 6), dpi = 600)
                        for varname in vartouse_var:
                            newvar = varname
                            if varname in translate_varname_var:
                                newvar = translate_varname_var[varname]
                            if varname in translate_varname_traj:
                                newvar = translate_varname_traj[varname]
                            newmetric = metric_name_use
                            if metric_name_use in metric_translate:
                                newmetric = metric_translate[metric_name_use]
                            if metric_name_use in metric_translate_traj:
                                newmetric = metric_translate_traj[metric_name_use]
                            cix = 0
                            six = 0 
                            plt.subplot(5, 1, tx + 1)
                            plt.xlim(min(list_ws), max(list_ws))
                            plt.yticks([lims_for_plt[varname + metric_name_use][0], (lims_for_plt[varname + metric_name_use][0] + lims_for_plt[varname + metric_name_use][1]) / 2, lims_for_plt[varname + metric_name_use][1]])
                            plt.ylim(lims_for_plt[varname + metric_name_use][0], lims_for_plt[varname + metric_name_use][1])
                            if tx == 0:
                                plt.title(newmetric)
                            for model_name_use in ord_metric:
                                plt_dict = []
                                for val_ws in list_ws:
                                    plt_dict.append(dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use])
                                if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                    plt_dict = [x * 100 for x in plt_dict]
                                if tx == len(vartouse_var) - 1:    
                                    plt.plot(list_ws, plt_dict, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                                else:
                                    plt.plot(list_ws, plt_dict, color = lnc[cix], linestyle = lns[six])
                                cix += 1
                                if cix == len(lnc):
                                    cix = 0
                                    six += 1
                                    if six == len(lns):
                                        six = 0
                            if tx == len(vartouse_var) - 1:
                                plt.xticks(list_ws)
                                plt.xlabel("Forecasting time")
                                plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -2))
                            else:
                                plt.xticks([])
                            plt.ylabel(newvar.capitalize().replace(", the", ",\nthe").replace(" offset", "\noffset").replace(" interval", "\ninterval"))
                            tx += 1
                        plt.savefig("latest_plot/all_var_" + metric_name_use + "_test.png", bbox_inches = "tight")
                        plt.close()
                if use_horizontal:
                    lims_for_plt = dict()
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            for tn in range(5):
                                lims_for_plt[varname + metric_name_use + str(tn)] = (MAXVALTOTAL, -MAXVALTOTAL)
                                for model_name_use in ord_metric:
                                    for val_ws in list_ws:
                                        val_use = dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn]
                                        if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                             val_use = val_use * 100
                                        if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use + str(tn)][0]:
                                            lims_for_plt[varname + metric_name_use + str(tn)] = (val_use, lims_for_plt[varname + metric_name_use + str(tn)][1])
                                        if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use + str(tn)][1]:
                                            lims_for_plt[varname + metric_name_use + str(tn)] = (lims_for_plt[varname + metric_name_use + str(tn)][0], val_use)  
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            plt.figure(figsize = (8, 6), dpi = 600)
                            newvar = varname
                            if varname in translate_varname_var:
                                newvar = translate_varname_var[varname]
                            if varname in translate_varname_traj:
                                newvar = translate_varname_traj[varname]
                            newmetric = metric_name_use
                            if metric_name_use in metric_translate:
                                newmetric = metric_translate[metric_name_use]
                            if metric_name_use in metric_translate_traj:
                                newmetric = metric_translate_traj[metric_name_use]
                            for tn in range(5):
                                cix = 0
                                six = 0 
                                plt.subplot(5, 1, tn + 1)
                                plt.xlim(min(list_ws), max(list_ws))
                                plt.yticks([lims_for_plt[varname + metric_name_use + str(tn)][0], (lims_for_plt[varname + metric_name_use + str(tn)][0] + lims_for_plt[varname + metric_name_use + str(tn)][1]) / 2, lims_for_plt[varname + metric_name_use + str(tn)][1]])
                                plt.ylim(lims_for_plt[varname + metric_name_use + str(tn)][0], lims_for_plt[varname + metric_name_use + str(tn)][1])
                                if tn == 0:
                                    plt.title(newvar.capitalize() + " " + newmetric)
                                for model_name_use in ord_metric:
                                    plt_dict = []
                                    for val_ws in list_ws:
                                        plt_dict.append(dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn])
                                    if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                        plt_dict = [x * 100 for x in plt_dict]
                                    if tn == 4:    
                                        plt.plot(list_ws, plt_dict, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                                    else:
                                        plt.plot(list_ws, plt_dict, color = lnc[cix], linestyle = lns[six])
                                    cix += 1
                                    if cix == len(lnc):
                                        cix = 0
                                        six += 1
                                        if six == len(lns):
                                            six = 0
                                if tn == 4:
                                    plt.xticks(list_ws)
                                    plt.xlabel("Forecasting time")
                                    plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -2))
                                else:
                                    plt.xticks([])
                                plt.ylabel("Test " + str(tn + 1) + "\n" + newmetric.replace(" distance", "\ndistance").replace(" (time)", "\n(time)"))
                            plt.savefig("latest_plot/" + varname + "_" + metric_name_use + "_test.png", bbox_inches = "tight")
                            plt.close()
                if use_vertical: 
                    lims_for_plt = dict()
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            for tn in range(5):
                                lims_for_plt[varname + metric_name_use + str(tn)] = (MAXVALTOTAL, -MAXVALTOTAL)
                                for model_name_use in ord_metric:
                                    for val_ws in list_ws:
                                        val_use = dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn]
                                        if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                             val_use = val_use * 100
                                        if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use + str(tn)][0]:
                                            lims_for_plt[varname + metric_name_use + str(tn)] = (val_use, lims_for_plt[varname + metric_name_use + str(tn)][1])
                                        if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use + str(tn)][1]:
                                            lims_for_plt[varname + metric_name_use + str(tn)] = (lims_for_plt[varname + metric_name_use + str(tn)][0], val_use)       
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            plt.figure(figsize = (8, 6), dpi = 600)
                            newvar = varname
                            if varname in translate_varname_var:
                                newvar = translate_varname_var[varname]
                            if varname in translate_varname_traj:
                                newvar = translate_varname_traj[varname]
                            newmetric = metric_name_use
                            if metric_name_use in metric_translate:
                                newmetric = metric_translate[metric_name_use]
                            if metric_name_use in metric_translate_traj:
                                newmetric = metric_translate_traj[metric_name_use]
                            for tn in range(5):
                                cix = 0
                                six = 0 
                                plt.subplot(1, 5, tn + 1)
                                plt.ylim(min(list_ws), max(list_ws))
                                plt.xticks([lims_for_plt[varname + metric_name_use + str(tn)][0], lims_for_plt[varname + metric_name_use + str(tn)][0] + (lims_for_plt[varname + metric_name_use + str(tn)][1] - lims_for_plt[varname + metric_name_use + str(tn)][0]) * 0.6])
                                plt.xlim(lims_for_plt[varname + metric_name_use + str(tn)][0], lims_for_plt[varname + metric_name_use + str(tn)][1])
                                if tn == 2:
                                    plt.title(newvar.capitalize() + " " + newmetric)
                                for model_name_use in ord_metric:
                                    plt_dict = []
                                    for val_ws in list_ws:
                                        plt_dict.append(dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn])
                                    if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                        plt_dict = [x * 100 for x in plt_dict]
                                    if tn == 0:    
                                        plt.plot(plt_dict, list_ws, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                                    else:
                                        plt.plot(plt_dict, list_ws, color = lnc[cix], linestyle = lns[six])
                                    cix += 1
                                    if cix == len(lnc):
                                        cix = 0
                                        six += 1
                                        if six == len(lns):
                                            six = 0
                                if tn == 0:
                                    plt.yticks(list_ws)
                                    plt.ylabel("Forecasting time")
                                    plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -0.43))
                                else:
                                    plt.yticks([])
                                plt.xlabel(newmetric.replace(" distance", "\ndistance").replace(" (time)", "\n(time)") + "\nTest " + str(tn + 1))
                            plt.savefig("latest_plot/" + varname + "_" + metric_name_use + "_reverse_test.png", bbox_inches = "tight")
                            plt.close()
                if use_all:
                    lims_for_plt = dict()
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            for tn in range(5):
                                lims_for_plt[varname + metric_name_use + str(tn)] = dict()
                                for vn in range(5):
                                    lims_for_plt[varname + metric_name_use + str(tn)][vn] = (MAXVALTOTAL, -MAXVALTOTAL)
                                    for model_name_use in ord_metric:
                                        for val_ws in list_ws:
                                            val_use = dicti_all_latest[tn][vn][varname][model_name_use][str(val_ws)][metric_name_use]
                                            if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                                 val_use = val_use * 100
                                            if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use + str(tn)][vn][0]:
                                                lims_for_plt[varname + metric_name_use + str(tn)][vn] = (val_use, lims_for_plt[varname + metric_name_use + str(tn)][vn][1])
                                            if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use + str(tn)][vn][1]:
                                                lims_for_plt[varname + metric_name_use + str(tn)][vn] = (lims_for_plt[varname + metric_name_use + str(tn)][vn][0], val_use)
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            plt.figure(figsize = (8, 6), dpi = 600)
                            newvar = varname
                            if varname in translate_varname_var:
                                newvar = translate_varname_var[varname]
                            if varname in translate_varname_traj:
                                newvar = translate_varname_traj[varname]
                            newmetric = metric_name_use
                            if metric_name_use in metric_translate:
                                newmetric = metric_translate[metric_name_use]
                            if metric_name_use in metric_translate_traj:
                                newmetric = metric_translate_traj[metric_name_use]
                            for tn in range(5):
                                for vn in range(5):
                                    cix = 0
                                    six = 0 
                                    plt.subplot(5, 5, tn * 5 + vn + 1)
                                    plt.xlim(min(list_ws), max(list_ws))
                                    plt.ylim(lims_for_plt[varname + metric_name_use + str(tn)][vn][0], lims_for_plt[varname + metric_name_use + str(tn)][vn][1])
                                    if tn == 0 and vn == 2:
                                        plt.title(newvar.capitalize() + " " + newmetric)
                                    for model_name_use in ord_metric:
                                        plt_dict = []
                                        for val_ws in list_ws:
                                            plt_dict.append(dicti_all_latest[tn][vn][varname][model_name_use][str(val_ws)][metric_name_use])
                                        if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                            plt_dict = [x * 100 for x in plt_dict]
                                        if tn == 4 and vn == 0:    
                                            plt.plot(list_ws, plt_dict, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                                        else:
                                            plt.plot(list_ws, plt_dict, color = lnc[cix], linestyle = lns[six])
                                        cix += 1
                                        if cix == len(lnc):
                                            cix = 0
                                            six += 1
                                            if six == len(lns):
                                                six = 0
                                    if tn == 4:
                                        plt.xticks(list_ws_short)
                                        plt.xlabel("Forecasting time\nValidation " + str(vn + 1))
                                    else:
                                        plt.xticks([])
                                    if tn == 4 and vn == 0:
                                        plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -2.25))
                                    if vn == 0:
                                        plt.ylabel("Test " + str(tn + 1) + "\n" + newmetric.replace(" distance", "\ndistance").replace(" (time)", "\n(time)"))
                                        plt.yticks([lims_for_plt[varname + metric_name_use + str(tn)][vn][0], (lims_for_plt[varname + metric_name_use + str(tn)][vn][0] + lims_for_plt[varname + metric_name_use + str(tn)][vn][1]) / 2, lims_for_plt[varname + metric_name_use + str(tn)][vn][1]])
                                    else:
                                        plt.yticks([])
                            plt.savefig("latest_plot/" + varname + "_" + metric_name_use + "_all.png", bbox_inches = "tight")
                            plt.close()

        if use_traj:
            if use_single:
                lims_for_plt = dict()
                for varname in vartouse_traj:
                    for metric_name_use in metric_dicti_traj:
                        lims_for_plt[varname + metric_name_use] = (MAXVALTOTAL, -MAXVALTOTAL)
                        for model_name_use in ord_metric_traj:
                            for val_ws in list_ws:
                                if use_val == 0:
                                    if use_test == 0:
                                        val_use = dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]
                                    else:
                                        val_use = dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1]
                                else:
                                    val_use = dicti_all_traj_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]
                                if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                     val_use = val_use * 100
                                if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use][0]:
                                    lims_for_plt[varname + metric_name_use] = (val_use, lims_for_plt[varname + metric_name_use][1])
                                if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use][1]:
                                    lims_for_plt[varname + metric_name_use] = (lims_for_plt[varname + metric_name_use][0], val_use)  
                for varname in vartouse_traj:
                    for metric_name_use in metric_dicti_traj:
                        plt.figure(figsize = (8, 6), dpi = 600)
                        newvar = varname
                        if varname in translate_varname_var:
                            newvar = translate_varname_var[varname]
                        if varname in translate_varname_traj:
                            newvar = translate_varname_traj[varname]
                        newmetric = metric_name_use
                        if metric_name_use in metric_translate:
                            newmetric = metric_translate[metric_name_use]
                        if metric_name_use in metric_translate_traj:
                            newmetric = metric_translate_traj[metric_name_use]
                        title_use = newvar.capitalize() + " " + newmetric
                        if use_val == 0:
                            if use_test > 0:
                                title_use += "\n" + dicti_my_title[use_test] + " testing dataset"
                        else:
                            title_use += "\n" + dicti_my_title[use_test] + " testing dataset " + dicti_my_title[use_val] + " validation dataset"
                        plt.title(title_use)
                        cix = 0
                        six = 0
                        for model_name_use in ord_metric_traj:
                            plt_dict = []
                            for val_ws in list_ws:
                                if use_val == 0:
                                    if use_test == 0:
                                        plt_dict.append(dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use])
                                    else:
                                        plt_dict.append(dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1])
                                else:
                                    plt_dict.append(dicti_all_traj_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use])
                            if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                plt_dict = [x * 100 for x in plt_dict]
                            plt.plot(list_ws, plt_dict, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                            cix += 1
                            if cix == len(lnc):
                                cix = 0
                                six += 1
                                if six == len(lns):
                                    six = 0
                        plt.xlim(min(list_ws), max(list_ws))
                        plt.ylim(lims_for_plt[varname + metric_name_use][0], lims_for_plt[varname + metric_name_use][1])
                        plt.xticks(list_ws)
                        ytick_vals = []
                        stepval = (lims_for_plt[varname + metric_name_use][1] - lims_for_plt[varname + metric_name_use][0]) / 10
                        for ytick_val in np.arange(lims_for_plt[varname + metric_name_use][0], lims_for_plt[varname + metric_name_use][1] + stepval, stepval):
                            ytick_vals.append(ytick_val)
                        plt.yticks(ytick_vals)
                        plt.xlabel("Forecasting time")
                        plt.ylabel(newmetric)
                        plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -0.35))
                        plt.savefig("latest_plot/" + str(use_test) + "/" + str(use_val) + "/" + varname + "_" + metric_name_use + "_" + str(use_test) + "_" + str(use_val) + ".png", bbox_inches = "tight")
                        plt.close()

            if use_test == 0 and use_val == 0:
                if use_merged:
                    lims_for_plt = dict()
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            lims_for_plt[varname + metric_name_use] = (MAXVALTOTAL, -MAXVALTOTAL)
                            for model_name_use in ord_metric_traj:
                                for val_ws in list_ws:
                                    val_use = dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]
                                    if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                            val_use = val_use * 100
                                    if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use][0]:
                                        lims_for_plt[varname + metric_name_use] = (val_use, lims_for_plt[varname + metric_name_use][1])
                                    if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use][1]:
                                        lims_for_plt[varname + metric_name_use] = (lims_for_plt[varname + metric_name_use][0], val_use)  
                    for metric_name_use in metric_dicti_traj:
                        tx = 0
                        plt.figure(figsize = (8, 6), dpi = 600)
                        for varname in vartouse_traj:
                            newvar = varname
                            if varname in translate_varname_var:
                                newvar = translate_varname_var[varname]
                            if varname in translate_varname_traj:
                                newvar = translate_varname_traj[varname]
                            newmetric = metric_name_use
                            if metric_name_use in metric_translate:
                                newmetric = metric_translate[metric_name_use]
                            if metric_name_use in metric_translate_traj:
                                newmetric = metric_translate_traj[metric_name_use]
                            cix = 0
                            six = 0 
                            plt.subplot(5, 1, tx + 1)
                            plt.xlim(min(list_ws), max(list_ws))
                            plt.yticks([lims_for_plt[varname + metric_name_use][0], (lims_for_plt[varname + metric_name_use][0] + lims_for_plt[varname + metric_name_use][1]) / 2, lims_for_plt[varname + metric_name_use][1]])
                            plt.ylim(lims_for_plt[varname + metric_name_use][0], lims_for_plt[varname + metric_name_use][1])
                            if tx == 0:
                                plt.title(newmetric)
                            for model_name_use in ord_metric_traj:
                                plt_dict = []
                                for val_ws in list_ws:
                                    plt_dict.append(dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use])
                                if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                    plt_dict = [x * 100 for x in plt_dict]
                                if tx == len(vartouse_traj) - 1:    
                                    plt.plot(list_ws, plt_dict, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                                else:
                                    plt.plot(list_ws, plt_dict, color = lnc[cix], linestyle = lns[six])
                                cix += 1
                                if cix == len(lnc):
                                    cix = 0
                                    six += 1
                                    if six == len(lns):
                                        six = 0
                            if tx == len(vartouse_traj) - 1:
                                plt.xticks(list_ws)
                                plt.xlabel("Forecasting time")
                                plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -2))
                            else:
                                plt.xticks([])
                            plt.ylabel(newvar.capitalize().replace(", the", ",\nthe").replace(" offset", "\noffset").replace(" interval", "\ninterval"))
                            tx += 1
                        plt.savefig("latest_plot/all_traj_" + metric_name_use + "_test.png", bbox_inches = "tight")
                        plt.close()
                if use_horizontal:
                    lims_for_plt = dict()
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            for tn in range(5):
                                lims_for_plt[varname + metric_name_use + str(tn)] = (MAXVALTOTAL, -MAXVALTOTAL)
                                for model_name_use in ord_metric_traj:
                                    for val_ws in list_ws:
                                        val_use = dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn]
                                        if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                             val_use = val_use * 100
                                        if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use + str(tn)][0]:
                                            lims_for_plt[varname + metric_name_use + str(tn)] = (val_use, lims_for_plt[varname + metric_name_use + str(tn)][1])
                                        if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use + str(tn)][1]:
                                            lims_for_plt[varname + metric_name_use + str(tn)] = (lims_for_plt[varname + metric_name_use + str(tn)][0], val_use)
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            plt.figure(figsize = (8, 6), dpi = 600)
                            newvar = varname
                            if varname in translate_varname_var:
                                newvar = translate_varname_var[varname]
                            if varname in translate_varname_traj:
                                newvar = translate_varname_traj[varname]
                            newmetric = metric_name_use
                            if metric_name_use in metric_translate:
                                newmetric = metric_translate[metric_name_use]
                            if metric_name_use in metric_translate_traj:
                                newmetric = metric_translate_traj[metric_name_use]
                            for tn in range(5):
                                cix = 0
                                six = 0 
                                plt.subplot(5, 1, tn + 1)
                                plt.xlim(min(list_ws), max(list_ws))
                                plt.yticks([lims_for_plt[varname + metric_name_use + str(tn)][0], (lims_for_plt[varname + metric_name_use + str(tn)][0] + lims_for_plt[varname + metric_name_use + str(tn)][1]) / 2, lims_for_plt[varname + metric_name_use + str(tn)][1]])
                                plt.ylim(lims_for_plt[varname + metric_name_use + str(tn)][0], lims_for_plt[varname + metric_name_use + str(tn)][1])
                                if tn == 0:
                                    plt.title(newvar.capitalize() + " " + newmetric)
                                for model_name_use in ord_metric_traj:
                                    plt_dict = []
                                    for val_ws in list_ws:
                                        plt_dict.append(dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn])
                                    if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                        plt_dict = [x * 100 for x in plt_dict]
                                    if tn == 4:    
                                        plt.plot(list_ws, plt_dict, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                                    else:
                                        plt.plot(list_ws, plt_dict, color = lnc[cix], linestyle = lns[six])
                                    cix += 1
                                    if cix == len(lnc):
                                        cix = 0
                                        six += 1
                                        if six == len(lns):
                                            six = 0
                                if tn == 4:
                                    plt.xticks(list_ws)
                                    plt.xlabel("Forecasting time")
                                    plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -2))
                                else:
                                    plt.xticks([])
                                plt.ylabel("Test " + str(tn + 1) + "\n" + newmetric.replace(" distance", "\ndistance").replace(" (time)", "\n(time)"))
                            plt.savefig("latest_plot/" + varname + "_" + metric_name_use + "_test.png", bbox_inches = "tight")
                            plt.close()
                if use_vertical:      
                    lims_for_plt = dict()
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            for tn in range(5):
                                lims_for_plt[varname + metric_name_use + str(tn)] = (MAXVALTOTAL, -MAXVALTOTAL)
                                for model_name_use in ord_metric_traj:
                                    for val_ws in list_ws:
                                        val_use = dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn]
                                        if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                             val_use = val_use * 100
                                        if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use + str(tn)][0]:
                                            lims_for_plt[varname + metric_name_use + str(tn)] = (val_use, lims_for_plt[varname + metric_name_use + str(tn)][1])
                                        if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use + str(tn)][1]:
                                            lims_for_plt[varname + metric_name_use + str(tn)] = (lims_for_plt[varname + metric_name_use + str(tn)][0], val_use)  
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            plt.figure(figsize = (8, 6), dpi = 600)
                            newvar = varname
                            if varname in translate_varname_var:
                                newvar = translate_varname_var[varname]
                            if varname in translate_varname_traj:
                                newvar = translate_varname_traj[varname]
                            newmetric = metric_name_use
                            if metric_name_use in metric_translate:
                                newmetric = metric_translate[metric_name_use]
                            if metric_name_use in metric_translate_traj:
                                newmetric = metric_translate_traj[metric_name_use]
                            for tn in range(5):
                                cix = 0
                                six = 0 
                                plt.subplot(1, 5, tn + 1)
                                plt.ylim(min(list_ws), max(list_ws))
                                plt.xticks([lims_for_plt[varname + metric_name_use + str(tn)][0], lims_for_plt[varname + metric_name_use + str(tn)][0] + (lims_for_plt[varname + metric_name_use + str(tn)][1] - lims_for_plt[varname + metric_name_use + str(tn)][0]) * 0.6])
                                plt.xlim(lims_for_plt[varname + metric_name_use + str(tn)][0], lims_for_plt[varname + metric_name_use + str(tn)][1])
                                if tn == 2:
                                    plt.title(newvar.capitalize() + " " + newmetric)
                                for model_name_use in ord_metric_traj:
                                    plt_dict = []
                                    for val_ws in list_ws:
                                        plt_dict.append(dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn])
                                    if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                        plt_dict = [x * 100 for x in plt_dict]
                                    if tn == 0:    
                                        plt.plot(plt_dict, list_ws, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                                    else:
                                        plt.plot(plt_dict, list_ws, color = lnc[cix], linestyle = lns[six])
                                    cix += 1
                                    if cix == len(lnc):
                                        cix = 0
                                        six += 1
                                        if six == len(lns):
                                            six = 0
                                if tn == 0:
                                    plt.yticks(list_ws)
                                    plt.ylabel("Forecasting time")
                                    plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -0.43))
                                else:
                                    plt.yticks([])
                                plt.xlabel(newmetric.replace(" distance", "\ndistance").replace(" (time)", "\n(time)") + "\nTest " + str(tn + 1))
                            plt.savefig("latest_plot/" + varname + "_" + metric_name_use + "_reverse_test.png", bbox_inches = "tight")
                            plt.close()
                if use_all:
                    lims_for_plt = dict()
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            for tn in range(5):
                                lims_for_plt[varname + metric_name_use + str(tn)] = dict()
                                for vn in range(5):
                                    lims_for_plt[varname + metric_name_use + str(tn)][vn] = (MAXVALTOTAL, -MAXVALTOTAL)
                                    for model_name_use in ord_metric_traj:
                                        for val_ws in list_ws:
                                            val_use = dicti_all_traj_latest[tn][vn][varname][model_name_use][str(val_ws)][metric_name_use]
                                            if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                                 val_use = val_use * 100
                                            if abs(val_use) < TOPOFPLOT and val_use < lims_for_plt[varname + metric_name_use + str(tn)][vn][0]:
                                                lims_for_plt[varname + metric_name_use + str(tn)][vn] = (val_use, lims_for_plt[varname + metric_name_use + str(tn)][vn][1])
                                            if abs(val_use) < TOPOFPLOT and val_use > lims_for_plt[varname + metric_name_use + str(tn)][vn][1]:
                                                lims_for_plt[varname + metric_name_use + str(tn)][vn] = (lims_for_plt[varname + metric_name_use + str(tn)][vn][0], val_use)
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            plt.figure(figsize = (8, 6), dpi = 600)
                            newvar = varname
                            if varname in translate_varname_var:
                                newvar = translate_varname_var[varname]
                            if varname in translate_varname_traj:
                                newvar = translate_varname_traj[varname]
                            newmetric = metric_name_use
                            if metric_name_use in metric_translate:
                                newmetric = metric_translate[metric_name_use]
                            if metric_name_use in metric_translate_traj:
                                newmetric = metric_translate_traj[metric_name_use]
                            for tn in range(5):
                                for vn in range(5):
                                    cix = 0
                                    six = 0 
                                    plt.subplot(5, 5, tn * 5 + vn + 1)
                                    plt.xlim(min(list_ws), max(list_ws))
                                    plt.ylim(lims_for_plt[varname + metric_name_use + str(tn)][vn][0], lims_for_plt[varname + metric_name_use + str(tn)][vn][1])
                                    if tn == 0 and vn == 2:
                                        plt.title(newvar.capitalize() + " " + newmetric)
                                    for model_name_use in ord_metric_traj:
                                        plt_dict = []
                                        for val_ws in list_ws:
                                            plt_dict.append(dicti_all_traj_latest[tn][vn][varname][model_name_use][str(val_ws)][metric_name_use])
                                        if "R2" in metric_name_use or "NRMSE" in metric_name_use:
                                            plt_dict = [x * 100 for x in plt_dict]
                                        if tn == 4 and vn == 0:    
                                            plt.plot(list_ws, plt_dict, label = model_name_use.replace("UniTS", "Foundation").replace("_256", "").replace("_longlat_speed_direction", "").replace("_", " "), color = lnc[cix], linestyle = lns[six])
                                        else:
                                            plt.plot(list_ws, plt_dict, color = lnc[cix], linestyle = lns[six])
                                        cix += 1
                                        if cix == len(lnc):
                                            cix = 0
                                            six += 1
                                            if six == len(lns):
                                                six = 0
                                    if tn == 4:
                                        plt.xticks(list_ws_short)
                                        plt.xlabel("Forecasting time\nValidation " + str(vn + 1))
                                    else:
                                        plt.xticks([])
                                    if tn == 4 and vn == 0:
                                        plt.legend(ncol = 4, loc = "lower left", bbox_to_anchor = (0, -2.25))
                                    if vn == 0:
                                        plt.ylabel("Test " + str(tn + 1) + "\n" + newmetric.replace(" distance", "\ndistance").replace(" (time)", "\n(time)"))
                                        plt.yticks([lims_for_plt[varname + metric_name_use + str(tn)][vn][0], (lims_for_plt[varname + metric_name_use + str(tn)][vn][0] + lims_for_plt[varname + metric_name_use + str(tn)][vn][1]) / 2, lims_for_plt[varname + metric_name_use + str(tn)][vn][1]])
                                    else:
                                        plt.yticks([])
                            plt.savefig("latest_plot/" + varname + "_" + metric_name_use + "_all.png", bbox_inches = "tight")
                            plt.close()

    if use_sizes:
        print(use_test, use_val)
        best_dict_total_R2 = dict()
        best_dict_total_other = dict()
        best_dict_total = dict()
        best_dict_R2 = dict()
        best_dict_other = dict()
        best_dict = dict()
        for model_name_use in ord_metric:
            best_dict_total_R2[model_name_use] = []
            best_dict_total_other[model_name_use] = []
            best_dict_total[model_name_use] = []
            best_dict_R2[model_name_use] = []
            best_dict_other[model_name_use] = []
            best_dict[model_name_use] = []
                        
        if use_var:
            for varname in vartouse_var:
                for metric_name_use in metric_dicti:
                    for val_ws in list_ws:
                        min_model = ""
                        min_val = MAXVALTOTAL
                        max_model = ""
                        max_val = -MAXVALTOTAL
                        for model_name_use in ord_metric:
                            if use_val == 0:
                                if use_test == 0:
                                    val_use = dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]
                                else:
                                    val_use = dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1]
                            else:
                                val_use = dicti_all_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]
                            if val_use > max_val:
                                max_model = model_name_use
                                max_val = val_use
                            if val_use < min_val:
                                min_model = model_name_use
                                min_val = val_use
                        if "R2" in metric_name_use:
                            best_dict_total[max_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict[max_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict_total_R2[max_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict_R2[max_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                        else:
                            best_dict_total[min_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict[min_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict_total_other[min_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict_other[min_model].append(varname + " " + metric_name_use + " " + str(val_ws))

            print("vars")
            print("R2")
            for model_name_use in dict(sorted(best_dict_R2.items(), key = lambda x: len(x[1]), reverse = True)):
                print(model_name_use, len(best_dict_R2[model_name_use]), len(best_dict_R2[model_name_use]) / (len(vartouse_var) * sum(["R2" in x for x in metric_dicti]) * len(list_ws)) * 100)
                break
            print("other")
            for model_name_use in dict(sorted(best_dict_other.items(), key = lambda x: len(x[1]), reverse = True)):
                print(model_name_use, len(best_dict_other[model_name_use]), len(best_dict_other[model_name_use]) / (len(vartouse_var) * (len(metric_dicti) - sum(["R2" in x for x in metric_dicti])) * len(list_ws)) * 100)
                break
            print("all")
            for model_name_use in dict(sorted(best_dict.items(), key = lambda x: len(x[1]), reverse = True)):
                print(model_name_use, len(best_dict[model_name_use]), len(best_dict[model_name_use]) / (len(vartouse_var) * len(metric_dicti) * len(list_ws)) * 100)
                break

        if use_traj:
            best_dict = dict()
            for model_name_use in ord_metric_traj:
                best_dict_R2[model_name_use] = []
                best_dict_other[model_name_use] = []
                best_dict[model_name_use] = []

            for varname in vartouse_traj:
                for metric_name_use in metric_dicti_traj:
                    for val_ws in list_ws:
                        min_model = ""
                        min_val = MAXVALTOTAL
                        max_model = ""
                        max_val = -MAXVALTOTAL
                        for model_name_use in ord_metric_traj:
                            if use_val == 0:
                                if use_test == 0:
                                    val_use = dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]
                                else:
                                    val_use = dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][use_test - 1]
                            else:
                                val_use = dicti_all_traj_latest[use_test - 1][use_val - 1][varname][model_name_use][str(val_ws)][metric_name_use]
                            if val_use > max_val:
                                max_model = model_name_use
                                max_val = val_use
                            if val_use < min_val:
                                min_model = model_name_use
                                min_val = val_use
                        if "R2" in metric_name_use:
                            best_dict_total[max_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict[max_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict_total_R2[max_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict_R2[max_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                        else:
                            best_dict_total[min_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict[min_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict_total_other[min_model].append(varname + " " + metric_name_use + " " + str(val_ws))
                            best_dict_other[min_model].append(varname + " " + metric_name_use + " " + str(val_ws))

            print("trajs")
            print("R2")
            for model_name_use in dict(sorted(best_dict_R2.items(), key = lambda x: len(x[1]), reverse = True)):
                print(model_name_use, len(best_dict_R2[model_name_use]), len(best_dict_R2[model_name_use]) / (len(vartouse_traj) * sum(["R2" in x for x in metric_dicti_traj]) * len(list_ws)) * 100)
                break
            print("other")
            for model_name_use in dict(sorted(best_dict_other.items(), key = lambda x: len(x[1]), reverse = True)):
                print(model_name_use, len(best_dict_other[model_name_use]), len(best_dict_other[model_name_use]) / (len(vartouse_traj) * (len(metric_dicti_traj) - sum(["R2" in x for x in metric_dicti_traj])) * len(list_ws)) * 100)
                break
            print("all")
            for model_name_use in dict(sorted(best_dict.items(), key = lambda x: len(x[1]), reverse = True)):
                print(model_name_use, len(best_dict[model_name_use]), len(best_dict[model_name_use]) / (len(vartouse_traj) * len(metric_dicti_traj) * len(list_ws)) * 100)
                break

        print("all")
        print("R2")
        for model_name_use in dict(sorted(best_dict_total_R2.items(), key = lambda x: len(x[1]), reverse = True)):
            print(model_name_use, len(best_dict_total_R2[model_name_use]), len(best_dict_total_R2[model_name_use]) / ((len(vartouse_var) + len(vartouse_traj)) * (sum(["R2" in x for x in metric_dicti]) + sum(["R2" in x for x in metric_dicti_traj])) * len(list_ws)) * 100)
            break
        print("other")
        for model_name_use in dict(sorted(best_dict_total_other.items(), key = lambda x: len(x[1]), reverse = True)):
            print(model_name_use, len(best_dict_total_other[model_name_use]), len(best_dict_total_other[model_name_use]) / ((len(vartouse_var) + len(vartouse_traj)) * (len(metric_dicti) + len(metric_dicti_traj) - sum(["R2" in x for x in metric_dicti]) - sum(["R2" in x for x in metric_dicti_traj])) * len(list_ws)) * 100)
            break
        print("all")
        for model_name_use in dict(sorted(best_dict_total.items(), key = lambda x: len(x[1]), reverse = True)):
            print(model_name_use, len(best_dict_total[model_name_use]), len(best_dict_total[model_name_use]) / ((len(vartouse_var) + len(vartouse_traj)) * (len(metric_dicti) + len(metric_dicti_traj)) * len(list_ws)) * 100)
            break

    if use_outliers:
        if use_test == 0 and use_val == 0:
            limit_set = 0.5
            flag_reverse = False
            skip_names = ["LSTM_"]
            skip_models = set()
            for model_name_use in ord_metric:
                found_part = False
                for part in skip_names:
                    if part in model_name_use:
                        found_part = True
                        break
                if found_part:
                    skip_models.add(model_name_use)
            print(skip_models)
            for model_name_use in ord_metric_traj:
                found_part = False
                for part in skip_names:
                    if part in model_name_use:
                        found_part = True
                        break
                if found_part:
                    skip_models.add(model_name_use)
            if use_var:
                for varname in vartouse_var:
                    for metric_name_use in metric_dicti:
                        plt_dict = dict()
                        min_for_model = dict()
                        max_for_model = dict()
                        range_for_model = dict()
                        for model_name_use in ord_metric:
                            if model_name_use in skip_models:
                                continue
                            plt_dict[model_name_use] = []
                            for val_ws in list_ws:
                                plt_dict[model_name_use].append(dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use])
                        for model_name_use in plt_dict:
                            min_for_model[model_name_use] = min(plt_dict[model_name_use])
                            max_for_model[model_name_use] = max(plt_dict[model_name_use])
                            range_for_model[model_name_use] = max_for_model[model_name_use] - min_for_model[model_name_use]
                        total_min = min(min_for_model.values())
                        total_max = max(max_for_model.values())
                        total_range = total_max - total_min
                        min_range = min(range_for_model.values())
                        max_range = max(range_for_model.values())
                        if (flag_reverse and (min_range / total_range < limit_set or min_range / max_range < limit_set)) or (not flag_reverse and not (min_range / total_range < limit_set or min_range / max_range < limit_set)):
                            print(varname, metric_name_use, min_range / total_range * 100, max_range / total_range * 100, min_range / max_range * 100)
                for varname in vartouse_var:
                    for metric_name_use in metric_dicti:
                        for tn in range(5):
                            plt_dict = dict()
                            min_for_model = dict()
                            max_for_model = dict()
                            range_for_model = dict()
                            for model_name_use in ord_metric:
                                if model_name_use in skip_models:
                                    continue
                                plt_dict[model_name_use] = []
                                for val_ws in list_ws:
                                    plt_dict[model_name_use].append(dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn])
                            for model_name_use in plt_dict:
                                min_for_model[model_name_use] = min(plt_dict[model_name_use])
                                max_for_model[model_name_use] = max(plt_dict[model_name_use])
                                range_for_model[model_name_use] = max_for_model[model_name_use] - min_for_model[model_name_use]
                            total_min = min(min_for_model.values())
                            total_max = max(max_for_model.values())
                            total_range = total_max - total_min
                            min_range = min(range_for_model.values())
                            max_range = max(range_for_model.values())
                            if (flag_reverse and (min_range / total_range < limit_set or min_range / max_range < limit_set)) or (not flag_reverse and not (min_range / total_range < limit_set or min_range / max_range < limit_set)):
                                print(varname, metric_name_use, tn, min_range / total_range * 100, max_range / total_range * 100, min_range / max_range * 100)
                for varname in vartouse_var:
                    for metric_name_use in metric_dicti:
                        for tn in range(5):
                            for vn in range(5):
                                plt_dict = dict()
                                min_for_model = dict()
                                max_for_model = dict()
                                range_for_model = dict()
                                for model_name_use in ord_metric:
                                    if model_name_use in skip_models:
                                        continue
                                    plt_dict[model_name_use] = []
                                    for val_ws in list_ws:
                                        plt_dict[model_name_use].append(dicti_all[tn][vn][varname][model_name_use][str(val_ws)][metric_name_use])
                                for model_name_use in plt_dict:
                                    min_for_model[model_name_use] = min(plt_dict[model_name_use])
                                    max_for_model[model_name_use] = max(plt_dict[model_name_use])
                                    range_for_model[model_name_use] = max_for_model[model_name_use] - min_for_model[model_name_use]
                                total_min = min(min_for_model.values())
                                total_max = max(max_for_model.values())
                                total_range = total_max - total_min
                                min_range = min(range_for_model.values())
                                max_range = max(range_for_model.values())
                                if (flag_reverse and (min_range / total_range < limit_set or min_range / max_range < limit_set)) or (not flag_reverse and not (min_range / total_range < limit_set or min_range / max_range < limit_set)):
                                    print(varname, metric_name_use, tn, vn, min_range / total_range * 100, max_range / total_range * 100, min_range / max_range * 100)
                                
            if use_traj:
                for varname in vartouse_traj:
                    for metric_name_use in metric_dicti_traj:
                        plt_dict = dict()
                        min_for_model = dict()
                        max_for_model = dict()
                        range_for_model = dict()
                        for model_name_use in ord_metric_traj:
                            if model_name_use in skip_models:
                                continue
                            plt_dict[model_name_use] = []
                            for val_ws in list_ws:
                                plt_dict[model_name_use].append(dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use])
                        for model_name_use in plt_dict:
                            min_for_model[model_name_use] = min(plt_dict[model_name_use])
                            max_for_model[model_name_use] = max(plt_dict[model_name_use])
                            range_for_model[model_name_use] = max_for_model[model_name_use] - min_for_model[model_name_use]
                        total_min = min(min_for_model.values())
                        total_max = max(max_for_model.values())
                        total_range = total_max - total_min
                        min_range = min(range_for_model.values())
                        max_range = max(range_for_model.values())
                        if (flag_reverse and (min_range / total_range < limit_set or min_range / max_range < limit_set)) or (not flag_reverse and not (min_range / total_range < limit_set or min_range / max_range < limit_set)):
                            print(varname, metric_name_use, min_range / total_range * 100, max_range / total_range * 100, min_range / max_range * 100)
                for varname in vartouse_traj:
                    for metric_name_use in metric_dicti_traj:
                        for tn in range(5):
                            plt_dict = dict()
                            min_for_model = dict()
                            max_for_model = dict()
                            range_for_model = dict()
                            for model_name_use in ord_metric_traj:
                                if model_name_use in skip_models:
                                    continue
                                plt_dict[model_name_use] = []
                                for val_ws in list_ws:
                                    plt_dict[model_name_use].append(dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn])
                            for model_name_use in plt_dict:
                                min_for_model[model_name_use] = min(plt_dict[model_name_use])
                                max_for_model[model_name_use] = max(plt_dict[model_name_use])
                                range_for_model[model_name_use] = max_for_model[model_name_use] - min_for_model[model_name_use]
                            total_min = min(min_for_model.values())
                            total_max = max(max_for_model.values())
                            total_range = total_max - total_min
                            min_range = min(range_for_model.values())
                            max_range = max(range_for_model.values())
                            if (flag_reverse and (min_range / total_range < limit_set or min_range / max_range < limit_set)) or (not flag_reverse and not (min_range / total_range < limit_set or min_range / max_range < limit_set)):
                                print(varname, metric_name_use, tn, min_range / total_range * 100, max_range / total_range * 100, min_range / max_range * 100)
                for varname in vartouse_traj:
                    for metric_name_use in metric_dicti_traj:
                        for tn in range(5):
                            for vn in range(5):
                                plt_dict = dict()
                                min_for_model = dict()
                                max_for_model = dict()
                                range_for_model = dict()
                                for model_name_use in ord_metric_traj:
                                    if model_name_use in skip_models:
                                        continue
                                    plt_dict[model_name_use] = []
                                    for val_ws in list_ws:
                                        plt_dict[model_name_use].append(dicti_all_traj[tn][vn][varname][model_name_use][str(val_ws)][metric_name_use])
                                for model_name_use in plt_dict:
                                    min_for_model[model_name_use] = min(plt_dict[model_name_use])
                                    max_for_model[model_name_use] = max(plt_dict[model_name_use])
                                    range_for_model[model_name_use] = max_for_model[model_name_use] - min_for_model[model_name_use]
                                total_min = min(min_for_model.values())
                                total_max = max(max_for_model.values())
                                total_range = total_max - total_min
                                min_range = min(range_for_model.values())
                                max_range = max(range_for_model.values())
                                if (flag_reverse and (min_range / total_range < limit_set or min_range / max_range < limit_set)) or (not flag_reverse and not (min_range / total_range < limit_set or min_range / max_range < limit_set)):
                                    print(varname, metric_name_use, tn, vn, min_range / total_range * 100, max_range / total_range * 100, min_range / max_range * 100)
                             
    if use_minmax:
        if use_test == 0 and use_val == 0:
            if use_var:
                for varname in vartouse_var:
                    for metric_name_use in metric_dicti:
                        max_for_ws = dict()
                        min_for_ws = dict()
                        for val_ws in list_ws:
                            mini_model = ""
                            min_for_model = MAXVALTOTAL
                            maxi_model = ""
                            max_for_model = -MAXVALTOTAL
                            for model_name_use in ord_metric:
                                    val = dicti_all_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]
                                    if val < min_for_model:
                                        min_for_model = val
                                        mini_model = model_name_use
                                    if val > max_for_model:
                                        max_for_model = val
                                        maxi_model = model_name_use
                            max_for_ws[val_ws] = (maxi_model, max_for_model)
                            min_for_ws[val_ws] = (mini_model, min_for_model)
                        if "wt" in metric_name_use or "RMSE" in metric_name_use:
                            continue
                        print(varname, metric_name_use)
                        if "R2" in metric_name_use:
                            print([x[0] for x in max_for_ws.values()])
                            print([x[1] for x in max_for_ws.values()])
                        else:
                            print([x[0] for x in min_for_ws.values()])
                            print([x[1] for x in min_for_ws.values()])
                if use_detail:
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            for tn in range(5):
                                max_for_ws = dict()
                                min_for_ws = dict()
                                for val_ws in list_ws:
                                    mini_model = ""
                                    min_for_model = MAXVALTOTAL
                                    maxi_model = ""
                                    max_for_model = -MAXVALTOTAL
                                    for model_name_use in ord_metric:
                                            val = dicti_all_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn]
                                            if val < min_for_model:
                                                min_for_model = val
                                                mini_model = model_name_use
                                            if val > max_for_model:
                                                max_for_model = val
                                                maxi_model = model_name_use
                                    max_for_ws[val_ws] = (maxi_model, max_for_model)
                                    min_for_ws[val_ws] = (mini_model, min_for_model)
                                if "wt" in metric_name_use or "RMSE" in metric_name_use:
                                    continue
                                print(varname, metric_name_use, tn)
                                if "R2" in metric_name_use:
                                    print([x[0] for x in max_for_ws.values()])
                                    print([x[1] for x in max_for_ws.values()])
                                else:
                                    print([x[0] for x in min_for_ws.values()])
                                    print([x[1] for x in min_for_ws.values()])
                    for varname in vartouse_var:
                        for metric_name_use in metric_dicti:
                            for tn in range(5):
                                for vn in range(5):
                                    max_for_ws = dict()
                                    min_for_ws = dict()
                                    for val_ws in list_ws:
                                        mini_model = ""
                                        min_for_model = MAXVALTOTAL
                                        maxi_model = ""
                                        max_for_model = -MAXVALTOTAL
                                        for model_name_use in ord_metric:
                                                val = dicti_all_latest[tn][vn][varname][model_name_use][str(val_ws)][metric_name_use]
                                                if val < min_for_model:
                                                    min_for_model = val
                                                    mini_model = model_name_use
                                                if val > max_for_model:
                                                    max_for_model = val
                                                    maxi_model = model_name_use
                                        max_for_ws[val_ws] = (maxi_model, max_for_model)
                                        min_for_ws[val_ws] = (mini_model, min_for_model)
                                    if "wt" in metric_name_use or "RMSE" in metric_name_use:
                                        continue
                                    print(varname, metric_name_use, tn, vn)
                                    if "R2" in metric_name_use:
                                        print([x[0] for x in max_for_ws.values()])
                                        print([x[1] for x in max_for_ws.values()])
                                    else:
                                        print([x[0] for x in min_for_ws.values()])
                                        print([x[1] for x in min_for_ws.values()])
            if use_traj:
                for varname in vartouse_traj:
                    for metric_name_use in metric_dicti_traj:
                        max_for_ws = dict()
                        min_for_ws = dict()
                        for val_ws in list_ws:
                            mini_model = ""
                            min_for_model = MAXVALTOTAL
                            maxi_model = ""
                            max_for_model = -MAXVALTOTAL
                            for model_name_use in ord_metric_traj:
                                    val = dicti_all_traj_latest_avg[varname][model_name_use][str(val_ws)][metric_name_use]
                                    if val < min_for_model:
                                        min_for_model = val
                                        mini_model = model_name_use
                                    if val > max_for_model:
                                        max_for_model = val
                                        maxi_model = model_name_use
                            max_for_ws[val_ws] = (maxi_model, max_for_model)
                            min_for_ws[val_ws] = (mini_model, min_for_model)
                        if "wt" in metric_name_use or "RMSE" in metric_name_use:
                            continue
                        print(varname, metric_name_use)
                        if "R2" in metric_name_use:
                            print([x[0] for x in max_for_ws.values()])
                            print([x[1] for x in max_for_ws.values()])
                        else:
                            print([x[0] for x in min_for_ws.values()])
                            print([x[1] for x in min_for_ws.values()])
                if use_detail:
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            for tn in range(5):
                                max_for_ws = dict()
                                min_for_ws = dict()
                                for val_ws in list_ws:
                                    mini_model = ""
                                    min_for_model = MAXVALTOTAL
                                    maxi_model = ""
                                    max_for_model = -MAXVALTOTAL
                                    for model_name_use in ord_metric_traj:
                                            val = dicti_all_traj_latest_by_test_avg[varname][model_name_use][str(val_ws)][metric_name_use][tn]
                                            if val < min_for_model:
                                                min_for_model = val
                                                mini_model = model_name_use
                                            if val > max_for_model:
                                                max_for_model = val
                                                maxi_model = model_name_use
                                    max_for_ws[val_ws] = (maxi_model, max_for_model)
                                    min_for_ws[val_ws] = (mini_model, min_for_model)
                                if "wt" in metric_name_use or "RMSE" in metric_name_use:
                                    continue
                                print(varname, metric_name_use, tn)
                                if "R2" in metric_name_use:
                                    print([x[0] for x in max_for_ws.values()])
                                    print([x[1] for x in max_for_ws.values()])
                                else:
                                    print([x[0] for x in min_for_ws.values()])
                                    print([x[1] for x in min_for_ws.values()])
                    for varname in vartouse_traj:
                        for metric_name_use in metric_dicti_traj:
                            for tn in range(5):
                                for vn in range(5):
                                    max_for_ws = dict()
                                    min_for_ws = dict()
                                    for val_ws in list_ws:
                                        mini_model = ""
                                        min_for_model = MAXVALTOTAL
                                        maxi_model = ""
                                        max_for_model = -MAXVALTOTAL
                                        for model_name_use in ord_metric_traj:
                                                val = dicti_all_traj_latest[tn][vn][varname][model_name_use][str(val_ws)][metric_name_use]
                                                if val < min_for_model:
                                                    min_for_model = val
                                                    mini_model = model_name_use
                                                if val > max_for_model:
                                                    max_for_model = val
                                                    maxi_model = model_name_use
                                        max_for_ws[val_ws] = (maxi_model, max_for_model)
                                        min_for_ws[val_ws] = (mini_model, min_for_model)
                                    if "wt" in metric_name_use or "RMSE" in metric_name_use:
                                        continue
                                    print(varname, metric_name_use, tn, vn)
                                    if "R2" in metric_name_use:
                                        print([x[0] for x in max_for_ws.values()])
                                        print([x[1] for x in max_for_ws.values()])
                                    else:
                                        print([x[0] for x in min_for_ws.values()])
                                        print([x[1] for x in min_for_ws.values()])

use_table = True
use_plot = False
use_sizes = False
use_outliers = False
use_minmax = False
use_detail = False
use_single = False
use_vertical = False
use_horizontal = False
use_all = False
use_merged = True
use_test = 0
use_val = 0
use_std = True
use_var = True
use_traj = True

my_table_print(use_table = use_table, use_plot = use_plot, use_sizes = use_sizes, use_outliers = use_outliers, use_minmax = use_minmax, use_detail = use_detail, use_single = use_single, use_vertical = use_vertical, use_horizontal = use_horizontal, use_all = use_all, use_merged = use_merged, use_std = use_std, use_var = use_var, use_traj = use_traj)

use_table = False
use_plot = True
use_sizes = False
use_outliers = False
use_minmax = False
use_detail = False
use_single = False
use_vertical = False
use_horizontal = False
use_all = False
use_merged = True
use_test = 0
use_val = 0
use_std = False
use_var = True
use_traj = True

my_table_print(use_table = use_table, use_plot = use_plot, use_sizes = use_sizes, use_outliers = use_outliers, use_minmax = use_minmax, use_detail = use_detail, use_single = use_single, use_vertical = use_vertical, use_horizontal = use_horizontal, use_all = use_all, use_merged = use_merged, use_std = use_std, use_var = use_var, use_traj = use_traj)
#for use_test in range(0, 6):
    #my_table_print(use_table = use_table, use_plot = use_plot, use_sizes = use_sizes, use_outliers = use_outliers, use_minmax = use_minmax, use_detail = use_detail, use_single = use_single, use_vertical = use_vertical, use_horizontal = use_horizontal, use_all = use_all, use_merged = use_merged, use_test = use_test, use_std = use_std, use_var = use_var, use_traj = use_traj)
    #for use_val in range(0, 6):
        #my_table_print(use_table = use_table, use_plot = use_plot, use_sizes = use_sizes, use_outliers = use_outliers, use_minmax = use_minmax, use_detail = use_detail, use_single = use_single, use_vertical = use_vertical, use_horizontal = use_horizontal, use_all = use_all, use_merged = use_merged, use_test = use_test, use_val = use_val, use_std = use_std, use_var = use_var, use_traj = use_traj)