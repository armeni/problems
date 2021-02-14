#include <ostream>
#include <array>

void message(std::ostream &stream, const char *string) {}

template<typename T, typename... Args>
void message(std::ostream &stream, const char *string, T &&arg, Args &&... args) {
	while (*string) {
		if (*string == '%') {
			string++;
			break;
		}
		stream << *string;
		string++;
	}
	stream << arg;
	message(stream, string, args...);
}

template<class T, size_t N>
std::array<T, N> cat(std::array<T, N> arr) {
	return arr;
}

template<typename T, size_t N, typename... Args>
auto cat(std::array<T, N> arr, const Args&... args) {
    	std::array<T, N * (sizeof...(args)) + N> arr1;
    	std::array<T, N * (sizeof...(args))> arr2 = std::move(cat(args...));
    	std::move(arr.begin(), arr.end(), arr1.begin());
    	std::move(arr2.begin(), arr2.end(), arr1.begin() + N);
    	return arr1;
}

template <class T, int N, int M>
struct Tie {
    	std::array<T*, M> arr;

    	Tie(std::array<T*, M> arr1) {
        	arr = arr1;
    	}

    	void operator=(const std::array<T, N*M>& rhs) {
        	for(int i = 0; i < M; i++) {
            		for(int j = 0; j < N; j++) {
                		arr[i][j] = *(rhs.begin() + i * N + j);
			}
		}
    	}
};

template <class T, size_t N, typename... Args>
auto tie(std::array<T, N>& head, Args&... tail) -> Tie<T, N, sizeof...(tail) + 1> {
	std::array<T*, sizeof...(tail) + 1> arrays {head.begin(), (tail).begin()...};
    	return Tie<T, N, sizeof...(tail) + 1>(arrays);
}
