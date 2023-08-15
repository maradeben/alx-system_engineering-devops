# increase number of open files allowed for more traffic/time

exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'sudo nginx -s reload',
  path    => '/etc/init.d/'
}
