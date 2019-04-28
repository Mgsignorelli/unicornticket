Feature: Registering a user

  Scenario Outline: Registering as a new user
    Given I am a user with email of registration-user@example.com
    When I navigate to registration
    And I enter my email correctly
    And I enter "<username>" into the username field
    And I enter my password correctly into the password1 field
    And I enter my password <password_validity> into the password2 field
    And I submit the registration form
    Then I should be told "<registration_message>"

    Examples:  Password
      | username          | password_validity | registration_message                 |
      | test_user         | incorrectly       | Passwords must match                 |
      | test user         | correctly         | Enter a valid username.              |
      | test_user         | correctly         | Successfully registered a new user!  |