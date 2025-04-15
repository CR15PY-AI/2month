import sqlite3

class Task:
    def __init__(self, id, title, description, is_done = False):
        self.id = id
        self.title = title
        self.description = description
        self.is_done = is_done
    
    def save(self, task):
        self.cursor.execute("INSERT INTO todomanager (title, description, is_done) VALUES (?,?)", (task.title, task.description, task.is_done))
        self.connection.commit()
    def mark_done(self):
        self.cursor.execute("UPDATE todomanager SET is_done = ? WHERE is_done = ?", (1, 0))
    def delete(self, id):
        self.cursor.execute("DELETE FROM todomanager WHERE id = ?", (id,))




class TaskManager:
    def __init__(self, db_name = "todomanager.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS todomanager(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                description TEXT,
                is_done BOOLEAN)
                            """)
    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM todomanager")
        tasks = self.cursor.fetchall()
        print(tasks)

    def get_pending_tasks(self):
        self.cursor.execute('SELECT * FROM todomanager WHERE is_done = ?',(0))
        pend_tasks = self.cursor.fetchall()
        print(pend_tasks)
    def get_task_by_id(self, id):
        self.cursor.execute("SELECT * FROM todomanager WHERE id = ?", (id,))
        o = self.cursor.fetchone()
        print(o)
    def delete_by_id(self, id):
        self.cursor.execute("DELETE FROM todomanager WHERE id = ?", (id,))