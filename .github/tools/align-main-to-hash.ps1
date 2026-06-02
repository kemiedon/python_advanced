Param(
    [Parameter(Mandatory = $true)]
    [string]$Hash,
    [string]$MainBranch = "main",
    [string]$Remote = "origin",
    [switch]$Push
)

$ErrorActionPreference = "Stop"

# 檢查 git 是否可用
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "找不到 git，請先安裝 Git"
}

# 取得 repo 根路徑
$repoRoot = git rev-parse --show-toplevel 2>$null
if (-not $repoRoot) {
    throw "這裡不是 git 倉庫，請在專案裡執行"
}
Set-Location $repoRoot

# 檢查工作樹是否乾淨
$hasDirty = git status --porcelain
if ($hasDirty) {
    throw "工作樹有未提交變更，請先處理再對齊 main"
}

# 確認當前分支不是 main
$currentBranch = git symbolic-ref --short HEAD 2>$null
if ($currentBranch -eq $MainBranch) {
    throw "目前在 $MainBranch，請切換到其他分支再執行，避免覆蓋工作樹"
}

# 驗證目標 commit 是否存在
try {
    git rev-parse --verify "$Hash^{commit}" | Out-Null
} catch {
    throw "找不到 commit $Hash，請確認 hash 是否正確"
}

# 確認 main 分支引用是否存在
$mainRef = "refs/heads/$MainBranch"
$mainExists = git show-ref --verify $mainRef 2>$null
if (-not $mainExists) {
    Write-Host "未找到 $MainBranch，將以 $Hash 建立分支" -ForegroundColor Yellow
}

# 強制將 main 指向指定 hash
Write-Host "將 $MainBranch 對齊到 $Hash" -ForegroundColor Cyan
git branch -f $MainBranch $Hash | Out-Null

# 顯示對齊後的 commit
$newHead = git rev-parse $MainBranch
Write-Host "$MainBranch 目前指向 $newHead" -ForegroundColor Green

# 若需要推送，使用 force-with-lease 確保安全
if ($Push) {
    Write-Host "推送 $MainBranch 到 $Remote（force-with-lease）" -ForegroundColor Cyan
    git push $Remote $MainBranch --force-with-lease
    Write-Host "已推送完成" -ForegroundColor Green
} else {
    Write-Host "僅更新本地 $MainBranch，尚未推送" -ForegroundColor Yellow
}
