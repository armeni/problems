gtest = dependency('gtest', main: true) 

test(
    'linalg_test', 
    executable(
        'linalg_test', 
	sources: ['linalg_test.cc'], 
	include_directories: src, 
	dependencies: [gtest]
  ) 
) 
executable(
    'linalg', 
    sources: ['main.cc'], 
    include_directories: src
)
