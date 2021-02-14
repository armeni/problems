gtest = dependency('gtest', main: true)
test(
        'account',
        executable(
                'account_test',
                sources: ['account_test.cc'],
                include_directories: src,
                dependencies: [gtest]
        )
)
