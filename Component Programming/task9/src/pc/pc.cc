#include <sys/types.h>
#include <unistd.h>

template <class T>
inline T check(T ret) {
    if(ret == T(-1))
	throw std::system_error(errno, std::generic_category());
    return ret;
}

auto num_spc_members() {
    int pipefd[2];
    check(pipe(pipefd));

    auto pid = check(fork());
    if (pid == 0) {
        check(close(pipefd[0]));
        check(dup2(pipefd[1], STDOUT_FILENO));
	check(execlp("ggg", "ggg", "members", "spc", 0));
        exit(0);
    } else {
        check(close(pipefd[1]));

        int lines;
        char buffer[1];
        while(check(read(pipefd[0], buffer, 1)) != 0) {
            if (buffer[0] == '\n') lines++;
        }
        return lines;
    }
}
