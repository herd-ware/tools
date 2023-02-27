#!/bin/bash

# ******************************
#           ARGUMENTS
# ******************************
SIM_NAME=$1
PRJ_DIR=$2

# ******************************
#           VARIABLES
# ******************************
HW_DIR=${PRJ_DIR}/hw
SIM_DIR=${PRJ_DIR}/sim
HEX_DIR=${PRJ_DIR}/sw/isa-tests/hex

SRC_DIR=${SIM_DIR}/src
VCD_DIR=${SIM_DIR}/vcd
LOG_DIR=${SIM_DIR}/log
EXE_DIR=${SIM_DIR}/exe
OBJ_DIR=${SIM_DIR}/obj
TST_DIR=${SIM_DIR}/tst

# ******************************
#           RUN TESTS
# ******************************
{ while IFS= read -r line
do
  test=`echo "$line" | awk '{print $1;}'`
  ninstret=`echo "$line" | awk '{print $2;}'`
  trigger=`echo "$line" | awk '{print $3;}'`
  ${EXE_DIR}/${SIM_NAME} --test --boot ${HEX_DIR}/${test}-rom.hex --vcd ${VCD_DIR}/${SIM_NAME}/${test}.vcd --trigger ${trigger} --ninst ${ninstret}
done < "${TST_DIR}/${SIM_NAME}.tst"
} | tee ${LOG_DIR}/${SIM_NAME}.log
