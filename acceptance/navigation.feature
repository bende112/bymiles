Feature: Test for a quick quote

  Scenario: a user navigate to the homepage
    Given a user is on the  homepage
    When the user click on the "GET A QUOTE"
    Then the "Get a quote, quickly" is displayed


