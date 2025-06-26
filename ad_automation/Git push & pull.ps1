# Git Pull & Push Automation Script with Pause

Write-Host "Pulling latest changes from GitHub..."
git pull

Write-Host "Staging all changes..."
git add .

Write-Host "Committing changes..."
git commit -m "Auto update from script" 2>$null

Write-Host "Pushing to GitHub..."
git push

Write-Host "`nAll operations completed."
Write-Host "Press any key to exit..."
[void][System.Console]::ReadKey($true)
