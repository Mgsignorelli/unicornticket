Feature: Password reset

  Scenario Outline: With a User that exists
    Given I am a user with email of user@example.com
    When I navigate to password_reset
    And I enter my email <email_validity>
    And I submit the password_reset form
    Then I should be told "<passwordreset_message>"

    Examples:  Password
      | email_validity | passwordreset_message              |
      | incorrectly    | No registered user with that email |
      | correctly      | Check your email for a reset link  |


  Scenario Outline: With a User that does not exist
    Given I am a user with email of user@doesnot.exist
    When I navigate to password_reset
    And I enter my email <email_validity>
    And I submit the password_reset form
    Then I should be told "<passwordreset_message>"

    Examples:  Password
      | email_validity | passwordreset_message              |
      | incorrectly    | No registered user with that email |
      | correctly      | No registered user with that email |
