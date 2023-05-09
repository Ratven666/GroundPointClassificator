import os
import sqlite3

from CONFIG import DATABASE_NAME
from ground_point_filter.base.Point import Point


class SqlLiteScanIterator:
    """
    Иттератор скана из БД SQLite
    Реализован через стандартную библиотеку sqlite3
    """
    def __init__(self, scan):
        self.__path = os.path.join("data_bases", DATABASE_NAME)
        self.scan_id = scan.id
        self.cursor = None
        self.generator = None

    def __iter__(self):
        connection = sqlite3.connect(self.__path)
        self.cursor = connection.cursor()
        self.generator = (Point.parse_point_from_db_row(data) for data in
                          self.cursor.execute("""SELECT p.id, p.X, p.Y, p.Z,
                                                    p.R, p.G, p.B, p.is_ground
                                                    FROM points p
                                                    JOIN points_scans ps ON ps.point_id = p.id
                                                    WHERE ps.scan_id = (?)""", (self.scan_id,)))
        return self.generator

    def __next__(self):
        try:
            return next(self.generator)
        except StopIteration:
            self.cursor.close()
            raise StopIteration
        finally:
            self.cursor.close()
