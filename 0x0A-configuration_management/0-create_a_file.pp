# This manifest creates a file school at /tmp
file {'/tmp/school': ensure =>file,content => 'I love Puppet',group => 'www-data',owner => 'www-data',mode => '0744',}
