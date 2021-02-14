#include <gtest/gtest.h>
#include <unordered_set>
#include "account.cc"


bool is_bash(Account a) {
    return a.shell == "bash";
}

TEST(users, using_bash) {
    std::vector<Account> data {
        Account(1, "Linus", "Torvalds", "bash"),
        Account(2, "Donald", "Knuth", "pdksh"),
        Account(3, "Bjarne", "Stroustrup", "sh"),
        Account(4, "Mark", "Zuckerberg", "bash")
    };

    std::vector<Account> ans {
        Account(1, "Linus", "Torvalds", "bash"),
        Account(4, "Mark", "Zuckerberg", "bash")
    };

    std::vector<Account> res;

    for (auto it=std::find_if(data.begin(), data.end(), is_bash); it!=data.end(); it=std::find_if(it + 1, data.end(), is_bash))
        res.push_back(*it);

    EXPECT_EQ(res, ans);
}


TEST(users, id_sort) {
    std::vector<Account> data {
        Account(1021, "Linus", "Torvalds", "bash"),
        Account(754, "Donald", "Knuth", "pdksh"),
        Account(0, "Bjarne", "Stroustrup", "sh"),
        Account(2451, "Mark", "Zuckerberg", "bash")
    };

    std::vector<Account> ans {
	Account(0, "Bjarne", "Stroustrup", "sh"),
        Account(754, "Donald", "Knuth", "pdksh")
    };

    std::vector<Account> res;

    std::map<unsigned int, Account> map;
    for (const auto& a: data)
        map.insert({a.id, a});
    auto lower = map.lower_bound(0);
    auto upper = map.lower_bound(1000);
    for (auto it=lower; it!=upper; ++it)
	res.push_back(it -> second);

    EXPECT_EQ(res, ans);
}

TEST(users, using_shell) {
    std::vector<Account> data {
        Account(1, "Linus", "Torvalds", "bash"),
        Account(4, "Donald", "Knuth", "pdksh"),
        Account(2, "Bjarne", "Stroustrup", "sh"),
        Account(3, "Mark", "Zuckerberg", "bash")
    };

    std::unordered_map<std::string, int> res;

    for (const auto& a: data)
	++res[a.shell];

    EXPECT_EQ(res["bash"], 2);
    EXPECT_EQ(res["sh"], 1);
    EXPECT_EQ(res["pdksh"], 1);
}

TEST(users, id_duplicates) {
    std::vector<Account> data {
        Account(1, "Linus", "Torvalds", "bash"),
        Account(3, "Donald", "Knuth", "pdksh"),
        Account(2, "Bjarne", "Stroustrup", "sh"),
        Account(3, "Mark", "Zuckerberg", "bash")
    };

    std::vector<Account> ans {
        Account(3, "Donald", "Knuth", "pdksh"),
        Account(3, "Mark", "Zuckerberg", "bash")
    };

    std::vector<Account> res;

    std::unordered_set<unsigned int> unique;
    std::unordered_set<unsigned int> duplicates;
    for (const auto& a: data) {
        bool t = unique.insert(a.id).second;
        if (!t)
	    duplicates.insert(a.id);
    }

    for (const auto& a: data)
        if (duplicates.contains(a.id))
            res.push_back(a);

    EXPECT_EQ(res, ans);
}
