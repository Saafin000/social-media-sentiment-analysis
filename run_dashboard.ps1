# Launch the Streamlit Dashboard
Write-Host "Starting Sentiment Analysis Dashboard..." -ForegroundColor Green
Write-Host "Dashboard will open at: http://localhost:8501" -ForegroundColor Cyan
Write-Host ""

cd (Split-Path -Parent $MyInvocation.MyCommand.Path)
python -m streamlit run app/streamlit_app.py
