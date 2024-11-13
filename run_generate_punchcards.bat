@echo off
:: Set terminal colors (background and text)


:: Change to the specified directory
cd /d C:\Users\Kiosk\OneDrive\Documents\Punsh_card_maker

:: Run the generate_punchcards.py script
python generate_punchcard.py

:: Prompt the user to open the output folder
set /p openfolder="Do you want to open the output folder? (y/n): "

if /i "%openfolder%"=="y" (
    start "" "C:\Users\Kiosk\OneDrive\Documents\Punsh_card_maker\output"
)

pause
