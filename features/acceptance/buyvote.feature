Feature: Buy votes for features

  Scenario: Voting for a feature without votes // Buying a vote
    Given I am a user with email of user@example.com
    And I am logged in
    And I have not bought votes
    When I navigate to show_feature with id 1
    And I click on the upvote button
    Then I should get a dialogue saying I do not have votes and a link redirected to the shop page


  Scenario: Voting for a feature with votes // Buying a vote
    Given I am a user with email of user@example.com
    And I am logged in
    And I have bought votes
    When I navigate to show_feature with id 1
    And I click on the upvote button
    Then I should be told "You must buy votes"