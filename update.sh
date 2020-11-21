#!/usr/bin/env bash
git clone https://github.com/bart02/onti_junior_devel.git
cd onti_junior_devel

cp -rf model/* /home/clover/.gazebo/models/
cp -f simulator.launch /home/clover/catkin_ws/src/clover/clover_simulation/launch/
cp -f parquet.jpg /home/clover/catkin_ws/src/clover/clover_simulation/models/parquet_plane/materials/textures/
cp -f clover.world /home/clover/catkin_ws/src/clover/clover_simulation/resources/worlds/
cp -f onti.py /home/clover/catkin_ws/src/clover/clover_simulation/scripts/

cd ..
rm -rf onti_junior_devel

echo "Done!"
