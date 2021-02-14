#include <gtest/gtest.h>
#include "pc.cc"
#include <cstdio>
#include <iostream>
#include <memory>
#include <string>
#include <array>

std::string exec(const char* cmd) {
    std::array<char, 128> buffer;
    std::string res;
    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd, "r"), pclose);
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        res += buffer.data();
    }
    return res;
}

TEST(pc, pc_test) {
    auto res = num_spc_members();
    auto ans = std::stoi(exec("ggg members spc | wc -l"));
    EXPECT_EQ(res, ans);
}
