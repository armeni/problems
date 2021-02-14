#include <iostream>

template <class T>
class Vector {
	using iterator = T*;
	size_t size_, capacity_;
	T* v;

	void reallocate() {
        	capacity_ *= 2;
        	T* temp = new T[capacity_];
        	std::swap(temp, v);
        	for(size_t i = 0; i < size_; ++i) {
        		v[i] = std::move(temp[i]);
		}
        	delete[] temp;
	}

public:
	Vector(): size_(0), capacity_(10), v(new T[10]) {};
	explicit Vector(size_t n): size_(n), capacity_(2 * n), v(new T[2 * n]) {
		for (size_t i = 0; i < n; ++i) {
			v[i] = T();
		}
	}

	Vector(size_t n, const T& val): size_(n), capacity_(2 * n), v(new T[2 * n]) {
		for (size_t i = 0; i < n; ++i) {
			v[i] = val;
		}
	}

	Vector(std::initializer_list<T> init_list): size_(init_list.size()), capacity_(init_list.size() * 2), v(new T[init_list.size() * 2]) {
        	for (size_t i = 0; i < init_list.size(); ++i) {
           		v[i] = *(init_list.begin() + i);
		}
	}

	Vector(const Vector& other): size_(other.size_), capacity_(other.capacity_), v(new T[other.capacity_]) {
        	for (size_t i = 0; i < size_; ++i) {
            		v[i] = other.v[i];
		}
	}

	Vector(Vector&& other) noexcept: size_(0), capacity_(0), v(nullptr) {
       		this -> swap(other);
	}

	bool operator==(const Vector& other) const {
		for (size_t i = 0; i < size_; ++i)
        		if (!(v[i] == other[i]))
            			return false;
    		return true;
	}

	Vector& operator = (const Vector& other) {
        	/*delete[] v;
        	size_ = other.size_;
        	capacity_ = other.capacity_;
        	v = new T[capacity_];
       		for (size_t i = 0; i < size_; ++i) {
            		v[i] = other.v[i];
		}*/
		auto u = other;
		swap(u);
		return *this;
	}

	Vector& operator = (Vector&& other) noexcept {
       		/*delete[] v;
        	v = nullptr;
        	size_ = 0;
        	capacity_ = 0;
        	swap(other);*/
        	return swap(this);
	}

	const T& operator[](size_t index) const {
       		return *(v + index);
	}

	T& operator[](size_t index) {
        	return *(v + index);
   	}

	~Vector() {
		delete[] v;
	}

	void swap(Vector& other) {
		std::swap(size_, capacity_);
		std::swap(capacity_, other.capacity_);
		std::swap(v, other.v);
	}

	void pop_back() {
        	v[--size_].~T();
	}

    	void push_back(const T& val) {
        	if (size_ >= capacity_)
           	reallocate();
       		*(v + size_) = val;
        	size_++;
	}

	void push_back(T&& val) {
        	if (size_ >= capacity_) {
           		capacity_ *= 2;
           		T* temp = new T[capacity_];
            		std::swap(temp, v);
            		for (size_t i = 0; i < size_; ++i) {
                		v[i] = std::move(temp[i]);
			}
            		delete[] temp;
       		}
        	*(v + size_) = std::move(val);
        	size_++;
    	}

	void erase(iterator first, iterator last) {
       		for(iterator i = first; i < end() - (last - first); ++i) {
            		*i = *(i - (last - first));
        	}
        	size_ -= last - first;
    	}

	void erase(iterator pos) {
        	erase(pos, pos + 1);
    	}


    	size_t size() const {
        	return size_;
    	}

    	iterator begin() const {
        	return v;
    	}

    	iterator end() const {
        	return v + size_;
    	}
};

template<typename T>
void swap(Vector<T>& one, Vector<T>& two){
        one.swap(two);
}
