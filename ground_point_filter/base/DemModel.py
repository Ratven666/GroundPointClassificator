from ground_point_filter.base.DemCell import DemCell
from ground_point_filter.base.Scan import Scan
from ground_point_filter.base.SegmentedModelABC import SegmentedModelABC
from ground_point_filter.base.sm_utils.DemTypeEnum import DemTypeEnum


class DemModel(SegmentedModelABC):
    """
    Стандартная DEM модель связанная с базой данных
    """

    def __init__(self, voxel_model):
        self.model_type = DemTypeEnum.DEM
        self.model_name = f"{self.model_type.name}_from_{voxel_model.vm_name}"
        self.mse_data = None
        self.cell_type = DemCell
        super().__init__(voxel_model, self.cell_type)

    def _calk_segment_model(self):
        """
        Метод определяющий логику создания стандартной DEM модели
        :return: None
        """
        self.logger.info(f"Начат расчет модели {self.model_name}")
        base_scan = Scan.get_scan_from_id(self.voxel_model.base_scan_id)
        self.__calk_average_z(base_scan)
        self._calk_cell_mse(base_scan)

    def __calk_average_z(self, base_scan):
        """
        Расчет средней высотной отметки между точками в ячейке
        :param base_scan: базовый скан воксельной модели
        :return: None
        """
        for point in base_scan:
            dem_cell = self.get_model_element_for_point(point)
            if dem_cell is None:
                continue
            try:
                dem_cell.avr_z = (dem_cell.avr_z * dem_cell.len + point.Z) / (dem_cell.len + 1)
                dem_cell.len += 1
            except AttributeError:
                dem_cell.avr_z = point.Z
                dem_cell.len = 1
        self.logger.info(f"Расчет средних высот модели {self.model_name} завершен")
