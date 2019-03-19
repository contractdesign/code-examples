
How to run an ansible play locally [see](https://gist.github.com/alces/caa3e7e5f46f9595f715f0f55eef65c1)

    ansible-playbook --connection=local 127.0.0.1, playbook.yml

Note the comma after the IP address.

Another way is to specify in the playbook header itself

    - hosts: 127.0.0.1
      connection: local
