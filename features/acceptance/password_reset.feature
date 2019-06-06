Feature: Password reset

  Scenario Outline: Triggering a Password Reset
    Given I am a user with email of <email>
    When I navigate to password_reset
    And I enter my email <validity> in the password_reset form
    And I submit the password_reset form
    Then I <told> told "You will receive an email if you are a registered user"
    And <received>

    Examples: Password Reset
      | email              | validity    | told          | received                                                                   |
      | user@example.com   | correctly   | should be     | I should have received an email with a subject containing "Password reset" |
      | user@example.com   | incorrectly | should not be | I should not have received an email                                        |
      | user@doesnot.exist | correctly   | should be     | I should not have received an email                                        |
      | user@doesnot.exist | incorrectly | should not be | I should not have received an email                                        |
