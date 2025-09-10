# Awareness Demo — Cyber-Lab Launcher

This version of the project is designed as a **user awareness demonstration**.  
Instead of opening a website, the launcher will open the root of the **C drive** in File Explorer.  
This makes the program’s effect **highly visible** while still being completely harmless.

---

## 🎯 Objective
- Show how a small C program can trigger unexpected system actions.  
- Demonstrate to students/users that *“if this were malicious, it could have done far worse.”*  
- Reinforce awareness around **why unknown executables should not be trusted**.

---

## 📂 Code Example

```c
#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

int main() {
    // Delay for dramatic effect (3 seconds)
    Sleep(3000);

    // Awareness payload: open the C drive in Explorer
    system("start C:\");

    return 0;
}
```

---

## 🧩 Learning Points

1. **Initialization** → the program starts quietly.  
2. **Sleep()** → adds a short pause, simulating “waiting for a trigger.”  
3. **system("start C:\")** → launches File Explorer at the root of the C drive.  

This sequence makes it clear that:
- Small programs can perform surprising actions.  
- The action here is harmless, but illustrates the potential impact of code execution.  

---

## 📝 Exercises

- Change the delay in `Sleep(3000)` to different values (1s, 5s, 10s) and observe the timing.  
- Replace `C:\` with another safe folder path, e.g. `Documents` or `Downloads`.  
- Try changing the payload to open Notepad:  
  ```c
  system("start notepad.exe");
  ```
- Discuss what could happen if the payload were *not* harmless (e.g., deleting files, installing persistence).

---

## 📊 Awareness Angle

This project is ideal for:
- Classroom or family awareness training.  
- Demonstrating **how programs can run behind the scenes**.  
- Highlighting the importance of **least privilege**, **application whitelisting**, and **user caution**.  

---

## 🔀 Suggested Workflow

Keep this demo in a separate branch:

```bash
git checkout -b awareness-demo
git add open_dash.c README.md
git commit -m "Add awareness demo version that opens C drive"
git push -u origin awareness-demo
```

---

## ⚖️ Ethical Use Notice
This demonstration is **for awareness training in a controlled lab**.  
It contains **no persistence, privilege escalation, or destructive behavior**.  
Always use responsibly and with user consent.
