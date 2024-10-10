import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def str_convert_new(val):
    new_val = val
    power_to = 0
    while abs(new_val) < 1 and new_val != 0.0:
        new_val *= 10
        power_to += 1 
    rounded = "$" + str(np.round(new_val, 2))
    if rounded[-2:] == '.0':
        rounded = rounded[:-2]
    if power_to != 0:  
        rounded += " \\times 10^{-" + str(power_to) + "}"
    return rounded + "$"

def new_metric_translate(metric_name):
    new_metric_name = {"euclid": "Euclidean distance",
                       "haversine": "Haversine distance"}
    if metric_name in new_metric_name:
        return new_metric_name[metric_name]
    else:
        return metric_name
    
def translate_category(long):
    translate_name = {
        "long no abs": "$x$ and $y$ offset",  
        "long speed dir": "Speed, heading, and time", 
        "long speed ones dir": "Speed, heading, and a 1s time interval",
        "long speed actual dir": "Speed, heading, and actual time"
    }
    if long in translate_name:
        return translate_name[long]
    else:
        return long
    
def draw_mosaic(rides_actual, rides_predicted, name, last_name):
    
    x_dim_rides = int(np.sqrt(len(rides_actual)))
    y_dim_rides = x_dim_rides
 
    while x_dim_rides * y_dim_rides < len(rides_actual):
        y_dim_rides += 1
    
    plt.figure(figsize = (10, 10 * y_dim_rides / x_dim_rides), dpi = 80)

    for ix_ride in range(len(rides_actual)):
 
        x_actual, y_actual = rides_actual[ix_ride]["long"], rides_actual[ix_ride]["lat"]
        x_predicted, y_predicted = rides_predicted[ix_ride]["long"], rides_predicted[ix_ride]["lat"]
            
        plt.subplot(y_dim_rides, x_dim_rides, ix_ride + 1)
        plt.rcParams.update({'font.size': 28}) 
        plt.rcParams['font.family'] = "serif"
        plt.rcParams["mathtext.fontset"] = "dejavuserif"
        plt.axis("equal")
        plt.axis("off")

        plt.plot(x_predicted, y_predicted, c = "b", linewidth = 2, label = "Estimated")
    
        plt.plot(x_actual, y_actual, c = "k", linewidth = 2, label = "Original")

    if not os.path.isdir(name):
        os.makedirs(name)
    plt.savefig(name + last_name + ".png", bbox_inches = "tight")
    plt.savefig(name + last_name + ".svg", bbox_inches = "tight")
    plt.savefig(name + last_name + ".pdf", bbox_inches = "tight")
    plt.close()
    
def draw_mosaic_one(x_actual, y_actual, x_predicted, y_predicted, k, model_name, name, ws_use, hidden_use, dist_name, metric_dist, dist_val):
     
    plt.figure(figsize = (10, 10), dpi = 80)
    plt.rcParams.update({'font.size': 28}) 
    plt.rcParams['font.family'] = "serif"
    plt.rcParams["mathtext.fontset"] = "dejavuserif"
    plt.axis("equal")
  
    plt.plot(x_predicted, y_predicted, c = "b", linewidth = 10, label = "Estimated")
  
    plt.plot(x_actual, y_actual, c = "k", linewidth = 10, label = "Original")

    plt.plot(x_actual[0], x_actual[0], marker = "o", label = "Start", color = "k", mec = "k", mfc = "g", ms = 20, mew = 10, linewidth = 10) 
   
    split_file_veh = k.split("/")
    vehicle = split_file_veh[0].replace("Vehicle_", "")
    ride = split_file_veh[-1].replace("events_", "").replace(".csv", "")
  
    title_new = "Vehicle " + vehicle + " Ride " + ride + "\n" + model_name.replace("_", " ") + " model\n" + "Window size " + str(ws_use) + "\n" + "Hidden layers " + str(hidden_use) + "\n" 

    title_new += translate_category(dist_name) + "\n" 
    
    title_new += metric_dist + ": " + str_convert_new(dist_val) + "\n"

    plt.title(title_new)
    plt.legend()
    plt.savefig(name, bbox_inches = "tight")
    plt.close()

vehicle_zero = os.listdir("csv_results_traj/1/1/")[0]
ride_zero = os.listdir("csv_results_traj/1/1/" + vehicle_zero)[0]
var_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/")
model_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/")
ws_long_list = os.listdir("csv_results_traj/1/1/" + vehicle_zero + "/" + ride_zero + "/" + var_list[0] + "/" + model_list[0] + "/")

round_val = ["R2", "MAE", "euclid", "haversine"]

df_dictio = pd.read_csv("data_frame_traj_val.csv", index_col = False)

dictio = dict()
for ix in range(len(df_dictio["variable"])):
    var = df_dictio["variable"][ix]
    if "time" in var:
        continue
    model = df_dictio["model"][ix]
    ws = df_dictio["ws"][ix]
    if var not in dictio:
        dictio[var] = dict()
    if model not in dictio[var]:
        dictio[var][model] = dict()
    if ws not in dictio[var][model]:
        dictio[var][model][ws] = dict()
    for metric in round_val:
        if metric not in df_dictio:
            continue
        if metric not in dictio[var][model][ws]:
            dictio[var][model][ws][metric] = []
        else:
            use_stdev = True
        dictio[var][model][ws][metric].append(df_dictio[metric][ix])

sf1, sf2 = 5, 5
for var in var_list:
    for model in model_list:
        for ws_long in ws_long_list:
            for nf2 in range(sf2):
                actual_rides = dict()
                predicted_rides = dict()
                ix_r = 0
                for nf1 in range(sf1):
                    for vehicle in os.listdir("csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"):
                        for ride in os.listdir("csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle):
                            traj_path = "csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + vehicle  + "/" + ride + "/" + var + "/" + model + "/" + ws_long
                            pd_file = pd.read_csv(traj_path, index_col = False)
                            predicted_rides[ix_r] = dict()
                            actual_rides[ix_r] = dict()
                            predicted_rides[ix_r]["long"] = pd_file["predicted long"]
                            actual_rides[ix_r]["long"] = pd_file["actual long"]
                            predicted_rides[ix_r]["lat"] = pd_file["predicted lat"]
                            actual_rides[ix_r]["lat"] = pd_file["actual lat"]
                            ix_r += 1
                print(var + "/" + model + "/" + str(nf2 + 1) + "/" + ws_long, len(actual_rides))
                draw_mosaic(actual_rides, predicted_rides, "compile_images/" + var + "/" + model + "/" + str(nf2 + 1) + "/", ws_long.replace("_predicted.csv", "_merge_val"))