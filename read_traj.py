from utilities import load_object
import os
import pandas as pd

sf1, sf2 = 5, 5

num_to_ws = [-1, 5, 6, 5, 6, 5, 6, 5, 6, 2, 10, 20, 30, 2, 10, 20, 30, 2, 10, 20, 30, 2, 10, 20, 30, 3, 3, 3, 3, 4, 4, 4, 4, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 15, 15, 15, 15, 19, 19, 19, 19, 25, 25, 25, 25, 29, 29, 29, 29, 16, 16, 16, 16, 32, 32, 32, 32]

num_to_params = [-1, 1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

short_list_coord = ["long", "lat"]
short_list_names = ["predicted", "actual"]
long_list_names = [x + "_" + y for x in short_list_names for y in short_list_coord]
short_list_var = ["no abs", "speed actual dir"]
long_list_var = [x + " " + y for x in short_list_coord for y in short_list_var]

for nf1 in range(sf1):

    for nf2 in range(sf2):

        ride_name = "csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"
        
        predicted_all_units = dict()
        for l in long_list_names:
            predicted_all_units[l] = load_object("UniTS_final_result_ws/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/longlat_speed_direction/" + l)

        predicted_all_attention = dict()
        for l in long_list_names:
            predicted_all_attention[l] = load_object("attention_result/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + l)
    
        for units_model in predicted_all_units[long_list_names[0]]:
            for ws in predicted_all_units[long_list_names[0]][units_model]:
                for short_var in short_list_var:
                    for ride in predicted_all_units[long_list_names[0]][units_model][ws][long_list_var[0]]:
                        dict_write = dict()
                        for short_coord in short_list_coord:
                            dict_write["predicted " + short_coord] = predicted_all_units["predicted_" + short_coord][units_model][ws][short_coord + " " + short_var][ride]
                            dict_write["actual " + short_coord] = predicted_all_units["actual_" + short_coord][units_model][ws][ride]
                        ride_name = "csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + ride.replace(".csv", "/").replace("/cleaned_csv/", "/") + short_var + "/" + units_model.split("_")[0] + "/" 
                        if not os.path.isdir(ride_name):
                            os.makedirs(ride_name)
                        df_write = pd.DataFrame(dict_write)
                        df_write.to_csv(ride_name + str(ws) + "_predictions.csv", index = False)
                        print(ride_name + str(ws) + "_predictions.csv")
                        
        for attention_model in predicted_all_attention[long_list_names[0]]:
            for num in predicted_all_attention[long_list_names[0]][attention_model]:
                for short_var in short_list_var:
                    for ride in predicted_all_attention[long_list_names[0]][attention_model][num][long_list_var[0]]:
                        dict_write = dict()
                        for short_coord in short_list_coord:
                            dict_write["predicted " + short_coord] = predicted_all_attention["predicted_" + short_coord][attention_model][num][short_coord + " " + short_var][ride]
                            dict_write["actual " + short_coord] = predicted_all_attention["actual_" + short_coord][attention_model][num][ride]
                        ride_name = "csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + ride.replace(".csv", "/").replace("/cleaned_csv/", "/") + short_var + "/" + attention_model + "_" + str(num_to_params[num]) + "/" 
                        if not os.path.isdir(ride_name):
                            os.makedirs(ride_name)
                        df_write = pd.DataFrame(dict_write)
                        df_write.to_csv(ride_name + str(num_to_ws[num]) + "_predictions.csv", index = False)
                        print(ride_name + str(num_to_ws[num]) + "_predictions.csv")

        predicted_all_pytorch = dict()

        for part_name in os.listdir("pytorch_result/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"):
            predicted_all_pytorch[part_name] = dict()
            for l in long_list_names:
                predicted_all_pytorch[part_name][l] = load_object("pytorch_result/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + part_name + "/" + l)
            for pytorch_model in predicted_all_pytorch[part_name][long_list_names[0]]:
                for ws in predicted_all_pytorch[part_name][long_list_names[0]][pytorch_model]:
                    for hl in predicted_all_pytorch[part_name][long_list_names[0]][pytorch_model][ws]:
                        for short_var in short_list_var:
                            for ride in predicted_all_pytorch[part_name][long_list_names[0]][pytorch_model][ws][hl][long_list_var[0]]:
                                dict_write = dict()
                                for short_coord in short_list_coord:
                                    dict_write["predicted " + short_coord] = predicted_all_pytorch[part_name]["predicted_" + short_coord][pytorch_model][ws][hl][short_coord + " " + short_var][ride]
                                    dict_write["actual " + short_coord] = predicted_all_pytorch[part_name]["actual_" + short_coord][pytorch_model][ws][hl][ride]
                                ride_name = "csv_results_traj/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + ride.replace(".csv", "/").replace("/cleaned_csv/", "/") + short_var + "/" + pytorch_model + "/" 
                                if not os.path.isdir(ride_name):
                                    os.makedirs(ride_name)
                                df_write = pd.DataFrame(dict_write)
                                df_write.to_csv(ride_name + str(ws) + "_predictions.csv", index = False)
                                print(ride_name + str(ws) + "_predictions.csv")