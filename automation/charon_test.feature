Feature: Charon smoke and regression tests

  Scenario: Import account
    Given I click Get Started button
    When I click Import account button
    When I type credentials
    When I click Import account
    When I choose cookie and click confirm
    When I click all done button
    Then I verify I am on the dhub page

  Scenario: Publish and delete post
    When I click New Post button
    Then I see element with text "Post has been created successfully"
    When I delete published post
    Then I see element with text "Post has been removed successfully"

  Scenario: Edit profile info
    Given I open menu
    When I open user page
    When I open user profile page
    When I fill in the first name field
    When I fill in the last name field
    When I select gender
    When I fill in the bio field
    When I fill in the password field
    When I fill in the confirm password field
    When I click Save button
    Then I see element with text "User was successfully updated"

  Scenario: Lock, unlock, restore account
    Given I open small menu
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

  Scenario: Send token
    Given I open dPortal page
    When I open Assets tab
    When I click Send button
    When I input amount
    When I input wallet address
    When I click Send button
    Then I see element with text "Successfully sent"

  Scenario: Validation sending form
    Given I open dPortal page
    When I open Assets tab
    When I click Send button
    Then I see validation message for amount field
      | amount     | text                      |
      | 0          | Minimum value is 0.000001 |
      | 0.0000001  | Minimum value is 0.000001 |
      | 0.01233212 | Incorrect amount format   |

    Then I see validation message for wallet address field
      | wallet_address                                 | text                                |
      | decentr1mg58f6pgknl3cev273vh78f3sy7eamx7pwl    | Enter valid wallet address          |
      | decentr1mg58f6pgknl3cev273vh78f3sy7eamx7pwlxvz | You cannot send to your own account |
