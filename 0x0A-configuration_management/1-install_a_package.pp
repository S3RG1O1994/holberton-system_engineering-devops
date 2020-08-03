# This script for install an package

package { 'puppet-lint':

  ensure   => '2.1.1',
  provider => 'gem',
}
