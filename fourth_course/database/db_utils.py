import sqlite3

db_name = 'orgtehnika.db'


def get_db_connection():
    try:
        connection = sqlite3.connect(db_name)
        return connection
    except Exception as exc:
        print('Ошибка при подключении к БД: {exc}'.format(
            exc=exc
        ))
        return None


def if_user_exists(self, login, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    select 
        u_phone, u_fio, u_role
    from
        users
    where
        u_login = ? and u_password = ?;
    """, (login, password)
    )
    result = self.cursor.fetchone()

    return result
