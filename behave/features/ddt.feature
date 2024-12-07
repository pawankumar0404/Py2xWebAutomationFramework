Feature: showing off behave with Scenario Outline
  Scenario Outline: Run a simple test with argument
    Given we have behave installed
    When we say <greeting>
    Then behave should respond with <response>
    Examples:
      |greeting |response       |
      |Hello    |Hi there!      |
      |Goodbye  |see you later! |
      |thanks   |you're welcome!|
