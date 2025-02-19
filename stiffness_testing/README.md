# Stiffness testing

Some stiffness tests with O2-O3 in various optomechanical arrangements.

## Goal:

To find a mechanical arrangement that is 'stiff enough' to maintain O2-O3 alignment during 'normal operations' with the microscope. Normal operations are things like:
- Applying up to 40lb of pressure on the O2-O3 base plate (human interaction).
- Adding or removing opto-mechanics to the base plate around O2-O3.
- Sliding the microscope around on a table.
- Moving the microscope between tables.

## Setup:
- Make a 10mm collimated beam with a 532nm alignment laser and check with a shear plate.
- Align a reduced beam diameter (~1mm) to O2 (Nikon 40x0.95 air objective).
- Align O3 to O2 in a straight through configuration with no beam deviation to center the fields of view.
- Set O2-O3 separation to maintain collimation with a shear plate.
- O2 mount: fixed mount on M25x0.75 to SM2 adapter, SM2 lens tube, SM2 flexure clamp, 1inch post and Polaris clamp.
- O3 mount: Polaris 2inch tip tilt mount with M25x0.75 to SM2 adapter, 1inch post and Polaris clamp.

## Testing:
Apply pressure between O2-O3 and check the shear plate for deviations to collimation. Record pressure required to achieve 1 fringe worth of rotation with the 5-10mm shear plate.

## Results:
0) [**Collimation check:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/00_collimation_check.jpg) an example of the collimated laser beam on the shear plate.
1) [**Force test example:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/01_force_test_example.jpg) an example of the force test. A "Tension and Compression Force Gauge for Tight Spaces, 40 lbs. Capacity" from McMaster was used (part number 1365T24).
2) [**Optical table:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/02_optical_table.jpg) the mounts were bolted directly to the optical table (305mm thick, Newport part number M-RS4000-46-12). Pressure to defocus 1 fringe **~13lbs**.
3) [**Breadboard:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/03_breadboard.jpg) the mounts were bolted directly to the center of a standard breadboard (12.7mm thick, Thorlabs part number MB4545/M). The breadboard was bolted to the optical table in all 5 locations (4 corners + center). Pressure to defocus 1 fringe **~6lbs**.
4) [**Breadboard cross brace adjacent:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/04_breadboard_cross_brace_adjacent.jpg) the mounts were bolted directly to the center of the breadboard. The breadboard was bolted to the optical table in the 4 corners. A 1inch cross brace was added adjacent to O2-O3. Pressure to defocus 1 fringe **~3lbs**.
5) [**Breadboard cross brace adjacent double:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/05_breadboard_cross_brace_adjacent_double.jpg) the same as 4 with another cross brace on the opposing side of O2-O3. Pressure to defocus 1 fringe **~5lbs**.
6) [**Breadboard cross brace direct:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/06_breadboard_cross_brace_direct.jpg) the same as 4 but with the cross brace added directly to the 1inch posts on O2-O3. Pressure to defocus 1 fringe **~16lbs**.
7) [**Optical table cross brace direct:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/07_optical_table_cross_brace_direct.jpg) the mounts were bolted directly to the optical table with the cross brace added directly to the 1inch posts on O2-O3. Pressure to defocus 1 fringe **>40lbs**. [See here for close-up photo.](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/07_optical_table_cross_brace_direct_close-up.jpg).
8) [**Breadboard on 4 posts:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/08_breadboard_on_4_posts.jpg) this mimics what a portable system might look like. The mounts were bolted directly to the center of the breadboard. The breadboard was bolted to the optical table with 4 125mm 1inch posts (each corner). Pressure to defocus 1 fringe **~0.5lbs**.
9) [**Breadboard on 4 posts cross brace directly under:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/09_breadboard_on_4_posts_cross_brace_directly_under.jpg) the same as 8 but with a 1inch cross brace directly under O2-O3. Pressure to defocus 1 fringe **~2.5lbs**.
10) [**Breadboard on 4 posts with tombstone:**](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/10_breadboard_with_tombstone.jpg) The mounts were bolted directly to the center of the breadboard on a Thorlabs 'tombstone' (part number TS240/M). The breadboard was bolted to the optical table with 4 125mm 1inch posts (each corner). Pressure to defocus 1 fringe **>40lbs**. [See here for close-up photo.](https://github.com/amsikking/SOLS_O2-O3_optomechanics/blob/main/stiffness_testing/10_breadboard_with_tombstone_close-up.jpg).

**Note:** for test 10 the pressure was also directly applied to the tombstone in various locations with no visible movement of the fringes on the shear plate.

## Conclusion:
**A single 'monolithic' aluminium mount for O2-O3 is the preferred mounting solution for stiffness** (e.g. the Thorlabs 'tombstone'). Even with a relatively floppy breadboard for the base (test 8 onwards) a human cannot reasonable misalign O2-O3 with normal pressure on or around the base plate (up to 40lb).
