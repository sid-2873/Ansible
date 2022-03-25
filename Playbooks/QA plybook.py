---
- name: "Chocolatey"
  hosts: windows
  tasks:
    - name: Install googlechrome
      win_chocolatey:
          name: googlechrome
          state: present
          ignore_checksums: yes
    - name: Install sql-server-express
      win_chocolatey:
          name: sql-server-express
          state: present
          ignore_checksums: yes
    - name: Install firefox
      win_chocolatey:
          name: firefox
          state: present
          ignore_checksums: yes
    - name: Install edge
      win_chocolatey:
          name: microsoft-edge
          state: present
          ignore_checksums: yes
    - name: Install vlc
      win_chocolatey:
          name: vlc
          state: present
          ignore_checksums: yes
    - name: Install vscode
      win_chocolatey:
          name: vscode
          state: present
          ignore_checksums: yes
    - name: Install adobereader
      win_chocolatey:
          name: adobereader
          state: present
          ignore_checksums: yes
    - name: Install anydesk
      win_chocolatey:
          name: anydesk
          state: present
          ignore_checksums: yes
    - name: Install winrar
      win_chocolatey:
          name: winrar
          state: present
          ignore_checksums: yes

