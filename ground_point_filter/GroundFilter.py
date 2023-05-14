from ground_point_filter.base.BIModel import BiModel
from ground_point_filter.base.DemModel import DemModel
from ground_point_filter.base.PlaneModel import PlaneModel
from ground_point_filter.base.VoxelModel import VoxelModel
from ground_point_filter.base.sm_utils.DemTypeEnum import DemTypeEnum
from ground_point_filter.point_filters.PointFilterByMaxV import PointFilterMaxV
from ground_point_filter.point_filters.PointFilterMedian import PointFilterMedian


class GroundFilter:

    def __init__(self, scan, n_vm, max_v=1, k_value=4):
        self.scan = scan
        self.k_value = k_value
        self.max_v = max_v
        self.n_vm = n_vm
        self.voxels_models = []


    def filter_scan(self, n, step):
        for n_vm in range(self.n_vm):
            delta = round(1 / self.n_vm * n_vm, 2)
            vm = VoxelModel(self.scan, step, dx=delta, dy=delta)
            self.voxels_models.append(vm)

        for idx in range(n):
            for n_vm, vm in enumerate(self.voxels_models):
                # dem_model = PlaneModel(vm)
                # dem_model = DemModel(vm)
                dem_model = BiModel(vm, DemTypeEnum.DEM)
                # dem_model = BiModel(vm, DemTypeEnum.PLANE, enable_mse=False)
                pf = PointFilterMedian(self.scan, dem_model, self.k_value)
                self.write_mse(pf, n_vm, idx, vm)
                if pf.median * self.k_value < self.max_v:
                    pf.filter_scan()
                else:
                    PointFilterMaxV(self.scan, dem_model, self.max_v).filter_scan()
                dem_model.delete_model()
            self.scan.save_scan_in_file(f"{self.scan.scan_name}_filt_{n_vm}_{idx}.txt")
            print("\n"*50)

    def write_mse(self, pfm, n_vm, n, vm):
        with open(f"{self.scan.scan_name}_mse_data.txt", "a", encoding="utf-8") as file:
            data = f"{n_vm} {n} {vm.vm_name} {self.scan.len} {pfm.MSE} {pfm.median}\n"
            file.write(data)

