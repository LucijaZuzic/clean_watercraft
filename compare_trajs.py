import os
import pandas as pd
import scipy.stats as stats

sf1, sf2 = 5, 5

var_list = os.listdir("csv_results_traj_merged_validation/total/")
ws_long_list = os.listdir("csv_results_traj_merged_validation/total/" + var_list[0] + "/")

vehicle_zero = os.listdir("csv_results_traj/1/1/")[0]
ride_zero = os.listdir("csv_results_traj/1/1/" + vehicle_zero)[0]
model_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
model_list.append("actual")

dicti_mann_whitney_traj = {"variable": [], "ws": [], "model1": [], "model2": [], "u long": [], "p long": [], "u lat": [], "p lat": []}

for var in var_list:
    for ws_long in ws_long_list:
        path_to_file = "csv_results_traj_merged_validation/total/" + var + "/" + ws_long
        pd_file = pd.read_csv(path_to_file, index_col = False)
        for model1_ix in range(len(model_list)):
            for model2_ix in range(model1_ix + 1, len(model_list)):
                xmodel1 = pd_file[model_list[model1_ix] + " long"]
                ymodel1 = pd_file[model_list[model1_ix] + " lat"]
                xmodel2 = pd_file[model_list[model2_ix] + " long"]
                ymodel2 = pd_file[model_list[model2_ix] + " lat"]
                #total1 = [[xmodel1[ix], ymodel1[ix]] for ix in range(len(xmodel1))]
                #total2 = [[xmodel2[ix], ymodel2[ix]] for ix in range(len(xmodel2))]
                #uval, pval = stats.mannwhitneyu(total1, total2)
                #uval1, uval2, pval1, pval2 = uval[0], uval[1], pval[0], pval[1]
                uval1, pval1 = stats.mannwhitneyu(xmodel1, xmodel2)
                uval2, pval2 = stats.mannwhitneyu(ymodel1, ymodel2)
                print(var, ws_long.split("_")[0], model_list[model1_ix], model_list[model2_ix], uval1, pval1, uval2, pval2)
                dicti_mann_whitney_traj["variable"].append(var)
                dicti_mann_whitney_traj["ws"].append(ws_long.split("_")[0])
                dicti_mann_whitney_traj["model1"].append(model_list[model1_ix])
                dicti_mann_whitney_traj["model2"].append(model_list[model2_ix])
                dicti_mann_whitney_traj["u long"].append(uval1)
                dicti_mann_whitney_traj["p long"].append(pval1)
                dicti_mann_whitney_traj["u lat"].append(uval2)
                dicti_mann_whitney_traj["p lat"].append(pval2)

df_write = pd.DataFrame(dicti_mann_whitney_traj)
df_write.to_csv("dicti_mann_whitney_traj.csv", index = False)