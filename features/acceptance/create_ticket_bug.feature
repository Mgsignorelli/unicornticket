Feature: Creating a ticket as a bug

  Scenario: Create a ticket
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to create_ticket
    And I enter "test" into the title field
    And I enter "description" into the description field
    And I submit the TicketForm form
    Then I should be told "Ticket successfully created!"
