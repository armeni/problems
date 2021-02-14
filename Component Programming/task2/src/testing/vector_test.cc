#include "gtest/gtest.h"
#include <vector>
#include <algorithm>
#include <fstream>
#include <type_traits>

using namespace std;

TEST(vector, push_back) {
	vector<int> v;
	EXPECT_EQ(v.size(), 0);

	int push_back_element = 1;
	v.push_back(push_back_element);
	EXPECT_EQ(v[v.size() - 1], push_back_element);
}

TEST(vector, pop_back) {
	vector<int> v = {1, 2, 3};
	EXPECT_EQ(v[v.size() - 1], 3);

	v.pop_back();
	EXPECT_EQ(v[v.size() - 1], 2);
}

TEST(vector, erase) {
	vector<int> v = {1, 2, 3};
	EXPECT_EQ(v.size(), 3);

	v.erase(begin(v), begin(v) + 2);
	EXPECT_EQ(v.size(), 1);
}

TEST(vector, begin_and_end) {
	vector<int> v = {1, 2, 3};
	vector<int> u;
	for(auto i = begin(v); i != end(v); ++i){
		u.push_back(*i);
	}

	EXPECT_EQ(v, u);
}

TEST(vector, size) {
	vector<int> v;
	EXPECT_EQ(v.size(), 0);

	v.push_back(1);
	EXPECT_EQ(v.size(), 1);
}

TEST(vector, constructor1) {
	const vector<int>& v = {1, 2, 3};
	vector<int> new_v(v);

	EXPECT_EQ(new_v, v);
}

TEST(vector, constructor2) {
	vector<int>&& v = {1, 2, 3};
	vector<int> new_v = move(v);

	EXPECT_EQ(new_v.size(), 3);
	EXPECT_EQ(v.size(), 0);
}

TEST(vector, operator1) {
	vector<int> v = {1, 2, 3};
	vector<int> new_v = v;

	EXPECT_EQ(new_v, v);
}

TEST(vector, operator2) {
	vector<int> v = {1, 2, 3};
	vector<int> new_v;
	new_v = move(v);

	EXPECT_EQ(new_v.size(), 3);
	EXPECT_EQ(v.size(), 0);
}


template <class T>
struct Erase_params {
	vector<T> elements;
	size_t start_index;
	size_t end_index;
	vector<T> result;
};

class erase_test: public ::testing::TestWithParam<Erase_params<int>>{};

TEST_P(erase_test, _) {
	const Erase_params<int>& param = GetParam();
	vector<int> erased = param.elements;
	vector<int> res = param.result;
	erased.erase(begin(erased) + param.start_index, begin(erased) + param.end_index);

	EXPECT_EQ(erased, res);
}

INSTANTIATE_TEST_CASE_P(_, erase_test, ::testing::Values(
			Erase_params<int>{{1, 2, 3}, 1, 2, {1, 3}},
			Erase_params<int>{{1, 2, 3}, 0, 3, {}}
			));

template <class T>
struct push_back_test: public ::testing::Test {};

typedef ::testing::Types<float, string, ofstream> Types;

TYPED_TEST_CASE(push_back_test, Types);

TYPED_TEST(push_back_test, push_back) {
	TypeParam obj = {};
	vector<TypeParam> objects;
	if constexpr((is_same<float, TypeParam>::value) || (is_same<string, TypeParam>::value)){
		EXPECT_EQ(objects.size(), 0);
		objects.push_back(obj);
		EXPECT_EQ(objects[objects.size() - 1], obj);
	} else {
		bool start = obj.is_open();
		EXPECT_EQ(objects.size(), 0);
		objects.push_back(move(obj));

		if (objects[0].is_open() == start){
			start = true;
		} else {start = false;}
		EXPECT_TRUE(start);
	}
}
