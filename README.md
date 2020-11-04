       uid=value and gid=value
              Set the owner and group of the root of the filesystem
              (default: uid=gid=0, but with option uid or gid without
              specified value, the UID and GID of the current process are
              taken).

       setuid=value and setgid=value
              Set the owner and group of all files.

       mode=value
              Set the mode of all files to value & 0777 disregarding the
              original permissions.  Add search permission to directories
              that have read permission.  The value is given in octal.

       protect
              Do not allow any changes to the protection bits on the
              filesystem.

       usemp  Set UID and GID of the root of the filesystem to the UID and
              GID of the mount point upon the first sync or umount, and then
              clear this option.  Strange...
