Feature: Creating a ticket as a bug

  Scenario: Create a Bug
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to create_ticket
    And I enter "test" into the title field of the ticket_create form
    And I enter "some words describing the bug" into the description field of the ticket_create form
    And I choose "bug" from the choices in the type field of the ticket_create form
    And I submit the ticket_create form
    Then I should be told "Ticket successfully created!"

  Scenario: Create a Feature
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to create_ticket
    And I enter "test" into the title field of the ticket_create form
    And I enter "some words describing the feature" into the description field of the ticket_create form
    And I choose "feature" from the choices in the type field of the ticket_create form
    And I submit the ticket_create form
    Then I should be told "Ticket successfully created!"
