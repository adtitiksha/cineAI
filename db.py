import sqlite3

import pandas as pd

# DB_FILE = "sqlite:///db_finfolio.sqlite3" # for SQLAlchemy
DB_FILE = "db.sqlite"


def query(sql_query: str, **kwargs) -> pd.DataFrame:
    """
    Wrapper around pd.read_sql to gracefully close database connection after use.
    To be used for all SELECT statements

    Parameters
    ----------
    sql_query
        _description_

    Returns
    -------
        _description_
    """

    con = sqlite3.connect(DB_FILE)
    try:
        df = pd.read_sql(sql_query, con, **kwargs)
    finally:
        con.close()
    return df


def write_table(df: pd.DataFrame, table_name: str, **kwargs) -> int | None:
    """
    Wrapper around pd.to_sql to gracefully close database connection after use.

    Parameters
    ----------
    df
        _description_

    Returns
    -------
        _description_
    """

    con = sqlite3.connect(DB_FILE)
    try:
        ret_value = df.to_sql(name=table_name, con=con, index=False, **kwargs)
    finally:
        con.close()
    return ret_value


def execute(sql_query: str, data: tuple | list, bulk: bool = False) -> None:
    """Helper function for (bulk) INSERT / UPDATE / DELETE queries

    Parameters
    ----------
    sql_query
        _description_
    data
        _description_
    bulk, optional
        whether to call execute, or executemany, by default False
    """

    con = sqlite3.connect(DB_FILE)
    try:
        cur = con.cursor()
        if bulk:
            cur.executemany(sql_query, data)
        else:
            cur.execute(sql_query, data)
        con.commit()
    finally:
        con.close()
