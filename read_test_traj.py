import os
import pandas as pd
import math
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import os
from utilities import haversine_array, euclidean

sf1, sf2 = 5, 5

vehicle_zero = os.listdir("csv_results_traj/1/1/")[0]
ride_zero = os.listdir("csv_results_traj/1/1/" + vehicle_zero)[0]
var_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/")
model_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
ws_long_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/" + model_list[0] + "/")

if not os.path.isfile("data_frame_traj_total_reverse.csv"):

    data_frame_traj_total_reverse = {"variable": [], "model": [], "ws": [], "R2": [], "MAE": [], "MSE": [], "RMSE": [], "euclid": [], "haversine": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                print(var, model, ws_long)
                path_to_file = ride_name = "csv_traj_merged_validation/total/" + var + "/" + model + "/" + ws_long
                pd_file = pd.read_csv(path_to_file, index_col = False)
                predicted_long = pd_file["predicted long"]
                actual_long = pd_file["actual long"]
                predicted_lat = pd_file["predicted lat"]
                actual_lat = pd_file["actual lat"]
                actual = [[actual_long[ix], actual_lat[ix]] for ix in range(len(actual_long))]
                predicted = [[predicted_long[ix], predicted_lat[ix]] for ix in range(len(predicted_long))]
                euclidean_dist = euclidean(actual_long, actual_lat, predicted_long, predicted_lat)
                haversine_dist = haversine_array(actual_long, actual_lat, predicted_long, predicted_lat)
                r2_pred = r2_score(actual, predicted)
                mae_pred = mean_absolute_error(actual, predicted)
                mse_pred = mean_squared_error(actual, predicted)
                rmse_pred = math.sqrt(mse_pred)
                print(r2_pred, mae_pred, mse_pred, rmse_pred, euclidean_dist, haversine_dist)
                data_frame_traj_total_reverse["variable"].append(var)
                data_frame_traj_total_reverse["model"].append(model)
                data_frame_traj_total_reverse["ws"].append(ws_long.split("_")[0])
                data_frame_traj_total_reverse["R2"].append(r2_pred)
                data_frame_traj_total_reverse["MAE"].append(mae_pred)
                data_frame_traj_total_reverse["MSE"].append(mse_pred)
                data_frame_traj_total_reverse["RMSE"].append(rmse_pred)
                data_frame_traj_total_reverse["euclid"].append(euclidean_dist)
                data_frame_traj_total_reverse["haversine"].append(haversine_dist)

    df_data_frame_traj_total_reverse = pd.DataFrame(data_frame_traj_total_reverse)
    df_data_frame_traj_total_reverse.to_csv("data_frame_traj_total_reverse.csv", index = False)

if False and not os.path.isfile("data_frame_traj_total.csv"):

    data_frame_traj_total = {"variable": [], "model": [], "ws": [], "R2": [], "MAE": [], "MSE": [], "RMSE": [], "euclid": [], "haversine": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                print(var, model, ws_long)
                path_to_file = ride_name = "csv_traj_merged/total/" + var + "/" + model + "/" + ws_long
                pd_file = pd.read_csv(path_to_file, index_col = False)
                predicted_long = pd_file["predicted long"]
                actual_long = pd_file["actual long"]
                predicted_lat = pd_file["predicted lat"]
                actual_lat = pd_file["actual lat"]
                actual = [[actual_long[ix], actual_lat[ix]] for ix in range(len(actual_long))]
                predicted = [[predicted_long[ix], predicted_lat[ix]] for ix in range(len(predicted_long))]
                euclidean_dist = euclidean(actual_long, actual_lat, predicted_long, predicted_lat)
                haversine_dist = haversine_array(actual_long, actual_lat, predicted_long, predicted_lat)
                r2_pred = r2_score(actual, predicted)
                mae_pred = mean_absolute_error(actual, predicted)
                mse_pred = mean_squared_error(actual, predicted)
                rmse_pred = math.sqrt(mse_pred)
                print(r2_pred, mae_pred, mse_pred, rmse_pred, euclidean_dist, haversine_dist)
                data_frame_traj_total["variable"].append(var)
                data_frame_traj_total["model"].append(model)
                data_frame_traj_total["ws"].append(ws_long.split("_")[0])
                data_frame_traj_total["R2"].append(r2_pred)
                data_frame_traj_total["MAE"].append(mae_pred)
                data_frame_traj_total["MSE"].append(mse_pred)
                data_frame_traj_total["RMSE"].append(rmse_pred)
                data_frame_traj_total["euclid"].append(euclidean_dist)
                data_frame_traj_total["haversine"].append(haversine_dist)

if False and not os.path.isfile("data_frame_traj_test_reverse.csv"):

    df_data_frame_traj_total = pd.DataFrame(data_frame_traj_total)
    df_data_frame_traj_total.to_csv("data_frame_traj_total.csv", index = False)

    data_frame_traj_test_reverse = {"variable": [], "model": [], "ws": [], "val": [], "R2": [], "MAE": [], "MSE": [], "RMSE": [], "euclid": [], "haversine": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                for nf2 in range(sf2):
                    print(var, model, ws_long, nf2)
                    path_to_file = ride_name = "csv_traj_merged_validation/" + str(nf2 + 1) + "/total/" + var + "/" + model + "/" + ws_long
                    pd_file = pd.read_csv(path_to_file, index_col = False)
                    predicted_long = pd_file["predicted long"]
                    actual_long = pd_file["actual long"]
                    predicted_lat = pd_file["predicted lat"]
                    actual_lat = pd_file["actual lat"]
                    actual = [[actual_long[ix], actual_lat[ix]] for ix in range(len(actual_long))]
                    predicted = [[predicted_long[ix], predicted_lat[ix]] for ix in range(len(predicted_long))]
                    euclidean_dist = euclidean(actual_long, actual_lat, predicted_long, predicted_lat)
                    haversine_dist = haversine_array(actual_long, actual_lat, predicted_long, predicted_lat)
                    r2_pred = r2_score(actual, predicted)
                    mae_pred = mean_absolute_error(actual, predicted)
                    mse_pred = mean_squared_error(actual, predicted)
                    rmse_pred = math.sqrt(mse_pred)
                    print(r2_pred, mae_pred, mse_pred, rmse_pred, euclidean_dist, haversine_dist)
                    data_frame_traj_test_reverse["variable"].append(var)
                    data_frame_traj_test_reverse["model"].append(model)
                    data_frame_traj_test_reverse["ws"].append(ws_long.split("_")[0])
                    data_frame_traj_test_reverse["val"].append(nf2 + 1)
                    data_frame_traj_test_reverse["R2"].append(r2_pred)
                    data_frame_traj_test_reverse["MAE"].append(mae_pred)
                    data_frame_traj_test_reverse["MSE"].append(mse_pred)
                    data_frame_traj_test_reverse["RMSE"].append(rmse_pred)
                    data_frame_traj_test_reverse["euclid"].append(euclidean_dist)
                    data_frame_traj_test_reverse["haversine"].append(haversine_dist)

    df_data_frame_traj_test_reverse = pd.DataFrame(data_frame_traj_test_reverse)
    df_data_frame_traj_test_reverse.to_csv("data_frame_traj_test_reverse.csv", index = False)

if False and not os.path.isfile("data_frame_traj_test.csv"):

    data_frame_traj_test = {"variable": [], "model": [], "ws": [], "test": [], "R2": [], "MAE": [], "MSE": [], "RMSE": [], "euclid": [], "haversine": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                for nf1 in range(sf1):
                    print(var, model, ws_long, nf1)
                    path_to_file = ride_name = "csv_traj_merged/" + str(nf1 + 1) + "/total/" + var + "/" + model + "/" + ws_long
                    pd_file = pd.read_csv(path_to_file, index_col = False)
                    predicted_long = pd_file["predicted long"]
                    actual_long = pd_file["actual long"]
                    predicted_lat = pd_file["predicted lat"]
                    actual_lat = pd_file["actual lat"]
                    actual = [[actual_long[ix], actual_lat[ix]] for ix in range(len(actual_long))]
                    predicted = [[predicted_long[ix], predicted_lat[ix]] for ix in range(len(predicted_long))]
                    euclidean_dist = euclidean(actual_long, actual_lat, predicted_long, predicted_lat)
                    haversine_dist = haversine_array(actual_long, actual_lat, predicted_long, predicted_lat)
                    r2_pred = r2_score(actual, predicted)
                    mae_pred = mean_absolute_error(actual, predicted)
                    mse_pred = mean_squared_error(actual, predicted)
                    rmse_pred = math.sqrt(mse_pred)
                    print(r2_pred, mae_pred, mse_pred, rmse_pred, euclidean_dist, haversine_dist)
                    data_frame_traj_test["variable"].append(var)
                    data_frame_traj_test["model"].append(model)
                    data_frame_traj_test["ws"].append(ws_long.split("_")[0])
                    data_frame_traj_test["test"].append(nf1 + 1)
                    data_frame_traj_test["R2"].append(r2_pred)
                    data_frame_traj_test["MAE"].append(mae_pred)
                    data_frame_traj_test["MSE"].append(mse_pred)
                    data_frame_traj_test["RMSE"].append(rmse_pred)
                    data_frame_traj_test["euclid"].append(euclidean_dist)
                    data_frame_traj_test["haversine"].append(haversine_dist)

    df_data_frame_traj_test = pd.DataFrame(data_frame_traj_test)
    df_data_frame_traj_test.to_csv("data_frame_traj_test.csv", index = False)

if False and not os.path.isfile("data_frame_traj_val.csv"):

    data_frame_traj_val  = {"variable": [], "model": [], "ws": [], "test": [], "val": [], "R2": [], "MAE": [], "MSE": [], "RMSE": [], "euclid": [], "haversine": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                for nf1 in range(sf1):
                    for nf2 in range(sf2):
                        print(var, model, ws_long, nf1, nf2)
                        path_to_file = ride_name = "csv_traj_merged_validation/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + var + "/" + model + "/" + ws_long
                        pd_file = pd.read_csv(path_to_file, index_col = False)
                        predicted_long = pd_file["predicted long"]
                        actual_long = pd_file["actual long"]
                        predicted_lat = pd_file["predicted lat"]
                        actual_lat = pd_file["actual lat"]
                        actual = [[actual_long[ix], actual_lat[ix]] for ix in range(len(actual_long))]
                        predicted = [[predicted_long[ix], predicted_lat[ix]] for ix in range(len(predicted_long))]
                        euclidean_dist = euclidean(actual_long, actual_lat, predicted_long, predicted_lat)
                        haversine_dist = haversine_array(actual_long, actual_lat, predicted_long, predicted_lat)
                        r2_pred = r2_score(actual, predicted)
                        mae_pred = mean_absolute_error(actual, predicted)
                        mse_pred = mean_squared_error(actual, predicted)
                        rmse_pred = math.sqrt(mse_pred)
                        print(r2_pred, mae_pred, mse_pred, rmse_pred, euclidean_dist, haversine_dist)
                        data_frame_traj_val["variable"].append(var)
                        data_frame_traj_val["model"].append(model)
                        data_frame_traj_val["ws"].append(ws_long.split("_")[0])
                        data_frame_traj_val["test"].append(nf1 + 1)
                        data_frame_traj_val["val"].append(nf2 + 1)
                        data_frame_traj_val["R2"].append(r2_pred)
                        data_frame_traj_val["MAE"].append(mae_pred)
                        data_frame_traj_val["MSE"].append(mse_pred)
                        data_frame_traj_val["RMSE"].append(rmse_pred)
                        data_frame_traj_val["euclid"].append(euclidean_dist)
                        data_frame_traj_val["haversine"].append(haversine_dist)

    df_data_frame_traj_val = pd.DataFrame(data_frame_traj_val)
    df_data_frame_traj_val.to_csv("data_frame_traj_val.csv", index = False)