from ground_point_filter.base.DemModel import DemModel
from ground_point_filter.base.PlaneModel import PlaneModel
from ground_point_filter.base.VoxelModel import VoxelModel
from ground_point_filter.base.Scan import Scan
from ground_point_filter.point_filters.PointFilterByModelMSE import PointFilterByModelMSE
from ground_point_filter.point_filters.PointFilterByZminZmax import PointFilterByZminZmax
from ground_point_filter.point_filters.PointFilterMedian import PointFilterMedian
from ground_point_filter.start_db import create_db


def main():
    create_db()

    scan_full = Scan("Forest_full")
    scan_full.load_scan_from_file(file_name="src/forest_full_05.txt")
    # scan_full.save_scan_in_file("forest_filt_1.txt")

    scan_gp = Scan("Forest_gp_m")
    scan_gp.load_scan_from_file(file_name="src/forest_gp_m_1.txt")
    scan_gp.load_scan_from_file(file_name="src/forest_gp_m_2.txt")
    scan_gp.load_scan_from_file(file_name="src/forest_gp_m_3.txt")
    # scan_full.plot()

    vm_full = VoxelModel(scan_full, 20)
    vm_gp = VoxelModel(scan_gp, 10)

    plane_model_full = PlaneModel(vm_full)
    plane_model_gp = PlaneModel(vm_gp)
    # plane_model_full.plot()
    # plane_model_gp.plot_mse()
    # plane_model_gp.plot_mse_hist()
    #
    # # plane_model_full.plot_mse()
    # plane_model_full.plot_mse_hist()

    # PointFilterByModelMSE(scan_full, full_dem_model=plane_model_full,
    #                       ground_dem_model=plane_model_gp,
    #                       k_value=6).filter_scan()
    PointFilterMedian(scan_full, full_dem_model=plane_model_full, k_value=3).filter_scan()
    plane_model_full.delete_model()
    plane_model_full = PlaneModel(vm_full)
    PointFilterMedian(scan_full, full_dem_model=plane_model_full, k_value=4)

    scan_full.save_scan_in_file("forest_filt_1.txt")

    # plane_model_full.plot_mse()
    # plane_model_full.plot_mse_hist()

    # scan_full.plot()


if __name__ == "__main__":
    main()
