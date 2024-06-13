Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Car into search field
    And Click on search icon
    Then Product results for Car are shown


  @smoke
  Scenario: User can filter by sale status Out of Stocks
    Given Open the main (log in) page
    When Log in to the page
    When Click on “off plan” at the left side menu
    Then Verify the right page opens
    When Filter by sale status of “Out of Stocks”
    Then Verify each product contains the Out of Stocks tag


  Scenario: User can open map page(mobile simulation)
    Given Open the main (log in) page
    When Log in to the page
    When Go to Map page
    Then Verify Map page is opened