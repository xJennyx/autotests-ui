from components.base_component import BaseComponent
from playwright.sync_api import Page
import re
from components.navigation.sidebar_list_item_component import SidebarListItemComponent


class SidebarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logout_list_item = SidebarListItemComponent(page)
        self.courses_list_item = SidebarListItemComponent(page)
        self.dashboard_list_item = SidebarListItemComponent(page)

    def check_visible(self):
        self.logout_list_item.check_visible('Logout', 'logout')
        self.courses_list_item.check_visible('Courses', 'courses')
        self.dashboard_list_item.check_visible('Dashboard', 'dashboard')

    def click_logout(self, identifier: str):
        self.logout_list_item.navigate(re.compile(r".*/#/auth/login"), identifier=identifier)

    def click_courses(self, identifier: str):
        self.courses_list_item.navigate(re.compile(r".*/#/courses"), identifier=identifier)

    def click_dashboard(self, identifier: str):
        self.dashboard_list_item.navigate(re.compile(r".*/#/dashboard"), identifier=identifier)