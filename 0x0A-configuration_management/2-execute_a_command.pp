# execute a command to kill a process using exec

exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
