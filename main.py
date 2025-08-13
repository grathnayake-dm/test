# main.py
import sys

def run(diff_path):
    with open(diff_path, 'r') as f:        
        diff = f.read()        
    print("🧠 Reviewing PR difff...")    
    print(diff)  

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ No diff file provided_test.")
    else:
        run(sys.argv[1])
