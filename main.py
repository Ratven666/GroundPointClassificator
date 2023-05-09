from ground_point_filter.base.DemModel import DemModel
from ground_point_filter.base.PlaneModel import PlaneModel
from ground_point_filter.base.VoxelModel import VoxelModel
from ground_point_filter.base.Scan import Scan
from ground_point_filter.start_db import create_db


def main():
    create_db()

    scan = Scan("PIT")
    scan.load_scan_from_file(file_name="src/New_1.txt")
    # scan.plot()

    vm = VoxelModel(scan, 1)
    # vm.plot()

    dem_model = DemModel(vm)
    # dem_model.plot()

    plane_model = PlaneModel(vm)
    plane_model.plot()

if __name__ == "__main__":
    main()
