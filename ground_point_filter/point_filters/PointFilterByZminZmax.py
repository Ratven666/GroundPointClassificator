from ground_point_filter.point_filters.PointFilterABC import PointFilterABC


class PointFilterByZminZmax(PointFilterABC):

    def __init__(self, scan, z_min=None, z_max=None):
        super().__init__(scan)
        self.z_min = z_min
        self.z_max = z_max

    def _filter_logic(self, point):
        if self.z_min is not None and point.Z < self.z_min:
            return False
        if self.z_max is not None and point.Z > self.z_max:
            return False
        return True
