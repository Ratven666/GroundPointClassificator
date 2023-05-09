from ground_point_filter.base.scan_utils.iterators.BaseScanIterator import BaseScanIterator
from ground_point_filter.base.scan_utils.iterators.SqlLiteScanIterator import SqlLiteScanIterator
from ground_point_filter.start_db import engine


class ScanIterator:
    """
    Фабрика иттераторов сканов для сканов из БД
    """
    def __init__(self, scan):
        self.__scan_iterator = None
        self.__scan = scan
        self.__chose_scan_iterator()

    def __chose_scan_iterator(self):
        """
        Выбирает иттератор скана на основании типа используемой БД
        :return:
        """
        db_type = engine.dialect.name
        if db_type == "sqlite":
            self.__scan_iterator = SqlLiteScanIterator(self.__scan)
        else:
            self.__scan_iterator = BaseScanIterator(self.__scan)

    def __iter__(self):
        return iter(self.__scan_iterator)
