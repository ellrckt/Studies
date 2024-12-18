import tkinter as tk
from tkinter import messagebox, ttk
from abc import ABC, abstractmethod
import psycopg2
from datetime import datetime
from typing import List, Dict, Union
import matplotlib.pyplot as plt

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="mydatabase",
            user="myuser",
            password="mypassword",
            host="localhost",
            port="5432"
        )
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                subscription BOOLEAN DEFAULT FALSE,
                comments INTEGER DEFAULT 0,
                likes INTEGER DEFAULT 0,
                country TEXT,
                is_admin BOOLEAN DEFAULT FALSE
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS pages (
                id SERIAL PRIMARY KEY,
                tittle TEXT NOT NULL,
                content TEXT NOT NULL,
                likes INTEGER DEFAULT 0,
                comments INTEGER DEFAULT 0
            );
        """)
        self.connection.commit()

    def create_comment(self, page_id: int, username: str, comment: str):
        self.cursor.execute(
            "INSERT INTO comments (page_id, username, comment) VALUES (%s, %s, %s)",
            (page_id, username, comment)
        )
        self.connection.commit()

    def update_likes(self, page_id: int):
        self.cursor.execute("UPDATE pages SET likes = likes + 1 WHERE id = %s;", (page_id,))
        self.connection.commit()

    def create_user(self, username: str, email: str, password: str, country: str):
        try:
            self.cursor.execute(
                "INSERT INTO users (username, email, password, country) VALUES (%s, %s, %s, %s)",
                (username, email, password, country)
            )
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            print(f"Error: {e}")

    def get_user(self, email: str):
        self.cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return self.cursor.fetchone()

    def get_users(self):
        self.cursor.execute("SELECT username, email, country, password, likes, comments FROM users;")
        return self.cursor.fetchall()

    def get_pages(self):
        self.cursor.execute("SELECT id, tittle, content, likes, comments FROM pages;")
        return self.cursor.fetchall()

    def get_most_active(self):
        self.cursor.execute("""
            SELECT id, username, email, likes, comments
            FROM users
            ORDER BY (likes + comments) DESC
            LIMIT 1;
        """)
        return self.cursor.fetchone()

    def get_average_likes_and_comments(self):
        self.cursor.execute("SELECT AVG(likes) FROM users;")
        avg_likes = self.cursor.fetchone()[0]
        self.cursor.execute("SELECT AVG(comments) FROM users;")
        avg_comments = self.cursor.fetchone()[0]
        return avg_likes, avg_comments

    def get_most_popular_page(self):
        self.cursor.execute("""
            SELECT id, tittle, likes, comments
            FROM pages
            ORDER BY (likes + comments) DESC
            LIMIT 1;
        """)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.connection.close()

class UserManager(ABC):
    def delete_user(user_id)->None:
        pass

    def create_user(email: str,username: str,password: str,country: str)->None:
        pass

    def get_user(id: int)-> None:
        pass

    def update_user(email: str,username: str,password: str,country: str)->None:
        pass

class UserManagerImpl(UserManager):

    def __init__(self,db: Database):
        self.db = db


    def delete_user(user_id)->None:
        self.db.delete_user()

    def create_user(email: str,username: str,password: str,country: str)->None:
        self.db.create_user()

    def get_user(id: int)-> None:
        pass

    def update_user(email: str,username: str,password: str,country: str)->None:
        pass

class User(ABC):
    @abstractmethod
    def visit_page(self, page_id: int) -> None:
        pass

    @abstractmethod
    def like_page(self, page_id: int) -> None:
        pass

    @abstractmethod
    def comment_on_page(self, page_id: int, comment: str) -> None:
        pass

class Page(ABC):
    def __init__(self, page_id: int, content: str, likes: int = 0):
        self.page_id = page_id
        self.content = content
        self.likes = likes

class PageImpl(Page):
    def __init__(self,page_id,content,likes):
        super().__init__(page_id,content,likes)

class Report(ABC):
    def __init__(self, report_id: int, title: str, content: str, format: str, date: datetime):
        self.report_id = report_id
        self.title = title
        self.content = content
        self.format = format
        self.date = date

class ReportImpl(Report):
    def __init__(self, report_id: int, title: str, content: str, format: str, date: datetime):
        super().__init__(report_id, title, content, format, date)

class Admin(User):
    def __init__(self, user_id: int, username: str, email: str, country: str,user_manager: UserManagerImpl):
        self.is_admin = True
        self.user_id = user_id
        self.username = username
        self.email = email
        self.country = country
        self.user_manager = user_manager

    def generate_report(self, title: str, users: List[Dict[str, Union[str, int]]], pages: List[Dict[str, Union[str, int]]]) -> 'Report':
        active_user = max(users, key=lambda x: x['likes'] + x['comments'])
        avg_user_likes = sum(user['likes'] for user in users) / len(users)
        avg_user_comments = sum(user['comments'] for user in users) / len(users)

        active_page = max(pages, key=lambda x: x['likes'] + x['comments'])
        avg_page_likes = sum(page['likes'] for page in pages) / len(pages)
        avg_page_comments = sum(page['comments'] for page in pages) / len(pages)

class AdminPanel:
    def __init__(self, db: Database):
        self.db = db
        self.root = tk.Tk()
        self.root.title("Admin Panel")
        self.create_main_window()

    def create_main_window(self):
        tk.Label(self.root, text="Admin Panel", font=("Arial", 20)).pack(pady=20)
        tk.Button(self.root, text="Users", command=self.show_users_window).pack(pady=10)
        tk.Button(self.root, text="Pages", command=self.show_pages_window).pack(pady=10)

    def show_users_window(self):
        users_window = tk.Toplevel(self.root)
        users_window.title("Users")

        tk.Button(users_window, text="Back", command=users_window.destroy).pack(pady=5)
        tk.Button(users_window, text="Most Active User", command=self.show_most_active_user).pack(pady=5)
        tk.Button(users_window, text="Average Activity", command=self.show_average_activity).pack(pady=5)
        tk.Button(users_window, text="Plot User Activity", command=self.plot_user_activity).pack(pady=5)

        columns = ("name", "email", "country", "password", "likes", "comments")
        self.users_tree = ttk.Treeview(users_window, columns=columns, show='headings')
        for col in columns:
            self.users_tree.heading(col, text=col.capitalize())
            self.users_tree.column(col, width=100)

        self.users_tree.pack(pady=10)
        self.show_all_users()

    def show_all_users(self):
        self.users_tree.delete(*self.users_tree.get_children())
        users = self.db.get_users()
        for user in users:
            self.users_tree.insert("", tk.END, values=user)

    def show_all_pages(self):
        self.pages_tree.delete(*self.pages_tree.get_children())
        pages = self.db.get_pages()
        for page in pages:
            self.pages_tree.insert("", tk.END, values=page)

    def show_pages_window(self):
        pages_window = tk.Toplevel(self.root)
        pages_window.title("Pages")

        tk.Button(pages_window, text="Back", command=pages_window.destroy).pack(pady=5)
        tk.Button(pages_window, text="Most Popular Page", command=self.show_most_popular_page).pack(pady=5)
        tk.Button(pages_window, text="Plot Page Activity", command=self.plot_page_activity).pack(pady=5)

        columns = ("id", "title", "content", "likes", "comments")
        self.pages_tree = ttk.Treeview(pages_window, columns=columns, show='headings')
        for col in columns:
            self.pages_tree.heading(col, text=col.capitalize())
            self.pages_tree.column(col, width=100)

        self.pages_tree.pack(pady=10)
        self.show_all_pages()

    def show_most_active_user(self):
        most_active_user = self.db.get_most_active()
        report = f"User: {most_active_user[0]}, Likes: {most_active_user[1]}, Comments: {most_active_user[2]}"
        messagebox.showinfo("Most Active User", report)
        self.save_to_file("most_active_user.txt", report)

    def show_average_activity(self):
        avg_likes, avg_comments = self.db.get_average_likes_and_comments()
        report = f"Average Likes: {avg_likes}\nAverage Comments: {avg_comments}"
        messagebox.showinfo("Average Activity", report)
        self.save_to_file("average_activity.txt", report)

    def show_most_popular_page(self):
        most_popular_page = self.db.get_most_popular_page()
        report = f"Page: {most_popular_page[1]}, Likes: {most_popular_page[2]}, Comments: {most_popular_page[3]}"
        messagebox.showinfo("Most Popular Page", report)
        self.save_to_file("most_popular_page.txt", report)

    def plot_user_activity(self):
        users = self.db.get_users()
        names = [user[0] for user in users]
        likes = [user[4] for user in users]
        comments = [user[5] for user in users]

        x = range(len(names))
        plt.bar(x, likes, width=0.4, label='Likes', align='center')
        plt.bar(x, comments, width=0.4, label='Comments', align='edge')
        plt.xticks(x, names, rotation=45)
        plt.title('User Activity')
        plt.xlabel('Users')
        plt.ylabel('Count')
        plt.legend()
        plt.tight_layout()

        plt.savefig('user_activity.png')
        plt.close()
        messagebox.showinfo("Plot Saved", "User activity plot saved as user_activity.png")

    def plot_page_activity(self):
        pages = self.db.get_pages()
        titles = [page[1] for page in pages]
        likes = [page[3] for page in pages]
        comments = [page[4] for page in pages]

        x = range(len(titles))
        plt.bar(x, likes, width=0.4, label='Likes', align='center')
        plt.bar(x, comments, width=0.4, label='Comments', align='edge')
        plt.xticks(x, titles, rotation=45)
        plt.title('Page Activity')
        plt.xlabel('Pages')
        plt.ylabel('Count')
        plt.legend()
        plt.tight_layout()

        plt.savefig('page_activity.png')
        plt.close()
        messagebox.showinfo("Plot Saved", "Page activity plot saved as page_activity.png")

    def save_to_file(self, filename, content):
        with open(filename, 'w') as file:
            file.write(content)


    def run(self):
        self.root.mainloop()

if __name__ == "__main__": 
    db = Database()
    admin_panel = AdminPanel(db)  
    admin_panel.run()
    db.close()