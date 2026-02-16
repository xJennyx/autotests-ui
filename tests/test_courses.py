from playwright.sync_api import expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page):

    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.navbar.check_visible('username')
    courses_list_page.sidebar.check_visible()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page, create_course_page):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.create_course_toolbar.check_visible(is_create_course_disabled=True)
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False, identifier='create-course-preview')
    create_course_page.create_exercise_course_toolbar.check_visible()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.image_upload_widget.upload_preview_image(
        '/Users/a1111/PycharmProjects/PythonProject/autotests-ui/testdata/files/images.jpeg',
        identifier='create-course-preview'
    )
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True, identifier='create-course-preview')
    create_course_page.create_course_form.fill(title='Playwright',
                                               estimated_time='2 weeks',
                                               description='Playwright',
                                               max_score='100',
                                               min_score='10')
    create_course_page.create_course_form.check_visible(title='Playwright',
                                               estimated_time='2 weeks',
                                               description='Playwright',
                                               max_score='100',
                                               min_score='10')
    create_course_page.create_course_toolbar.click_create_course_button()
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0, title='Playwright', max_score='100', min_score='10', estimated_time='2 weeks'
    )