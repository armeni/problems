#include <iterator>

template <class E>
constexpr typename std::iterator_traits<E>::difference_type
my_count(E first, E last) {
    using category = typename std::iterator_traits<E>::iterator_category;
    if constexpr (std::is_same_v<category, std::random_access_iterator_tag>) {
        return last - first;
    }

    typename std::iterator_traits<E>::difference_type count = 0;
    auto iter = first;
    while (iter != last) {
        iter = std::next(iter);
        ++count;
    }
    return count;
}
