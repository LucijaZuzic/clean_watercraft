import os
import pandas as pd

sf1, sf2 = 5, 5

vehicle_zero = os.listdir("csv_results/1/1/")[0]
ride_zero = os.listdir("csv_results/1/1/" + vehicle_zero)[0]
var_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/")
model_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
ws_long_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/" + model_list[0] + "/")
for var in var_list:
    for ws_long in ws_long_list:
        for nf1 in range(sf1):
            for nf2 in range(sf2):
                for vehicle in os.listdir("csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"):
                    for ride in os.listdir("csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/"):
                        predictions_models = dict()
                        min_len = 100000000
                        for model in model_list:
                            path_to_file = "csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/" + str(ride) + "/" + var + "/" + model + "/" + ws_long
                            pd_file = pd.read_csv(path_to_file, index_col = False)
                            if "actual" not in predictions_models:
                                predictions_models["actual"] = pd_file["actual"]
                            predictions_models[model] = pd_file["predicted"]
                            if len(predictions_models[model]) < min_len:
                                min_len = len(predictions_models[model])
                        predictions_models["actual"] = predictions_models["actual"][:min_len]
                        for model in model_list:
                            predictions_models[model] = predictions_models[model][:min_len]
                        path_to_file_new = "csv_results_merged/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/" + str(ride) + "/" + var + "/"
                        if not os.path.isdir(path_to_file_new):
                            os.makedirs(path_to_file_new)
                        df_write = pd.DataFrame(predictions_models)
                        df_write.to_csv(path_to_file_new + ws_long, index = False)
                        print(path_to_file_new + ws_long)