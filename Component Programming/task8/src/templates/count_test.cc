#include <gtest/gtest.h>
#include <vector>
#include <list>
#include "my_count.cc"

TEST(count, vector) {
    std::vector<int> v(8);

    EXPECT_EQ(8, my_count(v.begin(), v.end()));
}

TEST(count, list) {
    std::list<int> l(6);

    EXPECT_EQ(6, my_count(l.begin(), l.end()));
}
