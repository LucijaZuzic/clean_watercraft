import os
import pandas as pd
import math
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import os

sf1, sf2 = 5, 5

vehicle_zero = os.listdir("csv_results/1/1/")[0]
ride_zero = os.listdir("csv_results/1/1/" + vehicle_zero)[0]
var_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/")
model_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
ws_long_list = os.listdir("csv_results/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/" + model_list[0] + "/")

if not os.path.isfile("data_frame_total_reverse.csv"):

    data_frame_total_reverse = {"variable": [], "model": [], "ws": [], "R2": [], "MAE": [], "MSE": [], "RMSE": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                print(var, model, ws_long)
                path_to_file = ride_name = "csv_merged_validation/total/" + var + "/" + model + "/" + ws_long
                pd_file = pd.read_csv(path_to_file, index_col = False)
                predicted = pd_file["predicted"]
                actual = pd_file["actual"]
                r2_pred = r2_score(actual, predicted)
                mae_pred = mean_absolute_error(actual, predicted)
                mse_pred = mean_squared_error(actual, predicted)
                rmse_pred = math.sqrt(mse_pred)
                print(r2_pred, mae_pred, mse_pred, rmse_pred)
                data_frame_total_reverse["variable"].append(var)
                data_frame_total_reverse["model"].append(model)
                data_frame_total_reverse["ws"].append(ws_long.split("_")[0])
                data_frame_total_reverse["R2"].append(r2_pred)
                data_frame_total_reverse["MAE"].append(mae_pred)
                data_frame_total_reverse["MSE"].append(mse_pred)
                data_frame_total_reverse["RMSE"].append(rmse_pred)

    df_data_frame_total_reverse = pd.DataFrame(data_frame_total_reverse)
    df_data_frame_total_reverse.to_csv("data_frame_total_reverse.csv", index = False)

if False and not os.path.isfile("data_frame_total.csv"):

    data_frame_total = {"variable": [], "model": [], "ws": [], "R2": [], "MAE": [], "MSE": [], "RMSE": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                print(var, model, ws_long)
                path_to_file = ride_name = "csv_merged/total/" + var + "/" + model + "/" + ws_long
                pd_file = pd.read_csv(path_to_file, index_col = False)
                predicted = pd_file["predicted"]
                actual = pd_file["actual"]
                r2_pred = r2_score(actual, predicted)
                mae_pred = mean_absolute_error(actual, predicted)
                mse_pred = mean_squared_error(actual, predicted)
                rmse_pred = math.sqrt(mse_pred)
                print(r2_pred, mae_pred, mse_pred, rmse_pred)
                data_frame_total["variable"].append(var)
                data_frame_total["model"].append(model)
                data_frame_total["ws"].append(ws_long.split("_")[0])
                data_frame_total["R2"].append(r2_pred)
                data_frame_total["MAE"].append(mae_pred)
                data_frame_total["MSE"].append(mse_pred)
                data_frame_total["RMSE"].append(rmse_pred)

if False and not os.path.isfile("data_frame_test_reverse.csv"):

    df_data_frame_total = pd.DataFrame(data_frame_total)
    df_data_frame_total.to_csv("data_frame_total.csv", index = False)

    data_frame_test_reverse = {"variable": [], "model": [], "ws": [], "val": [], "R2": [], "MAE": [], "MSE": [], "RMSE": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                for nf2 in range(sf2):
                    print(var, model, ws_long, nf2)
                    path_to_file = ride_name = "csv_merged_validation/" + str(nf2 + 1) + "/total/" + var + "/" + model + "/" + ws_long
                    pd_file = pd.read_csv(path_to_file, index_col = False)
                    predicted = pd_file["predicted"]
                    actual = pd_file["actual"]
                    r2_pred = r2_score(actual, predicted)
                    mae_pred = mean_absolute_error(actual, predicted)
                    mse_pred = mean_squared_error(actual, predicted)
                    rmse_pred = math.sqrt(mse_pred)
                    print(r2_pred, mae_pred, mse_pred, rmse_pred)
                    data_frame_test_reverse["variable"].append(var)
                    data_frame_test_reverse["model"].append(model)
                    data_frame_test_reverse["ws"].append(ws_long.split("_")[0])
                    data_frame_test_reverse["val"].append(nf2 + 1)
                    data_frame_test_reverse["R2"].append(r2_pred)
                    data_frame_test_reverse["MAE"].append(mae_pred)
                    data_frame_test_reverse["MSE"].append(mse_pred)
                    data_frame_test_reverse["RMSE"].append(rmse_pred)

    df_data_frame_test_reverse = pd.DataFrame(data_frame_test_reverse)
    df_data_frame_test_reverse.to_csv("data_frame_test_reverse.csv", index = False)

if False and not os.path.isfile("data_frame_test.csv"):

    data_frame_test = {"variable": [], "model": [], "ws": [], "test": [], "R2": [], "MAE": [], "MSE": [], "RMSE": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                for nf1 in range(sf1):
                    print(var, model, ws_long, nf1)
                    path_to_file = ride_name = "csv_merged/" + str(nf1 + 1) + "/total/" + var + "/" + model + "/" + ws_long
                    pd_file = pd.read_csv(path_to_file, index_col = False)
                    predicted = pd_file["predicted"]
                    actual = pd_file["actual"]
                    r2_pred = r2_score(actual, predicted)
                    mae_pred = mean_absolute_error(actual, predicted)
                    mse_pred = mean_squared_error(actual, predicted)
                    rmse_pred = math.sqrt(mse_pred)
                    print(r2_pred, mae_pred, mse_pred, rmse_pred)
                    data_frame_test["variable"].append(var)
                    data_frame_test["model"].append(model)
                    data_frame_test["ws"].append(ws_long.split("_")[0])
                    data_frame_test["test"].append(nf1 + 1)
                    data_frame_test["R2"].append(r2_pred)
                    data_frame_test["MAE"].append(mae_pred)
                    data_frame_test["MSE"].append(mse_pred)
                    data_frame_test["RMSE"].append(rmse_pred)

    df_data_frame_test = pd.DataFrame(data_frame_test)
    df_data_frame_test.to_csv("data_frame_test.csv", index = False)

if not os.path.isfile("data_frame_val.csv"):

    data_frame_val  = {"variable": [], "model": [], "ws": [], "test": [], "val": [], "R2": [], "MAE": [], "MSE": [], "RMSE": []}
    for var in var_list:
        for model in model_list:
            for ws_long in ws_long_list:
                for nf1 in range(sf1):
                    for nf2 in range(sf2):
                        print(var, model, ws_long, nf1, nf2)
                        path_to_file = ride_name = "csv_merged_validation/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + var + "/" + model + "/" + ws_long
                        pd_file = pd.read_csv(path_to_file, index_col = False)
                        predicted = pd_file["predicted"]
                        actual = pd_file["actual"]
                        r2_pred = r2_score(actual, predicted)
                        mae_pred = mean_absolute_error(actual, predicted)
                        mse_pred = mean_squared_error(actual, predicted)
                        rmse_pred = math.sqrt(mse_pred)
                        print(r2_pred, mae_pred, mse_pred, rmse_pred)
                        data_frame_val["variable"].append(var)
                        data_frame_val["model"].append(model)
                        data_frame_val["ws"].append(ws_long.split("_")[0])
                        data_frame_val["test"].append(nf1 + 1)
                        data_frame_val["val"].append(nf2 + 1)
                        data_frame_val["R2"].append(r2_pred)
                        data_frame_val["MAE"].append(mae_pred)
                        data_frame_val["MSE"].append(mse_pred)
                        data_frame_val["RMSE"].append(rmse_pred)

    df_data_frame_val = pd.DataFrame(data_frame_val)
    df_data_frame_val.to_csv("data_frame_val.csv", index = False)