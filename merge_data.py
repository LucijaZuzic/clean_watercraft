import os
import pandas as pd

sf1, sf2 = 5, 5

vehicle_zero = os.listdir("csv_results/1/1/")[0]
ride_zero = os.listdir("csv_results/1/1/" + vehicle_zero)[0]
ride_zero = os.listdir("csv_results/1/1/" + vehicle_zero)[0]
var_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/")
model_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
ws_long_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/" + model_list[0] + "/")
for var in var_list:
    for model in model_list:
        for ws_long in ws_long_list:
            list_pred = []
            list_actual = []
            for nf1 in range(sf1):
                list_pred_test = []
                list_actual_test = []
                for nf2 in range(sf2):
                    list_pred_val = []
                    list_actual_val = []
                    for vehicle in os.listdir("csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"):
                        for ride in os.listdir("csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/"):
                            path_to_file = "csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle + "/" + str(ride) + "/" + var + "/" + model + "/" + ws_long
                            pd_file = pd.read_csv(path_to_file, index_col = False)
                            predicted = pd_file["predicted"]
                            actual = pd_file["actual"]
                            list_pred_val.extend(predicted)
                            list_actual_val.extend(actual)
                            list_pred_test.extend(predicted)
                            list_actual_test.extend(actual)
                            list_pred.extend(predicted)
                            list_actual.extend(actual)
                    dict_write = {"predicted": list_pred_val,
                                  "actual": list_actual_val}
                    ride_name = "csv_merged/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + var + "/" + model + "/"
                    if not os.path.isdir(ride_name):
                        os.makedirs(ride_name)
                    df_write = pd.DataFrame(dict_write)
                    df_write.to_csv(ride_name + ws_long, index = False)
                    print(ride_name + ws_long)
                dict_write = {"predicted": list_pred_test,
                              "actual": list_actual_test}
                ride_name = "csv_merged/" + str(nf1 + 1) + "/total/" + var + "/" + model + "/"
                if not os.path.isdir(ride_name):
                    os.makedirs(ride_name)
                df_write = pd.DataFrame(dict_write)
                df_write.to_csv(ride_name + ws_long, index = False)
                print(ride_name + ws_long)
            dict_write = {"predicted": list_pred,
                          "actual": list_actual}
            ride_name = "csv_merged/total/" + var + "/" + model + "/"
            if not os.path.isdir(ride_name):
                os.makedirs(ride_name)
            df_write = pd.DataFrame(dict_write)
            df_write.to_csv(ride_name + ws_long, index = False)
            print(ride_name + ws_long)