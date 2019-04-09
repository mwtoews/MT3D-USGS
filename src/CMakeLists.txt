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
target_compile_options(mt3d-usgs
  PRIVATE ${Fortran_WARN_FLAGS}
  PRIVATE ${Fortran_BUILD_FLAGS}
)

write_openspec_inc(openspec.inc mt3d-usgs)

install(TARGETS mt3d-usgs
  RUNTIME DESTINATION bin
)
