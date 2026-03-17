from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import allure
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.button = Button(page, 'create-course-toolbar-create-course-button', 'Create Course')

    @allure.step('Check visible create course toolbar view')
    def check_visible(self, is_create_course_disabled = True):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        if is_create_course_disabled:
            self.button.check_disabled()
        else:
            self.button.check_enabled()

    @allure.step('Click create course button')
    def click_create_course_button(self):
        self.button.click()