# CMake file to build mt3dms executable

# Modify copy of source code of one file in binary directory
message(STATUS "Rewriting mt3dms5.for to use GETARG(1,FLNAME)")
file(READ mt3dms5.for MT3DMS5_FOR_IN)
string(REPLACE "CALL GETCL(FLNAME)" "CALL GETARG(1,FLNAME)"
       MT3DMS5_FOR_OUT ${MT3DMS5_FOR_IN})
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/mt3dms5.for ${MT3DMS5_FOR_OUT})

set(SOURCE
  ${CMAKE_CURRENT_BINARY_DIR}/mt3dms5.for
  mt_adv5.for
  mt_btn5.for
  mt_dsp5.for
  mt_fmi5.for
  mt_gcg5.for
  mt_hss5.for
  mt_rct5.for
  mt_ssm5.for
  mt_tob5.for
  mt_utl5.for
)

add_executable(mt3dms ${SOURCE})
target_compile_options(mt3dms
  PRIVATE ${Fortran_WARN_FLAGS}
  PRIVATE ${Fortran_BUILD_FLAGS}
)

write_openspec_inc(FILESPEC.INC mt3dms)

install(TARGETS mt3dms
  RUNTIME DESTINATION bin
)
