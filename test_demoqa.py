import os
from selene import browser, be, have

First_name = 'Petr'
Last_name = 'Petrov'
Email = 'test123@mail.ru'
Phone = '8929111111'
Current_address = 'Sweet home'


def test_successful_student_registration_form(open_browser):
    browser.open('/automation-practice-form')
    browser.element('[id="firstName"]').should(be.blank).type(First_name)
    browser.element('[id="lastName"]').should(be.blank).type(Last_name)
    browser.element('[id="userEmail"]').should(be.blank).type(Email)
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').should(be.blank).type(Phone)
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]>option[value="1"]').click()
    browser.element('[class="react-datepicker__year-select"]>option[value="1999"]').click()
    browser.element('.react-datepicker__day--001').click()
    browser.element('[id="subjectsInput"]').click().type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[id="uploadPicture"]').send_keys(os.path.abspath('../python_qa_guru_7_5/data/student.jpg'))
    browser.element('[id="currentAddress"]').type(Current_address)
    browser.element('[id="react-select-4-input"]').should(be.not_.enabled)
    browser.element('[id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').should(be.enabled).type('Delhi').press_enter()
    browser.element('[id="submit"]').press_enter()
    #     Проверка итоговой таблицы
    browser.element('.modal-header>.modal-title').should(
        have.text('Thanks for submitting the form')
    )

    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Petr Petrov',
            'test123@mail.ru',
            'Male',
            '8929111111',
            '01 February,1999',
            'Maths',
            'Reading, Music',
            'student.jpg',
            'Sweet home',
            'NCR Delhi',
        )
    )

