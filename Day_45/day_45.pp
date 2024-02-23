$file_path = '/path/to/150_days_of_code'
$owner = 'trendswave'
$group = 'trendswave'
$mode = '0700'
$content = 'create one'

file { $file_path:
  ensure  => directory,    # Ensure that the directory exists
  owner   => $owner,       # Set the owner of the directory
  group   => $group,       # Set the group of the directory
  mode    => $mode,        # Set the permissions of the directory
  recurse => true,         # Enable recursive actions on the directory
  purge   => true,         # Remove unmanaged files in the directory
}

file { "${file_path}/file.txt":
  ensure  => file,         # Ensure that the file exists
  owner   => $owner,       # Set the owner of the file
  group   => $group,       # Set the group of the file
  mode    => $mode,        # Set the permissions of the file
  content => $content,     # Set the content of the file
}

file { $file_path:
  ensure    => 'present',  # Ensure that the directory is present
  mode      => '0755',     # Set permissions to allow public access
  recurse   => true,       # Enable recursive actions on the directory
  subscribe => File[$file_path],  # Subscribe to changes in the directory
  notify    => Service['httpd'],  # Notify the httpd service (replace with appropriate service name)
}
