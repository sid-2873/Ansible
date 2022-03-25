---
- name: "Chocolatey"
  hosts: windows
  tasks:
    - name: Install googlechrome
      win_chocolatey:
          name: googlechrome
          version: '99.0.4844.51'
          state: present
          ignore_checksums: yes
    - name: Install tortoisesvn
      win_chocolatey:
          name: tortoisesvn
          version: '1.14.1.29085'
          state: present
          ignore_checksums: yes
    - name: Install filezilla
      win_chocolatey:
          name: filezilla
          version: '3.58.0'
          state: present
          ignore_checksums: yes
    - name: Install epicgameslauncher
      win_chocolatey:
          name: epicgameslauncher
          version: '1.1.298.0'
          state: present
          ignore_checksums: yes
    - name: Install blender
      win_chocolatey:
          name: blender
          version: '3.0.1'
          state: present
          ignore_checksums: yes