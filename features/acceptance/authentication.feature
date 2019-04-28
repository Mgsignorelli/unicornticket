Feature: Authenticating a user

  Scenario Outline: Authenticating an existing user with the wrong password
    Given I am a user with email of user@example.com
    When I navigate to login
    And I enter my username correctly
    And I enter my password <password_validity>
    And I submit the login form
    Then I should be told "<login_message>"

    Examples:  Password
      | password_validity | login_message                           |
      | correctly         | Welcome!                                |
      | incorrectly       | Your username or password is incorrect  |