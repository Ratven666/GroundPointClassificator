from ground_point_filter.point_filters.PointFilterABC import PointFilterABC


class PointFilterByModelMSE(PointFilterABC):

    def __init__(self, scan, full_dem_model, ground_dem_model=None, k_value=2.5):
        super().__init__(scan)
        self.dem_model = full_dem_model
        self.ground_dem_model = ground_dem_model
        if ground_dem_model is not None:
            self.MSE = self.ground_dem_model.mse_data
        else:
            self.MSE = self.dem_model.mse_data
        self.k_value = k_value

    def _filter_logic(self, point):
        cell = self.dem_model.get_model_element_for_point(point)
        if cell is None or cell.mse is None:
            return False
        try:
            cell_z = cell.get_z_from_xy(point.X, point.Y)
        except TypeError:
            return False
        v = point.Z - cell_z
        if v <= self.MSE * self.k_value:
            return True
        else:
            return False
