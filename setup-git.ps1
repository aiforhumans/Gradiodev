# AI Companion Studio - Git Setup Script
# Run this after installing Git for Windows

# Navigate to project directory
Set-Location "c:\Users\markd\Gradiodev"

# Initialize git repository
git init

# Set up Git identity (replace with your actual name and email)
git config user.name "Mark"
git config user.email "mark@example.com"

# Add all files to staging area
git add .

# Create initial commit
git commit -m "🎉 Initial commit: AI Companion Studio GUI

- Add complete Gradio interface with tabbed layout
- Implement chat, persona, and settings components  
- Create modular component structure
- Add comprehensive README and project documentation
- Set up proper .gitignore for Python/Gradio project
- Include requirements.txt and MIT license"

# Check repository status
git status

# View commit history
git log --oneline

Write-Host "Git repository successfully created!" -ForegroundColor Green
Write-Host "Repository location: c:\Users\markd\Gradiodev" -ForegroundColor Cyan
Write-Host "Ready for development!" -ForegroundColor Yellow
