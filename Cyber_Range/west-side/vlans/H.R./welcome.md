📂 Awareness Demo Package (Files to Create Locally)
1. Awareness Excel File (Salary_Adjustments_2025.xlsm)
Steps:

Open Excel → create a new workbook.

Add a fake HR-looking table (e.g., “Proposed Salary Adjustments – Confidential”).

Press ALT + F11 → VBA Editor.

Double-click ThisWorkbook in the left pane.

Paste this code:

Private Sub Workbook_Open()
    MsgBox " SECURITY AWARENESS DEMO " & vbCrLf & vbCrLf & _
           "If this had been a real malicious file, your system might already be compromised." & vbCrLf & vbCrLf & _
           " Lesson: Never enable macros from unexpected attachments.", vbCritical, "Cyber Awareness Training"
End Sub


Save the file as Excel Macro-Enabled Workbook (.xlsm) with the name:

Salary_Adjustments_2025.xlsm


📌 This will trigger the awareness popup when someone opens the file and enables macros.

2. Awareness PDF (HR_Policy_Update.pdf)
Steps:

Open Word or any editor.

Copy this text into a new document:

[Company Logo Placeholder]

Human Resources Department
Policy Update – 2025

Lorem ipsum text here (make it look like a real HR doc).

---

⚠️ Cyber Awareness Training Demo ⚠️

Did you notice?

- The email sender address was suspicious.
- The subject line created unnecessary urgency.
- The attachment type (.xlsm) was unusual for HR policies.

👉 Lesson: Never open unexpected attachments or enable macros unless you trust the sender.


Save as PDF:

HR_Policy_Update.pdf

3. Upload to GitHub

Move both files into your repo folder:

Portfolio_2025_In_Works/Cyber_Range/west-side/vlans/H.R./MicrosoftOfficeFiles/


Then run:

git add .
git commit -m "Add Cyber Awareness Demo files (PDF + XLSM)"
git push


✅ End result:

Salary_Adjustments_2025.xlsm → Safe awareness macro demo.

HR_Policy_Update.pdf → Awareness PDF with training text.

Both will sit in your MicrosoftOfficeFiles folder, ready to use in your Cyber Range email simulations.
