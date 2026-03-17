from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
import allure
from elements.button import Button
from elements.text import Text


class CreateCourseExercisesToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-exercises-box-toolbar-title-text', 'Title')
        self.create_button = Button(
            page, 'create-course-exercises-box-toolbar-create-exercise-button', 'Create Exercises'
        )

    @allure.step('Check visible exercise toolbar view and create button')
    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Exercises')

        self.create_button.check_visible()

    @allure.step('Open exercise form')
    def click_create_exercise_button(self):
        self.create_button.click()