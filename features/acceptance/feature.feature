Feature: Creating and working with Features

  Scenario: Create a Feature
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to create_ticket
    And I enter "test" into the title field of the ticket_create form
    And I enter "some words describing the feature" into the description field of the ticket_create form
    And I choose "feature" from the choices in the type field of the ticket_create form
    And I submit the ticket_create form
    Then I should be told "Ticket successfully created!"


  Scenario: Editing a Feature
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to show_feature with id 1
    And I enter "test" into the title field of the feature_edit form
    And I enter "some words describing the feature" into the description field of the feature_edit form
    And I select "todo" from the choices in the status field of the feature_edit form
    And I submit the feature_edit form
    Then I should be told "The feature has been updated"

  Scenario: Voting on a Feature with votes
    Given I am a user with email of user@example.com
    And I am logged in
    And I have some votes
    When I navigate to show_feature with id 1
    And I click on the upvote button
    Then I should be told "Thank you for your vote"

  Scenario: Voting on a Feature without votes
    Given I am a user with email of user@example.com
    And I am logged in
    When I navigate to show_feature with id 1
    And I click on the upvote button
    Then I should be told "You must buy votes"

