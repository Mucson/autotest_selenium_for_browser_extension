#Feature: Authorization into the system
#
#  Scenario: Import account
#    Given I click Get Started button
#    When I click Import account button
#    When I type credentials
#    When I click Import account
#    Then I verify I am on the dhub page

Feature: Smoke tests
  Background:
    Given I imported my account

  Scenario: Publish and delete post
    When I click New Post button
    Then I see element with text "Post has been created successfully"
    When I delete published post
    Then I see element with text "Post has been removed successfully"

  Scenario: Fill in the user info
    Given I open menu
    When I open account details page
    When I fill in the account details page
    When I fill in the first name field
    When I fill in the last name field
    When I select gender
    When I fill in the bio field
    When I fill in the nickname field
    When I fill in the password field
    When I fill in the confirm password field
    When I click Save button
    Then I see element with text "User was successfully updated"

  Scenario: Lock, unlock, restore account
    Given I open menu
    When I click lock account
    When I click restore account
    When I click back
    When I fill in the password
    When I click unlock
    Then I verify I am on the dhub page
    When I open menu
    When I click lock account
    When I click restore account
    Then I assert I am on the correct page
    When I type credentials
    When I click restore button
    Then I verify I am on the dhub page