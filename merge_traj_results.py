import os
import pandas as pd

sf1, sf2 = 5, 5

vehicle_zero = os.listdir("csv_results_traj/1/1/")[0]
ride_zero = os.listdir("csv_results_traj/1/1/" + vehicle_zero)[0]
var_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/")
model_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
ws_long_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/" + model_list[0] + "/")
for var in var_list:
    for ws_long in ws_long_list:
        for nf1 in range(sf1):
            for nf2 in range(sf2):
                for vehicle in os.listdir("csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"):
                    for ride in os.listdir("csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/"):
                        predictions_models = dict()
                        min_len = 100000000
                        for model in model_list:
                            path_to_file = "csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/" + str(ride) + "/" + var + "/" + model + "/" + ws_long
                            pd_file = pd.read_csv(path_to_file, index_col = False)
                            if "actual long" not in predictions_models:
                                predictions_models["actual long"] = pd_file["actual long"]
                            if "actual lat" not in predictions_models:
                                predictions_models["actual lat"] = pd_file["actual lat"]
                            predictions_models[model + " long"] = pd_file["predicted long"]
                            predictions_models[model + " lat"] = pd_file["predicted lat"]
                            if len(predictions_models[model + " long"]) < min_len:
                                min_len = len(predictions_models[model + " long"])
                        predictions_models["actual long"] = predictions_models["actual long"][:min_len]
                        predictions_models["actual lat"] = predictions_models["actual lat"][:min_len]
                        for model in model_list:
                            predictions_models[model + " long"] = predictions_models[model + " long"][:min_len]
                            predictions_models[model + " lat"] = predictions_models[model + " lat"][:min_len]
                        path_to_file_new = "csv_results_traj_merged/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/" + str(ride) + "/" + var + "/"
                        if not os.path.isdir(path_to_file_new):
                            os.makedirs(path_to_file_new)
                        df_write = pd.DataFrame(predictions_models)
                        df_write.to_csv(path_to_file_new + ws_long, index = False)
                        print(path_to_file_new + ws_long)