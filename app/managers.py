import sqlite3

from app.models import Actor


class ActorManager():
    def __init__(self) -> None:
        self.db_name = "db_name"
        self.table_name = "table_name"
        self._connection = sqlite3.connect(f"{self.db_name}")

    def create(self, first_name: str, last_name: str) -> None:
        self._connection.execute(
            f"INSERT INTO {self.table_name} (FORMAT) VALUES (?)",
            (first_name, last_name)
        )
        self._connection.execute()

    def all(self) -> list:
        actor_manager_cursor = self._connection.execute(
            f"SELECT * FROM {self.table_name}"
        )
        if not actor_manager_cursor:
            return []
        return [Actor(*row) for row in actor_manager_cursor]

    def update(self, pk: int, new_first_name: str, new_last_name: str) -> None:
        self._connection.execute(
            f"UPDATE {self.table_name} "
            "SET FORMAT = ? "
            "WHERE ID = ? ",
            (new_first_name, new_last_name, pk)
        )
        self._connection.commit()

    def delete(self, pk: int) -> None:
        self._connection.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            (pk, )
        )
        self._connection.commit()
