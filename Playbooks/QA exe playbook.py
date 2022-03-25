---
- hosts: windows
  tasks:
    - name: Download the java 1.8
      win_get_url:
        url: https://download.oracle.com/java/17/latest/jdk-17_windows-x64_bin.exe
        arguments: /S
    - name: Download the Screenrec
      win_get_url:
        url: https://screenrec.com/download/ScreenRec_webinstall_all.exe
        arguments: /S
    - name: Download the Slack
      win_get_url:
        url: https://downloads.slack-edge.com/releases/windows/4.23.0/prod/x64/SlackSetup.exe
        arguments: /S
    - name: Download the eclipse neon
      win_get_url:
        url: https://ftp.yz.yamagata-u.ac.jp/pub/eclipse/oomph/epp/2021-12/R/eclipse-inst-jre-win64.exe
        arguments: /S
	