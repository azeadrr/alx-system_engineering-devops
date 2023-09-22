#!/usr/bin/env bash
#make changes to our configuration file
include stdlib
file_line { 'Turn off password':
  ensure  => present,
  line    => '    PasswordAuthentication no',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}
file_line { 'identity file':
  ensure  => present,
  line    => '     IdentityFile ~/.ssh/school',
  path    => '/etc/ssh/ssh_config',
  replace => true,
}
