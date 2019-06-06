Feature: Creating and working with Bugs

  Scenario: Create a Bug
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to create_ticket
    And I enter "test" into the title field of the ticket_create form
    And I enter "some words describing the bug" into the description field of the ticket_create form
    And I choose "bug" from the choices in the type field of the ticket_create form
    And I submit the ticket_create form
    Then I should be told "Ticket successfully created!"


  Scenario: Editing a Bug
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to show_bug with id 1
    And I enter "test" into the title field of the bug_edit form
    And I enter "some words describing the bug" into the description field of the bug_edit form
    And I select "todo" from the choices in the status field of the bug_edit form
    And I submit the bug_edit form
    Then I should be told "The bug has been updated"
