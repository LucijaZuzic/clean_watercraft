import os
import pandas as pd
import scipy.stats as stats

sf1, sf2 = 5, 5

var_list = os.listdir("csv_results_merged_validation/total/")
ws_long_list = os.listdir("csv_results_merged_validation/total/" + var_list[0] + "/")

vehicle_zero = os.listdir("csv_results/1/1/")[0]
ride_zero = os.listdir("csv_results/1/1/" + vehicle_zero)[0]
model_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
model_list.append("actual")

test_var = "wilcoxon"

if test_var == "wilcoxon":
    dicti_wilcoxon = {"variable": [], "ws": [], "model1": [], "model2": [], "u": [], "p": []}

    for var in var_list:
        for ws_long in ws_long_list:
            path_to_file = "csv_results_merged_validation/total/" + var + "/" + ws_long
            pd_file = pd.read_csv(path_to_file, index_col = False)
            for model1_ix in range(len(model_list)):
                for model2_ix in range(model1_ix + 1, len(model_list)):
                    try:
                        uval, pval = stats.wilcoxon(pd_file[model_list[model1_ix]], pd_file[model_list[model2_ix]])
                    except:
                        uval, pval = 1.0, 1.0
                    print(model_list[model1_ix], model_list[model2_ix], uval, pval)
                    dicti_wilcoxon["variable"].append(var)
                    dicti_wilcoxon["ws"].append(ws_long.split("_")[0])
                    dicti_wilcoxon["model1"].append(model_list[model1_ix])
                    dicti_wilcoxon["model2"].append(model_list[model2_ix])
                    dicti_wilcoxon["u"].append(uval)
                    dicti_wilcoxon["p"].append(pval)

    df_write = pd.DataFrame(dicti_wilcoxon)
    df_write.to_csv("dicti_wilcoxon.csv", index = False)

if test_var == "mann_whitney":
    dicti_mann_whitney = {"variable": [], "ws": [], "model1": [], "model2": [], "u": [], "p": []}

    for var in var_list:
        for ws_long in ws_long_list:
            path_to_file = "csv_results_merged_validation/total/" + var + "/" + ws_long
            pd_file = pd.read_csv(path_to_file, index_col = False)
            for model1_ix in range(len(model_list)):
                for model2_ix in range(model1_ix + 1, len(model_list)):
                    uval, pval = stats.mannwhitneyu(pd_file[model_list[model1_ix]], pd_file[model_list[model2_ix]])
                    print(model_list[model1_ix], model_list[model2_ix], uval, pval)
                    dicti_mann_whitney["variable"].append(var)
                    dicti_mann_whitney["ws"].append(ws_long.split("_")[0])
                    dicti_mann_whitney["model1"].append(model_list[model1_ix])
                    dicti_mann_whitney["model2"].append(model_list[model2_ix])
                    dicti_mann_whitney["u"].append(uval)
                    dicti_mann_whitney["p"].append(pval)

    df_write = pd.DataFrame(dicti_mann_whitney)
    df_write.to_csv("dicti_mann_whitney.csv", index = False)

            #print(stats.normaltest(list_pred_test))
            #print(stats.shapiro(list_pred_test))
            #print(stats.kstest(list_pred_test, 'norm'))
            
            #print(stats.normaltest(list_actual_test))
            #print(stats.shapiro(list_actual_test))
            #print(stats.kstest(list_actual_test, 'norm'))

            #print(stats.ttest_ind(list_actual_test, list_pred_test, equal_var = False))
            #print(stats.ranksums(list_actual_test, list_pred_test))
            #print(nf2, stats.mannwhitneyu(list_actual_test, list_pred_test))