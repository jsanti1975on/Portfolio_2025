#  ROT13 Decoder – Windows Forms App

**A simple ROT13 encoder/decoder** built with C# and Windows Forms.  
This tool converts text using the ROT13 cipher, which shifts each letter 13 positions forward in the alphabet.

---

##  Features

-  Clean, minimal interface with custom dark styling
-  Supports ROT13 encoding **and decoding** (they're the same!)
-  Preserves capitalization
-  Ignores punctuation, numbers, and special characters
-  Easily extensible for other classic ciphers

---

##  Screenshot

![screenshot](https://github.com/user-attachments/assets/2b7b874a-a363-4713-b435-07d058129dae)

---

##  How It Works

The ROT13 cipher:
- Shifts **A–Z** and **a–z** forward by 13 letters
- Wraps around after Z
- Leaves all non-alphabet characters untouched

###  ROT13 Example

Input:

```plaintext
Gung vf EBG13 Evtug Gurer Qhom!!!!!
```


Output:

```plaintext
That is ROT13 Right There Dubz!!!!!
```

---

##  Project Structure

| File                | Description                             |
|---------------------|-----------------------------------------|
| `Form1.cs`          | Main logic and event handler            |
| `Form1.Designer.cs` | Auto-generated form layout              |
| `Program.cs`        | Application entry point                 |
| `screenshot.png`    | Interface screenshot (optional)         |

---

##  Usage

###  Requirements
- Visual Studio 2019 or later
- .NET Framework 4.7.2 or newer

### Code Highlight

```csharp
private string Rot13(string input)
{
    char[] buffer = input.ToCharArray();

    for (int i = 0; i < buffer.Length; i++)
    {
        char letter = buffer[i];

        if (letter >= 'A' && letter <= 'Z')
            letter = (char)(((letter - 'A' + 13) % 26) + 'A');
        else if (letter >= 'a' && letter <= 'z')
            letter = (char)(((letter - 'a' + 13) % 26) + 'a');

        buffer[i] = letter;
    }

    return new string(buffer);
}
```

### Future Ideas
- Add Clear & Copy buttons
- Export output to .txt file
- Add Caesar cipher support with adjustable shift
- Theme toggle (light/dark)
 
### Author
- Jason Santiago
- Built with 🧠 + ☕ + Coconut Oil for the 2025 ROT13 proof-of-concept
- Powered by jas.digital.tools (c)

 

 

