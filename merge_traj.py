import os
import pandas as pd

sf1, sf2 = 5, 5

vehicle_zero = os.listdir("csv_results_traj/1/1/")[0]
ride_zero = os.listdir("csv_results_traj/1/1/" + vehicle_zero)[0]
ride_zero = os.listdir("csv_results_traj/1/1/" + vehicle_zero)[0]
var_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/")
model_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
ws_long_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/" + model_list[0] + "/")
for var in var_list:
    for model in model_list:
        for ws_long in ws_long_list:
            list_pred_long = []
            list_actual_long = []
            list_pred_lat = []
            list_actual_lat = []
            for nf1 in range(sf1):
                list_pred_test_long = []
                list_actual_test_long = []
                list_pred_test_lat = []
                list_actual_test_lat = []
                for nf2 in range(sf2):
                    list_pred_val_long = []
                    list_actual_val_long = []
                    list_pred_val_lat = []
                    list_actual_val_lat = []
                    for vehicle in os.listdir("csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"):
                        for ride in os.listdir("csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/"):
                            path_to_file = "csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/" + str(ride) + "/" + var + "/" + model + "/" + ws_long
                            pd_file = pd.read_csv(path_to_file, index_col = False)
                            predicted_long = pd_file["predicted long"]
                            actual_long = pd_file["actual long"]
                            predicted_lat = pd_file["predicted lat"]
                            actual_lat = pd_file["actual lat"]
                            list_pred_val_long.extend(predicted_long)
                            list_actual_val_long.extend(actual_long)
                            list_pred_test_long.extend(predicted_long)
                            list_actual_test_long.extend(actual_long)
                            list_pred_long.extend(predicted_long)
                            list_actual_long.extend(actual_long)
                            list_pred_val_lat.extend(predicted_lat)
                            list_actual_val_lat.extend(actual_lat)
                            list_pred_test_lat.extend(predicted_lat)
                            list_actual_test_lat.extend(actual_lat)
                            list_pred_lat.extend(predicted_lat)
                            list_actual_lat.extend(actual_lat)
                    dict_write = {"predicted long": list_pred_val_long,
                                  "actual long": list_actual_val_long,
                                  "predicted lat": list_pred_val_lat,
                                  "actual lat": list_actual_val_lat}
                    ride_name = "csv_traj_merged/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + var + "/" + model + "/"
                    if not os.path.isdir(ride_name):
                        os.makedirs(ride_name)
                    df_write = pd.DataFrame(dict_write)
                    df_write.to_csv(ride_name + ws_long, index = False)
                    print(ride_name + ws_long)
                dict_write = {"predicted long": list_pred_test_long,
                              "actual long": list_actual_test_long,
                              "predicted lat": list_pred_test_lat,
                              "actual lat": list_actual_test_lat}
                ride_name = "csv_traj_merged/" + str(nf1 + 1) + "/total/" + var + "/" + model + "/"
                if not os.path.isdir(ride_name):
                    os.makedirs(ride_name)
                df_write = pd.DataFrame(dict_write)
                df_write.to_csv(ride_name + ws_long, index = False)
                print(ride_name + ws_long)
            dict_write = {"predicted long": list_pred_long,
                          "actual long": list_actual_long,
                          "predicted lat": list_pred_lat,
                          "actual lat": list_actual_lat}
            ride_name = "csv_traj_merged/total/" + var + "/" + model + "/"
            if not os.path.isdir(ride_name):
                os.makedirs(ride_name)
            df_write = pd.DataFrame(dict_write)
            df_write.to_csv(ride_name + ws_long, index = False)
            print(ride_name + ws_long)