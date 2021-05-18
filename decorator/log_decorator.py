def log(func):
    def _wrapper(*args, **kwargs):
        print(f'input của hàm {func} là: {args} {kwargs}')
        try:
            result = func(*args, **kwargs)
            print(f'output của hàm {func} là {result}')
        except BaseException as exc:
            print(
                f'hàm {func} văng lỗi: {exc}'
            )
            raise exc

    return _wrapper


class DBConnector:
    instance = None

    def __init__(
            self,
            db_conn_string,
    ):
        self.db_conn_string = db_conn_string
        self.conn = {
            'db': db_conn_string
        }

    @log
    def query(self, sql):
        return self.conn['db'] + sql

    @log
    def select(self, sql):
        return sql


@log
def tong(a, b, tong_so_am=False):
    if (a < 0 or b < 0) and not tong_so_am:
        raise ValueError(
            'Hàm này không thích tính tổng của số âm'
        )

    return a + b


tong(1, 2)
tong(-1, 2)
tong(-1, 2, tong_so_am=True)
