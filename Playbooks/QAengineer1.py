---
- name: "Chocolatey"
  hosts: windows
  tasks:
    - name: Install javaruntime
      win_chocolatey:
          name: javaruntime
          version: '8.0.231'
          state: present
          ignore_checksums: yes
    - name: Install vscode
      win_chocolatey:
          name: vscode
          version: '1.66.0'
          state: present
          ignore_checksums: yes
    - name: Install postman
      win_chocolatey:
          name: postman
          version: '9.15.2'
          state: present
          ignore_checksums: yes
    - name: Install jmeter
      win_chocolatey:
          name: jmeter
          version: '5.4.3'
          state: present
          ignore_checksums: yes
    - name: Install nodejs
      win_chocolatey:
          name: nodejs
          version: '17.8.0'
          state: present
          ignore_checksums: yes
    - name: Install office365business
      win_chocolatey:
          name: office365business
          version: '14729.20228'
          state: present
          ignore_checksums: yes