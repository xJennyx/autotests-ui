from components.base_component import BaseComponent
from playwright.sync_api import Page
from elements.text import Text
from elements.image import Image
import allure


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page,'{identifier}-widget-title-text','Title')
        self.chart = Image(page,'{identifier}-{chart_type}-chart', 'Chart')

    @allure.step('Check visible chart view')
    def check_visible(self, title: str, identifier: str, chart_type: str):
        self.title.check_visible(identifier=identifier)
        self.title.check_have_text(title, identifier=identifier)

        self.chart.check_visible(identifier=identifier, chart_type=chart_type)