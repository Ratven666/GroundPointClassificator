from ground_point_filter.base.PlaneModel import PlaneModel
from ground_point_filter.base.VoxelModel import VoxelModel
from ground_point_filter.point_filters.PointFilterByMaxV import PointFilterMaxV
from ground_point_filter.point_filters.PointFilterMedian import PointFilterMedian


class GroundFilter:

    def __init__(self, scan, max_v=1, k_value=4):
        self.scan = scan
        self.k_value = k_value
        self.max_v = max_v

    def filter_scan(self, n, step):
        vm = VoxelModel(self.scan, step)
        for _ in range(n):
            dem_model = PlaneModel(vm)
            pf = PointFilterMedian(self.scan, dem_model, self.k_value)
            if pf.median * self.k_value < self.max_v:
                pf.filter_scan()
            else:
                PointFilterMaxV(self.scan, dem_model, self.max_v).filter_scan()
            dem_model.delete_model()
        self.scan.save_scan_in_file("forest_filt_1.txt")
