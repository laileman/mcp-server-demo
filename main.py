# server

from mcp.server.fastmcp import FastMCP
from utils.schema import mysqlClient

# create a mcp server
server = FastMCP("mysql")


# create a user
@server.tool("create a user")
def create_user(name: str, age: int) -> int:
    """
    create a user
    :param name:
    :param age:
    :return: a user id
    """
    res = mysqlClient.create_user(name, age)
    return res


# search all users
@server.tool("search all users")
def search_all_users() -> list:
    """
    search all users
    :return:
    """
    return mysqlClient.search_all_users()


# search a user
@server.tool("search a user")
def search_user(name: str) -> list:
    """
    search a user
    :param name:
    :return:
    """
    return mysqlClient.search_user(name)


# create a group
@server.tool("create a group")
def create_group(name: str) -> int:
    """
    create a group
    :param name:
    :return: group id
    """
    res = mysqlClient.create_group(name)
    return res


# search all groups
@server.tool("search all groups")
def search_all_groups() -> list:
    """
    search all groups
    :return:
    """
    return mysqlClient.search_all_groups()


# search a group
@server.tool("search a group")
def search_group(name: str) -> list:
    """
    search a group
    :param name:
    :return:
    """
    return mysqlClient.search_group(name)


# get all tables
@server.tool("get all tables")
def get_all_tables() -> list:
    """
    get all tables
    :return:
    """
    tables = mysqlClient.search_all_table()
    return tables


#
if __name__ == "__main__":
    server.run(transport="stdio")
