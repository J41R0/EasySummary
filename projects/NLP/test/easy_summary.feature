Feature: Easy Summary functionality

Scenario: Summary
    Given I have enterd the number of expected ideas 1
    Given I also input a list of opinions {"opinions":[{"id": 1,"text": "The cats are really cute animals"},{"id": 2,"text": "The cutest pets are cats. They are my favorite animal."},{"id": 3,"text": "I am a dog lover and hate cats. I will never have a cat as a pet."}]} to summarizer
    When I call the function get_summary
    Then I get result The cats are really cute animals.

