
    $username = "edmondsylar@swrht.onmicrosoft.com"
    $password = ConvertTo-SecureString "Sylar963(0)" -AsPlainText -Force
    $cred = New-Object System.Management.Automation.PSCredential($username, $password)
    Connect-SPOService -Url https://swrht-admin.sharepoint.com/ -Credential $cred
    