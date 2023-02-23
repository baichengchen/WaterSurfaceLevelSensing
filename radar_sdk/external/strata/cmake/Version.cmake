macro(setVersion ver)
    string(REPLACE "." ";" VERSION_LIST ${ver})
    list(APPEND VERSION_LIST "0")

    list(GET VERSION_LIST 0 STRATA_VERSION_MAJOR)
    list(GET VERSION_LIST 1 STRATA_VERSION_MINOR)
    list(GET VERSION_LIST 2 STRATA_VERSION_PATCH)
    list(GET VERSION_LIST 3 STRATA_VERSION_BUILD)

    message(STATUS "Strata version : ${STRATA_VERSION_MAJOR}.${STRATA_VERSION_MINOR}.${STRATA_VERSION_PATCH}.${STRATA_VERSION_BUILD}")

    set(STRATA_VERSION_DEFINES
        STRATA_VERSION_MAJOR=${STRATA_VERSION_MAJOR}
        STRATA_VERSION_MINOR=${STRATA_VERSION_MINOR}
        STRATA_VERSION_PATCH=${STRATA_VERSION_PATCH}
        STRATA_VERSION_BUILD=${STRATA_VERSION_BUILD}
        )
endmacro()
