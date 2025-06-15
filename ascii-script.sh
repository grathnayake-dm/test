sudo apt-get install -y cowsay
cowsay "Hello, World!" > output.txt
grep -i "output" output.txt
cat output.txt
ls -ltra