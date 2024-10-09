from utilities import load_object
import os
import pandas as pd

sf1, sf2 = 5, 5

num_to_ws = [-1, 5, 6, 5, 6, 5, 6, 5, 6, 2, 10, 20, 30, 2, 10, 20, 30, 2, 10, 20, 30, 2, 10, 20, 30, 3, 3, 3, 3, 4, 4, 4, 4, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 15, 15, 15, 15, 19, 19, 19, 19, 25, 25, 25, 25, 29, 29, 29, 29, 16, 16, 16, 16, 32, 32, 32, 32]

num_to_params = [-1, 1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

for nf1 in range(sf1):

    for nf2 in range(sf2):

        ride_name = "csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"

        varnames = os.listdir("actual/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/")
        actual_var = dict()
        for v in varnames:
            var = v.replace("actual_", "")
            actual_var[var] = load_object("actual/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + v)
            
        predicted_all_units = load_object("UniTS_final_result_ws/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/longlat_speed_direction/predicted_all")
        predicted_all_attention = load_object("attention_result/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/predicted_all")
    
        for var in predicted_all_units:
            for units_model in predicted_all_units[var]:
                for ws in predicted_all_units[var][units_model]:
                    for ride in predicted_all_units[var][units_model][ws]:
                        dict_write = {"predicted": predicted_all_units[var][units_model][ws][ride], 
                                      "actual": actual_var[var][ride][:len(predicted_all_units[var][units_model][ws][ride])]}
                        ride_name = "csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + ride.replace(".csv", "/").replace("/cleaned_csv/", "/") + str(var) + "/" + units_model.split("_")[0] + "/" 
                        if not os.path.isdir(ride_name):
                            os.makedirs(ride_name)
                        df_write = pd.DataFrame(dict_write)
                        df_write.to_csv(ride_name + str(ws) + "_predictions.csv", index = False)
                        print(ride_name + str(ws) + "_predictions.csv")

        for var in predicted_all_attention:
            for attention_model in predicted_all_attention[var]:
                for num in predicted_all_attention[var][attention_model]:
                    for ride in predicted_all_attention[var][attention_model][num]:
                        dict_write = {"predicted": predicted_all_attention[var][attention_model][num][ride],
                                      "actual": actual_var[var][ride][:len(predicted_all_attention[var][attention_model][num][ride])]}
                        ride_name = "csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + ride.replace(".csv", "/").replace("/cleaned_csv/", "/") + str(var) + "/" + attention_model + "_" + str(num_to_params[num]) + "/" 
                        if not os.path.isdir(ride_name):
                            os.makedirs(ride_name)
                        df_write = pd.DataFrame(dict_write)
                        df_write.to_csv(ride_name + str(num_to_ws[num]) + "_predictions.csv", index = False)
                        print(ride_name + str(num_to_ws[num]) + "_predictions.csv")

        predicted_all_pytorch = dict()

        for part_name in os.listdir("pytorch_result/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"):
            predicted_all_pytorch[part_name] = load_object("pytorch_result/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + part_name + "/predicted_all")
            for var in predicted_all_pytorch[part_name]:
                for pytorch_model in predicted_all_pytorch[part_name][var]:
                    for ws in predicted_all_pytorch[part_name][var][pytorch_model]:
                        for hl in predicted_all_pytorch[part_name][var][pytorch_model][ws]:
                            for ride in predicted_all_pytorch[part_name][var][pytorch_model][ws][hl]:
                                dict_write = {"predicted": predicted_all_pytorch[part_name][var][pytorch_model][ws][hl][ride],
                                              "actual": actual_var[var][ride][:len(predicted_all_pytorch[part_name][var][pytorch_model][ws][hl][ride])]}
                                ride_name = "csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + ride.replace(".csv", "/").replace("/cleaned_csv/", "/") + str(var) + "/" + pytorch_model + "/" 
                                if not os.path.isdir(ride_name):
                                    os.makedirs(ride_name)
                                df_write = pd.DataFrame(dict_write)
                                df_write.to_csv(ride_name + str(ws) + "_predictions.csv", index = False)
                                print(ride_name + str(ws) + "_predictions.csv")