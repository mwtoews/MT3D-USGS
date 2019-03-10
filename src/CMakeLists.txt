# CMake file to build mt3d-usgs executable

set(SOURCE
  mt3d-usgs.f
  mt_module.f90
  adv1.f
  btn1.f
  cts1.f
  dsp1.f
  fmi1.f
  gcg1.f
  gnt1.f
  hss1.f
  lkt1.f
  rct1.f
  sft1.f
  ssm1.f
  tob1.f
  utl1.f
  uzt1.f
  xmd1.f
  xmdlib1.f
)

add_executable(mt3d-usgs ${SOURCE})

message(STATUS "Writing configured openspec.inc for mt3d-usgs")
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/openspec.inc ${OPENSPEC})
target_include_directories(mt3d-usgs PRIVATE
  ${CMAKE_CURRENT_BINARY_DIR})
# also overwrite file in directory that contains the source files
# TODO: is there any workaround to not modify source?
file(WRITE openspec.inc ${OPENSPEC})

install(TARGETS mt3d-usgs RUNTIME DESTINATION bin)
