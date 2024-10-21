#include <iostream>
#include <string>
#include <vector>
#include <cstdlib> // For system()
#include <iomanip>

struct Question {
    std::string questionText;
    std::vector<std::string> choices;
    std::string correctAnswer; // Correct answer as a string
};

void displayQuestions(const std::vector<Question>& questions) {
    for (size_t i = 0; i < questions.size(); ++i) {
        const Question& q = questions[i];
        std::cout << "Question " << (i + 1) << ": " << q.questionText << std::endl;

        for (size_t j = 0; j < q.choices.size(); ++j) {
            std::cout << "  " << (j + 1) << ": " << q.choices[j] << std::endl;
        }

        std::cout << "Please enter the number of your choice: ";
        
        int answer;
        std::cin >> answer;

        // Simple input validation
        if (answer < 1 || answer > q.choices.size()) {
            std::cout << "Invalid choice. Please try again." << std::endl;
            --i; // Repeat the question
        } else {
            // Get the selected choice
            std::string selectedChoice = q.choices[answer - 1];

            // Check if the answer is correct
            if (selectedChoice == q.correctAnswer) {
                std::cout << "Correct! You chose: " << selectedChoice << std::endl;
            } else {
                std::cout << "Incorrect. The correct answer was: " << q.correctAnswer << std::endl;
            }
        }
        std::cout << std::endl; // Add space between questions
    }
}

int main() {
    // Define questions, choices, and correct answers
    std::vector<Question> questions = {
        {"did you decode this?", {"Yes", "No", "Maybe", "I dont know"}, "Yes"},
        {"what is this coded in? (a type of C)", {"C++", "C#", "C", "C+"}, "C++"},
        {"Which programming language decoded the exe??", {"C++", "Python", "Java", "JavaScript"}, "Python"}
    };

    std::cout << "Welcome to the Surprise Quiz!" << std::endl;
    std::cout << "Answer the following questions:" << std::endl;
    std::cout << std::endl;

    displayQuestions(questions);

    std::cout << "Thank you for participating!" << std::endl;
    std::cout << "If you enjoyed this, stay tuned for more surprises!" << std::endl;

    // Open a link in the default web browser
    std::string url = "https://www.roblox.com/games/125152702139847/TESTING-VERY-BUGGY-the-Doors-Engine-recreation"; // Change to your desired URL
    std::cout << "Heres your surprise!: " << std::endl;
    std::string command = "start " + url; // For Windows
    // std::string command = "xdg-open " + url; // For Linux
    // std::string command = "open " + url; // For macOS
    system(command.c_str());

    return 0;
}
