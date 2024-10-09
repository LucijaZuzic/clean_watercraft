import os
import pandas as pd

sf1, sf2 = 5, 5

vehicle_zero = os.listdir("csv_results_traj_merged/1/1/")[0]
ride_zero = os.listdir("csv_results_traj_merged/1/1/" + vehicle_zero)[0]
var_list = os.listdir("csv_results_traj_merged/1/1/" + vehicle_zero + "/" + ride_zero + "/")
ws_long_list = os.listdir("csv_results_traj_merged/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
for var in var_list:
    for ws_long in ws_long_list:
        dict_pred = dict()
        for nf1 in range(sf1):
            dict_test_pred = dict()
            for nf2 in range(sf2):
                dict_val_pred = dict()
                for vehicle in os.listdir("csv_results_traj_merged/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"):
                    for ride in os.listdir("csv_results_traj_merged/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/"): 
                        path_to_file = "csv_results_traj_merged/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/" + str(ride) + "/" + var + "/" + ws_long
                        pd_file = pd.read_csv(path_to_file, index_col = False)
                        model_list = list(pd_file.keys())
                        for model in model_list:
                            if model not in dict_pred:
                                dict_pred[model] = []
                            if model not in dict_test_pred:
                                dict_test_pred[model] = []
                            if model not in dict_val_pred:
                                dict_val_pred[model] = []
                            dict_pred[model].extend(pd_file[model])
                            dict_test_pred[model].extend(pd_file[model])
                            dict_val_pred[model].extend(pd_file[model])
                ride_name = "csv_results_traj_merged_merged/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/total/" + var + "/"
                if not os.path.isdir(ride_name):
                    os.makedirs(ride_name)
                df_write = pd.DataFrame(dict_val_pred)
                df_write.to_csv(ride_name + ws_long, index = False)
                print(ride_name + ws_long)
            ride_name = "csv_results_traj_merged_merged/" + str(nf1 + 1) + "/total/" + var + "/"
            if not os.path.isdir(ride_name):
                os.makedirs(ride_name)
            df_write = pd.DataFrame(dict_test_pred)
            df_write.to_csv(ride_name + ws_long, index = False)
            print(ride_name + ws_long)
        ride_name = "csv_results_traj_merged_merged/total/" + var + "/"
        if not os.path.isdir(ride_name):
            os.makedirs(ride_name)
        df_write = pd.DataFrame(dict_pred)
        df_write.to_csv(ride_name + ws_long, index = False)
        print(ride_name + ws_long)