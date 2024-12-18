import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from database import Database


class AdminPanelView:
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

        columns = ("username", "email", "country", "likes", "comments")
        self.users_tree = ttk.Treeview(users_window, columns=columns, show='headings')
        for col in columns:
            self.users_tree.heading(col, text=col.capitalize())
            self.users_tree.column(col, width=100)

        self.users_tree.pack(pady=10)
        self.show_all_users()

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
        report = f"User: {most_active_user[0]}, Likes: {most_active_user[3]}, Comments: {most_active_user[4]}"
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