1. update_board_image.py -o \<OS> -b \<board> -d <seach_dir>
 
Search dir is folder to search image files

when os is linux and board is ...: copy file rootfs to , image to , dtb to 
 
This command is call via ctest
  phat-san will add add_test(command) in CMake file

  
2. CI job
  
- Update QNX BSP Image: When renesas/os/bsp/qnx is changed
- Update Linux Image:   When renesas/tools/yocto_linux/CMakeLists.txt is changed
  

Update QNX BSP Pipeline:

- Job 1 : Generate BSP Image 
- Job 2 : Update to test machine (needs jobs 1)

$ ctest -R update_board_image

Update Linux RootFS, Image, DTB Pipeline:

- Job 1 : Download RootFS, Image, DTB (phat)
- Job 2 : Update to test machine (needs jobs 1)

$ ctest -R update_board_image
