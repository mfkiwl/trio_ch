#!/usr/bin/env python

import data_containers as dc
import radar_plots as rplt


def main(conf_data):
    # Load Data from .mat file
    if conf_data["filename_LeftRadar"]:
        l = []
        l.append(conf_data["path_data_folder"])
        l.append(conf_data["filename_LeftRadar"])
        leftradar_path = ''.join(l)

        lst_det_left = dc.DetectionList()
        lst_det_left.append_from_m_file(leftradar_path, True, conf_data["EGO_car_width"])
        mcc_interval_left = lst_det_left.get_mcc_interval()
        print("MCC Left starts at: ", mcc_interval_left[0],
              "and ends at: ", mcc_interval_left[1])
    else:
        lst_det_left = None

    if conf_data["filename_RightRadar"]:
        l = []
        l.append(conf_data["path_data_folder"])
        l.append(conf_data["filename_RightRadar"])
        rightradar_path = ''.join(l)

        lst_det_right = dc.DetectionList()
        lst_det_right.append_from_m_file(rightradar_path, False, conf_data["EGO_car_width"])
        mcc_interval_right = lst_det_right.get_mcc_interval()
        print("MCC Right starts at: ", mcc_interval_right[0], "and ends at: ", mcc_interval_right[1])
    else:
        lst_det_right = None

    if conf_data["output_folder"]:
        l = []
        l.append(conf_data["output_folder"])
        fname_det = '_tmp%s.png' % conf_data["scenario"]
        l.append(fname_det)
        output_path = ''.join(l)
    else:
        output_path = None

    rplt.static_plot(lst_det_left, lst_det_right, conf_data["beams_tp"], output_path)


if __name__ == "__main__":
    conf_data = dc.parse_CMDLine("./analysis.cnf")

if conf_data:
        main(conf_data)
