from components.base_component import BaseComponent
from playwright.sync_api import Page, expect


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('dashboard-toolbar-title-text')

    def check_visible(self, text_title: str):
        expect(self.title).to_have_text(text_title)