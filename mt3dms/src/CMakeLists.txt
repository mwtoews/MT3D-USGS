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

message(STATUS "Writing configured FILESPEC.INC for mt3dms")
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/FILESPEC.INC ${OPENSPEC})
target_include_directories(mt3dms PRIVATE ${CMAKE_CURRENT_BINARY_DIR})
# also (potentially) overwrite file in directory that contains the source files
# TODO: is there any workaround to not modify source?
file(WRITE FILESPEC.INC ${OPENSPEC})

install(TARGETS mt3dms RUNTIME DESTINATION bin)
