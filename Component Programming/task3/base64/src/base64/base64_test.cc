#include <gtest/gtest.h>
#include <base64/base64.hh>
#include <string>
#include <algorithm>
#include <limits>
#include <stdexcept>

TEST(base64, rem0) {
	std::string word = "foobar";
	std::string code = "Zm9vYmFy";

	std::string encoded;
	encoded.resize(base64_encoded_size(word.size()));
	base64_encode(word.data(), word.size(), &encoded[0]);
	EXPECT_EQ(encoded, code);

	std::string decoded;
	decoded.resize(base64_max_decoded_size(code.size()));
        base64_decode(code.data(), code.size(), &decoded[0]);
	EXPECT_EQ(decoded, word);
}

TEST(base64, rem1) {
	std::string word = "foob";
	std::string code = "Zm9vYg==";

	std::string encoded;
	encoded.resize(base64_encoded_size(word.size()));
	base64_encode(word.data(), word.size(), &encoded[0]);
	EXPECT_EQ(encoded, code);

	std::string decoded;
	decoded.resize(base64_max_decoded_size(code.size()));
	base64_decode(code.data(), code.size(), &decoded[0]);
	decoded.resize(decoded.size() - 2);
	EXPECT_EQ(decoded, word);
}

TEST(base64, rem2) {
	std::string word = "fooba";
	std::string code = "Zm9vYmE=";

	std::string encoded;
	encoded.resize(base64_encoded_size(word.size()));
	base64_encode(word.data(), word.size(), &encoded[0]);
	EXPECT_EQ(encoded, code);

	std::string decoded;
	decoded.resize(base64_max_decoded_size(code.size()));
	base64_decode(code.data(), code.size(), &decoded[0]);
	decoded.resize(decoded.size() - 1);
	EXPECT_EQ(decoded, word);
}

TEST(base64, decode_if){
	std::string word{"foob" + std::string{char(0)} + std::string{"5"}};
	std::string code = "Zm9vYg=1";

	std::string decoded;
	decoded.resize(base64_max_decoded_size(code.size()));
	base64_decode(code.data(), code.size(), &decoded[0]);
	EXPECT_EQ(decoded, word);
}

TEST(base64, decode_len0) {
	std::string code = "", word;
	auto decoded = base64_decode(code.data(), code.size(), &word[0]);
	EXPECT_EQ(decoded, 0);
}

TEST(base64, length_error) {
	try {
		auto size = base64_encoded_size(std::numeric_limits<size_t>::max() / 4u * 3u);
		FAIL() << "no length error";
	} catch(std::length_error const &err){
		EXPECT_EQ(err.what(), std::string("base64 length is too large"));
	}
}

struct decode_param{
	std::string encoded;
	std::string error;
};

class decode_test: public ::testing::TestWithParam<decode_param>{};

TEST_P(decode_test, catch_errors){
	const decode_param& param = GetParam();
	std::string res;
	try{
		res.resize(base64_max_decoded_size(param.encoded.size()));
		base64_decode(param.encoded.data(), param.encoded.size(), &res[0]);
		FAIL() << "no error";
	} catch(std::invalid_argument const &err){
		EXPECT_EQ(err.what(), param.error);
	} catch(std::length_error const &err){
		EXPECT_EQ(err.what(), param.error);
	}
}

INSTANTIATE_TEST_CASE_P(_, decode_test, ::testing::Values(
			decode_param{"123", "bad base64 string"},
			decode_param{"123,", "bad base64 string"},
			decode_param{std::string("123" + std::string{char(134)}) , "bad base64 string"})
);
