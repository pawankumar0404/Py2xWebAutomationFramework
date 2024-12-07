Feature: Google search for the The Testing Academy
  Scenario: Search for the TTA on Google
    Given I am on the Google Home Page
    When I search for "TheTestingAcademy"
    Then I should see the "TheTestingAcademy" in the result
