#include <vector>
#include <string>

using namespace std;

struct Account {
    unsigned int id;
    string login;
    string name;
    string shell;
    string home_directory;

    Account(unsigned int id, string login, string name, string shell):
        id(id),
        login(login),
        name(name),
        shell(shell),
        home_directory("/home/" + login + "/")
    {}

    bool operator<(const Account &other) const {
        return id < other.id;
    }

    bool operator==(const Account&) const = default;
};
