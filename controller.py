from datetime import datetime
from typing import List, Dict


class UserController:
    def __init__(self, user_manager: UserManagerImpl):
        self.user_manager = user_manager

    def create_user(self, email: str, username: str, password: str) -> User:
        return self.user_manager.create_user(email, username, password)

    def delete_user(self, user_id: int) -> None:
        self.user_manager.delete_user(user_id)

    def update_user(self, user_id: int, new_data: str) -> User:
        return self.user_manager.update_user(user_id, new_data)

    def get_user(self, email: str) -> User:
        return self.user_manager.get_user(email)

class PageController:
    def __init__(self, page_manager: PageManager):
        self.page_manager = page_manager

    def add_page(self, title: str) -> Page:
        return self.page_manager.add_page(title)

    def get_page(self, page_id: int) -> Page:
        return self.page_manager.get_page(page_id)

class ReportController:
    def __init__(self, report_manager: ReportManager):
        self.report_manager = report_manager

    def create_report(self, title: str, format: str) -> Report:
        return self.report_manager.create_report(title, format)

    def generate_report(self, report_id: int) -> None:

        pass

class AdminPanelController:
    def __init__(self, admin_panel: AdminPanel):
        self.admin_panel = admin_panel

    def manage_user(self, action: str, user_email: str) -> User:
        admin_panel.manage_user()
        

    def make_report(self, title: str, format: str) -> Report:
        return self.admin_panel.generate_report(title,content, format)

