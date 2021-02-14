figures = shared_library( 
    'figures', 
    sources: ['figures.cc'],
    version: meson.project_version()
) 
executable( 
    'myapp', 
    link_with: figures, 
    sources: ['main.cc'], 
    include_directories: src
)

gtest = dependency('gtest', main: true) 
test(
    'count_test', 
    executable(
        'count_test', 
        sources: ['count_test.cc'], 
	include_directories: src, 
	dependencies: [gtest]
  )
)
