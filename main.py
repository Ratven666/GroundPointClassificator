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

    # scan_full = Scan("Forest_full_5")
    # scan_full.load_scan_from_file(file_name="src/forest_full.txt")
    # GroundFilter(scan_full, max_v=2, k_value=3, n_vm=5).filter_scan(n=5, step=2.5)

    # scan_full = Scan("Forest_full_2")
    # scan_full.load_scan_from_file(file_name="src/forest_full.txt")
    # GroundFilter(scan_full, max_v=2, k_value=3, n_vm=5).filter_scan(n=5, step=2.5)
    #
    scan_full = Scan("Forest_full_13")
    scan_full.load_scan_from_file(file_name="src/forest_full_05.txt")
    GroundFilter(scan_full, max_v=2, k_value=4, n_vm=5).filter_scan(n=5, step=5)
    #
    # scan_full = Scan("Forest_full_4")
    # scan_full.load_scan_from_file(file_name="src/forest_full.txt")
    # GroundFilter(scan_full, max_v=2, k_value=3, n_vm=5).filter_scan(n=5, step=5)
if __name__ == "__main__":
    main()
