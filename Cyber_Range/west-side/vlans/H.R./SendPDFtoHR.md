# SendPDFtoHR
```vba
Sub SendPDFtoHR()
    Dim ws As Worksheet
    Dim FilePath As String
    Dim FileName As String
    Dim FullPath As String
    Dim OutApp As Object
    Dim OutMail As Object
    Dim HR_Email As String

    ' Set target worksheet
    Set ws = ThisWorkbook.Sheets("Sheet1") ' Change as needed

    ' Setup file path and name
    FilePath = Environ("TEMP") & "\"
    FileName = "HR_Report_" & Format(Now, "yyyymmdd_hhmmss") & ".pdf"
    FullPath = FilePath & FileName

    ' Export as PDF
    On Error GoTo ErrHandler
    ws.ExportAsFixedFormat Type:=xlTypePDF, Filename:=FullPath, Quality:=xlQualityStandard

    ' Setup Outlook
    Set OutApp = CreateObject("Outlook.Application")
    Set OutMail = OutApp.CreateItem(0)

    HR_Email = "hr@example.com" ' {^_^}LOOKFLAG=> Change to  ai domain

    With OutMail
        .To = HR_Email
        .Subject = "HR Report PDF"
        .Body = "Hello HR Team," & vbCrLf & vbCrLf & _
                "Please find attached the requested report in PDF format." & vbCrLf & vbCrLf & _
                "Best regards," & vbCrLf & _
                Application.UserName
        .Attachments.Add FullPath
        .Display ' Use .Send if you want to auto-send
    End With

    MsgBox "PDF generated and email prepared.", vbInformation

CleanExit:
    Set OutMail = Nothing
    Set OutApp = Nothing
    Exit Sub

ErrHandler:
    MsgBox "Error occurred: " & Err.Description, vbExclamation
    Resume CleanExit
End Sub
```
