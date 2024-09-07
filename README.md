# TextCloak
## A tool for concealing writing style using LLM
<!-- DESCRIPTION -->
## Description:

Concealing one's writing style offers several benefits, particularly in contexts where anonymity or impartiality is crucial. Additionally, concealing one's style can protect privacy, making it harder for others to attribute sensitive or controversial writings to a particular individual.

<!-- INSTALLATION -->
## Installation:

    $ git clone https://github.com/umutcamliyurt/TextCloak.git
    $ cd TextCloak/
    $ sudo apt-get install python3
    $ pip3 install -r requirements.txt
    $ python3 textcloak.py

<!-- DEMO -->
## Demo:
```
nemesis@kali:~/Projects/TextCloak$ python3 textcloak.py 
Failed to load libllamamodel-mainline-cuda-avxonly.so: dlopen: libcudart.so.11.0: cannot open shared object file: No such file or directory
Failed to load libllamamodel-mainline-cuda.so: dlopen: libcudart.so.11.0: cannot open shared object file: No such file or directory
Welcome to the interactive LLM chat session!
Type 'exit' to end the session.
You: This is a demo of TextCloak!!!
Model: Here's the rewritten text:

"Hey, I just wanted to share something cool with you guys. Check out this thing called TextCloak - it's pretty neat!"
```

<!-- LICENSE -->
## License

Distributed under the GPLv3 License. See `LICENSE` for more information.
