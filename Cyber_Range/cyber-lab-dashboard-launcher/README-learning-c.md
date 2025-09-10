# Learning C Branch — Cyber-Lab Launcher

This branch is a **teaching and breakdown branch** of the Cyber-Lab Dashboard Launcher project.  
Instead of focusing on the final product, this branch explains **how the program runs step by step**, with smaller demo files to highlight individual C concepts.

---

## 📂 Files in This Branch

- **open_dash.c**  
  Simplified launcher version that:
  - Uses `Sleep()` instead of the `ping` trick
  - Waits for a few seconds, then launches a URL
  - Shows a clean flow of initialization → delay → action

- **snprintf_demo.c**  
  Demonstrates how string formatting works:
  - `%s` inserts a string
  - `%d` inserts an integer
  - `%f` inserts a floating-point number  
  This helps understand the line:
  ```c
  snprintf(flagPath, MAX_PATH, "%s\\minimized.flag", tmpDir);
  ```

- **filemodes_demo.c**  
  Demonstrates file modes when opening files:
  - `"w"` → write (create or empty the file)
  - `"a"` → append (create if missing, add to end)
  - `"r"` → read (requires file to exist)  
  This ties back to the line:
  ```c
  FILE *f = fopen(flagPath, "w");
  ```

- **README.md**  
  This document. Explains the educational goals of the branch.

---

## 🧩 Learning Objectives

By working through this branch, you will:

1. Understand how **string formatting** (`snprintf`, `%s`, `%d`, `%f`) works.
2. See how **file initialization** modes (`"w"`, `"a"`, `"r"`) affect behavior.
3. Learn the difference between **standard C libraries** (`<stdio.h>`, `<stdlib.h>`) and **Windows-specific libraries** (`<windows.h>`).
4. Practice editing, compiling, and running small C programs before recombining them into a larger project.

---

## 📝 Suggested Exercises

- In `open_dash.c`:  
  Change `Sleep(5000)` to `Sleep(2000)` and observe the shorter delay.
- In `snprintf_demo.c`:  
  Add a new line that prints a sentence with your name and age.
- In `filemodes_demo.c`:  
  Run the program multiple times with `"w"` vs `"a"` and see how the output file changes.
- Print out the values of `tmpDir` and `flagPath` to see real paths in your environment.

---

## 📊 Why This Branch Exists

- The `main` branch shows the **finished product** for portfolio use.  
- The `learning-c` branch shows the **inner workings** programmatically, for educational purposes.  
- This separation mirrors professional workflows: production-ready code vs. exploratory/teaching code.

---

## 🔀 Workflow

To create and work with this branch:

```bash
git checkout main
git pull origin main

git checkout -b learning-c
# Add the demo files here

git add .
git commit -m "Add learning branch with C breakdown demos"
git push -u origin learning-c
```
