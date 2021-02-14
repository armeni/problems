#include <gtest/gtest.h>
#include <variadic/variadic.hh>
#include <iostream>
#include <sstream>

TEST(message, first_test) {
	char ans[] = "a + 2 = 3";
    	std::stringstream ss;
    	message(ss, "% + % = %\n", 'a', 2, 3.0);
    	EXPECT_EQ(ss.str(), ans);
}


TEST(message, second_test) {
    	char ans[] = "a + 2 = 3";
    	std::stringstream ss;
	message(ss, "% + % = %%%\n", 'a', 2, 3.0);
    	EXPECT_EQ(ss.str(), ans);
}

TEST(cat, cat_test) {
    	std::array<float, 3> vec1{1.0f, 2.0f, 3.0f};
    	std::array<float, 3> vec2{4.0f, 5.0f, 6.0f};

    	std::array<float, 6> ans{1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f};
    	std::array<float, 6> res = cat(vec1, vec2);
    	EXPECT_EQ(res, ans);
}

TEST(tie, tie_test) {
    	std::array<float, 6> r{1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f};
    	std::array<float, 3> vec1, vec2;

	std::array<float, 3> v1{1.0f, 2.0f, 3.0f}, v2{4.0f, 5.0f, 6.0f};
    	tie(vec1, vec2) = r;
    	EXPECT_EQ(vec1, v1);
    	EXPECT_EQ(vec2, v2);
}
