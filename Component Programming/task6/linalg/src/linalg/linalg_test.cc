#include <gtest/gtest.h>
#include <linalg/linalg.hh>

TEST(unary, minus) {
    Vector<int> a {1, -1};
    Vector<int> b {-1, 1};
    EXPECT_EQ(-a, b);
}

TEST(binary, less) {
    Vector<int> a {1, 2, 3};
    Vector<int> b {1, 3, 4};
    Vector<bool> c {false, true, true};
    EXPECT_EQ(a < b, c);
}

TEST(binary, multiply) {
    Vector<int> a {1, -1, 1};
    Vector<int> b {1, 2, 3};
    Vector<int> c {1, -2, 3};
    EXPECT_EQ(a * b, c);
}

TEST(ternary, _) {
    Vector<bool> a {true, false, true};
    Vector<int> b {0, 0, 0};
    Vector<int> c {1, 1, 1};
    Vector<int> expected {0, 1, 0};
    EXPECT_EQ(where(a, b, c), expected);
}
