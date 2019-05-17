Ansible RethinkDB
=========
[![Build Status](https://travis-ci.org/Rocklviv/ansible-rethinkdb.svg?branch=master)](https://travis-ci.org/Rocklviv/ansible-rethinkdb)

RethinkDB Ansible Role that managed RethinkDB setup as single node and as a cluster.

## Dependencies

* Ansible >= 2.4

Role Variables
--------------
```YAML
    # User and group used to run rethinkdb
    runuser: "rethinkdb"
    rungroup: "rethinkdb"
    
    # Log directory
    log_directory: "/var/log/rethinkdb"
    
    # Port that used for drivers to connect to rethinkdb
    driver_port: 28015
    
    # Cluster port used for RethinkDB slaves to connect to master
    cluster_port: 29015
    
    # Data storage path
    data_storage_path: "/var/lib/rethinkdb/default"
    
    # Set's master node from instances in rethinkdb group.
    # Used in cluster setup.
    master_node: "{{ groups['rethinkdb_cluster'][0] }}"
```

Example Playbook
----------------

Example play to install single node RethinkDB
```YAML
    - hosts: rethinkdb
      roles:
         - { role: rethinkdb }
```

Example play to install RethinkDB Cluster with overiding variables:
```YAML
    - hosts: rethinkdb_cluster
      roles:
        - { role: rethinkdb }
      vars:
        driver_port: 30000
        cluster_port: 31000
        data_storage_path: "/opt/rethinkdb/"
```

License
-------
MIT / BSD

## Contributing
In lieu of a formal style guide, take care to maintain the existing coding style. Add unit tests and examples for any new or changed functionality.

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

Author Information
------------------

Denis Chekirda aka <Rocklviv>