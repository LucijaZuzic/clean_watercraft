from utilities import load_object
import os
import numpy as np
import matplotlib.pyplot as plt

def make_hist(list_lens, title_use):
    print(title_use)
    print(min(list_lens), max(list_lens), np.average(list_lens), np.mean(list_lens), np.median(list_lens))
    print(np.percentile(list_lens, 0), np.percentile(list_lens, 25), np.percentile(list_lens, 50), np.percentile(list_lens, 75), np.percentile(list_lens, 100))
    plt.figure()
    varnew = title_use.replace("_", " ").replace("longitude no abs", "$x$ offset").replace("direction", "heading")
    varnew = varnew.replace("latitude no abs", "$y$ offset").replace("Area x", "Area $x$").replace("Area y", "Area $y$")
    plt.hist(list_lens)
    if "time" == title_use:
        plt.xlabel(varnew.capitalize() + " ($s$)")
    if "speed" == title_use:
        plt.xlabel(varnew.capitalize() + " ($km/h$)")
    if "longitude_no_abs" == title_use:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    if "latitude_no_abs" == title_use:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    if "direction" == title_use:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    if "Area" in title_use and "total" not in title_use:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    if "Area" in title_use and "total" in title_use:
        plt.xlabel(varnew.capitalize() + " ($\degree^{2}$)")
    if "Size" in title_use and "total" not in title_use:
        plt.xlabel(varnew.capitalize())
    plt.ylabel("Frequency")
    if not os.path.isdir("hist_plot"):
        os.makedirs("hist_plot")
    plt.savefig("hist_plot/" + title_use.lower().replace(" ", "_") + ".png", bbox_inches = "tight")
    plt.savefig("hist_plot/" + title_use.lower().replace(" ", "_") + ".svg", bbox_inches = "tight")
    plt.savefig("hist_plot/" + title_use.lower().replace(" ", "_") + ".pdf", bbox_inches = "tight")
    plt.close()

sf1, sf2 = 5, 3

num_to_ws = [-1, 5, 6, 5, 6, 5, 6, 5, 6, 2, 10, 20, 30, 2, 10, 20, 30, 2, 10, 20, 30, 2, 10, 20, 30, 3, 3, 3, 3, 4, 4, 4, 4, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 15, 15, 15, 15, 19, 19, 19, 19, 25, 25, 25, 25, 29, 29, 29, 29, 16, 16, 16, 16, 32, 32, 32, 32]

num_to_params = [-1, 1, 1, 2, 2, 3, 3, 4, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

actual_var = dict()
actual_var_all = dict()
lens_dict = dict()
for nf2 in [sf2]:
    for nf1 in range(sf1):
        ride_name = "csv_results/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/"
        varnames = os.listdir("actual/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/")
        for v in varnames:
            var = v.replace("actual_", "")
            actual_var_par = load_object("actual/" + str(nf1 + 1) + "/" + str(nf2 + 1) + "/" + v)
            for r in actual_var_par:
                if r not in actual_var:
                    actual_var[r] = dict()
                actual_var[r][var] = actual_var_par[r]
                if var not in actual_var_all:
                    actual_var_all[var] = []
                actual_var_all[var].extend(actual_var_par[r])
                if var not in lens_dict:
                    lens_dict[var] = dict()
                lens_dict[var][r] = len(actual_var_par[r])
print(len(actual_var))
print(list(actual_var_all.keys()))
for var in lens_dict:
    make_hist(list(lens_dict[var].values()), "Size " + var)
    print(sum(list(lens_dict[var].values())))
for var in actual_var_all:
    make_hist(actual_var_all[var], var)
ix_plot = 0
plt.figure()
for var in actual_var_all:
    if "time" in var:
        continue
    ix_plot += 1
    plt.subplot(2, 2, ix_plot)
    varnew = var.replace("_", " ").replace("longitude no abs", "$x$ offset").replace("direction", "heading")
    varnew = varnew.replace("latitude no abs", "$y$ offset")
    if "speed" == var:
        plt.xlabel(varnew.capitalize() + " ($km/h$)")
    if "longitude_no_abs" == var:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    if "latitude_no_abs" == var:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    if "direction" == var:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    plt.ylabel("Frequency")
    plt.hist(actual_var_all[var])
    if not os.path.isdir("hist_plot"):
        os.makedirs("hist_plot")
plt.savefig("hist_plot/all_var_no_time_hist.png", bbox_inches = "tight")
plt.savefig("hist_plot/all_var_no_time_hist.svg", bbox_inches = "tight")
plt.savefig("hist_plot/all_var_no_time_hist.pdf", bbox_inches = "tight")
plt.close()
ix_plot = 0
plt.figure()
for var in actual_var_all:
    ix_plot += 1
    plt.subplot(2, 3, ix_plot)
    varnew = var.replace("_", " ").replace("longitude no abs", "$x$ offset").replace("direction", "heading")
    varnew = varnew.replace("latitude no abs", "$y$ offset")
    if "time" == var:
        plt.xlabel(varnew.capitalize() + " ($s$)")
    if "speed" == var:
        plt.xlabel(varnew.capitalize() + " ($km/h$)")
    if "longitude_no_abs" == var:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    if "latitude_no_abs" == var:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    if "direction" == var:
        plt.xlabel(varnew.capitalize() + " ($\degree$)")
    plt.ylabel("Frequency")
    plt.hist(actual_var_all[var])
    if not os.path.isdir("hist_plot"):
        os.makedirs("hist_plot")
plt.savefig("hist_plot/all_var_hist.png", bbox_inches = "tight")
plt.savefig("hist_plot/all_var_hist.svg", bbox_inches = "tight")
plt.savefig("hist_plot/all_var_hist.pdf", bbox_inches = "tight")
plt.close()
area_x_dict = dict()
area_y_dict = dict()
area_total_dict = dict()
for r in actual_var:
    list_long = actual_var[r]["longitude_no_abs"]
    list_lat = actual_var[r]["latitude_no_abs"]
    area_x_dict[r] = max(list_long) - min(list_long)
    area_y_dict[r] = max(list_lat) - min(list_lat)
    area_total_dict[r] = area_x_dict[r] * area_y_dict[r]
list_lens = list(area_x_dict.values())
make_hist(list(area_x_dict.values()), "Area x")
make_hist(list(area_y_dict.values()), "Area y")
make_hist(list(area_total_dict.values()), "Area total")
ix_plot = 0
plt.figure(figsize = (10, 10 * 21 / 19), dpi = 80)
for r in actual_var:
    ix_plot += 1
    plt.subplot(21, 19, ix_plot)
    plt.rcParams.update({'font.size': 28}) 
    plt.rcParams['font.family'] = "serif"
    plt.rcParams["mathtext.fontset"] = "dejavuserif"
    plt.axis("equal")
    plt.axis("off")
    plt.plot(actual_var[r]["longitude_no_abs"], actual_var[r]["latitude_no_abs"], c = "k", linewidth = 2)
plt.savefig("hist_plot/all_trajs.png", bbox_inches = "tight")
plt.savefig("hist_plot/all_trajs.svg", bbox_inches = "tight")
plt.savefig("hist_plot/all_trajs.pdf", bbox_inches = "tight")
plt.close()