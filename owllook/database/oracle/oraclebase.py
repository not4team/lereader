#!/usr/bin/env python
import cx_Oracle
from owllook.utils.tools import singleton


@singleton
class OracleBase:
    db201909220328_medium = """(description= (address=(protocol=tcps)(port=1522)(host=adb.ap-seoul-1.oraclecloud.com))(connect_data=(service_name=khtstzmwgpzncgm_db201909220328_medium.adwc.oraclecloud.com))(security=(ssl_server_cert_dn=
        "CN=adb.ap-seoul-1.oraclecloud.com,OU=Oracle ADB SEOUL,O=Oracle Corporation,L=Redwood City,ST=California,C=US"))   )"""

    connect_string = ("%s/%s@%s") % ("novel",
                                     "omNnd#235643", db201909220328_medium)

    def __init__(self):
        # Create the session pool
        self.pool = cx_Oracle.SessionPool("novel", "omNnd#235643", self.db201909220328_medium,
                                          min=2, max=5, increment=1, threaded=True, encoding="UTF-8", nencoding="UTF-8")

    def get_db(self):
        # Acquire a connection from the pool
        connection = self.pool.acquire()
        return connection

    def release(self, conn):
        self.pool.release(conn)
