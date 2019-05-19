Feature: Creating a ticket as a bug

  Scenario: Create a Bug
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to create_ticket
    And I enter "test" into the title field
    And I enter "description" into the description field
    And I choose "bug" from the choices in the type field
    And I submit the TicketForm form
    Then I should be told "Ticket successfully created!"

  Scenario: Create a Feature
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to create_ticket
    And I enter "test" into the title field
    And I enter "description" into the description field
    And I choose "feature" from the choices in the type field
    And I submit the TicketForm form
    Then I should be told "Ticket successfully created!"
