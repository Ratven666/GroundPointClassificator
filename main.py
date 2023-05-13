from ground_point_filter.GroundFilter import GroundFilter
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
    scan_full.load_scan_from_file(file_name="src/New_1.txt")
    # scan_full.save_scan_in_file("forest_filt_1.txt")
    vm1 = VoxelModel(scan_full, 0.25, dx=0.0, dy=0.0)
    vm2 = VoxelModel(scan_full, 0.25, dx=0.25, dy=0.25)
    vm3 = VoxelModel(scan_full, 0.25, dx=0.5, dy=0.5)
    vm4 = VoxelModel(scan_full, 0.25, dx=0.75, dy=0.75)


    pm1 = DemModel(vm1)
    pm2 = DemModel(vm2)
    pm3 = DemModel(vm3)
    pm4 = DemModel(vm4)


    pm1.plot_mse()
    pm2.plot_mse()
    pm3.plot_mse()
    pm4.plot_mse()

    # GroundFilter(scan_full, max_v=1.5, k_value=3).filter_scan(n=5, step=9)

if __name__ == "__main__":
    main()
