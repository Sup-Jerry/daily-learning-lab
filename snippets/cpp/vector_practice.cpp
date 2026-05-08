#include <iostream>
#include <string>
#include <vector>

int main() {
    std::vector<std::string> tasks = {"read notes", "write code", "review output"};

    std::cout << "Study tasks:" << std::endl;
    for (std::size_t index = 0; index < tasks.size(); ++index) {
        std::cout << index + 1 << ". " << tasks[index] << std::endl;
    }

    tasks.push_back("update log");

    std::cout << "\nAfter adding a task:" << std::endl;
    for (const std::string& task : tasks) {
        std::cout << "- " << task << std::endl;
    }

    std::cout << "Total tasks: " << tasks.size() << std::endl;
    return 0;
}
