from database.DB_connect import DBConnect
from model.album import Album
from model.track import Track

class DAO:

    @staticmethod
    def get_tracce():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * \
                    FROM track """

        cursor.execute(query)

        for row in cursor:
            result.append(Track(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_albums():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * \
                    FROM album """

        cursor.execute(query)

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def recupera_archi():
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        """query = select tr1.album_id as a1, tr2.album_id as a2
						from track tr1, track tr2
						where (tr1.id, tr2.id) IN (
                                                    select t1.id, t2.id
                                                    from track t1, track t2, playlist_track pt1, playlist_track pt2
                                                    where t1.album_id != t2.album_id and t1.id = pt1.track_id and t2.id = pt2.track_id and pt1.playlist_id = pt2.playlist_id
                                                    group by t1.id, t2.id)"""

        query = """SELECT DISTINCT t1.album_id AS a1, t2.album_id AS a2
                    FROM playlist_track pt1,
                         playlist_track pt2,
                         track t1,
                         track t2
                    WHERE pt1.playlist_id = pt2.playlist_id
                      AND pt1.track_id = t1.id
                      AND pt2.track_id = t2.id
                      AND t1.album_id < t2.album_id"""

        cursor.execute(query)

        for row in cursor:
            result.append((row["a1"], row["a2"])) #lista di tuple che sarebbero gli archi

        cursor.close()
        conn.close()
        return result
