# /etc/puppet/manifests/site.pp

exec { 'pkill killmenow':
  path    => '/usr/bin',
  command => 'pkill -x killmenow',
}
