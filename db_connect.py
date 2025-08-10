import oracledb

def get_connection():
    username = 'sys'
    password = 'orcl_RUC1'
    dsn = 'localhost:1521/orcl'
    
    connection = oracledb.connect(
        user=username,
        password=password,
        dsn=dsn,
        mode=oracledb.AUTH_MODE_SYSDBA  # Essential for sys user
    )
    return connection
