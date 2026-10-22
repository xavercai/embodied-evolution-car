# One-shot script to initialize a local git repo and make the first commit.
# Prerequisites: git installed and available on PATH.
#
# Usage (PowerShell):
#   powershell -ExecutionPolicy Bypass -File .\init_repo.ps1

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "ERROR: git not found. Install it first: https://git-scm.com/downloads" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path .git)) {
    git init
    Write-Host "Initialized empty git repository." -ForegroundColor Green
}

git add -A
git commit -m "Initial commit: embodied evolution car (paper, figures, docs)" 2>$null

if ($LASTEXITCODE -ne 0) {
    Write-Host "Nothing to commit (or commit failed)." -ForegroundColor Yellow
} else {
    Write-Host "Committed successfully." -ForegroundColor Green
}

Write-Host ""
Write-Host "Next steps (run manually after creating the remote repo on GitHub):" -ForegroundColor Cyan
Write-Host '  git branch -M main'
Write-Host '  git remote add origin https://github.com/xavercai/embodied-evolution-car.git'
Write-Host '  git push -u origin main'
Write-Host ""
Write-Host "If you use a different owner/repo name, adjust the 'origin' URL above." -ForegroundColor DarkGray