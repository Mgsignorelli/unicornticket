Feature: Password reset

  Scenario: With a User that exists
    Given I am a user with email of user@example.com
    When I navigate to password_reset
    And I enter my email incorrectly
    And I submit the password_reset form
    Then I should not be told "You will receive an email if you a registered user"

  Scenario: With a User that exists
    Given I am a user with email of user@example.com
    When I navigate to password_reset
    And I enter my email correctly
    And I submit the password_reset form
    Then I should be told "You will receive an email if you a registered user"

  Scenario: With a User that does not exist
    Given I am a user with email of user@doesnot.exist
    When I navigate to password_reset
    And I enter my email incorrectly
    And I submit the password_reset form
    Then I should not be told "You will receive an email if you a registered user"

  Scenario: With a User that does not exist
    Given I am a user with email of user@doesnot.exist
    When I navigate to password_reset
    And I enter my email correctly
    And I submit the password_reset form
    Then I should be told "You will receive an email if you a registered user"
