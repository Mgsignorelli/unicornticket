Feature: Buy votes for features

  Scenario: Voting for a feature without votes
    Given I am a user with email of user@example.com
    And I am logged in
    And I have no votes
    When I navigate to show_feature with id 1
    Then I should be told "Oh no! buy feature votes to vote on a feature"


  Scenario: Voting for a feature with votes
    Given I am a user with email of user@example.com
    And I am logged in
    And I have some votes
    When I navigate to show_feature with id 1
    And I click on the upvote button
    Then I should be told "Thank you for your vote"